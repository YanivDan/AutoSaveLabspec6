import pyautogui
import tkinter as tk
from tkinter import messagebox as mb
import os
import platform


def Save_by_end(s_name):
    # Buttons to be pressed
    # Get buttons locations
    spectra = pyautogui.locateCenterOnScreen("refresh.png")
    video = pyautogui.locateCenterOnScreen("vid1.jpg")
    lb_save = pyautogui.locateCenterOnScreen("sv.jpg")
    
    # Debug print for develop
    print("\n [-] Spectra:", spectra)
    print("\n [-] Video:", video)
    print("\n [-] Save button:", lb_save)

    # TODO --there is anothe one ask lital
    end_ls = [".ls6", ".txt", ".jpg"]
    
    # Go to spectra tab
    pyautogui.moveTo(x=spectra.x, y=spectra.y, duration=0.3)
    pyautogui.click()
    print("\n[#] Pressed spectra tab")
    
    # TODO ----> Optimaze the code - Write once
    for i in range(1,5):
        #      Spectra save - labspec, .txt, .jpeg format
        if i < 4:
            # Save Spectra tab
            pyautogui.moveTo(x=lb_save.x, y=lb_save.y, duration=0.3)
            pyautogui.click()

            # Write the name of the file
            pyautogui.write(s_name + str(i) + end_ls[i - 1])
            print("\n[-] Saved spectra in ", end_ls[i -1], "format")
        
        #             Video save - .jpeg format
        else:
            # Go to video tab
            pyautogui.moveTo(x=video.x, y=video.y, duration=0.3)
            pyautogui.click()

            # Save Video tab 
            pyautogui.moveTo(x=lb_save.x, y=lb_save.y, duration=0.3)
            pyautogui.click()

            # Write the name of the file
            pyautogui.write(s_name + str(i) + end_ls[2])
            print("\n[-] Saved video in .jpeg format")
        
        
        # Press the keyboared enter to save the file
        pyautogui.press(["enter"])

        print("\n[-] Done Saving")



def init_program():
    mb.showinfo("Wellcome", "Hi!, this is a program for savings - Have Fun!")
    # Creating the file name
    f_name = "FNUE.txt"
    libra_name = "/LLabspec6"
    
    # Get the machine type
    machine = platform.system()
    
    # Checking what is the os the user runs
    # Check for linux
    if machine == "Linux":
        pat = "/tmp"
        try:
            os.chdir(pat)
            if os.path.exists(pat + libra_name) == True:
                print("\n[-] LLabspec6 already exists")
                return True
            else:
                os.makedirs("LLabspec6")
                os.chdir(pat + libra_name)
                with open(f_name, 'w'):
                    pass
        except OSError:
            print ("Creation of the directory and file %s failed" % pat + libra_name)
            return False
        else:
            print ("Successfully created the directory and file %s " % pat + libra_name)
            return True  
    
    # OS that the program does not support
    else:
        print("The program dosen't support this os")
        return False



# print(init_program())

a = "/tmp/"
a = a + "yaniv"

with open("/tmp/LLabspec6/files.txt", "r") as f:
    for line in f:    
        print(line[:len(line) - 1])

# pyautogui.screenshot().save("screen shot.jpg")

# a = pyautogui.locateCenterOnScreen("plus_sign.png")

# pyautogui.moveTo(x=a.x, y=a.y, duration=0.5)
# pyautogui.click()