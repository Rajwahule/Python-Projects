#!/usr/bin/env python
# coding: utf-8

# In[6]:


def welcome_bot():
    #NetTech Welcoming you
    #Welcome user
    print("Welcome to NetTech")
    #ask user to its name
    user_name=input("Enter your name here: ")
    #greet user
    print("Hello",user_name)
    #ask user to its mobile number
    user_ph_no=input("Please Enter your phone number: ")
    #display users phone number
    print("user Phone number: ",user_ph_no)
    #Ask user to its email id
    user_email_id=input("Enter your email id here: ")
    #display users email ide
    print("User email id: ",user_email_id)
    #ask user to its preferred course
    user_pref_course=("Enter your preferred course here :")
    #display users preferred course here
    print("Users preferred course :",user_pref_course)
    #ask user to its preferred location
    user_pref_loc=("Enter your preferred location: ")
    #display users preferred location
    print("User preferred location: ",user_pref_loc)

def recommendation_bot():
    #Mumbai chai recommendation bot
    print("Welcome to city of garam garam chai | Amachi Mumbai")
    #ask user to its name
    user_name=input("Enter your name here :")
    #greet user
    print("Hello",user_name)
    #ask user to its budget
    user_budget=int(input("Enter your budget here:"))
    #<500 go to taj hotel
    if user_budget>500:
        print("Go to taj hotel")
    #100-500 go to udipi hotels
    elif user_budget>=100 and user_budget<=500:
        print("Go to udipi hotels")
    #20-50 go to prathamesh's cafe
    elif user_budget>=20 and user_budget<=50:
        print("Go to prathamesh's cafe")
    #5-20 go to tapari
    elif user_budget>=5 and user_budget<=20:
        print("Go to tapari | better than taj hotel")
    #5< go to simon
    else:
        print("Go to simon!")

def gk_quiz():
    #NetTech bot
    #Welcome user
    print("Welcome to India GK Quiz")
    user_q1=input("What is the national animal of india")
    
    if user_q1.lower()=="tiger":  #also here we are using upper() and capetalize()
        print("yes your answer is correct")
    
    else: 
        print("sorrry your answer is Incorrect")

def shopping_recommendation():
    #Welcome to Shopping budget recommendation bot
    print("Welcome to Shopping recommendation bot(Mumbai)!")
    #ask user to its name
    user_name=input("Enter your name here: ")
    #greet user
    print("Hello",user_name)
    #ask user to its budget
    budget=int(input("Enter your budget here: "))
    #<10000 go to mall
    if budget>=10000:
        print("Plese go to Mall for shopping")
    #5000-10000 go to Dmart for shopping
    elif budget>=5000 and budget<10000:
        print("Plese go to Dmart for shopping")
    #1000-5000  go to local shops
    elif budget>=100 and budget<5000:
        print("plese go to local shops")
    else:
        print(" Sorry No recommendation for this budget")

def heads_and_tails():
    #welcome to hedas and tails game
    print("Welcome to Heads & Tails game!")
    #check users choice heads or tails
    user_choice=input("Ente your choice here:")
    #display users choice
    print("you choose:",user_choice)
    #coin toss
    import random 
    if(random.choice("ht"))=='h':
        coin_toss="Heads"
    else:
        coin_toss="Tails"
    #display coin toss
    print("toss result:",coin_toss)
    #if user choice is equal to coin toss ---> you win
    if user_choice.lower()==coin_toss.lower():
        print("You win!")
    else:
        print("you lose!")
    #thank you messesge
    print("Thank you to play this game")

def dice_game():
    #Dice Game
    #Welcome to dice game
    print("Welcome to dice game!")
    #user roll dice
    user_roll=int(input("Enter your dice numbere here:"))
    if user_roll>=1:
        print("You chose",user_roll)
    else:
        print("No number in dice")
    #user roll dic
    import random
    dice_res=int(random.choice("123456"))
    #display user result
    print("Display user result", dice_res)
    #if dice res and user roll is equal --> you win
    if user_roll==dice_res:
        print("you win")
    else:
        print("you lose!")
    print("thank you for playing dice game")

def two_dice_game():
    #WElcome user
    print("Welcome to Two Dice Game!")
    #ask user to choose 1 input
    user_input=int(input("Enter your number here form 2 to 12: "))
    if user_input>=2 and user_input<=12:
        print("you choose",user_input)
        #roll dice
        import random
        dice_roll=(random.randrange(2,13))
        #display result
        print("display result",dice_roll)
        #if user choice3 is equal to dice roll --> you win
        if user_input==dice_roll:
            print("you win!")
        else:
            print("you lose!")

def multiplication_table():
    #Welcome to Multiplication table
    #WElcome user
    print("Welcome to Multplication Table of Mathematics!")
    #choose any number
    num=int(input("Enter your number here: "))
    #Display multiplication table
    for i in range(1,11):
        print(num,"x",i,"=",num*i)

