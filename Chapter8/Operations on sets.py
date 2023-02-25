print("Union")
a={1, 2, 3, 4, 5}
b={3, 4, 5, 6}
c= a.union(b) # or c= a|b   -->the result of union contain the unic values, it will not written repeated values. 
print("set a contain:",a)
print("set b contain:",b)
print("The union operation result:",c) # {1, 2, 3, 4, 5, 6}
print("\n")

print("Intersection") 
a={1, 2, 3, 4, 5}
b={3, 4, 5, 6} 
c= a.intersection(b) # or c= a & b  --> the result of interaction conatin the common between a and b
print("set a contain:",a)
print("set b contain:",b)
print("The Intersection operation result:",c)  # {3,4,5}
print("\n")

print("Difference")
c={1, 2, 3, 4}.difference({2, 3, 5}) #or c={1, 2, 3, 4} - {2, 3, 5}
print("The Difference operation result:",c)# {1, 4}
print("\n")

print("Symmetric difference")
c={1, 2, 3, 4}.symmetric_difference({2, 3, 5}) #  c={1, 2, 3, 4} ^ {2, 3, 5}   ->This will remove common between a and b
print("The Symmetric difference operation result:",c) # {1, 4, 5}
print("\n")

print("Superset check")
c={1, 2}.issuperset({1, 2, 3}) # {1, 2} >= {1, 2, 3} 
print("The Superset check operation result:",c) #False
print("\n")

print("Subset check")
c={1, 2}.issubset({1, 2, 3}) # {1, 2} <= {1, 2, 3} # True 
print("The Subset check operation result:",c)  # True
print("\n")

print("Disjoint check")
c={1, 2}.isdisjoint({3, 4}) # True
d={1, 2}.isdisjoint({1, 4}) # False
print("The Disjoint check operation result:",c) 
print("The Disjoint check operation result:",d) 
print("\n")
print("-----------------------------\n")

print("with single elements\n")
print()

print("Existence check")
a=2 in {1,2,3} # True
b=4 in {1,2,3} # False
c=4 not in {1,2,3} # True
print("result of a",a)
print("result of b",b)
print("result of c",c)
print()

print("Add and Remove")
s = {1,2,3}
print("result of s:",s)
s.add(4) # s == {1,2,3,4}
print("result of s:",s)
s.discard(3) # s == {1,2,4}
print("result of s:",s)
s.discard(5) # s == {1,2,4}
print("result of s:",s)
s.remove(2) # s == {1,4}
print("result of s:",s)
#s.remove(2) # KeyError!with single elements
print()


print("Existence check") 
a=2 in {1,2,3} # True
b=4 in {1,2,3} # False
c=4 not in {1,2,3} # True
print("result of a",a)
print("result of b",b)
print("result of c",c)
print()

print("Add and Remove")
s = {1,2,3}
print("result of s:",s)
s.add(4) # s == {1,2,3,4}
print("result of s:",s)
s.discard(3) # s == {1,2,4}
print("result of s:",s)
s.discard(5) # s == {1,2,4}
print("result of s:",s)
s.remove(2) # s == {1,4}
print("result of s:",s)
#s.remove(2) # KeyError!
