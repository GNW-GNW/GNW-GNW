import pyautogui as spam
import time

msg = input("Type the message you want to send - ")
limit = input("Enter the number of messages - ")
i = 0

time.sleep(5)

while i<int(limit):

    spam.typewrite(msg)
    spam.press('Enter')

    i+=1