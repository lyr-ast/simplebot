#!/usr/bin/env python
import webbrowser
import pyautogui
import os
import time
import datetime
import wikipedia
import random
finnished = False
def greet():
    now = datetime.datetime.now()
    hour = now.hour
    if hour < 12:
        greeting = "Good morning"
    elif hour < 16:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"
    print("{}!".format(greeting))
    print("I am AP214, your personal assistant")
    time.sleep(0.5)
def Time():
    try:
        t = datetime.datetime.now()
        print(f"The curent time is {t}")
    except:
        print("An error occured")
    
def add():
    try:
        num = input("How many numbers?> ")
        num = int(num)
        count = 0
        for i in range(num):
            a = input(f"What is number {i}> ")
            a = float(a)
            count = a + count
        print(f"The answer is {count}")
    except:
        print("an error occured")
def subtract():
    try:
        num = input("How many numbers?> ")
        num = int(num)
        num = num - 1
        count = 0
        num1 = input("number> ")
        num1 = int(num1)
        for i in range(num):
            a = input("number> ")
            a = float(a)
            #count = a + count
            num1 = num1 - a
        print(f"The answer is {num1}")
    except:
        print("an error occured")
def multiply():
    try:
        num = input("How many numbers?> ")
        num = int(num)
        count = 1
        for i in range(num):
            a = input(f"What is number {i}> ")
            a = float(a)
            count = a * count
        print(f"The answer is {count}")
    except:
        print("an error occured")
def divide():
    try:
        num = input("How many numbers?> ")
        num = int(num)
        num = num - 1
        num1 = input("number> ")
        num1 = int(num1)
        for i in range(num):
            a = input("number> ")
            a = int(a)
            num1 = num1 / a
        print(f"The answer is {num1}")
    except:
        print("an error occured")
def passwd():
    try:
        p_l = int(input("What's the lenght of the password> "))
        if p_l > 20 or p_l < 6:
            print("error generating password")
        else:
            print("Genrating password...")
            time.sleep(2)
            c = ""
            for i in range(p_l):
                a = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()")
                c = c + a
            print(f"Your password is {c}")
    except:
        print("an error occured")
def link():
    try:
        i = input("Enter the url you want to open> ")
        print(f"Opening {i}...")
        webbrowser.open(i)
    except:
        print("an error occured")
def search():
    try:
        a = input("what do you want to search> ")
        # time.sleep(5)
        # print(pyautogui.position())
        print("select the search engine:")
        print("""
        [1] Google
        [2] Bing
        [3] Yahoo
        [4] duckduckgo
        """)
        b = int(input("choose a number from above> "))
        if b == 1:
            print("searching google...")
            webbrowser.open("google.com")
            time.sleep(5)
            pyautogui.typewrite(f"{a}\n")
        if b == 2:
            print("searching Bing...")
            webbrowser.open("bing.com")
            time.sleep(5)
            pyautogui.typewrite(f"{a}")
            pyautogui.typewrite("\n")
        if b == 3:
            print("searching yahoo...")
            webbrowser.open("yahoo.com")
            time.sleep(5)
            pyautogui.typewrite(f"{a}\n")
        if b == 4:
            print("searching duckduckgo...")
            webbrowser.open("duckduckgo.com")
            time.sleep(5)
            pyautogui.typewrite(f"{a}\n")
    except:
        print("an error occured")
def wki():
    try:
        a = input("What should I search for> ")
        print('Searching Wikipedia...')
        results = wikipedia.summary(a, sentences=5)
        print("According to Wikipedia")
        print(results)
    except:
        print("try searching for something else")
def scroll():
    try:
        print('Press Ctrl-C to quit.')
        pyautogui.FAILSAFE = True
        pyautogui.PAUSE = 8
        while True:
            pyautogui.scroll(-5)
    except:
        print("exited")
greet()
while True:
    comm = input("What would you like me to do> ")
    comm = comm.lower()
    if comm == "exit":
        break
    elif comm == "add":
        add()
    elif comm == "subtract":
        subtract()
    elif comm == "multiply":
        multiply()
    elif comm == "divide":
        divide()
    elif comm == "password":
        passwd()
    elif comm == "time":
        Time()
    elif comm == "open link":
        link()
    elif comm == "search":
        search()
    elif comm == "wikipedia":
        wki()
    elif comm == "scroll":
        scroll()
    else:
        try:
            results = wikipedia.summary(comm, sentences=5)
            print("According to Wikipedia")
            print(results)
        except:
            print(f"I didn't understand {comm}")