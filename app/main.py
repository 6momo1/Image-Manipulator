# CMPT 120 Yet Another Image Processer
# Starter code for main.py
# Author(s): Tomi Lui, David Jia
# Date: December 7th 2020
# Description: To create image manipulator program

import cmpt120imageProj
import cmpt120imageManip
import tkinter.filedialog
import pygame
pygame.init()

# list of system options
system = [
            "Q: Quit",
            "O: Open Image",
            "S: Save Current Image",
            "R: Reload Original Image"
         ]

# list of basic operation options
basic = [
        "1: Invert",
        "2: Flip Horizontal",
        "3: Flip Vertical",
        "4: Switch to Intermeidate Functions",
        "5: Switch to Advanced Functions"
         ]

# list of intermediate operation options
intermediate = [
                "1: Remove Red Channel",
                "2: Remove Green Channel",
                "3: Remove Blue Channel",
                "4: Convert to Greyscale",
                "5: Apply Sepia Filter",
                "6: Decrease Brightness",
                "7: Increase Brightness",
                "8: Switch to Basic Functions",
                "9: Switch to Advanced Functions"
                 ]

# list of advanced operation options
advanced = [    "1: Rotate Left",
                "2: Rotate Right",
                "3: Pixelate",
                "4: Binarize",
                "5: Switch to Basic Functions",
                "6: Switch to Intermediate Functions"
             ]

# a helper function that generates a list of strings to be displayed in the interface
def generateMenu(state):
    """
    Input:  state - a dictionary containing the state values of the application
    Returns: a list of strings, each element represets a line in the interface
    """
    menuString = ["Welcome to CMPT 120 Image Processer!"]
    menuString.append("") # an empty line
    menuString.append("Choose the following options:")
    menuString.append("") # an empty line
    menuString += system
    menuString.append("") # an empty line

    # build the list differently depending on the mode attribute
    if state["mode"] == "basic":
        menuString.append("--Basic Mode--")
        menuString += basic
        menuString.append("")
        menuString.append("***Update this line to show the proper information***")
    elif state["mode"] == "intermediate":
        menuString.append("--Intermediate Mode--")
        menuString += intermediate
        menuString.append("")
        menuString.append("***Update this line to show the proper information***")
    elif state["mode"] == "advanced":
        menuString.append("--Advanced Mode--")
        menuString += advanced
        menuString.append("")
        menuString.append("***Update this line to show the proper information***")
    else:
        menuString.append("Error: Unknown mode!")

    return menuString

# a helper function that returns the result image as a result of the operation chosen by the user
# it also updates the state values when necessary (e.g, the mode attribute if the user switches mode)
def handleUserInput(state, img):
    """
        Input:  state - a dictionary containing the state values of the application
                img - the 2d array of RGB values to be operated on
        Returns: the 2d array of RGB vales of the result image of an operation chosen by the user
    """
    userInput = state["lastUserInput"].upper()
    # handle the system functionalities
    if userInput.isalpha(): # check if the input is an alphabet
        print("Log: Doing system functionalities " + userInput)
        if userInput == "Q": # this case actually won't happen, it's here as an example
            print("Log: Quitting...")
        # ***add the rest to handle other system functionalities***

    # or handle the manipulation functionalities based on which mode the application is in
    elif userInput.isdigit(): # has to be a digit for manipulation options
        print("Log: Doing manipulation functionalities " + userInput)
        # ***add the rest to handle other manipulation functionalities***

    else: # unrecognized user input
            print("Log: Unrecognized user input: " + userInput)

    return img

# use a dictionary to remember several state values of the application
appStateValues = {
                    "mode": "basic",
                    "lastOpenFilename": "",
                    "lastSaveFilename": "",
                    "lastUserInput": ""
                 }


currentImg = cmpt120imageProj.createBlackImage(600, 400)


cmpt120imageProj.showInterface(currentImg, "No Image", generateMenu(appStateValues)) # note how it is used

