import random

char="abcdefghijklmnopqrstuvwxyz"
specialchar="£$%^&*@~#?/\!"
numbers="0123456789"

password= ""
length= random.randint(10,12)
cache_length=length
while length>0:
    choice= random.randint(1,2)
    match choice:
        case 1:
            password+=char[random.randint(0,24)]
        case 2:
            password+=char[random.randint(0,24)].upper()
    length-=1
    password+=specialchar[random.randint(0,12)]
    length-=1
    password+=numbers[random.randint(0,9)]
    length-=1

print(f"Your password is {password} with a length of {cache_length} char")