import random
import csv

def password():
    char="abcdefghijklmnopqrstuvwxyz"
    specialchar="£$%^&*@~#?/\!"
    numbers="0123456789"

    password= ""
    length= random.randint(10,12)
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
    return password

def store(password,username):
    filename= "table.csv"
    rows=[]
    with open(filename, "a+") as file:
        file.write(f"\n{username},{password}")
