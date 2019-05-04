# %%
# from git hub
try:

    raise ValueError("exp was raise from clone repo")
    print("Hello world")
except Exception as ex:
    print(ex)