# ***this is the event-loop of the application. Keep the remainder of the code unmodified***
keepRunning = True
# a while-loop getting events from pygame
while keepRunning:
    ### use the pygame event handling system ###
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            appStateValues["lastUserInput"] = pygame.key.name(event.key)


            # BASIC FUNCTION LIST
            if appStateValues['mode'] == 'basic':  
                # prepare to quit the loop if user inputs "q" or "Q"
                if appStateValues["lastUserInput"].upper() == "Q":
                    keepRunning = False


                if appStateValues["lastUserInput"].upper() == "R":
                    currentImg = cmpt120imageManip.original()
                    cmpt120imageProj.showInterface(currentImg, "No Image", generateMenu(appStateValues))


                # OPEN NEW FILE
                if appStateValues["lastUserInput"].upper() == "O":
                    tkinter.Tk().withdraw()
                    openFilename = tkinter.filedialog.askopenfilename()
                    currentImg = cmpt120imageProj.getImage(openFilename)
                    cmpt120imageProj.showInterface(currentImg, "No Image", generateMenu(appStateValues))
                
                # SAVE CURRENT FILE
                if appStateValues["lastUserInput"].upper() == "S":
                    tkinter.Tk().withdraw()
                    saveFilename = tkinter.filedialog.asksaveasfilename()
                    cmpt120imageProj.saveImage(currentImg, saveFilename)
                    cmpt120imageProj.showInterface(currentImg, "No Image", generateMenu(appStateValues))


                if appStateValues["lastUserInput"].upper() == "1":
                    tkinter.Tk().withdraw()
                    currentImg = cmpt120imageManip.invert(currentImg)
                    cmpt120imageProj.showInterface(currentImg, "No Image", generateMenu(appStateValues))

                # FLIP HORIZONTAL
                if appStateValues["lastUserInput"].upper() == "2":
                    currentImg = cmpt120imageManip.flipH(currentImg)
                    cmpt120imageProj.showInterface(currentImg, "No Image", generateMenu(appStateValues))

                # FLIP VERTICAL
                if appStateValues["lastUserInput"].upper() == "3":
                    currentImg = cmpt120imageManip.flipV(currentImg)
                    cmpt120imageProj.showInterface(currentImg, "No Image", generateMenu(appStateValues))


                # set state to intermediate
                if appStateValues["lastUserInput"].upper() == "4":
                    tkinter.Tk().withdraw()
                    appStateValues['mode'] = 'intermediate'
                    cmpt120imageProj.showInterface(currentImg, "No Image", generateMenu(appStateValues))

                # set state to "advanced"
                if appStateValues["lastUserInput"].upper() == "5":
                    tkinter.Tk().withdraw()
                    appStateValues['mode'] = 'advanced'
                    cmpt120imageProj.showInterface(currentImg, "No Image", generateMenu(appStateValues))


            # INTERMEDIATE FUNCTION LIST
            elif appStateValues['mode'] == 'intermediate': 

                # quit program
                if appStateValues["lastUserInput"].upper() == "Q":
                    keepRunning = False

                # open original photo
                if appStateValues["lastUserInput"].upper() == "R":
                    currentImg = cmpt120imageManip.original()
                    cmpt120imageProj.showInterface(currentImg, "No Image", generateMenu(appStateValues))
                    

                # REMOVE RED CHANNEL
                if appStateValues["lastUserInput"].upper() == "1":
                    currentImg = cmpt120imageManip.remove_red_channel(currentImg)
                    cmpt120imageProj.showInterface(currentImg, "No Image", generateMenu(appStateValues))
                    

                # REMOVE GREEN CHANNEL
                if appStateValues["lastUserInput"].upper() == "2":
                    currentImg = cmpt120imageManip.remove_green_channel(currentImg)
                    cmpt120imageProj.showInterface(currentImg, "No Image", generateMenu(appStateValues))

                # REMOVE BLUE CHANNEL
                if appStateValues["lastUserInput"].upper() == "3":
                    currentImg = cmpt120imageManip.remove_blue_channel(currentImg)
                    cmpt120imageProj.showInterface(currentImg, "No Image", generateMenu(appStateValues))

                # CONVERT TO GREY SCALE
                if appStateValues["lastUserInput"].upper() == "4":
                    currentImg = cmpt120imageManip.greyscale(currentImg)
                    cmpt120imageProj.showInterface(currentImg, "No Image", generateMenu(appStateValues))
                    

                # APPLY SEPIA FILTER
                if appStateValues["lastUserInput"].upper() == "5":
                    currentImg = cmpt120imageManip.apply_sepia_filter(currentImg)
                    cmpt120imageProj.showInterface(currentImg, "No Image", generateMenu(appStateValues))

                # DECREASE BRIGHTNESS
                if appStateValues["lastUserInput"].upper() == "6":
                    currentImg = cmpt120imageManip.decrease_brightness(currentImg)
                    cmpt120imageProj.showInterface(currentImg, "No Image", generateMenu(appStateValues))

                # INCREASE BRIGHTNESS
                if appStateValues["lastUserInput"].upper() == "7":
                    currentImg = cmpt120imageManip.increase_brightness(currentImg)
                    cmpt120imageProj.showInterface(currentImg, "No Image", generateMenu(appStateValues))

                # set state to basic
                if appStateValues["lastUserInput"].upper() == "8":
                    tkinter.Tk().withdraw()
                    appStateValues['mode'] = 'basic'
                    cmpt120imageProj.showInterface(currentImg, "No Image", generateMenu(appStateValues))

                # set state to advanced
                if appStateValues["lastUserInput"].upper() == "9":
                    tkinter.Tk().withdraw()
                    appStateValues['mode'] = 'advanced'
                    cmpt120imageProj.showInterface(currentImg, "No Image", generateMenu(appStateValues))


            # ADVANCED FUNCTION LIST
            elif appStateValues['mode'] == 'advanced': 

                # quit program
                if appStateValues["lastUserInput"].upper() == "Q":
                    keepRunning = False

                # open original photo
                if appStateValues["lastUserInput"].upper() == "R":
                    currentImg = cmpt120imageManip.original()
                    cmpt120imageProj.showInterface(currentImg, "No Image", generateMenu(appStateValues))

                # ROTATE LEFT
                if appStateValues["lastUserInput"].upper() == "1":
                    currentImg = cmpt120imageManip.rotate_left(currentImg)
                    cmpt120imageProj.showInterface(currentImg, "No Image", generateMenu(appStateValues))

                # ROTATE RIGHT
                if appStateValues["lastUserInput"].upper() == "2":
                    currentImg = cmpt120imageManip.rotate_right(currentImg)
                    cmpt120imageProj.showInterface(currentImg, "No Image", generateMenu(appStateValues))

                # PIXELATE
                if appStateValues["lastUserInput"].upper() == "3":
                    currentImg = cmpt120imageManip.pixelate(currentImg)
                    cmpt120imageProj.showInterface(currentImg, "No Image", generateMenu(appStateValues))

                # BINARIZE
                if appStateValues["lastUserInput"].upper() == "4":
                    currentImg = cmpt120imageManip.binarize(currentImg)
                    cmpt120imageProj.showInterface(currentImg, "No Image", generateMenu(appStateValues))


                # set state to basic
                if appStateValues["lastUserInput"].upper() == "5":
                    tkinter.Tk().withdraw()
                    appStateValues['mode'] = 'basic'
                    cmpt120imageProj.showInterface(currentImg, "No Image", generateMenu(appStateValues))

                # set state to intermediate
                if appStateValues["lastUserInput"].upper() == "6":
                    tkinter.Tk().withdraw()
                    appStateValues['mode'] = 'intermediate'
                    cmpt120imageProj.showInterface(currentImg, "No Image", generateMenu(appStateValues))


            # otherwise let the helper function handle the input
            else:
                currentImg = handleUserInput(appStateValues, currentImg)
        elif event.type == pygame.QUIT: #another way to quit the program is to click the close botton
            keepRunning = False

# shutdown everything from the pygame package
pygame.quit()

print("Log: Program Quit")