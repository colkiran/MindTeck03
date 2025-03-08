
def outerFun(greet):

    def innerFun(sep):

        def innerMostFun(gname):
            from emojis import emojis

            emojized = emojis.encode(greet + " :" +  sep + ": " + gname)
            print(emojized)

        return innerMostFun

    return innerFun

kanGrt = outerFun("Namaskara")

kanGrtTgr = kanGrt("tiger")

kanGrtTgr("Prabhakar")





"""
outerFun("Welcome")("---->")("Sachin")

print("-" * 60)

engGrt = outerFun("Hello")
kanGrt = outerFun("Namaskara")

engGrtSngArw = engGrt("----->")
kanGrtDblArw = kanGrt("=====>>")

engGrtSngArw("Sachin")
engGrtSngArw("Virat")

kanGrtDblArw("Anil")
kanGrtDblArw("Rahul")
"""