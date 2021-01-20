import asyncio
import os
import sys
import json
import profile
import platform
import random
import time
import datetime

async def shutdownSys():
    print('To be advised: Your OS is shutting down! [10 Seconds...]\nTo cancel this, you can force shutdown the program using \'CTRL\' + \'Z\' in the terminal.')
    await asyncio.sleep(10)
    os.system("shutdown /s /t 1")

async def closeProgram():
    print('Program is closing..')
    await asyncio.sleep(3)
    print('Program closed.')
    exit()


def shutdown():
    asyncio.run(shutdownSys())

def leaveProgram():
    asyncio.run(closeProgram())

while True:
    sysOption = input("1. Shutdown system.\n2. Exit program\n")
    if int(sysOption) == 1:
        shutdown()
    elif int(sysOption) == 2:
        leaveProgram()
    else:
        print(f'{sysOption} is not a valid option, please choose from the available options.')