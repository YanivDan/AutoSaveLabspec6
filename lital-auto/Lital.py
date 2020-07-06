import pyautogui
import tkinter as tk
from tkinter import messagebox as mb
import os
import platform
from time import sleep

# Global variable
# Creating the dir and file name
f_name = "files.txt"
libray_name = "LLabspec6/"

path = ""

# Get the machine type
machine = platform.system()

# Init program to open a directory in the computer the prog will run from 
def init_program():
    # Message box for the initail of the program
    mb.showinfo("Wellcome", "Hi!, this is a program for savings - Have Fun!")
    
    # Checking what is the os the user runs
    
    # Check for linux
    if machine == "Linux":
        path = "/tmp/" 
    
    elif machine == "Windows":
        # Add windows path to save the file
        pass
    
    # OS that the program does not support
    else:
        print("The program dosen't support this os")
        return False
    
    # Change directory and open new dir and file
    try:
        if os.path.exists(path + libray_name) == True:
            print("\n[-] LLabspec6 already exists")
            path = path + libray_name
            print(path)
            return True
        else:
            os.chdir(path) # Change to tmp
            os.makedirs(libray_name) # Makes LLabspec6
            path = path + libray_name # Add to global variable path
            os.chdir(path) # Change to /tmp/LLabspec6
            with open(f_name, 'w') as f:
                f.write("Init Line: " + machine + "\n")
                f.write("yaniv\n") #  TODO ----> Delete
    except OSError:
        print ("Creation of the directory and file %s failed" % path)
        return False
    else:
        print ("Successfully created the directory and file %s " % path)
        return True
    

# Quit butoon function
def close_window(): 
    print("\n[!] Exit program button pressed by user\n")

    # Check again if the user want to quit
    if mb.askquestion("Warning","Are you sure you want to quit? ") == "yes":
        print("\n[#] User enter 'Y' for exit")
        root.destroy()
    else:
        print("\n[#] User enter 'N' program still runing")


# Check input from user function
def check_input(usr_str):
    if ('' or ' ' or '\n' or '\t') in usr_str:
        return False
    else:
        return True


# function that open a txt file and retruns its contents
def GetFileContent():
    # Log for develop
    print("\n[#] Show names in file has been pressed")

    # f_content is the list that contain the data from the file
    f_contnet = []
    
    # try-except to open the file
    try:
        print(path + f_name + "\n")

        with open(path + f_name, "r") as f:
            for line in f:    
                f_contnet.append(line[:len(line) - 1])

        return f_contnet

    # File wasn'nt found raise error
    except FileNotFoundError:
        labal = tk.Label(lower_frame, text="File doesn't match - Try again", bg="white")
        labal.place(relwidth=0.45, relheight=0.1, relx=0.2, rely=0, anchor='n')
    

# Print the file name that has been saved before
def PrintFileNames():
    # Delete the current info in the frame
    for widget in lower_frame.winfo_children():
        widget.destroy()
    
    # List that contaiin the data of 'files'
    f_content = GetFileContent()
    
    # Counter for the grid rows
    cot = 0
    
    # Print the files in the UI
    for line in f_content:
        cot += 1
        # Create a label to print the lines in the file name txt
        labal = tk.Label(lower_frame, text=str(cot) + ": " + line, bg="white", anchor='w')
        labal.grid(row=cot, column=0, sticky='W')

            
# Save file function
def Save(s_name):
    # Delete the current info in the frame
    for widget in lower_frame.winfo_children():
        widget.destroy()
    
    print("\n[-] Save button have been pressed")
    if check_input(s_name) == False and s_name.isalpha() != True:
        exit_ = tk.Label(lower_frame, text="Invalid input - enter another name.", bg="white")
        exit_.place(relwidth=0.5, relheight=0.1, relx=0, rely=0)
        return

    # TODO ----> Delete
    return

    # Buttons to be pressed
    spectra = pyautogui.locateCenterOnScreen("refresh.png")
    video = pyautogui.locateCenterOnScreen("vid1.jpg")
    lb_save = pyautogui.locateCenterOnScreen("sv.jpg")

    # Debug print for develop
    print("\n [-] Spectra:",spectra)
    print("\n [-] Video:",video)
    print("\n [-] Save button:",lb_save)

    # TODO ----> Ask lital about the '.lb6'
    ls = [".ls6", ".txt", ".jpg"]

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
            pyautogui.write(s_name + str(i) + ls[i - 1])
            print("\n[-] Saved spectra in ", ls[i -1], "format")

        #             Video save - .jpeg format
        else:
            # Go to video tab
            pyautogui.moveTo(x=video.x, y=video.y, duration=0.3)
            pyautogui.click()

            # Save Video tab 
            pyautogui.moveTo(x=lb_save.x, y=lb_save.y, duration=0.3)
            pyautogui.click()

            # Write the name of the file
            pyautogui.write(s_name + str(i) + ls[2])
            print("\n[-] Saved video in .jpeg format")


        # Press the keyboared enter to save the file
        pyautogui.press(["enter"])

        print("\n[-] Done Saving")

    labal = tk.Label(lower_frame, text="Done Saving", bg="white")
    labal.place(relwidth=0.45, relheight=0.1, relx=0.2, rely=0.4, anchor='n')


#--------------------------------------------------------------------------------------
#                                 Main Gui 


# TODO ----> Create an instance of the Gui in future version


# Tk instance
root = tk.Tk()

# Canvas instance
canvas = tk.Canvas(root, height=700, width=700, bg="#0a8ce3")
canvas.pack()

# Show all the name that have been used 
Quit_button = tk.Button(root, text="Quit", padx=2, pady=2, command=close_window)
Quit_button.place(relwidth=0.08, relheight=0.08, relx=0.5, rely=0.8, anchor='n')

# A Frame to the buttons, entry and top label
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.75, relheight=0.1, relx=0.5, rely=0.1, anchor='n')

# Save button
runSave = tk.Button(frame, text="Save Files", padx=10, pady=10, command=lambda: Save(usr_file_name.get()))
runSave.place(relwidth=0.5, relheight=0.5, relx=0.5, rely=0.5)

# Label box for file name from the usr
usr_entry = tk.Label(frame, text="Please enter the file name : ", bg="#c0a8cc", fg="#0a1ee3")
usr_entry.place(relwidth=0.5, relheight=0.5, relx=0, rely=0)

# Entry box for file name from the usr
usr_file_name = tk.Entry(frame)
usr_file_name.place(relwidth=0.5, relheight=0.5, relx=0, rely=0.5)

# Show all the name that have been used 
runShowCount = tk.Button(frame, text="Show files names", padx=10, pady=10, command=lambda: PrintFileNames())
runShowCount.place(relwidth=0.5, relheight=0.5, relx=0.5, rely=0)

# A Frame to see the results
lower_frame = tk.Frame(root, bg="white")
lower_frame.place(relwidth=0.75, relheight=0.5, relx=0.5, rely=0.25, anchor='n')



#--------------------------------------------------------------------------------------
#                                 Main Logic

# Init function 
if init_program() == True:
    root.mainloop()

else:
    mb.showerror("Error", "Program Failed")
    sleep(0.5)