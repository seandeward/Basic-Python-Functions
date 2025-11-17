# import 'os' module
import os

# set variables as colors
greenFORE = '\033[92]'
redFORE = '\033[91]'
resetFORE = '\033[00m'

## begin with a basic ping
# defines the parameters for the 'ping' command in line 6.
#param = '-n' if os.sys.platform().lower()=='win32' else '-c'
# define the hostname to be used in the command line prompt in the next line
hostname = input("Please Enter the Hostname: ")
# python will only count the amount of lost packets- meaning that if the result is 0, no packets were lost. If it's anything else, then a packet was lost.
response = os.system(f"ping -n 1 {hostname}") 

## check if print the result
# if "response" equals 0, print:
if response == 0:
    print(f"{hostname} is up!")
    # if "response" equals anything else, print this instead:
else:
    print(f"{hostname} is down! {response} packets were dropped.")
