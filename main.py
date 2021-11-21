from replit import db
import random
import math
import time
import os
import sys
import art
import colorama
from colorama import Fore
print(Fore.GREEN)
#print(os.getenv("REPLIT_DB_URL"))
clear = lambda: os.system('clear')
#clear()
def larprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1/1200)
def checkNum(thing):
  while True:
    try:
      money = float(input("How much money would you like to {}?: ".format(thing)))
      return money
    except:
      print()
      print("That is not a valid amount. Please try again.")
      print()
larprint(art.welcome)
for a in range (1,5,1):
  print()
newOld = input("Are you a new or returning user? (N/R): ").upper()
while (newOld != "N" and newOld != "R"):
  print()
  print("You did not enter a valid option.")
  newOld = input("Are you a new or returning user? (N/R): ").upper()
check1 = 0
while (newOld == "R"):
  if check1 == 0:
    print("\nWelcome Back!")
  user = input("\nPlease enter your username: ")
  password = input("Please enter the corresponding password: ")
  if user and password in db["storeUser"]:
    user,password,name,money = db["storeUser"]
    print("\nWelcome back {}!".format(name))
    print("Please press enter to continue:")
    input()
    num1 = 0
    break
  else:
    print("\nAccount not found.")
    check1 +=1
else:
  print("\nWelcome!")
  user = input("\nPlease enter a username: ")
  while user in db["storeUser"]:
    print("Sorry. The username {} was already taken.".format(user))
    user = input("\nPlease enter a username: ")
  password = input("Please enter a password: ")
  name = input("Please enter your name: ")
  money = 0
  db["storeUser"] = user,password,name, money
  print("\nCongratulations on creating an account!")
  print("Please press enter to continue:")
  input()
  num1 = 1
clear()
if num1 == 1:
  larprint(art.bank)
  for skip13 in range (1,5,1):
    print()
  while True:
    try:
      money = float(input("How much money would you like to deposit?: "))
      break
    except:
      print()
      print("That is not a valid amount. Please try again.")
      print()
  print()
  print("Excellent. Your account is all set. Please press enter to continue: ")
  input()
  clear()
larprint(art.bank)
for skip23 in range (1,5,1):
  print()
choice = 0
while (choice != 5):
  print("The current balance on your card is ${:.2f}".format(money))
  print()
  print("{:<15}".format("1. Make a deposit/withdrawal"))
  print("{:<15}".format("2. Take out a loan"))
  print("{:<15}".format("3. Deposit or write a check"))
  print("{:<15}".format("4. Apply for a credit card"))
  print("5. Close the program")
  print()
  while True:
    try:
      choice = int(input("What would you like to chose?: "))
      while (choice < 1 or choice > 5):
        print()
        print("That is not a valid option. Please try again.")
        print()
        choice = int(input("What would you like to chose?: "))
      break
    except:
      print()
      print("That is not a valid option. Please try again.")
      print()
  if choice == 1:
    print()
    print("Would you like to deposit or withdraw money from your account?")
    choice1 = input("(deposit/withdraw): ")
    while (choice1 != "deposit" and choice1 != "withdraw"):
      print()
      print("That is not a valid option. Please try again.")
      print()
      print("Would you like to deposit or withdraw money from your account?")
      choice1 = input("(deposit/withdraw): ")
    if choice1 == "deposit":
      print()
      thingy = "deposit"
      dep = (checkNum(thingy))
      money += dep
      print()
    else:
      print()
      thingy = "withdraw"
      wit = (checkNum(thingy))
      money -= wit
      print()
  if choice == 2:
    print()
    thingy = "take out a loan for"
    loan = checkNum(thingy)
    money += loan
    print()
  if choice == 3:
    print()
    print("Would you like to deposit or write a check?")
    choice1 = input("(deposit)/(write): ")
    while (choice1 != "deposit" and choice1 != "write"):
      print()
      print("That is not a valid option. Please try again.")
      print()
      print("Would you like to deposit or write a check?")
      choice1 = input("(deposit)/(write): ")
    if choice1 == "deposit":
      print()
      checkName = input("Who was the sender of the check: ")
      thingy = "deposit from the check"
      dep = (checkNum(thingy))
      money += dep
      print()
    if choice1 == "write":
      print()
      checkName1 = input("Who would you like the write the check for: ")
      thingy = "write the check for"
      chec = (checkNum(thingy))
      money -= chec
      print()
  if choice == 4:
    clear()
    print("CodeMaster's credit card service")
    print()
    while True:
      try:
        print()
        creditscore = int(input("How much is your current credit score?:  "))
        break
      except:
        print()
        print("That is not a valid amount. Please try again.")
    while True:
      try:
        print()
        age = int(input("Enter your current age: "))
        break
      except:
        print()
        print("That is not a valid age. Please try again.")
    while True:
      try:
        print()
        social = int(input("Enter your current social security number: "))
        break
      except:
        print()
        print("That is not a valid number. Please try again.")
    print()
    num1 = input("Do you have a stable source of income? (y/n): ").upper()
    while (num1 != "Y" and num1 != "N"):
      print()
      print("That is not a valid option.")
      num1 = input("Do you have a stable source of income? (y/n): ")
      print()
    print()
    if creditscore <= 750 or age < 21 or num1 == "N":
      print("You are ineligible to issue for a credit card. Sorry for the inconvenience.")
    else:
      print("You are eligible to issue for a credit card.")
      print()
      print("Your credit card number is", end = " ")
      for i in range (1,5,1):
        credNum = random.randint(0,9999)
        if i <= 3:
          print(credNum, end = " ")
        else:
          print("{}.".format(credNum))
    print()
    print("Press enter to continue: ")
    input()
  clear()
larprint(art.end)