import ctypes
import os
import sys
import requests
import getpass
import tqdm
from colorama import init, Style, Fore

init()

def is_admin():
    """ Проверяем права"""
    try:
        # Если админ вернет True
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if is_admin():
    ctype = 'root'
    utype = 'system'
    root = True

else:
    ctype = 'user'
    utype = getpass.getuser()
    root = False

import webview
from threading import Thread
#class Api:
#    def inject(self):
#        print('Injecting...')
#        sleep(2)
#        print('Done!')
    
def browser():
    window = webview.create_window('PyCmd WebBrowser', 'https://duckduckgo.com',)
    webview.start()


from time import sleep
import base64

os.system('cls')

#from cfonts import render, say

#testlogo = render('python CMD', colors=['white', 'magenta'], align='center')

def rlt(command):
    print("<system> try to change extension...\n")
    try:
        command = command.split(" ")
    except Exception as e:
        pass
    for i in range(5):
        try:
            command[i]
        except Exception as e:
            command.append("")
    argv1 = command[1]
    argv2 = command[2]
    if os.path.exists(argv1):
        argv1_splitted = argv1.split(".")
        new_file_name = (argv1_splitted[0]+str("\u202E")+str(argv2[::-1])+"."+str(argv1_splitted[1]))
        try:
            os.rename(argv1, new_file_name)
            print("<system> done")
        except Exception as e:
            printf("Error while renaming\nError: {e}")

    else:
        print("<system> file not found")

oldlogo = Style.BRIGHT + """
  ▄████▄   ███▄ ▄███▓▓█████▄ 
 ▒██▀ ▀█  ▓██▒▀█▀ ██▒▒██▀ ██▌ - Just a cmd adaptation.
 ▒▓█    ▄ ▓██    ▓██░░██   █▌ - Use like normal cmd.
 ▒▓▓▄ ▄██▒▒██    ▒██ ░▓█▄   ▌
 ▒ ▓███▀ ░▒██▒   ░██▒░▒████▓ 
 ░ ░▒ ▒  ░░ ▒░   ░  ░ ▒▒▓  ▒ 
   ░  ▒   ░  ░      ░ ░ ▒  ▒ 
 ░        ░      ░    ░ ░  ░ 
 ░ ░             ░      ░    
 ░                 ░     """

commands = Fore.MAGENTA + """
 ----------------- Commands -----------------
 - root               | Install root
 - delroot            | Delete root // ONLY ROOTED CMD
 - spoof              | Spoof file extension // ONLY ROOTED CMD
 - browser            | Open anonymous web browser
 - help               | Show commands
 - dm                 | Admin contact
 - check-root         | Displays root status
 - cmd                | Enter to normal console
 - settings-root      | Change "root@system >" // ONLY ROOTED CMD
 - pkg <pkg_name>     | Install package (pip)
 --------------------------------------------
 """ + Style.RESET_ALL

def title(name: str):
    import os
    os.system(f'title {name}')

title('@kryyaasoft // PyCmd.exe // best python sigma cmd')

print(f'{oldlogo}\n\n  Welcome to PyCmd!')
print(commands)

def download_files(url: str, filename: str):
    with open(filename, 'wb') as f:
        with requests.get(url, stream=True) as r:
            
            r.raise_for_status()
            total = int(r.headers.get('content-length', 0))

            tqdm_params = {
                'desc': 'building...',
                'total': total,
                'miniters': 1,
                'unit': 'it',
                'unit_scale': True,
                'unit_divisor': 1024,
            }

            with tqdm.tqdm(**tqdm_params) as pb:
                for chunk in r.iter_content(chunk_size=8192):
                    pb.update(len(chunk))
                    f.write(chunk)

# переменные 
nameeeee = getpass.getuser()
pkgbrow = False

