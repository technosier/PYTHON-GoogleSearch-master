import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pykeyboard import PyKeyboard
from clint.textui import colored
#Google Search
#Coded by | lucifer
#https://github.com/technosier
os.system('title Google Search')
os.system('color 0a')
def Main():
    search = raw_input("Enter search term : ")
    browser = webdriver.Firefox()
    browser.get("https://www.google.com")
    searchElement = browser.find_element_by_id("lst-ib")
    searchElement.send_keys(search)
    keyboard = PyKeyboard()
    keyboard.press_key(keyboard.enter_key)#Keyboard press 'ENTER'

    os.system('cls')#os.system('clear') if Linux
    print colored.yellow("[+] Google Search success!")
    browser.close()

if __name__ == "__main__":
    Main()
