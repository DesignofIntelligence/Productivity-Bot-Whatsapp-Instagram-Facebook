import os
import sys
from datetime import datetime
from time import sleep

import psutil as psutil
import pyautogui
import pyautogui as pt

# from win10toast import ToastNotifier

pyautogui.FAILSAFE = False
# toast = ToastNotifier()


# def resource_path(relative_path):
#     if hasattr(sys, '_MEIPASS'):
#         return os.path.join(sys._MEIPASS, relative_path)
#     return os.path.join(os.path.abspath("pictures"), relative_path)


whatsapp_open_count = 2
instagram_counter = 60
facebook_counter = 120
chat_opened = False


def restart():
    pt.moveTo(110, 50, duration=0.01)
    pt.click()
    # toast.show_toast("Maturing is painful", "Alternative is worse, absorb the pain", duration=2)


def archived_opened():
    position = pt.locateOnScreen("pictures/archive.png", confidence=0.6)
    if position is not None:  # we found archive
        return True
    else:
        return False


def whatsapp_opened_atm():
    position = pt.locateOnScreen("pictures/whatsapp_opened.png", confidence=0.9)
    if position is not None:
        return True
    else:
        return False


def facebook_search_detected():
    position = pt.locateOnScreen("pictures/facebook_search.png", confidence=0.9)
    if position is not None:
        return True
    else:
        return False


def instagram_detected():
    position = pt.locateOnScreen("pictures/instagram.png", confidence=0.8)
    if position is not None:
        return True
    else:
        return False


def instagram_search_detected():
    position = pt.locateOnScreen("pictures/instagram_search.png", confidence=0.8)
    if position is not None:
        return True
    else:
        return False


def emojis_opened():
    position = pt.locateOnScreen("pictures/emoji.png", confidence=0.8)
    if position is not None:
        return True
    else:
        return False


def is_chat_opened():
    position = pt.locateOnScreen("pictures/chat_opened.png", confidence=0.8)
    if position is not None:
        return True
    else:
        return False


def image_opened():
    position = pt.locateOnScreen("pictures/image_opened.png", confidence=0.8)
    if position is not None:
        return True
    else:
        return False


def facebook_profile_detected():
    position1 = pt.locateOnScreen("pictures/profile_of_friend.png", confidence=0.7)
    position2 = pt.locateOnScreen("pictures/profile_of_nonfriend.png", confidence=0.7)

    if position1 is not None or position2 is not None:
        return True
    else:
        return False


def facebook_detected():
    position = pt.locateOnScreen("pictures/facebook.png", confidence=0.7)
    if position is not None:
        return True
    else:
        return False


# sleep(60)
while 1:
    sleep(1)

    processes = [x.name() for x in psutil.process_iter()]
    # if "helperbot.exe" not in processes:
    #     os.system('shutdown -s')

    # if datetime.now().minute == 25 or datetime.now().minute == 55:
    # toast.show_toast("TAKE A BREAK!", "for 5 minutes", duration=60)

    if datetime.now().minute == 59:
        whatsapp_open_count = 2

    whatsapp_opened_this_cycle = False

    if "msedge.exe" in processes:
        if instagram_detected():
            if instagram_counter < 0:
                restart()
                continue

            instagram_counter = instagram_counter - 1
            if instagram_search_detected():
                restart()
                continue
############################################
        if facebook_detected():
            if facebook_counter < 0:
                restart()
                continue

            facebook_counter = facebook_counter - 1
            if facebook_search_detected() or facebook_profile_detected():
                restart()
                continue

        whatsapp_opened_this_cycle = whatsapp_opened_atm()

        if (whatsapp_open_count <= 0) and whatsapp_opened_this_cycle and (datetime.now().minute < 55):
            if is_chat_opened():
                restart()
                continue

        if whatsapp_opened_this_cycle:
            if is_chat_opened():
                sleep(2)
                if is_chat_opened():
                    chat_opened = True
            if archived_opened():
                restart()
                continue
            if emojis_opened():
                restart()
                continue
            while image_opened():
                sleep(0.25)

    if not whatsapp_opened_this_cycle and chat_opened:
        # pictures closed
        whatsapp_open_count -= 1
        # toast.show_toast("Whatsapp opened!", "Only " + str(whatsapp_open_count) + " time remaining", duration=2)
        chat_opened = False

# pyinstaller --noconfirm --onedir --windowed --name "orderbot" --add-data "C:/Users/youss/Desktop/Semester 8/CSE385
# Data Mining And Business/Project/pictures-bot/pictures;pictures/"  "C:/Users/youss/Desktop/Semester 8/CSE385 Data
# Mining And Business/Project/pictures-bot/pictures/main.py"
