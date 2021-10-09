import pyautogui
#import pytesseract
import time
#import imagehash
import os
from PIL import Image
from itertools import product
import PIL.ImageOps
from PIL import ImageGrab
import re
import cv2
import numpy as np
import win32gui
import keyboard
import pyperclip
import random

def loop():
    bbox = (-7,0,468,983)
    bbox2 = (450,0,916,983)
    bbox3 = (-7,0,916,983)
    #gotchas(bbox)
    #gotchas(bbox2)
    #delete_items()
    #send_gifts()
    #open_gifts(bbox,1)
    #open_gifts(bbox2,2)
    #evolve_mons()
    #delete_mons()
    #swap_accounts(bbox,1)
    img = ImageGrab.grab(bbox)
    print(scan_for_evolve(img,4))
    #string_search("",bbox3)
    evolve_mons(bbox3)



def gotchas(cage):
    print("=======================")
    print("== Activate Gotchas ===")
    print("=======================")
    im = ImageGrab.grab(cage)
    im.save(r'screen.png')
    time.sleep(1)
    gotcha_on_rgb = cv2.imread('templates\gotcha_on.png')
    gotcha_on_hsv = cv2.cvtColor(gotcha_on_rgb, cv2.COLOR_BGR2HSV)
    gotcha_off_rgb = cv2.imread('templates\gotcha_off.png')
    gotcha_off_hsv = cv2.cvtColor(gotcha_off_rgb, cv2.COLOR_BGR2HSV)
    scrn_rgb = cv2.imread('screen.png')
    scrn_hsv = cv2.cvtColor(scrn_rgb, cv2.COLOR_BGR2HSV)

    w,h = gotcha_on_rgb.shape[:-1]
    res = cv2.matchTemplate(scrn_hsv,gotcha_on_hsv,cv2.TM_CCOEFF_NORMED)
    threshold = 0.90
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(scrn_rgb,pt,(pt[0]+h,pt[1]+w),(0,255,255),2)
        pos = (int(pt[0]+(h/2))-5+random.randrange(10),int(pt[1]+(w/2))-5+random.randrange(10))
        print("gotcha on found")
        return

    time.sleep(1)
    gotcha_off = True
    while gotcha_off == True:
        im = ImageGrab.grab(cage)
        im.save(r'screen.png')
        time.sleep(1)
        scrn_rgb = cv2.imread('screen.png')
        scrn_hsv = cv2.cvtColor(scrn_rgb, cv2.COLOR_BGR2HSV)
        w,h = gotcha_off_rgb.shape[:-1]
        res = cv2.matchTemplate(scrn_hsv,gotcha_off_hsv,cv2.TM_CCOEFF_NORMED)
        threshold = 0.90
        loc = np.where( res >= threshold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(scrn_rgb,pt,(pt[0]+h,pt[1]+w),(0,255,255),2)
            pos = (int(pt[0]+(h/2))-5+random.randrange(10),int(pt[1]+(w/2))-5+random.randrange(10))
            pos2 = (int(pt[0]+(h/2))-100+random.randrange(10),int(pt[1]+(w/2))-5+random.randrange(10))
            print("gotcha off found")
            pyautogui.moveTo(pos)
            pyautogui.click()
            pyautogui.moveTo(pos2)
            time.sleep(10)
            break
        w,h = gotcha_on_rgb.shape[:-1]
        res = cv2.matchTemplate(scrn_hsv,gotcha_on_hsv,cv2.TM_CCOEFF_NORMED)
        threshold = 0.90
        loc = np.where( res >= threshold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(scrn_rgb,pt,(pt[0]+h,pt[1]+w),(0,255,255),2)
            pos = (int(pt[0]+(h/2))-5+random.randrange(10),int(pt[1]+(w/2))-5+random.randrange(10))
            print("gotcha on found")
            return

    return

def delete_items():

    return

def send_gifts():
    return

def open_gifts(cage,pos):
    print("====================")
    print("== Opening Gifts ===")
    print("====================")
    d2 = 0
    ph = 0
    if pos == 2:
        ph = ph + 450

    gifts_opened = 0

    open_rgb = cv2.imread('templates\open.png')
    open_hsv = cv2.cvtColor(open_rgb, cv2.COLOR_BGR2HSV)


    while gifts_opened < 30:
        pyautogui.moveTo(212+random.randrange(40)+ph,640+random.randrange(40))
        pyautogui.click()
        time.sleep(3)
        im = ImageGrab.grab(cage)
        im.save(r'screen.png')
        time.sleep(0.5)
        scrn_rgb = cv2.imread('screen.png')
        scrn_hsv = cv2.cvtColor(scrn_rgb, cv2.COLOR_BGR2HSV)

        w,h = open_rgb.shape[:-1]
        res = cv2.matchTemplate(scrn_hsv,open_hsv,cv2.TM_CCOEFF_NORMED)
        threshold = 0.90
        loc = np.where( res >= threshold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(scrn_rgb,pt,(pt[0]+h,pt[1]+w),(0,255,255),2)
            pos = (int(pt[0]+(h/2))-5+random.randrange(10)+ph,int(pt[1]+(w/2))-5+random.randrange(10))
            print("open found")
            pyautogui.moveTo(pos)
            pyautogui.click()
            time.sleep(20)
            pyautogui.moveTo(420+random.randrange(10)+ph,800+random.randrange(100))
            pyautogui.dragTo(10+random.randrange(15)+ph,810+random.randrange(80), 0.2, button='left')
            time.sleep(2)
            gifts_opened = gifts_opened + 1
            print("gifts opened: ",gifts_opened)
            break
    return

def evolve_mons(bbox):
    '''
    f = open("evolve_list.txt","r")

    not_ok = 1
    while not_ok == 1:
        pyautogui.moveTo(38-5+random.randrange(10),arrow_search_y-5+random.randrange(10))
        pyautogui.click()
        time.sleep(1)
        img = ImageGrab.grab(bbox)
        not_ok = check_if_ok(img)
        time.sleep(0.5)
    time.sleep(1)

    pyperclip.copy(f.readline())
    pyautogui.typewrite(pyperclip.paste(), interval=0.1)
    print("paste happens here^^")
    time.sleep(2)
    '''


    #moved to
    string_search("",bbox)


    for q in range(100):
        sx = [80, 530]
        sy = [334, 778]
        for x in sx:
            for y in sy:
                pyautogui.moveTo(x-5+random.randrange(10),y-5+random.randrange(10))
                pyautogui.click()
                time.sleep(0.2)

        print("loop: ",q)
        time.sleep(1)
        img = ImageGrab.grab(bbox)
        for p in range(4):
            evo_pos = scan_for_evolve(img,1)
            if evo_pos != ():
                pyautogui.moveTo(evo_pos)
                pyautogui.click()
            time.sleep(1)
            img = ImageGrab.grab(bbox)

        time.sleep(1)
        img = ImageGrab.grab(bbox)
        for p in range(4):
            yes_pos = scan_for_evolve(img,2)
            if yes_pos != ():
                pyautogui.moveTo(yes_pos)
                pyautogui.click()
            time.sleep(1)
            img = ImageGrab.grab(bbox)

        time.sleep(20)
        img = ImageGrab.grab(bbox)
        for p in range(4):
            checkmark_pos = scan_for_evolve(img,3)
            if checkmark_pos != ():
                pyautogui.moveTo(checkmark_pos)
                pyautogui.click()
            time.sleep(1)
            img = ImageGrab.grab(bbox)

    '''
    time.sleep(2)
    pkc = get_pcount(img)
    while pkc == -1:
        pyautogui.moveTo(81-5+random.randrange(10),355-5+random.randrange(10))
        pyautogui.click()
        time.sleep(2)
        evo_pos = ()
        evo_pos = scan_for_evolve(img,1)
        print(evo_pos)
        if evo_pos != ():
            time.sleep(0.4)
            pyautogui.moveTo(evo_pos)
            pyautogui.click()
            time.sleep(1)
            img = ImageGrab.grab(bbox)
            yes_pos = scan_for_evolve(img,2)
            pyautogui.moveTo(yes_pos)
            pyautogui.click()
            time.sleep(24)
            img = ImageGrab.grab(bbox)
            checkmark_pos = scan_for_evolve(img,2)
            pyautogui.moveTo(checkmark_pos)
            pyautogui.click()
            time.sleep(3)
        else:
            print("evo_pos: ")
        img = ImageGrab.grab(bbox)
        pkc = get_pcount(img)
    print("last pokemon evolved")
    '''

    return

def string_search(st,bbox):
    f = open("evolve_list.txt","r")
    sx = [38, 490]
    sy = [216, 650]

    pyperclip.copy(f.readline())
    for x in sx:
        for y in sy:
            img = ImageGrab.grab(bbox)
            while scan_for_evolve(img,4) == ():
                pyautogui.moveTo(x-5+random.randrange(10),y-5+random.randrange(10))
                pyautogui.click()
                time.sleep(1)
                img = ImageGrab.grab(bbox)
            pyautogui.typewrite(pyperclip.paste(), interval=0.1)
            print("paste happens here^^")
            time.sleep(1)
            pyautogui.moveTo(scan_for_evolve(img,4))
            pyautogui.click()
            time.sleep(2)

    return


def check_if_ok(im):
    if_ok = 1
    im.save(r'screen.png')
    time.sleep(1)
    tm_rgb = cv2.imread('templates/ok2.png')
    scrn_rgb = cv2.imread('screen.png')
    tm_hsv = cv2.cvtColor(tm_rgb, cv2.COLOR_BGR2HSV)
    scrn_hsv = cv2.cvtColor(scrn_rgb, cv2.COLOR_BGR2HSV)

    w,h = tm_rgb.shape[:-1]
    c_list = [(225,640)]

    res = cv2.matchTemplate(scrn_hsv,tm_hsv,cv2.TM_CCOEFF_NORMED)
    #res2 = cv2.matchTemplate(scrn_hsv,tm2_hsv,cv2.TM_CCOEFF_NORMED)

    threshold = 0.60
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        if_ok = 0
        print("ok found")

    return if_ok

def get_pcount(im):
    pcount = -1

    im.save(r'screen.png')
    time.sleep(1)
    tm_rgb = cv2.imread('templates/no_pokemon.png')
    scrn_rgb = cv2.imread('screen.png')
    tm_hsv = cv2.cvtColor(tm_rgb, cv2.COLOR_BGR2HSV)
    scrn_hsv = cv2.cvtColor(scrn_rgb, cv2.COLOR_BGR2HSV)

    w,h = tm_rgb.shape[:-1]
    c_list = [(225,640)]

    res = cv2.matchTemplate(scrn_hsv,tm_hsv,cv2.TM_CCOEFF_NORMED)

    threshold = 0.9
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        pcount = 1

    return pcount

def scan_for_evolve(im,j):
    im.save(r'screen.png')
    time.sleep(1)
    tm_rgb = cv2.imread('templates\EVOLVE.png')
    tm2_rgb = cv2.imread('templates\yes2.png')
    tm3_rgb = cv2.imread('templates\checkmark.png')
    tm4_rgb = cv2.imread('templates\ok2.png')
    scrn_rgb = cv2.imread('screen.png')
    tm_hsv = cv2.cvtColor(tm_rgb, cv2.COLOR_BGR2HSV)
    tm2_hsv = cv2.cvtColor(tm2_rgb, cv2.COLOR_BGR2HSV)
    tm3_hsv = cv2.cvtColor(tm3_rgb, cv2.COLOR_BGR2HSV)
    tm4_hsv = cv2.cvtColor(tm4_rgb, cv2.COLOR_BGR2HSV)
    scrn_hsv = cv2.cvtColor(scrn_rgb, cv2.COLOR_BGR2HSV)

    if j == 1:
        w,h = tm_rgb.shape[:-1]
    elif j == 2:
        w,h = tm2_rgb.shape[:-1]
    elif j == 3:
        w,h = tm3_rgb.shape[:-1]
    elif j == 4:
        w,h = tm4_rgb.shape[:-1]

    if j == 1:
        res = cv2.matchTemplate(scrn_hsv,tm_hsv,cv2.TM_CCOEFF_NORMED)
    elif j == 2:
        res = cv2.matchTemplate(scrn_hsv,tm2_hsv,cv2.TM_CCOEFF_NORMED)
    elif j == 3:
        res = cv2.matchTemplate(scrn_hsv,tm3_hsv,cv2.TM_CCOEFF_NORMED)
    elif j == 4:
        res = cv2.matchTemplate(scrn_hsv,tm4_hsv,cv2.TM_CCOEFF_NORMED)

    evolve_pos = ()
    threshold = 0.70
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(scrn_rgb,pt,(pt[0]+h,pt[1]+w),(0,255,255),2)
        evolve_pos = (int(pt[0]+(h/2))-5+random.randrange(10),int(pt[1]+(w/2))-5+random.randrange(10))

    return evolve_pos



def delete_mons():
    return

def swap_accounts(cage,acc):
    print("====================")
    print("== Swap Accounts ===")
    print("====================")
    d2 = 0
    im = ImageGrab.grab(cage)
    im.save(r'screen.png')
    time.sleep(1)
    menu_rgb = cv2.imread('templates\menu.png')
    menu_hsv = cv2.cvtColor(menu_rgb, cv2.COLOR_BGR2HSV)
    yes_rgb = cv2.imread('templates\yes.png')
    yes_hsv = cv2.cvtColor(yes_rgb, cv2.COLOR_BGR2HSV)
    settings_rgb = cv2.imread('templates\settings.png')
    settings_hsv = cv2.cvtColor(settings_rgb, cv2.COLOR_BGR2HSV)
    returning_rgb = cv2.imread('templates\\returning.png')
    returning_hsv = cv2.cvtColor(returning_rgb, cv2.COLOR_BGR2HSV)
    google_rgb = cv2.imread('templates\google.png')
    google_hsv = cv2.cvtColor(google_rgb, cv2.COLOR_BGR2HSV)
    signout_rgb = cv2.imread('templates\signout.png')
    signout_hsv = cv2.cvtColor(signout_rgb, cv2.COLOR_BGR2HSV)
    ok_rgb = cv2.imread('templates\ok.png')
    ok_hsv = cv2.cvtColor(ok_rgb, cv2.COLOR_BGR2HSV)
    choose_rgb = cv2.imread('templates\choose.png')
    choose_hsv = cv2.cvtColor(choose_rgb, cv2.COLOR_BGR2HSV)
    scrn_rgb = cv2.imread('screen.png')
    scrn_hsv = cv2.cvtColor(scrn_rgb, cv2.COLOR_BGR2HSV)

    w,h = menu_rgb.shape[:-1]
    res = cv2.matchTemplate(scrn_hsv,menu_hsv,cv2.TM_CCOEFF_NORMED)
    threshold = 0.90
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(scrn_rgb,pt,(pt[0]+h,pt[1]+w),(0,255,255),2)
        pos = (int(pt[0]+(h/2))-5+random.randrange(10),int(pt[1]+(w/2))-5+random.randrange(10))
        print("menu found")
        pyautogui.moveTo(pos)
        pyautogui.click()
        break

    time.sleep(3)
    in_menu = True
    while in_menu == True:
        im = ImageGrab.grab(cage)
        im.save(r'screen.png')
        time.sleep(1)
        scrn_rgb = cv2.imread('screen.png')
        scrn_hsv = cv2.cvtColor(scrn_rgb, cv2.COLOR_BGR2HSV)
        w,h = settings_rgb.shape[:-1]
        res = cv2.matchTemplate(scrn_hsv,settings_hsv,cv2.TM_CCOEFF_NORMED)
        threshold = 0.90
        loc = np.where( res >= threshold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(scrn_rgb,pt,(pt[0]+h,pt[1]+w),(0,255,255),2)
            pos = (int(pt[0]+(h/2))-5+random.randrange(10),int(pt[1]+(w/2))-5+random.randrange(10))
            print("settings found")
            pyautogui.moveTo(pos)
            pyautogui.click()
            in_menu = False
            break

    in_settings = True
    while in_settings == True:
        time.sleep(2)
        pyautogui.moveTo(320+random.randrange(20),730+random.randrange(30))
        pyautogui.dragTo(320+random.randrange(20),340+random.randrange(30),1.5)
        time.sleep(3)
        im = ImageGrab.grab(cage)
        im.save(r'screen.png')
        #signout_hsv.save(r'test.png')
        time.sleep(1)
        scrn_rgb = cv2.imread('screen.png')
        scrn_hsv = cv2.cvtColor(scrn_rgb, cv2.COLOR_BGR2HSV)
        w,h = signout_rgb.shape[:-1]
        res = cv2.matchTemplate(scrn_hsv,signout_hsv,cv2.TM_CCOEFF_NORMED)
        threshold = 0.9
        loc = np.where( res >= threshold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(scrn_rgb,pt,(pt[0]+h,pt[1]+w),(0,255,255),2)
            pos = (int(pt[0]+(h/2))-5+random.randrange(10),int(pt[1]+(w/2))-5+random.randrange(10))
            print("signout found")
            print(pos)
            pyautogui.moveTo(pos)
            pyautogui.click()
            in_settings = False
            break

    time.sleep(2)
    in_yn = True
    while in_yn == True:
        im = ImageGrab.grab(cage)
        im.save(r'screen.png')
        time.sleep(1)
        scrn_rgb = cv2.imread('screen.png')
        scrn_hsv = cv2.cvtColor(scrn_rgb, cv2.COLOR_BGR2HSV)
        w,h = settings_rgb.shape[:-1]
        res = cv2.matchTemplate(scrn_hsv,yes_hsv,cv2.TM_CCOEFF_NORMED)
        threshold = 0.90
        loc = np.where( res >= threshold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(scrn_rgb,pt,(pt[0]+h,pt[1]+w),(0,255,255),2)
            pos = (int(pt[0]+(h/2))-5+random.randrange(10),int(pt[1]+(w/2))-5+random.randrange(10))
            print("yes found")
            pyautogui.moveTo(pos)
            pyautogui.click()
            in_yn = False
            break

    time.sleep(2)
    in_player = True
    while in_player == True:
        im = ImageGrab.grab(cage)
        im.save(r'screen.png')
        time.sleep(1)
        scrn_rgb = cv2.imread('screen.png')
        scrn_hsv = cv2.cvtColor(scrn_rgb, cv2.COLOR_BGR2HSV)
        w,h = settings_rgb.shape[:-1]
        res = cv2.matchTemplate(scrn_hsv,returning_hsv,cv2.TM_CCOEFF_NORMED)
        threshold = 0.90
        loc = np.where( res >= threshold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(scrn_rgb,pt,(pt[0]+h,pt[1]+w),(0,255,255),2)
            pos = (int(pt[0]+(h/2))-5+random.randrange(10),int(pt[1]+(w/2))-5+random.randrange(10))
            print("returning found")
            pyautogui.moveTo(pos)
            pyautogui.click()
            in_player = False
            break

    time.sleep(2)
    in_with = True
    while in_with == True:
        im = ImageGrab.grab(cage)
        im.save(r'screen.png')
        time.sleep(1)
        scrn_rgb = cv2.imread('screen.png')
        scrn_hsv = cv2.cvtColor(scrn_rgb, cv2.COLOR_BGR2HSV)
        w,h = settings_rgb.shape[:-1]
        res = cv2.matchTemplate(scrn_hsv,google_hsv,cv2.TM_CCOEFF_NORMED)
        threshold = 0.90
        loc = np.where( res >= threshold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(scrn_rgb,pt,(pt[0]+h,pt[1]+w),(0,255,255),2)
            pos = (int(pt[0]+(h/2))-5+random.randrange(10),int(pt[1]+(w/2))-5+random.randrange(10))
            print("google found")
            pyautogui.moveTo(pos)
            pyautogui.click()
            in_with = False
            break
    time.sleep(4)
    select_account(acc)
    time.sleep(1)
    pyautogui.press('space')

    time.sleep(15)
    in_danger = True
    while in_danger == True:
        im = ImageGrab.grab(cage)
        im.save(r'screen.png')
        time.sleep(1)
        scrn_rgb = cv2.imread('screen.png')
        scrn_hsv = cv2.cvtColor(scrn_rgb, cv2.COLOR_BGR2HSV)
        w,h = settings_rgb.shape[:-1]
        res = cv2.matchTemplate(scrn_hsv,ok_hsv,cv2.TM_CCOEFF_NORMED)
        threshold = 0.90
        loc = np.where( res >= threshold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(scrn_rgb,pt,(pt[0]+h,pt[1]+w),(0,255,255),2)
            pos = (int(pt[0]+(h/2))-5+random.randrange(10),int(pt[1]+(w/2))-5+random.randrange(10))
            print("ok found")
            pyautogui.moveTo(pos)
            pyautogui.click()
            in_danger = False
            break

    return

def select_account(n):
    while n > 0:
        time.sleep(0.3)
        pyautogui.press('down')
        n = n - 1
    return
loop()

