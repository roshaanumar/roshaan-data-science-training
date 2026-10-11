#def greeting(name, age, dept):
    #print("Welcome, " + name)
    #print("Age: " + str(age))
    #print("Department: " + dept)
#greeting("Roshaan Umar", 30, "IT")
#def sum(num1, num2):
    #return num1 + num2
#sum1= sum(1, 2)
#sum2= sum(3, 4)
#sum3= sum1 + sum2
#print(sum3)
def lucky_number(name):
    number= len(name) * 9
    #print("Hello " + name + ". Your lucky number is: " + str(number))
lucky_number("Roshaan Umar")

def area_rectangle(l):
    w= 2
    area= l*w
    return area

result=area_rectangle(2)
#print(result)

def username(name):
    if len(name)<3:
        print("Invalid name. Name must be at least 3 characters long.")
    elif len(name)>15:
        print("Invalid name. Name must be at most 15 characters long.")
    else:
        print("Valid name. Welcome, " + name + "!")   

username("Roshaan Umar")