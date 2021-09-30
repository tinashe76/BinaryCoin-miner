# Binary Coin Miner ver 1.
# Created by tinashe76 => github

import turtle
from data import watcher
import psutil		# This is a module for reading system hardware stats like CPU frequency and Memory Usage
import platform		# This is a module for reading platform information like OS of the system , manufacturer etc
import random


log = open("log.txt", "w") # We are going to use this file to print the Specifications of the System
profit = open("profit.txt", "w") # We are going to use this file to print the profit and withdrawal code.
uname = platform.uname() # OS name
cpufreq = psutil.cpu_freq() # CPU frequency

system_checker_cores = int(psutil.cpu_count(logical=True)) # Number of CPU cores on the system

if system_checker_cores < 4: # if number of CPU cores is less than 4 
	print("Low End Hardware Detected\n")

log.write(f"System: {uname.system}\nCPU Cores: {psutil.cpu_count(logical=True)}\nFrequency: {cpufreq.max:.2f}Mhz")
log.close()

value1 = 4 ; value5 = 1
value2 = 2 ; value6 = 4
value3 = 8 ; value7 = 7
value4 = 3 ; #value8 = 8
values = f"{value1}{value2}{value3}{value4}{value5}{value6}{value7}"#{value8}

data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
aim = ""
count = 0
solved = 0

# Window Creation
wn = turtle.Screen()
wn.title("Binary Coin Miner ver 1.0.1")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Coins
coin = 0

# Output Text (BINARY COIN)
pen = turtle.Turtle()
pen.color("green")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("BNC: {}".format(coin / 100), align="center", font=("Monospace", 24, "normal")) # Text format

# Output Text (ATTEMPTING)
attempting = turtle.Turtle()
attempting.speed(0)
attempting.color("blue")
attempting.penup()
attempting.hideturtle()
attempting.goto(0, -200)
attempting.write("Speed: {} h/s".format(0), align="center", font=("Monospace", 18, "italic")) #Printing CPU Usage in % and Coins produced

# Output Text (Money)
money = turtle.Turtle()
money.speed(0)
money.color("orange")
money.penup()
money.hideturtle()
money.goto(0, 0)
money.write("ZW DOLLAR: ${}".format(coin / 1000), align="center", font=("Monospace", 48, "bold"))

while aim != values: # Loop will run as long as aim is not equal to values (which by the way is declared outside the loop) 
	num1 = random.choice(data) ; num5 = random.choice(data)
	num2 = random.choice(data) ; num6 = random.choice(data)
	num3 = random.choice(data) ; num7 = random.choice(data)
	num4 = random.choice(data) ; #num8 = random.choice(data)

	aim = f"{num1}{num2}{num3}{num4}{num5}{num6}{num7}"#{num8}
	attempting.clear() # clear() function (from Turtle) allows us to refresh the screen which prevents the text from piling on top of each other.
	attempting.write("Speed: {} h/s".format(aim), align="center", font=("Monospace", 18, "italic")) #Printing CPU Usage in % and Coins produced

	if num1 + num2 == num3 + num4:

		solved += 1
		coin += 1
		zw = coin / 1000000

		pen.clear()
		pen.write("BNC: {}".format(coin / 50000), align="center", font=("Monospace", 24, "normal"))
		money.clear()
		money.write("ZW DOLLAR: ${}".format(zw), align="center", font=("Monospace", 48, "bold"))

		

	for x in aim: #Simply put, if all the conditions in this loop are met, then aim will be equal to values and the While Loop will break
		if value1 == num1:
			num1 = value1
		
		if value2 == num2:
			num2 = value2

		if value3 == num3:
			num3 = value3

		if value4 == num4:
			num4 = value4

		if value5 == num5:
			num5 = value5

		if value6 == num6:
			num6 = value6

		if value7 == num7:
			num7 = value7
			
		#if value8 == num8:
			#num8 = value8			

		count += 1

bnc = coin / 50000

profit.write(f"ZW DOLLAR: ${zw}              |             Withdraw Code: {watcher.verify(bnc)}")
profit.close()

# --------------------------------------------------------------------------------------------------------------------------------
# Key Binding   || (Work in Progress)
wn.listen()
wn.onkeypress(save(zw, bnc), "s")
#-------------------------------------------------------------------------------------------------------------------------------


# Main gui loop
while True:
	wn.update()



