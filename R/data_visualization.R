# Objective: Code for data visualization and plotting in R as part of MasterBFG 2023

# Load necessary libraries
# Uncomment install.packages lines if the packages are not yet installed
# install.packages("ggplot2")
library(ggplot2)
# install.packages("reshape2")
library(reshape2)
# install.packages("data.table")
library(data.table)
# install.packages("plyr")
library(plyr)
# install.packages("RColorBrewer")
library(RColorBrewer)
# install.packages("gplots")
library(gplots)

# Define the path to the CSV file
path2csv <- 'C:/Users/feder/Desktop/project/masterBFG_FG/introR/'

# Read the CSV file with dataset
dat <- read.csv(paste0(path2csv, "output/dataset_drugs_export.csv"), header=TRUE, sep=",")
head(dat)

# Summary of the dataset
summary(dat)

# Count the number of each TreatmentType and create a barplot
table(dat$TreatmentType)
ggplot(data=dat) +
  geom_bar(mapping= aes(x=TreatmentType))

# Styled barplot for TreatmentType
ggplot(data=dat) +
  geom_bar(mapping= aes(x=TreatmentType), color='red', fill='darkblue', width=0.5) +
  ggtitle("Plot count of Treatment Types") +
  theme_minimal() +
  theme(
    plot.title = element_text(color='red', size=14, face='bold'),
    axis.title.x = element_text(color='green', size=12),
    axis.title.y = element_text(color='blue', size=12)
  )

# Prepare data for multiple bar plots: Gender and TreatmentType
dat_gender_TreatType <- dat[,c('Gender', 'TreatmentType')]
df_counts <- melt(table(dat_gender_TreatType)) # Library used: reshape2

# Create multiple bar plots for Gender and TreatmentType
ggplot(df_counts, aes(x=TreatmentType, y=value, fill=Gender)) +
  geom_bar(position="dodge", stat="identity", width=0.5) +
  theme_minimal() 

# Stacked bar plot
ggplot(df_counts, aes(x=TreatmentType, y=value, fill=Gender)) +
  geom_bar(position="stack", stat="identity", width=0.5) +
  theme_minimal()

# Stacked bar plot (percentage)
ggplot(df_counts, aes(x=TreatmentType, y=value, fill=Gender)) +
  geom_bar(position="fill", stat="identity", width=0.5) +
  theme_minimal()

# Pie chart showing percentage of each TreatmentType
ggplot(dat, aes(x="", y=TreatmentType, fill=TreatmentType)) +
  geom_bar(stat="identity", width=1) +
  coord_polar("y", start=0) +
  theme_void() # Remove background grid

# Histogram and density plots for GeneA
ggplot(dat, aes(x=GeneA)) + 
  geom_histogram(binwidth=.05, colour="black", fill="lightgrey") +
  theme_minimal()

ggplot(dat, aes(x=GeneA)) + 
  geom_density(fill='lightblue', alpha=0.6) +
  theme_minimal()

# Density plot with mean and median lines
ggplot(dat, aes(x=GeneA)) +
    geom_density() +
    geom_vline(aes(xintercept=mean(GeneA, na.rm=TRUE)), color="red", linetype="dashed", size=1) +
    geom_vline(aes(xintercept=median(GeneA, na.rm=TRUE)), color="darkgreen", linetype="dotted", size=1) +
    theme_minimal()

# Convert data from wide to long format for additional plots
dat_long <- melt(setDT(dat), id.vars=c("Patient_ID", "Timepoint", "Treatment", "TreatmentType", "Gender"))
head(dat_long)

# Density plots with transparent fill and group means
ggplot(dat_long, aes(x=value, fill=variable)) + 
  geom_density(alpha=.3) +
  theme_classic()

# Calculate mean of each group for density plots
cdat <- ddply(dat_long, "variable", summarise, value.mean=mean(value))

