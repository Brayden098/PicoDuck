#!/usr/bin/env python3

# Import libraries
import os
from time import sleep

# ASCII Art Title with Colors
print("\033[95m")  # Set text color to purple
print(r"""
    ____  _            ____             __  
   / __ \(_)________  / __ \__  _______/ /__
  / /_/ / / ___/ __ \/ / / / / / / ___/ //_/
 / ____/ / /__/ /_/ / /_/ / /_/ / /__/ ,<   
/_/   /_/\___/\____/_____/\__,_/\___/_/|_|  
                                            
              by The Ugly Gamer
""")
print("\033[0m")  # Reset text color

print("\033[92mWelcome to the PicoDuck Tool!\033[0m\n")
print("Choose an option below to deploy a payload on your Pico:\n")

options = [
    "\033[94m1) Launch Reverse Shell\033[0m",
    "\033[91m2) Disable Antivirus\033[0m",
    "\033[93m3) Extract WiFi Credentials\033[0m",
    "\033[96m4) Rickroll by The Ugly Gamer\033[0m",
    "\033[95m5) Display Hacked Message\033[0m",
    "\033[90m6) Custom Payload\033[0m"
]
for option in options:
    print(option)

# User selection
try:
    choice = int(input("\nEnter the option number and press Enter: "))
    if choice not in range(1, 7):
        raise ValueError
except ValueError:
    exit("\033[91m\nInvalid input. Please restart and choose a valid option number.\033[0m")

# Prepare the Pico
input("\nConnect your Pico (hold the BOOTSEL button while plugging in). Press Enter when ready...")

# Get drive letter
letter = input("\nEnter the drive letter assigned to your Pico (e.g., 'E'): ").strip().upper()

# Format and set up the Pico
print("\n\033[93m[1/4] Formatting the Pico...\033[0m")
os.system(f"copy src\\format.uf2 {letter}:\\")
sleep(20)

print("\033[96m[2/4] Installing CircuitPython...\033[0m")
os.system(f"copy src\\circuit_python.uf2 {letter}:\\")
sleep(20)

print("\033[95m[3/4] Copying HID libraries...\033[0m")
os.system(f"mkdir {letter}:\\lib\\adafruit_hid")
os.system(f"copy src\\lib\\adafruit_hid {letter}:\\lib\\adafruit_hid\\")
sleep(10)

print("\033[94m[4/4] Copying main program...\033[0m")
os.system(f"copy src\\code.py {letter}:\\code.py")
sleep(2)

print("\n\033[92mPicoDuck Setup Complete! Loading payload...\033[0m\n")

payloads = {
    1: "RevShell.dd",
    2: "Disable_Antivirus.dd",
    3: "Wifi_Extractor.dd",
    4: "RickRoll.dd",
    5: "Hacked.dd",
    6: "Custom.dd"
}

if choice == 1:
    input("Modify 'src\\scripts\\RevShell.dd' to your needs, then press Enter...")
    os.system(f"copy src\\scripts\\{payloads[1]} {letter}:\\payload.dd")
    print("\033[94mReverse Shell payload transferred!\033[0m")

elif choice == 2:
    os.system(f"copy src\\scripts\\{payloads[2]} {letter}:\\payload.dd")
    print("\033[91mDisable Antivirus payload transferred!\033[0m")

elif choice == 3:
    input("Modify 'src\\scripts\\Wifi_Extractor.dd' to your needs, then press Enter...")
    os.system(f"copy src\\scripts\\{payloads[3]} {letter}:\\payload.dd")
    print("\033[93mWiFi Extractor payload transferred!\033[0m")

elif choice == 4:
    os.system(f"copy src\\scripts\\{payloads[4]} {letter}:\\payload.dd")
    print("\033[96mRickroll payload transferred!\033[0m")

elif choice == 5:
    os.system(f"copy src\\scripts\\{payloads[5]} {letter}:\\payload.dd")
    print("\033[95mHacked Message payload transferred!\033[0m")

elif choice == 6:
    input("Create your custom file 'src\\scripts\\Custom.dd' and press Enter...")
    os.system(f"copy src\\scripts\\{payloads[6]} {letter}:\\payload.dd")
    print("\033[90mCustom payload transferred!\033[0m")

print("\n\033[92mAll done! Your PicoDuck (PD) is ready to deploy. Use responsibly!\033[0m\n")
exit("\033[94mGoodbye! Remember, with great power comes great responsibility.\033[0m")