# def sqr(number):
#     res=number*number
#     print("Result of square=",res)

# inp=int(input("Enter the number: "))
# sqr(inp)

# p,q,r = 5,10,15
# print(p,q)

# p,q=q,p
# print(p,q)


def getdata(m1,m2,m3):
    print("Enter your details\n")
    
    msg1="Enter your name: "
    msg2="Enter your age: "
    msg3="Enter your salary: "
    
    name = input(msg1) # string
    age = int(input(msg2))  # integer
    salary = float(input(msg3)) # float    
    display(name,age,salary)

    def display(name,age,salary):
    print("Hello ",name," as your age is ",age," and your salary is ",salary," so we offer you the loan.")

getdata()