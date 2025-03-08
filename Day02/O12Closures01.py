
def outerFun():
    gname = "Sachin"

    def innerFun():

        print("Hello World")
        print(gname)

    return innerFun

outerFun()()                # call inner1Fun

print("-" * 60)
inref = outerFun()

print("-" * 60)
# some other code
# after few lines of code

print("hello world \n" * 5)


inref()    # we have already lost the scope or outerFun
