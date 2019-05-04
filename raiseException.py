# %%
# from git hub
# try:
#     print("Ahoj"*10)
#     raise ValueError("exp was raise from clone repo")

# except Exception as ex:
#     print(ex)


# %%
# Handle exception with better performance
from timeit import timeit

codeToRun = """
def funcname():
    raise ValueError("test error")
    return None
funcname()
"""

print(timeit(codeToRun, number=10000000))

# %%
# raise exception is very cost better way retun none


# def methodWithNone(num: float):
#     if num == 0:
#         return None
#     print(1/num)


# print(methodWithNone(3.0))