def cube():
    #Welcome to cube dictonary
    #WElcome user
    print("Welcome to cube world!")
    #ask user to choose any number as a input
    num=int(input("Enter your number here: "))
    #diplsay cube of the number
    for i in range(1,num+1):
        print("cube of",i,"=",i**3)

def factorial():
    #Factorial
    #Welcome user
    print("Welcome to the world of factorial!")
    #aks user to take 1 numnber as a input
    num=int(input("Enter your number here: "))
    factorial=1
    #display the factorial of the number
    for i in range(1,num+1):
        factorial=factorial*i
    print("the factorial of the",i,factorial)

def fibonacci():
    #Fibonacci series
    #WElcome user
    print("WElcome to the world of fibonacci series!")
    #ask user to take 1 number as input
    num=int(input("Please Enter your number here: "))
    a=0
    b=1
    #display the fibonacci series
    for i in range(1,1+num):
        c=a+b
        print("The fibonacii series of the numbers",i,"=",c)
        a=b
        b=c

def password_generator():
    #Password generator by using string library
    #welcome user
    print("Welcome to the world of password generator")
    #ask user to length of the password
    len=int(input("Plese Enter the length of the password :"))
    if len>=8 and len<100:
        print("It is valid")
        #user random adn string library
        import random
        import string
        char=string.ascii_letters+string.digits+string.punctuation
        password=""
        #use for loop
        for i in range(len):
            password=password+(random.choice(char))
        print(password)
    
    elif len>=100:
        print("Plese Enter the less characters")
    else:
        print("Please Enter the more characters")

def countdown():
    from countdown import countdown
    
    # Create a countdown of 1 minute and 10 seconds
    countdown(mins=1, secs=10)
    
    # Create a countdown of 1 minute
    countdown(1)
    
    #Create a countdown of 10 seconds
    countdown(mins=0, secs=10)


def mind_game():    
    #mind Game
    #welcome user
    import time
    print("WElcome to th Mind guessing game!")
    #ask user to tis name
    name=input("Enter your name here:")
    #greet user
    print("Hello",name)
    #ask user to choose a number between 1 to 5000
    print("Guess a number in between 1 to 5000")
    time.sleep(3)
    #double the number
    print("okay now double the number")
    time.sleep(3)
    #add 50
    print("Okay! now add 50 into double number")
    time.sleep(3)
    #now divide the number by 2
    print("Nice! now divide the number by 2")
    time.sleep(3)
    #minus the guess number from original number
    print("okay! now minus guess number from original number")
    #answer
    print("I am thinking,,")
    time.sleep(3)
    print("your answer might be..")
    time.sleep(2)
    
    print("25")



      

#import tkinter library
import tkinter as tk
#creating a main window
window=tk.Tk()
#change title
window.title("Raj Wahule")
#size
window.geometry("730x500")
#label
tk.Label(window,text='pyhton project',font=("Helvetica",21),bg='black',fg='red').place(x=270,y=30)
tk.Label(window,text='Made by : Raj Wahule',font=("Helvetica",16,'bold')).place(x=220,y=100)

#Button
tk.Button(window,text='Welcome bot',command=welcome_bot).place(x=50,y=150,width=200,height=25)
tk.Button(window,text='Recommendation bot',command=recommendation_bot).place(x=270,y=150,width=200,height=25)
tk.Button(window,text='shoes Recommendation',command=shopping_recommendation).place(x=490,y=150,width=200,height=25)
tk.Button(window,text=' Gk Quiz',command=gk_quiz).place(x=50,y=200,width=200,height=25)
tk.Button(window,text=' Heads and tails game',command=heads_and_tails).place(x=270,y=200,width=200,height=25)
tk.Button(window,text='dice game',command=dice_game).place(x=490,y=200,width=200,height=25)
tk.Button(window,text='two dice game ',command=two_dice_game).place(x=50,y=250,width=200,height=25)
tk.Button(window,text='multiplication table',command=multiplication_table).place(x=270,y=250,width=200,height=25)
tk.Button(window,text='cube',command=cube).place(x=490,y=250,width=200,height=25)
tk.Button(window,text='factorail',command=factorial).place(x=50,y=300,width=200,height=25)
tk.Button(window,text='fiboancci',command=fibonacci).place(x=270,y=300,width=200,height=25)
tk.Button(window,text='countdown timer',command=countdown).place(x=490,y=300,width=200,height=25)
tk.Button(window,text='password generator',command=password_generator).place(x=50,y=350,width=200,height=25)
tk.Button(window,text='mind game',command=mind_game).place(x=270,y=350,width=200,height=25)

window.mainloop()


# In[4]:





# In[ ]:





# In[ ]:




