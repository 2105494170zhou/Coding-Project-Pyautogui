import pyautogui as gui
import time
import cv2


def open_google():
    gui.press("win")
    time.sleep(0.5)
    gui.write("Google")
    time.sleep(0.5)
    gui.press("enter")
    time.sleep(0.5)
    gui.moveTo(1400, 1300, 0.5)
    gui.click()
    with gui.hold("ctrl"):
        gui.press("t")
    time.sleep(1)


def open_menu():
    open_google()
    gui.write("https://nmhschool.myschoolapp.com/app/student#login")
    gui.press("enter")
    time.sleep(3)

    popup_image_path5 = r"C:\Pictures\20241105235907.png"
    popup_image_path6 = r"C:\Pictures\20241106002259.png"
    popup_image_path2 = r"C:\Pictures\20241105234731.png"
    popup_image_path3 = r"C:\Pictures\20241105235230.png"
    popup_image_path4 = r"C:\Pictures\20241105230310.png"
    popup_image_path7 = r"C:\Pictures\20241106191221.png"

    list_image = [popup_image_path5, popup_image_path6, popup_image_path4, popup_image_path7]
    check10 = True

    while check10:
        for i in list_image:
            try:
                popup_image_path = gui.locateOnScreen(i, confidence=0.8)
                if popup_image_path:
                    gui.click(gui.center(popup_image_path))
                    print("Popup detected and closed.")
                    checking = i
                    if checking == popup_image_path7:
                        check10 = False
                        break
                    continue
            except gui.ImageNotFoundException:
                print("Image not found. Retrying...")
                continue

    time.sleep(2)

    while True:
        try:
            popup_location2 = gui.locateOnScreen(popup_image_path2, confidence=0.8)
            if popup_location2:
                gui.click(gui.center(popup_location2))
                print("Popup detected and closed.")
                break
        except gui.ImageNotFoundException:
            print("Image not found. Retrying...")

    time.sleep(1)
    with gui.hold("ctrl"):
        gui.press("f")
    gui.write("Alumni Hall")

    while True:
        try:
            popup_location3 = gui.locateOnScreen(popup_image_path3, confidence=0.8)
            if popup_location3:
                gui.click(gui.center(popup_location3))
                print("Popup detected and closed.")
                break
        except gui.ImageNotFoundException:
            print("Image not found. Retrying...")


def open_doc():
    open_google()

    popup_image_path1 = r"C:\Pictures\20241105232611.png"
    popup_image_path2 = r"C:\Pictures\20241105232955.png"
    listed_path = [popup_image_path2, popup_image_path1]
    check10 = True

    while check10:
        for i in listed_path:
            try:
                popup_location = gui.locateOnScreen(i, confidence=0.8)
                if popup_location:
                    gui.click(gui.center(popup_location))
                    print("Popup detected and closed.")
                    checking = i
                    if checking == popup_image_path2:
                        check10 = False
                        break
                    time.sleep(0.5)
                    continue
            except gui.ImageNotFoundException:
                print("Image not found. Retrying...")
                continue


def open_Gmail():
    open_google()
    popup_image_path1 = r"C:\Pictures\20241105231914.png"

    while True:
        try:
            popup_location1 = gui.locateOnScreen(popup_image_path1, confidence=0.8)
            if popup_location1:
                gui.click(gui.center(popup_location1))
                print("Popup detected and closed.")
                break
        except gui.ImageNotFoundException:
            print("Image not found. Retrying...")


def open_canvus():
    open_google()
    gui.write("https://nmhschool.okta.com/")
    gui.press("enter")
    time.sleep(2)

    popup_image_path1 = r"C:\Pictures\20241105201143.png"
    popup_image_path2 = r"C:\Pictures\20241105203546.png"
    popup_image_path3 = r"C:\Pictures\20241105230310.png"
    popup_image_path4 = r"C:\Pictures\20241105230310.png"

    listed_path = [popup_image_path2, popup_image_path1, popup_image_path3, popup_image_path4]
    check10 = True

    while check10:
        for i in listed_path:
            try:
                popup_location = gui.locateOnScreen(i, confidence=0.7)
                if popup_location:
                    gui.click(gui.center(popup_location))
                    print("Popup detected and closed.")
                    checking = i
                    if checking == popup_image_path2:
                        check10 = False
                        break
                    continue
            except gui.ImageNotFoundException:
                print("Image not found. Retrying...")
                continue


while True:
    print("Here are the options you are able to open with this application: Canvus, Gmail, Google doc, menu")
    app_open = input("Please enter the app you want to open: ").lower()

    if app_open == "gmail":
        open_Gmail()
    elif app_open == "canvus":
        open_canvus()
    elif app_open == "google doc":
        open_doc()
    elif app_open == "menu":
        open_menu()
    else:
        print("Application not yet developed.")
