tutorial_numbers
================
ugo
2023-08-01

``` r
# Numbers
# We have two types of numbers in R: integers and doubles;
```

``` r
#Operations

#First of all, here is how to do basic mathematical operation in R:
# Plus, minus, multiply, divide

5 + 4 - 2 * 3 / 2
```

    ## [1] 6

``` r
# Power
4 ** 3
```

    ## [1] 64

``` r
# Logarithm
log(100) # base e
```

    ## [1] 4.60517

``` r
log10(100) # base 10
```

    ## [1] 2

``` r
log2(100) # base 2
```

    ## [1] 6.643856

``` r
log(100, base = 3) # choose the base
```

    ## [1] 4.191807

``` r
# Natural exponential
exp(2)
```

    ## [1] 7.389056

``` r
# Square root
sqrt(9)
```

    ## [1] 3

``` r
# An interesting operator is the modulus (%%) which returns the remainder of a division, for example:

7 %% 3
```

    ## [1] 1

``` r
# This can be useful to evaluate if a number is even or odd by calculating the remainder of the division x / 2 (so using x %% 2): if it is 0, the number x is even, otherwise it is odd.

11 %% 2
```

    ## [1] 1

``` r
12 %% 2
```

    ## [1] 0

``` r
# Rounding
# Another thing that we usually want to do is to round decimal number, especially after log transformation or division. To do so, we have 3 functions:

# Round to n decimal places
round(x = 1/3, digits = 2)
```

    ## [1] 0.33

``` r
# Round to upper integer
ceiling(10.2)
```

    ## [1] 11

``` r
# Round to lower integer
floor(14.9)
```

    ## [1] 14

``` r
# Look how ceiling and floor do not take into account the decimal part, even if it is greater or lower than 0.5.
```

``` r
# Tranform to type number

# Sometimes you want to transform a string that contains a number to a numeric type in R. I know we haven’t covered strings yet (next chapter will be on them), but let’s do a bit step forward now just to see this super useful function, that we use a lot when dealing with dataframes.
# To do so, we’ll use the function called as.numeric()

mystring <- "15" # This is a character, can you guess why R interpret it as a character?
typeof(mystring)
```

    ## [1] "character"

``` r
mynumber <- as.numeric(mystring)
typeof(mynumber)
```

    ## [1] "double"

``` r
#Exercises:

# Exercise 5.1 The results of a Real-Time PCR indicate that your triplicates for FOXP1 have these Ct: 22.4, 22.31, 22.24. Calculate the mean value and print it rounded to 2 decimal places.

mean_Ct <- (22.4 + 22.31 + 22.24) / 3

round_mean_Ct <- round(mean_Ct, digits = 2)

print(round_mean_Ct)
```

    ## [1] 22.32

``` r
# BETTER solution
rep1 <- 22.4
rep2 <- 22.31
rep3 <- 22.24
n_rep <- 3

mean_res_better <- (rep1 + rep2 + rep3) / n_rep
mean_res_better_round <- round(mean_res_better, digits = 2)
print(mean_res_better_round)
```

    ## [1] 22.32

``` r
# The second solution is better because every number is stored in a variable, that you then use to calculate the mean value.
```

``` r
# Exercise 5.2 Now calculate the sd of the data of exercise 5.1 and print the value rounded to upper integer, to lower integer and to a 4-digit decimal.

#first we calculate the variance:

var_calc <- ((rep1 - mean_res_better)^2 + (rep2 - mean_res_better)^2 + (rep3 - mean_res_better)^2) / (n_rep - 1)

# Now let's calculate sd
sd_calc <- sqrt(var_calc)

#value rounder to upper integer
sd_calc_ceil <- ceiling(sd_calc)
print(sd_calc_ceil)
```

    ## [1] 1

``` r
sd_mean_Ct <- sd(x = round_mean_Ct)

up_round_sd_mean_Ct <- round(ceiling(sd_mean_Ct))
print(up_round_sd_mean_Ct)
```

    ## [1] NA