ggplot(dat_long, aes(x=value, fill=variable)) + 
    geom_density(alpha=.3) +
    geom_vline(data=cdat, aes(xintercept=value.mean, color=variable), linetype="dashed", size=1) +
    theme_classic()

# Dotplot showing Gene expression across timepoints
ggplot(dat_long, aes(x=Timepoint, y=value)) + 
  geom_point(aes(color = variable, size=value), alpha=0.8) +
  scale_color_manual(values = c("blue", "green", "purple"))+
  theme_minimal()

# Gene expression across Patient_ID
ggplot(dat_long, aes(x=Patient_ID, y=value)) + 
  geom_point(aes(color = variable), size=4, alpha=0.8) +
  scale_color_manual(values = c("blue", "green", "purple"))+
  theme_minimal()

# Dotplot Gene expression across timepoints for specific treatments
ggplot(dat_long[(dat_long$variable == 'GeneA' & dat_long$Treatment == 'drug'),], aes(x=Timepoint, y=value, group=Patient_ID)) + 
  geom_point(aes(color = Patient_ID), size=4, alpha=0.8) +
  geom_line() +
  theme_minimal()

ggplot(dat_long[(dat_long$variable == 'GeneA' & dat_long$Treatment == 'placebo'),], aes(x=Timepoint, y=value, group=Patient_ID)) + 
  geom_point(aes(color = Patient_ID), size=4, alpha=0.8) +
  geom_line() +
  theme_minimal()

# Boxplot for Gene expression across timepoints
ggplot(dat_long[(dat_long$variable == 'GeneA' & dat_long$Treatment == 'drug'),], aes(x=as.factor(Timepoint), y=value)) + 
  geom_boxplot() +
  theme_minimal()

# Scatterplots comparing gene expressions
ggplot(data = dat, aes(x = GeneA, y = GeneB, color=Patient_ID, shape=TreatmentType)) + 
  geom_point(size=4) +
  theme_minimal()

ggplot(data = dat, aes(x = GeneA, y = GeneC, color=Patient_ID, shape=TreatmentType)) + 
  geom_point(size=4) +
  theme_minimal()

# Create a matrix for heatmap visualization
m <- as.matrix(dat[dat$Timepoint==4, c("GeneA", "GeneB", "GeneC")])

# Basic heatmaps with different dendrogram options
heatmap.2(m, Rowv=FALSE, Colv = FALSE, dendrogram="none", scale="none", col=bluered(100), trace="none", density.info = "none")

# Annotated heatmap with side colors
my_group <- as.numeric(as.factor(dat$TreatmentType))
colSide <- brewer.pal(9, "Set1")[my_group]

heatmap.2(m, Rowv=FALSE, Colv = FALSE, dendrogram="none", scale="none", col=bluered(100), trace="none", density.info = "none", RowSideColors = colSide)
legend("bottomleft", title="Treatment Type", legend=c("single drug", "double drug", "placebo"),
       fill=c("#4DAF4A", "#E41A1C", "#377EB8"), cex=0.8, box.lty=0)

# Save a boxplot as PNG
png(paste0(path2csv, "results/boxplot.png"), width = 350, height = 350)
ggplot(dat_long[(dat_long$variable == 'GeneA' & dat_long$Treatment == 'drug'),], aes(x=as.factor(Timepoint), y=value)) + 
  geom_boxplot() +
  ggtitle("Boxplot geneA expression across timepoints for drug treatments") +
  theme_minimal()
dev.off()

# Save a boxplot as PDF
pdf(paste0(path2csv, "results/boxplot.pdf"), width = 10, height = 10)
ggplot(dat_long[(dat_long$variable == 'GeneA' & dat_long$Treatment == 'drug'),], aes(x=as.factor(Timepoint), y=value)) + 
  geom_boxplot() +
  ggtitle("Boxplot GeneA expression across timepoints for drug treatments") +
  theme_minimal()
dev.off()
