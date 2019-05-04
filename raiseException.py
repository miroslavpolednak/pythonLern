# %%
try:

    raise ValueError("exp was raise")
    print("Hy")
except Exception as ex:
    print(ex)
