import asyncio
import os
import sys
import json
import profile
import platform
import random
import time
import datetime

def shutdown():
    print('To be advised: Your OS is shutting down!\n')
    os.system("shutdown /s /t 1")

def leaveProgram():
    print('Program exit.')
    exit()

while True:
    sysOption = input("1. Shutdown system.\n2. Exit program\n")
    if int(sysOption) == 1:
        shutdown()
    elif int(sysOption) == 2:
        leaveProgram()
    else:
        print(f'{sysOption} is not a valid option, please choose from the available options.')