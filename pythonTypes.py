
# %%
from pprint import pprint as pr
from sys import getsizeof
from collections import deque
# queue exampel
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
# remove item with zero index (left side)
startItem = queue.popleft()
queue.append(4)
print(queue, startItem)
# %%
# Tuples read only collection
points1 = (1, 2, 3, 4)
points2 = 4, 5, 6
points3 = 5,
points4: float = 100
x, y, z = points2
print(type(points1), type(points2), type(points3), points4)
# %%
y, y, z = points2
print(x, y, z)
if 6 in points1:
    print("Y")
# %%
# swap variables
x = 10
y = 20
x, y = y, x
print("X=", x, "Y=", y)

# %% Python sets is collection with no duplicates
numbers = [1, 2, 3, 4, 5, 5, 5, 7]
unique = set(numbers)
setDefinition = {1, 2, 2, 7, 8}
# print(unique, setDefinition)

setUnion = unique | setDefinition
setIntersection = unique & setDefinition
twoSetsDifferents = unique - setDefinition
print(setUnion, setIntersection)
print(twoSetsDifferents)
# %%
# Dictionary
cell = {"a": 10, "b": 20}
# or
cell2 = dict(a=10, b=20)
print(cell)
print(cell2)
# %%
# get not existing key
if "a" in cell2:
    print("exist")
# or
print(cell.get("Z"))
print(cell2.get("d", 0))
# %%
# comprehention
items = []
for item in range(5):
    items.append(item**2)
print(items)

# better implemention
items2 = [item**2 for item in range(1000)]
# %%
# generation object is good for large dataset, in each
# iteration create a value
gerObj = (item**2 for item in range(1000))
print("generation obj", getsizeof(gerObj))
print("list obj", getsizeof(items2))
# %%
# Unpacking operator same as spread operator in Js ... in
# python is *
listOfNum = [1, 2, 3]
print(listOfNum)
print(*listOfNum)

# %%
# join two list
firstList = [1, 2, 3]
secondList = [4, 5, 6]
joinList = [*firstList, *"Ahoj", *secondList]
print(joinList)


# %%
# Unpacking dictionary
dictioOfPoint = dict(c=10, f=20)
dictioOfPoint2 = dict(c=2, t=50)
joinDictio = {**dictioOfPoint, **dictioOfPoint2, "zz": 120}
print(joinDictio)


# %%
# Task find char with biggest occurrence
testString = "This is a common interview question"
listOfChar = [*testString]

listOfWords = testString.split(" ")
print(listOfWords)
# %%
discWithNumberOfChar = {}
for char in listOfChar:
    if char in discWithNumberOfChar:
        discWithNumberOfChar[char] += 1
    else:
        discWithNumberOfChar[char] = 1

maxInDisc = max(discWithNumberOfChar, key=discWithNumberOfChar.get)
pr(discWithNumberOfChar, width=1)
print("Max is: ", maxInDisc, "with number of ocurr: ",
      discWithNumberOfChar[maxInDisc])
# [discWithNumberOfChar[item]+=1 for item in listOfChar]
# print(discWithNumberOfChar)
