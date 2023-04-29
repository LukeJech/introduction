num1 = 42 #declaring variable to an int
num2 = 2.3 #declaring variable to a float
boolean = True #declaring a variable to a boolean
string = 'Hello World' #declaring variable as a string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #declraing variable as a list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #declaring variable as a dictionary 
fruit = ('blueberry', 'strawberry', 'banana') #declaring variable as a tuple
print(type(fruit)) #printing type which is a tuple
print(pizza_toppings[1]) #printing to console the second item in the pizza topping array which is Sausage
pizza_toppings.append('Mushrooms') #adding mushrooms to our pizza topping array, gross!
print(person['name']) #printing the name key of person which will be John
person['name'] = 'George' #changing the person dictionary name key to George instead of John
person['eye_color'] = 'blue' #adding the eye_color key of person which will bet set to blue
print(fruit[2]) #printing third item of the tuple in fruit which is banana.

if num1 > 45:
    print("It's greater")
else:
    print("It's lower") #if else statement to show if num1 is less or greater than 45. will print it's lower

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!") 
else:
    print("Just right!") #checking the character length on the string which will print just right since hello world is in between 5 and 15

for x in range(5):
    print(x) #for loop that prints numbers 0 to 4
for x in range(2,5):
    print(x) #for loop that prints numbers 2 to 4
for x in range(2,10,3): #for loop that prints every third number from 2 to 9
    print(x)
x = 0 # declaring variable x and setting it to int 0
while(x < 5):
    print(x)
    x += 1 #while loop that prints x as it increments by 1 until it gets to 5

pizza_toppings.pop() #removes last item in pizza array
pizza_toppings.pop(1) #removes secpmd item in pizza array
print(pizza_toppings)

print(person) #prints the dictionary person
person.pop('eye_color') #pops the eye_color key from person 
print(person) #prints the dictionary person now without eye color

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break # for loop that will print the sentance as long as it's not Pepproni. Then loop will stop once Olives is the topping being iterated

def print_hello_ten_times():
    for num in range(10):
        print('Hello') #function that prints hello ten times duhhhh

print_hello_ten_times() #function called

def print_hello_x_times(x):
    for num in range(x):
        print('Hello') #function that prints hello x times based on the argument given

print_hello_x_times(4) #calls function and prints hello 4 times

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello') #function prints hello ten times unless an arguement is passed

print_hello_x_or_ten_times() #hello ten times
print_hello_x_or_ten_times(4) #hello four times


"""
Bonus section
"""

# print(num3) #nameError because num3 isn't define yet
# num3 = 72 
# fruit[0] = 'cranberry' #typeError tuple can't be changed
# print(person['favorite_team'])  #keyerror as there isn't a favorite_team in the dictionary 
# print(pizza_toppings[7]) IndexError as it's outside of range of pizza toppings list
#   print(boolean) Indent error
# fruit.append('raspberry') #AttributeError
# fruit.pop(1) #AttributeError