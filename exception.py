# example of exception
# %%
try:
    inputValue = int(input("Age:"))
    xFactor = 10/inputValue
except Exception as ex:
    print("Age have to be number")
    print(ex)
    print(type(ex))

# print("Age is", inputValue)

# %%
from pprint import pprint as pr
try:
    file = open("App.py")
    fileContent = file.readlines()
    pr(fileContent, width=80)
    ageVal = 0
    factor = 10/ageVal
except Exception as ex:
    print(ex)
    print(type(ex))
finally:
    file.close()


# %%
# example of using block alternative in python: with clousule.
# Idisposible : object has two magic methods __enter__ and __exit__
try:
    with open("App.py") as file:
        for line in file.readlines():
            if line.strip():
                print(line)

except Exception as ex:
    print(ex)


# %%
# raise exception
