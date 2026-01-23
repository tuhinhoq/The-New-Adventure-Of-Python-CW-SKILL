num_1=10
num_2=20

print('Addition Num1 & Num2=', num_1+num_2) # num1+=num2 -> num1=num1+num2
print('Subtraction Num1 & Num2=', num_1-num_2) # num1-=num2 -> num1=num1-num2
print('Multiplication Num1 & Num2=', num_1*num_2) # num1*=num2 -> num1=num1*num2
print('Division Num1 & Num2=', num_1/num_2) # num1/=num2 -> num1=num1/num2
print('Modulus Num1 & Num2=', num_1%num_2)  # num1%=num2 -> num1=num1%num2
print('Modulus Num1 & Num2=', num_1%num_2)  # num1//=num2 -> num1=num1//num2

print('-------------ALT-------------')

num_1+=num_2
print('Add:',num_1)
num_1-=num_2
print('Sub:',num_1)
num_1*=num_2
print('Mul:',num_1)
num_1/=num_2
print('Div:',num_1)
num_1%=num_2
print('Mod:',num_1)

print('-------------COMPARISON-------------')

print(num_1>num_2)
print(num_1<num_2)
print(num_1>=num_2)
print(num_1<=num_2)
print(num_2>num_1 and num_2>5)
print(num_1==num_2 or num_2==20)
print(not(num_2==20))
print(num_1!=num_2)

# Calculating area of a circle
radius=10
area_of_circle=3.14*radius**2
print('Area_Of_Circle', area_of_circle)

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')                         

