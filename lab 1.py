import string
import random
import time

def q1():
    name = input("Enter your name : ")
    age = int(input("Enter your age : "))
    year100 = (100 - age)+2021
    print (f"Hi {name}, you will reach 100 years old in {year100}")

def q2():
    num = int(input("enter number : "))
    if  num%2==0 :
        print(f"{num} is an even number")
    else :
        print(f"{num} is an odd number")

def q3():
    a = [1,1,2,3,5,8,13,21,34,55,89]
    for x in a :
        if x<5 :
            print(x)

def q4():
    x = int(input("enter a number : "))
    for y in range (1,x+1) :
        if x%y==0 :
            print(y,end=" ")

def q5():
    a = [1,1,2,3,5,8,13,21,34,55,89]
    b = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    c = []
    for i in a:
        for j in b:
            if i==j:
                c.append(i)

    print(c)

def q6():
    a = input("enter a word : ")
    check = 0
    for i in range(0, int(len(a)/2)):
        if a[i] != a[len(a)-i-1]:
            check = 1
    if check == 0:
        print("it is palindrome")
    else :
        print ("it is not palindrome")

def q7():
    a=[1,4,9,16,25,36,49,64,81,100]
    b=[]
    for x in a:
        if x%2==0:
            b.append(x)
    print(b)

def q8():
    p1=input("Player 1 enter rock, scissor or paper : ").lower()
    p2=input("Player 2 enter rock, scissor or paper : ").lower()

    a=convert(p1)
    b=convert(p2)

    if(a==b):
        print("draw")
    elif(a==0 and b==2) or (a==2 and b==1) or (a==1 and b==0):
        print("Player 2 Win")
    elif(b==0 and a==2) or (b==2 and a==1) or (b==1 and a==0):
        print("Player 1 Win")

    answer = input("Start a new game? (Y/N) ").lower()
    if answer=="y":
        q8()


def convert(x):
    if x == "rock":
        return 0
    elif x == "scissor":
        return 1
    elif x == "paper":
        return 2
    else:
        return False

def q9():
    x = random.randint(1,9)
    print(x)
    num = int(input("Guess the generated number (1-9) : "))
    y= x-num
    if y==0:
        print("you guessed right")
    elif y>0:
        print("you guessed too low")
    elif y<0:
        print("you guessed too high")

def q10():
    x = int(input("Enter a number"))

