#Import
import os
import pyfiglet
import time

#Default
current = set()

#Shortcut
def clear():
  os.system('clear')

def Rinde():
    rinde = pyfiglet.figlet_format("pyRINDE v2", font = "slant")
    print(rinde)
    print("-------------------------------------------------------------------")
    print("Author: Szymon 'by-speece' Gałka 2020-2021")
    print("Codename: Fresh May | Build 17062021 | Version:0.7.1-experimental")
    print("-------------------------------------------------------------------")

def GlobalMenu():
    print("-------------------------------------------------------------------")
    print("b | Back to Main Menu")
    print("q | Quit")
    print("-------------------------------------------------------------------")

#Code of Program

def Main(): #Main Code of Program
    clear()
    Rinde()
    print("1 | Package Manager")
    print("2 | Install Apps with Configs")
    print("3 | Settings Manager")
    print("4 | Power Manager")
    GlobalMenu()

    MainInput = input("Command: ")
    if MainInput == "1": #Package Manager
        clear()
        Rinde()
        print("# | Packages Manager  ")
        print("1 | Full Update | Pacman + Yay")
        print("2 | Full Update | Pacman")
        print("3 | Fast Update | Pacman")
        print("4 | Fast Update | Yay")
        PackageInput = input("Command: ")
        if PackageInput == "1": #Full Update | Pacman + Yay
            os.system('sudo reflector --verbose --latest 10 --sort rate --save /etc/pacman.d/mirrorlist')
            os.system('sudo pacman -Syu --noconfirm')
            os.system('sudo pacman -Sc --noconfirm')
            os.system('sudo pacman -Rs $(pacman -Qtdq) --noconfirm')
            os.system('yay -Syu --noconfirm')
            os.system('yay -Rs $(yay -Qtdq) --noconfirm')
            Main()
        if PackageInput == "2": #Full Update | Pacman
            os.system('sudo reflector --verbose --latest 10 --sort rate --save /etc/pacman.d/mirrorlist')
            os.system('sudo pacman -Syu --noconfirm')
            os.system('sudo pacman -Sc --noconfirm')
            os.system('sudo pacman -Rs $(pacman -Qtdq) --noconfirm')
            Main()
        if PackageInput == "3": #Fast Update | Pacman
            os.system('sudo reflector --verbose --latest 10 --sort rate --save /etc/pacman.d/mirrorlist')
            os.system('sudo pacman -Syu --noconfirm')
            Main()
        if PackageInput == "4": #Fast Update | Yay
            os.system('yay -Syu --noconfirm')
            Main()
        if PackageInput == "b": #Back to Main Menu
            Main()
        if PackageInput == "q": #Quit
            exit()
        else:
            Main()
    if MainInput == "2": #Install apps with configs
        clear()
    if MainInput == "3": #Settings Manager
        clear()
        Rinde()
        print("# | Settings Menu ")
        print("1 | Packages Pack")
        print("2 | Drivers Pack")
        print("3 | Install Rice[You need Yay]")
        print("4 | Install Yay[Binary]")
        print("5 | Install Yay[From Code]")
        GlobalMenu()
        RindeInput = input("Command: ")
        if RindeInput == "1": #Packages Pack
            clear()
            Rinde()
        if RindeInput == "2": #Drivers Pack
            clear()
            Rinde()
        if RindeInput == "3": #Install Rice
            os.system('sh ~/.pyRinde/Data/Bash/rice.sh')
            os.system('cp -rf ~/.pyRinde/Data/Rice/* ~/.config/')
            os.system('mkdir ~/.pyrinde-user')
            os.system('cp -rf ~/.pyRinde/Data/pyrinde-user-template/* ~/.pyrinde-user/')
            os.system('sudo chmod +s /usr/bin/light')
            os.system('cp -rf ~/.pyRinde/Data/Rice/* ~/.config/')
            clear()
            Rinde()
        if RindeInput == "4": #Install Yay[Binary]
            os.system('sh Data/Bash/yay-bin.sh')
            clear()
            Rinde()
        if RindeInput == "5": #Install Yay[From Code]
            os.system('sh Data/Bash/yay-compile.sh')
            clear()
            Rinde()
        
        if RindeInput == "b": #Back to Main Menu
            Main()
        if RindeInput == "q": #Quit
            exit()
    if MainInput == "5": #NotebookManager
        NotebookMenu()
    if MainInput == "6": #PowerManager
        clear()
        Rinde()
    if MainInput == "b": #Classic Function
        Main()
    if MainInput == "q": #Classic Function
        exit()
    else: #User is just idiot 
        Main()

