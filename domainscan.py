import os
import sys

os.system('clear')

sys.ps1 = '\033[01;32m '

print(sys.ps1)

print('''

 ████████╗██████╗ ██████╗ ██████╗ 
╚══██╔══╝██╔══██╗╚════██╗╚════██╗
   ██║   ██████╔╝ █████╔╝ █████╔╝
   ██║   ██╔══██╗ ╚═══██╗ ╚═══██╗
   ██║   ██║  ██║██████╔╝██████╔╝
   ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚═════╝ 
                                 
                       
''')


lol = input('Enter the domain ya wanna scan: ')

os.system('whois '+lol)
os.system('dig '+lol)
