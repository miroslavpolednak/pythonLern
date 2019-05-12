# This is message from github

# text: str = "Hello \""
# text2: str = "from python"
# message: str = f"{text} {len(text)} {text2} {6+6}"
# multiText: str = """Multi
# text
# line
# """
# x: list = [1, 2, 3]
# x.append(55)
# isTrue = True
# if isTrue:
#     print(message[0:] * 2)
#     print(x[0:2])
#     print(x)
#     print(multiText)

# numbers convert from string
# int(x)
# float(x)
# bool(x)
# str(x)


# x = input("x:")
# if not x:
#     print("imput is empty")
# else:
#     y = 1 + float(x)
#     if y > 10:
#         print(y)
#         print(x)
#     elif y <= 10:
#         print("lower than 10")

# if  10<= x < 50:
#     pass  # pass do nothing, but if statement cannot be empty
# else:
#     pass

# # and or operators

# for item in range(5, 10):
#     print(item)

# for item in range(0, 9, 3):
#     print(item)
# if x.isdigit:
#     print("x is not a number")
# elif 10 <= float(x) < 20:
#     print("between")
# else:
#     print("end")


from Modules.Ecommerce.Sales import calcTax


def multiple(*items):
    total: int = 1
    for item in items:
        total *= item
    return total


def fizzBuzz(input: float):
    if input % 3 == 0 and input % 5 == 0:
        return "FizzBuzz"
    elif input % 3 == 0:
        return "Fizz"
    elif input % 5 == 0:
        return "Buzz"
    else:
        return input


print(fizzBuzz(15))

# def increment(number: int, by: int = 1) -> tuple:
#     return (number, number + by)


# print(multiple(1, 2, 3, 4, 5, 6))

print(calcTax())