######################################################################
######################################################################
######################################################################
def NotebookMenu(): #Laptop Menu
    clear()
    Rinde()
    print("# | Notebook Manager")
    print("1 | Check Battery Level")
    print("2 | Laptop Lid Light")
    print("3 | No Suspend on close laptop lid(On Battery)")
    print("4 | Suspend on close laptop lid(On Battery)")
    print("5 | Turn ON Ultra Energy Saving")
    print("6 | Turn OFF Ultra Energy Saving")
    GlobalMenu()
    NotebookInput = input("Command: ")
    if NotebookInput  == "1": #Check Battery %
        print("Your Battery Level is[%]:")
        os.system('cat /sys/class/power_supply/BAT0/capacity')
        time.sleep(3)
        clear()
        NotebookMenu()
    if NotebookInput == "2": #Laptop Lid Light
       LaptopLid() #  Another def with loop
    if NotebookInput == "3": #No Suspend on Closed Lid on Battery
        os.system('sudo cp -rf ~/.pyRinde/Data/NotebookManager/NoSuspend/logind.conf   /etc/systemd/')
    if NotebookInput == "4": #Suspend on Closed Lid on Battery
        os.system('sudo cp -rf ~/.pyRinde/Data/NotebookManager/Suspend/logind.conf   /etc/systemd/')
    if NotebookInput == "5": #Turn ON Ultra Energy Sabing
        os.system('sudo systemctl stop syncthing@$USER NetworkManager ')
    if NotebookInput == "6": #Turn OFF Ultra Energy Saving
        os.system('sudo systemctl start syncthing@$USER NetworkManager')
    if NotebookInput == "b": #Back to Main Menu
        clear()
        Main()
    if NotebookInput == "q": # Quit from App
        exit()
    else:
        NotebookMenu()

def LaptopLid(): #Laptop Lid
    clear()
    Rinde()
    print("#  | Laptop Lid Settting")
    print("1  | SET LID ON | 10%")
    print("2  | SET LID ON | 20%")
    print("3  | SET LID ON | 30%")
    print("4  | SET LID ON | 40%")
    print("5  | SET LID ON | 50%")
    print("6  | SET LID ON | 60%")
    print("7  | SET LID ON | 70%")
    print("8  | SET LID ON | 80%")
    print("9  | SET LID ON | 90%")
    print("10 | SET LID ON | 100%")
    GlobalMenu()

    LaptopLidInput = input("Command: ")
    if LaptopLidInput == "1": # 10%
        os.system('light -S 10')
        LaptopLid()
    if LaptopLidInput == "2": # 20%
        os.system('light -S 20')
        LaptopLid()
    if LaptopLidInput == "3": # 30%
        os.system('light -S 30')
        LaptopLid()
    if LaptopLidInput == "4": # 40%
        os.system('light -S 40')
        LaptopLid()
    if LaptopLidInput == "5": # 50%
        os.system('light -S 50')
        LaptopLid()
    if LaptopLidInput == "6": # 60%
        os.system('light -S 60')
        LaptopLid()
    if LaptopLidInput == "7": # 70%
        os.system('light -S 70')
        LaptopLid()
    if LaptopLidInput == "8": # 80%
        os.system('light -S 80')
        LaptopLid()
    if LaptopLidInput == "9": # 90%
        os.system('light -S 90')
        LaptopLid()
    if LaptopLidInput == "10": # 100%
        os.system('light -S 100')
        LaptopLid()
    if LaptopLidInput == "b": #Back to Main Menu
        clear()
        Main()
    if LaptopLidInput == "q": # Quit from App
        exit()
    else:
        LaptopLid()
#########################################################################



Main() #Start
