a, b, c, d = 2, 3, 5, 7
a ** (b + c) # parentheses
a * b ** c # exponent: same as `a * (b ** c)`
a + b * c / d # multiplication / division: same as `a + (b * c / d)`
#Extras: mathematical rules hold, but not always:
300 / 300 * 200
300 * 200 / 300
1e300 / 1e300 * 1e200
1e300 * 1e200 / 1e300       