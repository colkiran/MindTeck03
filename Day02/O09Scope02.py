
glbX = 100

def fun(x):         # x is a local variable
    global glbX
    print(f"x inside fun :{x}")
    glbX = 10
    print(f"inside fun glbX :{glbX}")


print(f"glbX before function call :{glbX}")

fun(50)

print(f"glbX after function call :{glbX}")