while True:
    if root == True:
        cmd = input(Style.BRIGHT + Fore.RED + f'{ctype}@{utype}' + Style.RESET_ALL + Style.BRIGHT + ' / > ')
    else:
        cmd = input(Style.BRIGHT + Fore.BLUE + f'{ctype}@{utype}' + Style.RESET_ALL + Style.BRIGHT + ' / > ')
    cmd.split(' ')
    #f = open('pycmd.ini', 'w')
    #f.write(f'---PYCMDLOGS---\nuser: {nameeeee}\ncmd-type: {ctype}\nuser-type: {utype}\nroot: {root}\nlast-input: {cmd}')
    #f.close()
    #os.system('move pycmd.ini C:/')
    if cmd == 'delroot':
        if root == True:
            anws = input('are you sure? (Y/N): ')
            if anws == 'Y' or 'y' or 'yes':
                print('<system> deleting root...')
                sleep(2)
                print('<system> done')
                ctype = 'user'
                utype = getpass.getuser()
                root = False
            else:
                print('<system> canceled')
        else:
            print('<system> CMD not rooted')
    elif cmd == 'root':
        if root == False:
            print('<system> rooting CMD...')
            sleep(1.5)
            print('<system> done')
            sleep(0.6)
            ctype = 'root'
            utype = 'system'
            root = True
        else:
            print('<system> CMD already rooted.')
    elif cmd == 'exit':
        print('<system> good bye!')
        sleep(1)
        os.system('taskkill /f /im Python.exe')
        os.system('taskkill /f /im PyCmd.exe')
    elif cmd == 'help':
        print(commands)
    elif cmd == 'dm':
        os.system('start https://t.me/kryyaa')
    elif cmd == 'spoof':
        if root == True:
            fl = input('<system> file name(test.exe): ')
            to = input('<system> new extension(mp3): ')
            command = f'root {fl} {to}'
            command = command.split(" ")
            rlt(command)
        else:
            print('<system> CMD not rooted')
    elif cmd == 'check-root':
        print(f'<system> root status: {root}')
    elif cmd == 'settings-root':
        if root == True:
            ctype = input('<system> change "root" text to: ')
            utype = input('<system> change "system" text to: ')
            sleep(1)
            print('<system> done')
        else:
            print('<system> CMD not rooted')
    elif 'title' in cmd:
        cmd = cmd.split(' ')
        i = 1
        tit = cmd[1]
        if root == True:
            title(f'{tit}')
        else:
            print('<system> permission dinied')
    elif 'pkg' in cmd:
        cmd = cmd.split(' ')
        pkg = cmd[1]
        if pkg == 'kinitopet.exe':
            if root == True:
                print('<system> wait whaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa-')
                sleep(0.3)
                os.system('cls')
                print(f'C:/Users/{nameeeee}/desktop> -find kinitopet.exe')
                title('Command prompt')
                print('> finding kinitopet.exe...')
                sleep(1)
                print('kinitopet.exe name["KinitoPET"]found.\n')
                sleep(0.5)
                download_files('https://github.com/kryyyaaaa/PyCmd/releases/download/1.0/KinitoPET.zip', 'kinitoPET[cracked@kryyaasoft].zip')
                print('\n> info Version 4.2.3-Sunny .C')
                sleep(0.2)
                print('> running...')
                sleep(0.5)
                os.system('start kinitoPET[cracked@kryyaasoft].zip')
                print('this is cracked product! telegram @sorryforhakck')
                os.system('cls')
                title('@kryyaasoft // PyCmd.exe // best python sigma cmd')
                print(f'{oldlogo}\n\n  Welcome to PyCmd!')
                print(commands)
            else:
                print(f'<system> "user" cant install {cmd[1]}!')
        elif pkg == 'update-pycmd':
            print('<system> finding update...')
            sleep(1)
            os.system('start https://github.com/kryyyaaaa/PyCmd/releases')
        elif pkg == 'dava.exe':
            download_files('https://github.com/kryyyaaaa/bbtd/releases/download/sigma/sigma.exe', 'dava.exe')
            print('<system> dava cat has been installed!')
        elif pkg == 'pycmd.browser':
            print('<system> installing browser...')
            sleep(2)
            print('<system> done. run command: browser')
            pkgbrow = True
        else:
            os.system(f'pip install {pkg}')
    elif cmd == 'browser':
        if pkgbrow == True:
            print('<system> running browser...')
            sleep(1)
            print('<system> done')
            browser()
        else:
            print('<system> package "browser" is not installed! install package: pycmd.browser')
    else:
        os.system(f'{cmd}')