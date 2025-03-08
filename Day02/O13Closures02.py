
def outerFun(greet):

    # simple curry
    def innerFun(gname):

        print(greet, gname)

    return  innerFun

inref = outerFun("Welcome")
kanGrt = outerFun("Namaskara")

inref("Sachin")
kanGrt("Anil")