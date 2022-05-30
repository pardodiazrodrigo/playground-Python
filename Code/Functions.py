#function = a block of code which is executed only when it is called.

def hello(first_name,last_name,age):
    print("hello "+first_name+" "+last_name)
    print("You are "+str(age)+" years old")
    print("Have a nice day!")

hello("Rodrigo","Pardo",30)


#return statement = Functions send Python values/objects back to the caller.
#                    These values/objects are known as the function’s return value

def multiply(number1,number2):
    return number1 * number2

x = multiply(6,8)

print(x)

#python #keyword #arguments

# keyword arguments =   arguments preceded by an identifier when we pass #                                           them to a function
#                                           The order of the arguments doesn't matter, unlike  #                                           positional arguments
#                                           Python knows the names of the arguments that     #                                           a function receives

def hello(first,middle,last):
    print("Hello "+first+" "+middle+" "+last)


hello(last="Code",middle="Dude",first="Bro")

# ========================================================
# scope = The region that a variable is recognized
#         A variable is only available from inside the region it is created.
#         A global and locally scoped versions of a variable can be created

name = "Bro" # global scope (available inside & outside functions)

def display_name():
    name = "Code"    # local scope (available only inside this function)
    print(name)


display_name()
print(name)


# *args =   parameter that will pack all arguments into a tuple
#                 useful so that a function can accept a varying amount of arguments

def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(add(1,2,3,4,5,6,7,8))

# **kwargs =   parameter that will pack all arguments into a dictionary
#                        useful so that a function can accept a varying amount of        #                        keyword arguments

def hello(**kwargs):
    #print("Hello " + kwargs['first'] + " " + kwargs['last'])
    print("Hello",end=" ")
    for key,value in kwargs.items():
        print(value,end=" ")


hello(title="Mr.",first="Bro",middle="Dude",last="Code")