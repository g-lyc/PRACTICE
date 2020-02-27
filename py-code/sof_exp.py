#!usr/bin/python
import random

def takeshot(prompt='do you want to take shot?\n'):
    answer = raw_input(prompt)
    if answer in ['yes','y']:
        print("taking shot...")
    else:
        print("not-working")

def cal(randomnum = random.randrange(0, 100) , baseaim = 15):
    totalaim = randomnum + baseaim
    return totalaim

def hitormiss(totalaim,hit=50):
    if totalaim >= hit:
        print("You have hit your target!")
    elif totalaim < hit:
        print("You have missed your target!")
    else:
        print("Revise Code.")

takeshot()
hitormiss(cal())
