

##import os
##import pyautogui
#os.system("notepad.exe")
#time.sleep(10)
##keyboard.press_and_release("ctrl+shift+esc")
##pyautogui.press("tab")
##pyautogui.typewrite('A')
##pyautogui.typewrite('enter')
##
##pyautogui.press("tab")
##pyautogui.press('enter')
##pyautogui.press("down")
##pyautogui.press('enter')

##pyautogui.press('ctrl','c')
##
##os.system("notepad.exe")
##pyautogui.press('ctrl','v')


##pyautogui.press('left')
##keyboard.press_and_release("yes")
##keyboard.press_and_release("enter")
##keyboard.press_and_release("y")
##keyboard.press_and_release("enter")

import subprocess
##subprocess.Popen(["rfkill", "block", "bluetooth"])
##import subprocess 
##a=subprocess.run (['netsh', 'interface', 'get', 'interface', "Wi-Fi"])
##print(a)
##a=subprocess.run ('netsh interface show interface')
##print(a)
##import os
##e=os.system("netsh interface show interface")
##print(e)
##
##def enable():
##    os.system("netsh interface set interface 'Wi-Fi' enabled")
##
##def disable():
##    os.system("netsh interface set interface 'Wi-Fi' disabled")
##disable()
import subprocess
# result = subprocess.run(["netsh", "interface", "set", "interface", "Wi-Fi", "DISABLED"])
# print(result)

while True:
    n = int(input("Enter the size :"))
    if n <=600:
        break
    else:
        print("maximum size is 600, Plaese renter the size")
product = []
val = []
prize = []
allvalue = []
for c in range(n):
    while True:
        name = str(input("enter the name of product : "))
        for i in name:
            if len(name) < 7 and ('a'<=i<='z' or '0'<=i<='9') :
                continue
            else:
                print("Please re-enter your name with less tha 7 letters and lowercase letters and in 0-9 digits only")
                break
        else:
            break

    while True:
        prize = int(input("enter the prize : "))
        if prize<10000:
                break
        else:
            print("Please enter the prize in numbers and less than 10000")

    while True:
        year = int(input("enter the year : "))
        if year < 2100:
            break
        else:
            print("year should be less than 2000")
    val = [name]
    val += [prize]
    val += [year]
    product.insert(c,val)
print(product)
while True:
    q = str(input("Enter the query[type1,type2,type3] :"))
    if q =="type1".lower():
        mf = str(input("Enter manufacture year :"))
        for j in range(n):
            if j == n-1:
                if str(product[j][2]) != str(mf):
                    print("manufacture year not found ")
                    break
                else :
                    print([product[j][0],product[j][1]])
                    break
            else:
                if mf == str(product[j][2]):
                    print(list(product[j][0], product[j][1]))
                    break
                else:
                    pass
        break
    elif q =="type2".lower():
        for j in range(n):
            if int(product[j][1]) < 500:
                value = [product[j][0], product[j][2]]
                if allvalue == []:
                    allvalue = [value]
                else:
                    allvalue.append(value)
            else:
                pass
        print(allvalue)
        break
    elif q =="type3".lower():
        for j in range(n):
            if int(product[j][1]) > 500:
                value = [product[j][0], product[j][2]]
                if allvalue == []:
                    allvalue = [value]
                else:
                    allvalue.append(value)
            else:
                pass
        print(allvalue)
        break
    else:
        print("invalid choice ! please reselect ")



