
def greet():
    print(f"Greetings Mr.Sachin, Welcome to the event......")

def greetGst(gnames):
    for gname in gnames:
        print(f"Greetings Mr.{gname}, Welcome to the event........")

# city is called default argument and gname is called a non default argument
def greetGstCty(gname, city = "Mumbai"):
    print(f"Greetings Mr.{gname} from {city}, welcome to the event........")
greet()

print("-" * 60)

greetGst(["Rahul", 'yuvraj'])
# greetGst("Sourav")
print("-" * 60)

greetGstCty("Rohit")
greetGstCty("Hardik")
greetGstCty("Rahul", "Bangalore")

print("-" * 60)
# args and kwargs
def admsn(fname, lname, dob, gender, conno, emailid, city, addrs):
    print(f"Name        :{fname + " " + lname}")
    print(f"DOB         :{dob}")
    print(f"Gender      :{gender}")
    print(f"Contact no  :{conno}")
    print(f"email id    :{emailid}")
    print(f"city        :{city}")
    print(f"address     :{addrs}")

# args
admsn('John', 'Nixon', '15/08/1989', 'Male', '234234234', 'john@gmail.com', 'California', '8th cross, First Lane, building no 10')

print("-" * 60)
# kwargs
admsn(city='Newyork', conno='934723984', gender='Female', lname='Tuner', emailid='tina@gmail.com', dob='23/04/1991', fname='Tina', addrs='1st lane, building no 45, 6th floor')

print("-" * 60)
# variable length args

def prodAll(*numbers):
    print(numbers)
    print(*numbers)         # unpack
    prod = 1
    for number in numbers:
        prod *= number
    return prod


print(prodAll(1, 2, 3, 4, 5))

print("-" * 60)

def extractDetials(**details):
    print(details)
    print("-" * 60)
    for k, v in details.items():
        print(k, "=>", v)


extractDetials(name="Rohit", age=38, runs=125, oppn='Aus', venue='Perth')

print("-" * 60)
# return

def multiplyMe(x, y):
    return x * y

i = 20
j = 8
print("%i * %i = %i" % (i, j, multiplyMe(i, j)))

print("-" * 60)

def arithCalc(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    return sum, diff, prod, quot

res = arithCalc(20, 8)
print(f"res :{res}")

print("-" * 60)
# python supports recursive calls
def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n - 1)

i = int(input("Enter the number :"))
print(f"The factorial of {i} is :{fact(i)}")

print("-" * 60)

"this is first line"

def fun():
    # This is a comment
    "This is a doc string"
    print("Hello World")

fun()
print(fun.__doc__)      # doc string
print("-" * 60)

def fun1(x, y):
    """
    fun1(x, y)

    if x and y are integers then the function fun will return the sum of the numbers
    if x and y are strings the function will concatenate and return the string
    if x and y are of different data types then it returns error
    """
    return x + y

print(fun1(10, 20))

print("-" * 60)
print(fun1("hello ",  "world"))

print("-" * 60)
# print(fun1(100, "abc"))

help(fun1)


