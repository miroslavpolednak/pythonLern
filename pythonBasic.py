# example of jupyter ipython notebook
# If you want debug notebook
# you can press shift + enter
# %%
import matplotlib.pyplot as plt
import numpy as np
# %%
# Create a list of evenly-spaced numbers over the range
x = np.linspace(0, 20, 1000)
plt.plot(x, np.sin(x))
plt.show()
# %%


def DoSomething(func, item: float) -> float:
    return func(item)


def multiple(x):
    return x*x


print(DoSomething(multiple, 4))
print(DoSomething(lambda x: (x*x) + (x*x), 2))

