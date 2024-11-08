# Load required libraries
library(DESeq2)
library(ggplot2)
library(pheatmap)
library(dplyr)

# Simulate a toy RNA-seq dataset
set.seed(42)
n_genes <- 1000     # Number of genes
n_samples <- 12     # Number of samples (6 per condition)

# Generate random counts for two conditions (A and B)
counts <- matrix(rnbinom(n_genes * n_samples, mu=100, size=1), nrow=n_genes)
colnames(counts) <- paste0("Sample", 1:n_samples)
rownames(counts) <- paste0("Gene", 1:n_genes)

# Metadata for experimental conditions
condition <- factor(rep(c("A", "B"), each = 6))
coldata <- data.frame(row.names = colnames(counts), condition = condition)

# Create the DESeqDataSet object
dds <- DESeqDataSetFromMatrix(countData = counts, colData = coldata, design = ~ condition)

# Filter out genes with low counts
dds <- dds[rowSums(counts(dds) >= 10) >= 3, ]

# Run DESeq for differential analysis
dds <- DESeq(dds)
res <- results(dds)

# View the first results
head(res)

# Filter results for significant genes
resSig <- res[which(res$padj < 0.05), ]
print(paste("Number of differentially expressed genes:", nrow(resSig)))

# Explore results: sort by adjusted p-value
resOrdered <- res[order(res$padj), ]
head(resOrdered)

# Normalize data
vsd <- vst(dds, blind=FALSE)

# PCA plot
pcaData <- plotPCA(vsd, intgroup="condition", returnData=TRUE)
percentVar <- round(100 * attr(pcaData, "percentVar"))
ggplot(pcaData, aes(PC1, PC2, color=condition)) +
    geom_point(size=3) +
    xlab(paste0("PC1: ", percentVar[1], "% variance")) +
    ylab(paste0("PC2: ", percentVar[2], "% variance")) +
    labs(title = "PCA of RNA-seq Samples") +
    theme_minimal()

# Heatmap of the most variable genes
select <- order(rowVars(assay(vsd)), decreasing = TRUE)[1:50]
pheatmap(assay(vsd)[select, ], cluster_rows=TRUE, show_rownames=FALSE,
         cluster_cols=TRUE, annotation_col=coldata)

# Volcano plot to visualize results
res$logP <- -log10(res$padj)
ggplot(res, aes(x = log2FoldChange, y = logP)) +
  geom_point(aes(color = padj < 0.05), size = 1) +
  scale_color_manual(values = c("grey", "red")) +
  labs(title = "Volcano Plot of Differentially Expressed Genes",
       x = "Log2 Fold Change", y = "-Log10(P-adj)") +
  theme_minimal()

# Export significant results to a CSV file
write.csv(resSig, "differential_expression_results.csv", row.names = TRUE)

# Generate additional statistics and plots
# Number of expressed genes per condition
countsByCondition <- rowSums(counts(dds, normalized=TRUE) > 10)
barplot(countsByCondition, main="Gene Counts per Condition", 
        ylab="Number of Genes", xlab="Conditions")

# Dispersion plot
plotDispEsts(dds, main="Dispersion Estimates for Each Gene")

# Heatmap of differentially expressed genes (DEGs)
topGenes <- rownames(resSig)[1:30]  # Top 30 DE genes
pheatmap(assay(vsd)[topGenes, ], cluster_rows=TRUE, show_rownames=TRUE,
         cluster_cols=TRUE, annotation_col=coldata,
         main = "Heatmap of Top DE Genes")

# Mean and standard deviation analysis plot
meanSdPlot(assay(vsd), ranks=FALSE, main="Mean vs SD of Expressed Genes")

# Function to calculate the number of significant genes for various cutoffs
calculate_significant_genes <- function(padj_cutoff) {
  sum(res$padj < padj_cutoff, na.rm=TRUE)
}

# Calculate the number of significant genes for different p-adj cutoffs
cutoffs <- c(0.01, 0.05, 0.1)
signif_genes <- sapply(cutoffs, calculate_significant_genes)
names(signif_genes) <- paste0("P-adj <", cutoffs)
print(signif_genes)

# Histogram of log2FoldChange values
ggplot(res, aes(x=log2FoldChange)) +
  geom_histogram(bins=30, fill="blue", alpha=0.7) +
  labs(title="Distribution of Log2 Fold Change Values",
       x="Log2 Fold Change", y="Count") +
  theme_minimal()

# Scatter plot comparing conditions for a representative DE gene
plotCounts(dds, gene=rownames(resSig)[1], intgroup="condition", 
           main="Expression of a Representative DE Gene")

# Sample correlation matrix
sampleDists <- dist(t(assay(vsd)))
pheatmap(as.matrix(sampleDists), clustering_distance_rows=sampleDists,
         clustering_distance_cols=sampleDists, main="Sample Correlation Matrix")

# End of code
print("DESeq2 analysis complete. Results saved in 'differential_expression_results.csv'")
