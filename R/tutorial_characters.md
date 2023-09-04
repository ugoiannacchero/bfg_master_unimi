---
title: "tutorial_characters"
author: "ugo"
date: "2023-09-04"
output: github_document
---

## Characters

When you analyze a data set, you don't have only numbers: you'll have gene names, protein names, mouse strains and other variables that R calls character (I will always call them strings, but remember that for R they are character). A character can be a single letter, a word or even a whole text. To create a character variables you have to include in `""` (double quotes) or in `''` (single quotes):

```{r}
mychar_d <- "SEC24C"
typeof(mychar_d)
```

```{r}
mychar_s <- "SEC24C"
typeof(mychar_s)
```

Even numbers can be considered as character if included by "":

```{r}
weight_n <- 12
typeof(weight_n)
```

```{r}
weight_c <- "12"
typeof(weight_c)
```

By adding the double or single quotes it changes everything. IMPORTANT: R interprets everything that is between a pair of single or double quotes as character, so if you forget to close a quote, nothing will work. Moreover, you can't use a single quote to close a character opened with a double quote and vice versa.

# Concatenate Strings

Sometimes you want to concatenate different string into one single string, and we can do it with two similar functions: paste() and paste0(). The unique difference among them is that in the former you can decide what character to use to separate what you are concatenating (default is a white space), while the latter do not insert any character. For example, let's say you have a variable `condition` and a variable `treatment`, and you want to concatenate them to create a variable `sample`; you will do:

```{r}
condition <- "control"
treatment <- "vector"
```

```{r}
sample <- paste(condition,
                treatment,
                sep = ".") #default is " "

print(sample)
```

```{r}
sample0 <- paste0(condition,
                  treatment)
                      
print(sample0)
```

You concatenate as many character as you want, just put them all inside that function.

# Substring:

The function `substr()` is used to slice the character and take only a part of it.

`substr(mychar_s, start = 2, stop = 4`

It needs a start and a stop value, they are both included in the result (in this case, character at position 2,3 and 4 are sliced). Remember: in R everything starts at 1, so the first element is at position 1. In other languages it starts from 0, but in R it starts from 1.

Another function is `nchar` and it is important when we use `substr` and we don't know how long is a character.

```{r}
nchar(mychar_s)
```

Let's say we want to take from position 3 until the end, but we don't know how long is a character, we can do it with:

```{r}
substr(mychar_s, start = 3, stop = nchar(mychar_s))
```

What happened here is that the result of the function `nchar(mychar_s)` is used as the value to indicate the stop. We will usually use these method in R, especially when we don't want to use memory to store a value that is used only once (as in the case).

# Substitution

The function `sub()`, and its big brother `gsub()`. They are used to substitute part of a character with another, the only difference is that the former changes only the first occurrence. Let's say we have the sample variable written as `"control_vector_3"` and we want to get rid of the underscores, we will do:

```{r}
sample2 <- "control_variable_2"
```

```{r}
sub_only <- sub(pattern = "_", #the part of the string to search to substitute
                replacement =  " ", #what to use to replace it
                x = sample2) #the variable in which to search
                    
print(sub_only)
```

```{r}
gsub_all <- gsub(pattern = "_", #the part of the string to search to substitute
                 replacement = " ", #what to use to replace it
                 x = sample2) #variable in which to search
```

This is the basic way of using these functions, but they can be very useful in complex analysis.

# Grep

Further parents of substitution, are `grep()` and its brother `grepl()`: they are used to check if a particular pattern is present in a character variable. The first one returns the index or the value of the variable that match the pattern, the second one returns a Boolean value (TRUE or FALSE) indicating the presence of the pattern in the variable. Let's see few example right away:

```{r}
gene_to_test <- "GAPDH"
pattern_to_check_1 <- "GA"
pattern_to_check_2 <- "PH"
```

```{r}
grep_1 <- grep(pattern = pattern_to_check_1,
               x = gene_to_test,
               value = T) #the default is FALSE (returns index)
print(grep_1)
```

```{r}
grep_2 <- grep(pattern = pattern_to_check_2,
               x = gene_to_test,
               value = T) #default is FALSE (returns index)
print(grep_2)
```

```{r}
grepl_1 <- grepl(pattern = pattern_to_check_1,
                 x = gene_to_test)
print(grepl_1)
```

```{r}
grepl_2 <- grepl(pattern = pattern_to_check_2,
                 x = gene_to_test)
print(grepl_2)
```

We can see that `grep_2` gives a `character(0)` as result, meaning that it is an empty character variable.

#Transform to type character

As for numbers, we can also convert a variable into a string: we use the function `as.character()`. You will use this function when a column of a dataframe is read as numeric while you want it to be read as character instead.

```{r}
ml_to_add <- 35
typeof(ml_to_add)
```

```{r}
ml_to_add <- as.character(ml_to_add)
typeof(ml_to_add)
```

This is an important lesson: in R variables can be overwritten with other types of data (this can't be done in other languages such as Java, C++, ecc.). THis can be both handy and risky at the same time: handy because we can save memory by overwriting useless variables, risky because we can overwrite without checking if the type is maintained.

# Exercise 5.1

In a list of genes to test, you find a gene called "NRG_1" and one called "SST R". In the report you have to present you want to print out "Involved genes are NRG1 and SSTR2". How to do it?

```{r}
gene1 <- "NRG_1"
gene2 <- "SST R"
```

```{r}
# correct gene names
gene1 <- gsub(pattern = "_", replacement = "", gene1)
gene2 <- gsub(pattern = " R", replacement = " R2", gene2)
```

```{r}
# concatenate all the string
all_string <- paste("Involved genes are", gene1, "and", gene2) 
print(all_string)
```

# Exercise 5.2

In a variable you have the gene name "HCN1" and in another you have its number of amino acids (890, as numeric!!!). Print out the string "HCN1 protein is 890 aa long"

```{r}
Gene <- "HCN1"
aa_num <- 890

#one string solution
to_print <- paste(Gene, "protein is", as.character(aa_num), "aalong")
print(to_print)
```
