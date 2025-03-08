

def fun(x):                     # x is a local variable
    print(f"inside fun x :{x}")
    y = "hello world"           # y is a local variable
    print(f"inside fun y :{y}")

fun(100)

# print(f"the value of x outside fun :{x}")
# print(f"the value of y outside fun :{y}")