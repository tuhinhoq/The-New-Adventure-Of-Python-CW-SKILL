# Day-4
#Creating String
letter='T'
print(letter)
print(len(letter))

greeting="I hope you are well"
print(len(greeting))

greetings='''Hi Iam Tuhin
from Dhaka'''
print(greetings)


first_name='Tuhin'
last_name='Hoque'
space=' '
age=36
flt=3.165487

print(first_name+space+last_name)
print(len(first_name+space+last_name))


print('I am Tuhin.\n I love \\programming \t ever')
print('Date \t Month \t Year')
print('01 \t 01 \t 2026')
print('------------------------------------------')

print('I am %s %s & %d years old. GPA: %.2f'%(first_name,last_name,age,flt))  # <--- Very Important

#format

print('I {} & {} years old'.format(first_name,age))

num_1=10
num_2=10

print('Sum {} + {}={}'.format(num_1,num_2, num_1+num_2))
print('Sub {} - {}={}'.format(num_1,num_2, num_1-num_2))
print('Multi {} * {}={}'.format(num_1,num_2, num_1*num_2))
print('Divi {} / {}={}'.format(num_1,num_2, num_1/num_2))
print('Mod {} % {}={}'.format(num_1,num_2, num_1%num_2))

print('------------------------------------------')




language='PYTHON'

a,b,c,d,e,f=language
print(a,b,c,d,e,f)

f_3=language[1:3]

print(f_3)

msg="Hi I'm Tuhin"
print(greetings.count('T'))
print(greetings.endswith('a' or 'b'))
print(msg.find('i'))
print(greeting.split())
print(msg.swapcase())
print(msg.replace("Tuhin","Python"))
print(msg.upper())
print(msg.lower())

print('------------------------------------------')