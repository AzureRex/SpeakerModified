import time
from time import sleep
import os

# Get input from the user and store it in a variable

def clear_console():
    os.system('cls')

host_text = input("Host IP: ")
pass_text = input("Host Password: ")
clear_console()
print("Searching for speakers...")
print("HOST: :", host_text)
print("PASS: :", pass_text)

sleep(6)

clear_console()

print("Found!")
sleep(2)
print("""
      Pracownia-124
      SalaGim-093
      Pracownia-127
      Komputer246
      Komputer247""")
print("If you want to select all type: A")
speaker_text = input("Speaker:")
if speaker_text== 'A':
    clear_console()
    print("Selected all speakers.")
    soundname_text = input("Sound OGG: ")
    clear_console()
    print("Sound: :", soundname_text)
    print("Trying to inject...")
    sleep(2)
    print("Succes!")
else:
    clear_console()
    print("Speaker: :", speaker_text)
    soundname_text = input("Sound OGG: ")
    clear_console()
    print("Sound: :", soundname_text)
    print("Trying to inject...")
    sleep(2)
    clear_console()
    print("Succes!")