import time #importing time

print("code by @himanshuaryan".center(110))

t = time.strftime('%H:%M:%S') #import full time
timestamp = time.strftime('%H')
h = int(timestamp) #import hour
timestamp = time.strftime('%M')
m = int(timestamp) #import minutes
timestamp = time.strftime('%S')
s = int(timestamp) #import seconds

show = "Current Time"
print(show.center(60),'\n',t.center(57),'\n')

#define a function that input user name which should be between 3 and 16
def only_greet(name):
    while True:
        if len(name) < 3  or  len(name) > 16 :
            print("Name shiuld be between 3 and 16 words.")
            name = input("Your name : ").title()
        else:
            print("Welcome,", name.title() + '!')
            break
                
#define a function that check the current time of the system, send greeting
def timely_greet(name):
    if h>=6 and h<=11:
        if m>=00 or m<59:
            if s>=00 or s<59:
                print("Good Morning,",name+'!')
    elif h>=12 and h<=16:
        if m>=00 or m<59:
            if s>=00 or s<59:
                print("Good Afternoon,",name+'!')
    elif h>=17 and h<=21:
        if m>=00 or m<59:
            if s>=00 or s<59:
                print("Good Evening,",name+'!')
    elif h>=22 and h<=23:
        if m>=00 or m<59:
            if s>=00 or s<59:
                print("Good Night,",name+'!')
    elif h>=00 and h<=5:
        if m>=00 or m<59:
            if s>=00 or s<59:
                print("Good Night,",name+'!')
    else:
        print("Resfresh or Retry Again..")
        
name = input("Your Name : ").strip().title() #argument
timely_greet(name)

print("\n","calculator\n".upper().center(60))

only_greet(name)

#print(" ")

do = ["Addition","Subtraction","Multiplication","Division", "Square","Square Root","Cube","Cube Root"]
item = [x for x in range(1, len(do)+1)]
operations = dict(zip(item,do))
print("\nThis calculator will perform only below eperations : \n")
for k,v in operations.items():
    print(f"\t{k}. {v}")

print(' ')    
    
def calc(operation):
    
    a = int(input("\nEnter first number : ").strip()) #First number  
    b = int(input("Enter second number : ").strip()) #Secind Number
    
    if operation == item[0]:
        print("\n\tSum of",a, "and", b, ":", a+b) 
    elif operation == item[1]:
        print("\n\tSubtraction of",a, "and", b, ":", a-b) 
    elif operation == item[2]:
        print("\n\tMultiplication of",a, "and", b, ":", a*b)
    elif operation == item[3]:
        if a != 0 and b != 0:
            print("\n\tDivion of", a, "and",b,":",a/b) 
        else:
            print("\nZeroError : 0 is not valid in division.")
    elif operation == item[4]:
        print("\n\tSquare of", a, ":",a**2) 
        print("\tSquare of", b, ":",b**2) 
    elif operation == item[5]:
        print("\n\tSquare root of",a,":",round(a**0.5, 2))
        print(f"\tSquare root of {b} : {round(b**0.5, 2)}")
    elif operation == item[6]:
        print(f"Cube of {a} : {a**3}")
        print(f"Cube of {b} : {b**3}")
    elif operation == item[7]:
        print(f"Cube root of {a} : {round(a**(1/3), 2)}")
        print(f"Cube root of {b} : {round(b**(1/3),2)}")
    else:
        print("\nInvalid data, Please enter from the showing operations")

operation = int(input(f"Select from above(1-{len(do)}) : "))
calc(operation)

try:
    user = str(input("\nCalculate again? (YES/NO)\n").upper())
    while True:
        if user == "YES":
            operation = int(input(f"\nSelect from above(1-{len(do)}) : "))
            calc(operation)
            user = str(input("\nCalculate again? (YES/NO)\n").upper())
        elif user == "NO":
            print("\nHave a nice day!",name)
            break
            
except:        
    if user != "YES" or user != "NO":
        print("Type Error : YES or NO only")