#!/usr/bin/python
import pyautogui 

def main():
	i=0
	x=100
	y=100
	while (i<=10000000000000000000000000):
		pyautogui.moveTo(x, y, duration = 10)
		pyautogui.click(x, y) 
		pyautogui.moveTo(x-10, y-10, duration = 10)
		pyautogui.click(x-10, y-100) 
		i=i+1

if __name__ == "__main__": main()
