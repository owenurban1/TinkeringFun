#FUNCTIONS
#take inputs (arguments that are passed into the function 
#when you call it and parameters that are variables
#defined in the function header that store these incoming arguments)
#and produce outputs

#function stucture
#def function_name(parameter list) # header
#    body

#definition = function header + function body
#the body of the function does ont execute until the function is called

#example 1: no arguments or return value
def say_hello():
    print("hello")

say_hello() #function call
for _ in range (5):
    say_hello()

#example 2: one parameter and no return value)
def say(message):
    print(message)

    say("hi there")
    say("goodbye")
    say("pythong is awesome!")

def compute_area(radius):
    area = 3.14 * radius ** 2
    print("area", area)
compute_area(3) #3 is the argument

def compute_area2(radius):
    area = 3.14 * radius ** 2
    return area 
result = compute_area2(5)
print("result:", result)
print("result rounded:", round(compute_area2(5), 2))
def compute_area_and_circumference(radius):
    area = 3.14 * radius ** 2
    circumference = 2 * 3.14 * radius
    return area , circumference #tuple (immutable list has 2 elements)
results = compute_area_and_circumference(5)
print("results:", results)

def add(a, b):
    print(a + b)
add(2, 3)
#example 5: one parameter with a default argument
def print_even_numbers(stop=20):
    for j in range(2, stop, 2):
        print(j, end=" , ")
    print(j+2)

print_even_numbers(90)
print_even_numbers()
print_even_numbers(stop=10)



#wiofn