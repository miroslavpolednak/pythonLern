# %%
# from git hub
try:
    print("Ahoj"*10)

    raise ValueError("exp was raise from clone repo")

except Exception as ex:
    print(ex)
