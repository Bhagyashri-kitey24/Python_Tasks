print("--------Basic Slicing--------")
a = "abcdef"
print(a) # "abcdef"
# Same as a[:] or a[::] since it uses the defaults for all three indices
print(a[-1]) # "f"
print(a[:]) # "abcdef"
print(a[::]) # "abcdef"
print(a[3:])# "def" (from index 3, to end(defaults to size of iterable))
print(a[:4]) # "abcd" (from beginning(default 0) to position 4 (excluded))
print(a[2:4]) # "cd" (from position 2, to position 4 (excluded))
print(a[::2] )# "ace" (every 2nd element)
print(a[1:4:2]) # "bd" (from index 1, to index 4 (excluded), every 2nd element)
print(a[:-1] )# "abcde" (from index 0 (default), to the second last element (last element - 1))
print(a[:-2] )# "abcd" (from index 0 (default), to the third last element (last element -2))
print(a[-1:] )# "f" (from the last element to the end (default len())
print(a[3:1:-1]) # "dc" (from index 2 to None (default), in reverse order)
print(a[::-1] ) # "fedcba" (from last element (default len()-1), to first, in reverse order(-1))
print(a[5:None:-1]) # "fedcba" (this is equivalent to a[::-1])
print(a[5:0:-1]) # "fedcb" (from the last element (index 5) to second element (index 1)


print("----------------Reversing an object----------------")
s = 'reverse me!'
print(s[::-1]) # '!em esrever'

print("------------------------Basic Indexing------------------------")
arr = ['a', 'b', 'c', 'd']
print(arr[0])
print(arr[1])
print(arr[2])


