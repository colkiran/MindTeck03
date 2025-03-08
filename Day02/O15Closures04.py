"""
whenever a function takes another function as argument or returns a function as a reference then we call it as HOF - Higher Order Function

"""
def fun(*args):
    print(args)
    # print(*args)


fun()
fun(10)
fun(10, 20)
fun(10, 20, 30)
print("-" * 60)


def sum(x, y):
    print(f"adding {x} and {y}")
    return x + y

def diff(x, y):
    print(f"difference of {x} and {y}")
    return x - y

def logDetials(fnc):
    logInfo = "Logging into a service....."
    def helper(*args):
        print(logInfo)
        print(fnc(*args))               # call back
        print("-" * 60)

    return helper


sumlogger = logDetials(sum)
sumlogger(10, 20)

print("-" * 60)

difflogger = logDetials(diff)
difflogger(20, 8)
