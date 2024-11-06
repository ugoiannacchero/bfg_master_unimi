# Tutorial: Numbers in R
# Author: Ugo
# Date: 2023-08-01

# Basic Number Types
# We have two main types of numbers in R: integers and doubles.

# Basic Operations
# Addition, subtraction, multiplication, division
basic_result <- 5 + 4 - 2 * 3 / 2
print(basic_result)

# Power
power_result <- 4 ** 3
print(power_result)

# Logarithms
log_result_e <- log(100)  # natural log (base e)
log_result_10 <- log10(100)  # base 10
log_result_2 <- log2(100)  # base 2
log_result_custom <- log(100, base = 3)  # custom base
print(c(log_result_e, log_result_10, log_result_2, log_result_custom))

# Exponential
exp_result <- exp(2)
print(exp_result)

# Square Root
sqrt_result <- sqrt(9)
print(sqrt_result)

# Modulus (remainder)
modulus_result <- 7 %% 3
print(modulus_result)

# Check even or odd using modulus
is_odd_11 <- 11 %% 2  # odd
is_even_12 <- 12 %% 2  # even
print(c(is_odd_11, is_even_12))

# Rounding
# Round to n decimal places
rounded_result <- round(1/3, digits = 2)
print(rounded_result)

# Round to upper integer
ceiling_result <- ceiling(10.2)
print(ceiling_result)

# Round to lower integer
floor_result <- floor(14.9)
print(floor_result)

# Converting String to Number
# Example of converting a string to numeric type
mystring <- "15"
print(typeof(mystring))  # character
mynumber <- as.numeric(mystring)
print(typeof(mynumber))  # double

# Exercises

# Exercise 5.1 - Calculate mean Ct for FOXP1 triplicates
rep1 <- 22.4
rep2 <- 22.31
rep3 <- 22.24
n_rep <- 3
mean_Ct <- (rep1 + rep2 + rep3) / n_rep
round_mean_Ct <- round(mean_Ct, digits = 2)
print(round_mean_Ct)

# Exercise 5.2 - Calculate SD for data from exercise 5.1
var_calc <- ((rep1 - mean_Ct)^2 + (rep2 - mean_Ct)^2 + (rep3 - mean_Ct)^2) / (n_rep - 1)
sd_calc <- sqrt(var_calc)

# Round SD to various levels
sd_ceil <- ceiling(sd_calc)
sd_floor <- floor(sd_calc)
sd_4decimal <- round(sd_calc, digits = 4)
print(c(sd_ceil, sd_floor, sd_4decimal))
