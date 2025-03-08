
def outerFun():
    gname = "Sachin"            # local variable

    def innerFun():
        nonlocal gname        # ONLY LOCAL VARIABLES CAN BE CONVERTED INTO NON LOCAL

        gname += " Tendulkar"
        print("Hello World")
        print(f"Greetings Mr.{gname}, Welcome to the event.....")

    innerFun()

outerFun()

