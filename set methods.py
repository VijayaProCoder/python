myset = {1, 2, 3}
print(myset)

# set of mixed datatypes
myset = {1.0, "Hello", (1, 2, 3)}
print(myset)


myset = {"apple", "banana", "cherry"}
print(myset)
print(len(myset))

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(set1)
set4=set1.union(set2)#union method
print(set4)
set5=set4.union(set3)
print(set5)
set1.update(set2)#update method
set5={1, 3, 8,}
set5=set5.intersection(set2)#intersection method 
print(set5)


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

