# Objective: Introduction to R, covering data loading, data management, and data exploration tasks.

# Load base R library (typically loaded by default)
library(base)

# Check the working directory
getwd()

# Load dataset from a CSV file
read.csv("C:/Users/feder/Desktop/project/masterBFG_FG/introR/data/dataset_drugs_import.csv", header=FALSE, sep=";")

# Get information on the read.csv function and its arguments
?read.csv

# Create a variable to store the file path
file_path <- 'C:/Users/feder/Desktop/project/masterBFG_FG/introR/data/dataset_drugs_import.csv'

# Load data into a variable called dat
dat <- read.csv(file_path, header=TRUE, sep=";")

# Display the first few rows of the dataset
head(dat)

# Display the last few rows of the dataset
tail(dat)

# Check the class of the data object
class(dat)

# Check dimensions, number of rows, and columns
dim(dat)
nrow(dat)
ncol(dat)

# Accessing Data by Index
dat[1, 1]  # Single value
dat[4, 7]  # Row 4, Column 7
dat[c(3, 5), c(5, 6)]  # Multiple rows and columns
dat[1:8, 1:4]  # First 8 rows and 4 columns
dat[5:10, 1:6]  # Rows 5-10, Columns 1-6
dat[5, ]  # All columns for row 5

# Accessing Data by Column Name
colnames(dat)
dat$Patient_ID
head(dat[, c('Patient_ID', 'GeneA')])

# Selecting Rows Based on Column Values
dat[dat$Gender == 'M', ]  # Rows with Gender 'M'
dat[dat$Gender != 'M', ]  # Rows where Gender is not 'M'
dat[dat$Gender == 'M' & dat$GeneA > 0.4, ]  # Multiple conditions
dat[dat$Patient_ID %in% c('pt1', 'pt2', 'pt3'), ]  # Specific Patient IDs

# Add a column with prefixed progressive numbers and set as row names
dat$newCol <- paste0("rn", 1:nrow(dat))
row.names(dat) <- dat$newCol
head(dat)

# Read CSV file with specified row names
dat <- read.csv(file_path, header=TRUE, sep=";", row.names = 1)

# Logical Vector Indexing
index <- dat$Treatment == 'drug'
dat[index, ]$GeneA

# Access values directly in one line
dat[dat$Treatment == 'drug', ]$GeneA

# Calculating Summary Statistics
max(dat$GeneA)  # Maximum
min(dat$GeneA)  # Minimum
mean(dat$GeneA)  # Mean
median(dat$GeneA)  # Median
sd(dat$GeneA)  # Standard Deviation

# Summarize multiple columns
summary(dat[, 5:7])

# Apply basic operations on a column
dat$GeneA + 1
dat$GeneA * 10
dat$GeneA > 0.5  # Logical comparison

# Check for values in a column and count occurrences
dat$GeneA > 1
any(dat$GeneA > 1)
sum(dat$GeneA > 0.7)

# Calculate mean, median, and standard deviation for GeneC
mean(dat$GeneC)
median(dat$GeneC)
sd(dat$GeneC)

# Get quantile values for GeneC
summary(dat$GeneC)

# Plot column values after multiplication
plot(dat$GeneA * 100)

# Filter by Patient_ID and Timepoint
dat[dat$Patient_ID == 'pt4' & dat$Timepoint == 4, c('GeneA')]

# Standardize GeneB values to create Z-scores
mean_geneB <- mean(dat$GeneB)
sd_geneB <- sd(dat$GeneB)
dat$ZscoreB <- (dat$GeneB - mean_geneB) / sd_geneB
head(dat$ZscoreB)

# Sorting Data
df2 <- dat[order(dat$Timepoint),]  # Sort by Timepoint
df2 <- dat[order(dat$Timepoint, dat$TreatmentType),]  # Sort by multiple columns
df2 <- dat[order(dat$GeneA, decreasing=TRUE),]  # Sort in descending order
df2 <- dat[order(dat$GeneA, decreasing=TRUE, na.last=FALSE),]  # Sort with NA first

# Print data structure and summary statistics
dat <- read.csv(file_path, header=TRUE, sep=";", stringsAsFactors = FALSE)
str(dat)
summary(dat)

# Factor Levels and Tables
levels(dat$Gender)
table(dat$Gender)
barplot(table(dat$Gender))

# Correct factor levels and drop unused levels
dat$Gender[dat$Gender == 'M'] <- 'm'
dat$Gender <- droplevels(dat$Gender)
barplot(table(dat$Gender))

# Modify specific levels in Gender
levels(dat$Gender)[2] <- 'f'
barplot(table(dat$Gender))

# Create a new data frame and merge with existing data
df <- data.frame(Patient_ID = c("pt1", "pt2", "pt3", "pt4", "pt5", "pt6", "pt7", "pt8", "pt9"),
                 Age = c(63, 41, 65, 58, 26, 83, 70, 52, 87))
total <- merge(dat, df, by="Patient_ID", all.x = TRUE)

# Data Import Options
read.csv("C:/Users/feder/Desktop/project/masterBFG_FG/introR/data/dataset_drugs_import.csv", 
         header=TRUE, sep=";", stringsAsFactors=TRUE, as.is=1)

# Export dataset
write.csv(dat, file = 'C:/Users/feder/Desktop/project/masterBFG_FG/introR/output/dataset_drugs_export.csv',
          row.names = FALSE, quote=FALSE)

# Useful Commands
getwd()  # Working directory
c('a', 'b')  # Create a character vector
head(dat)  # First few rows of the data
tail(dat)  # Last few rows of the data
str(dat)  # Structure of the data
dim(dat)  # Dimensions
nrow(dat)  # Number of rows
ncol(dat)  # Number of columns
colnames(dat)  # Column names
rownames(dat)  # Row names
dat$Patient_ID  # Access a column
unique(dat$Patient_ID)  # Unique values in a column
length(unique(dat$Patient_ID))  # Number of unique values
table(dat$GeneA)  # Frequency table
levels(dat$Patient_ID)  # Factor levels
paste0('hello', 'R')  # Concatenate strings
