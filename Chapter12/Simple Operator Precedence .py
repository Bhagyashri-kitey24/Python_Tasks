a, b, c, d = 2, 3, 5, 7
sum1=a ** (b + c) # parentheses
sum2=a * b ** c # exponent: same as `a * (b ** c)`
sum3=a + b * c / d # multiplication / division: same as `a + (b * c / d)`
print(sum1) #256
print(sum2) #486
print(sum3) #4.142857142857142