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
import threading
import logging
logging.basicConfig(filename='log.log', level=logging.DEBUG,
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


busy = False


def first_thread(name):
    bbox = (-7, 0, 468, 983)
    bbox2 = (450, 0, 916, 983)
    bbox3 = (-7, 0, 916, 983)
    logging.info("first thread started")
    # gotchas(bbox)
    # gotchas(bbox2)
    # delete_items()
    i = 10
    while i < 15:
        swap_accounts(bbox, i, 1)
        enter_friendlist(bbox, 1)
        open_gifts(bbox, 1)
        send_gifts(bbox, 1)
        # swap_accounts(bbox,i,1)
        i = i + 1
    # open_gifts(bbox,1)
    # open_gifts(bbox3,1)
    # delete_mons()
    # swap_accounts(bbox,1)
    #img = ImageGrab.grab(bbox)
    # logging.info(img_detect(img,4))
    # string_search("",bbox3)
    # evolve_mons(bbox3)


def second_thread(name):
    logging.info("second thread started")
    bbox3 = (-7, 0, 916, 983)
    bbox2 = (450, 0, 916, 983)
    j = 10
    while j < 15:
        swap_accounts(bbox2, j, 2)
        enter_friendlist(bbox2, 2)
        open_gifts(bbox2, 2)
        send_gifts(bbox2, 2)
        # swap_accounts(bbox2,j,2)
        j = j + 1
    # send_gifts(bbox2,2)


def enter_friendlist(cage, pos):
    global busy

    while busy == True:
        time.sleep(0.5)
    busy = True
    pyautogui.moveTo(48+random.randrange(40)+cage[0], 850+random.randrange(40))
    pyautogui.click()
    busy = False

    time.sleep(5)

    while busy == True:
        time.sleep(0.5)
    busy = True
    pyautogui.moveTo(300+random.randrange(40) +
                     cage[0], 140+random.randrange(40))
    pyautogui.click()
    busy = False


def gotchas(cage, pos):
    logging.info("=======================")
    logging.info("== Activate Gotchas ===")
    logging.info("=======================")
    time.sleep(1)
    gotcha_on_rgb = cv2.imread('templates\gotcha_on.png')
    gotcha_on_hsv = cv2.cvtColor(gotcha_on_rgb, cv2.COLOR_BGR2HSV)
    gotcha_off_rgb = cv2.imread('templates\gotcha_off.png')
    gotcha_off_hsv = cv2.cvtColor(gotcha_off_rgb, cv2.COLOR_BGR2HSV)
    scrn_rgb = screen_save(cage, pos)
    scrn_hsv = cv2.cvtColor(scrn_rgb, cv2.COLOR_BGR2HSV)

    w, h = gotcha_on_rgb.shape[:-1]
    res = cv2.matchTemplate(scrn_hsv, gotcha_on_hsv, cv2.TM_CCOEFF_NORMED)
    threshold = 0.90
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(scrn_rgb, pt, (pt[0]+h, pt[1]+w), (0, 255, 255), 2)
        pos = (int(pt[0]+(h/2))-5+random.randrange(10),
               int(pt[1]+(w/2))-5+random.randrange(10))
        logging.info("gotcha on found")
        return

    time.sleep(1)
    gotcha_off = True
    while gotcha_off == True:
        im = ImageGrab.grab(cage)
        im.save(r'screen.png')
        time.sleep(1)
        scrn_rgb = screen_save(cage, pos)
        scrn_hsv = cv2.cvtColor(scrn_rgb, cv2.COLOR_BGR2HSV)
        w, h = gotcha_off_rgb.shape[:-1]
        res = cv2.matchTemplate(scrn_hsv, gotcha_off_hsv, cv2.TM_CCOEFF_NORMED)
        threshold = 0.90
        loc = np.where(res >= threshold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(scrn_rgb, pt, (pt[0]+h, pt[1]+w), (0, 255, 255), 2)
            pos = (int(pt[0]+(h/2))-5+random.randrange(10),
                   int(pt[1]+(w/2))-5+random.randrange(10))
            pos2 = (int(pt[0]+(h/2))-100+random.randrange(10),
                    int(pt[1]+(w/2))-5+random.randrange(10))
            logging.info("gotcha off found")
            pyautogui.moveTo(pos)
            pyautogui.click()
            pyautogui.moveTo(pos2)
            time.sleep(10)
            break
        w, h = gotcha_on_rgb.shape[:-1]
        res = cv2.matchTemplate(scrn_hsv, gotcha_on_hsv, cv2.TM_CCOEFF_NORMED)
        threshold = 0.90
        loc = np.where(res >= threshold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(scrn_rgb, pt, (pt[0]+h, pt[1]+w), (0, 255, 255), 2)
            pos = (int(pt[0]+(h/2))-5+random.randrange(10),
                   int(pt[1]+(w/2))-5+random.randrange(10))
            logging.info("gotcha on found")
            return

    return


def delete_items():

    return


def send_gifts(cage, pos):
    global busy

    gifts_sent = 0
    ga_rgb = cv2.imread('templates\giftable.png')
    ga_hsv = cv2.cvtColor(ga_rgb, cv2.COLOR_BGR2HSV)
    gga_rgb = cv2.imread('templates\g_giftable.png')
    gga_hsv = cv2.cvtColor(gga_rgb, cv2.COLOR_BGR2HSV)

    x_rgb = cv2.imread('templates\X.png')
    x_hsv = cv2.cvtColor(x_rgb, cv2.COLOR_BGR2HSV)
    cr_rgb = cv2.imread('templates\can_rec.png')
    cr_hsv = cv2.cvtColor(cr_rgb, cv2.COLOR_BGR2HSV)
    crb_rgb = cv2.imread('templates\can_rec_bad.png')
    crb_hsv = cv2.cvtColor(crb_rgb, cv2.COLOR_BGR2HSV)
    crd_rgb = cv2.imread('templates\can_rec_done.png')
    crd_hsv = cv2.cvtColor(crd_rgb, cv2.COLOR_BGR2HSV)
    cs_rgb = cv2.imread('templates\cant_send.png')
    cs_hsv = cv2.cvtColor(cs_rgb, cv2.COLOR_BGR2HSV)

    # Check friend sort option
    while busy == True:
        time.sleep(0.5)
    busy = True
    pyautogui.moveTo(375+random.randrange(40) +
                     cage[0], 850+random.randrange(40))
    pyautogui.click()
    pyautogui.moveTo(416+cage[0], 965)
    busy = False
    time.sleep(2)
    scrn_rgb = screen_save(cage, pos)
    scrn_hsv = cv2.cvtColor(scrn_rgb, cv2.COLOR_BGR2HSV)

    look4canrecdone = img_detect(scrn_hsv, crd_hsv, 0.99, cage)
    look4canrecbad = img_detect(scrn_hsv, crb_hsv, 0.99, cage)
    look4canrec = img_detect(scrn_hsv, cr_hsv, 0.99, cage)
    # logging.info(look4x)
    if look4canrecdone != ():
        logging.info("Found can_rec_done")
        look4x = img_detect(scrn_hsv, x_hsv, 0.9, cage)
        if look4x != ():
            while busy == True:
                time.sleep(0.5)
            busy = True
            pyautogui.moveTo(look4x)
            pyautogui.click()
            busy = False
        else:
            logging.info("Did not find X")
    elif look4canrecbad != ():
        while busy == True:
            time.sleep(0.5)
        busy = True
        pyautogui.moveTo(look4canrecbad)
        pyautogui.click()
        busy = False
    elif look4canrec != ():
        while busy == True:
            time.sleep(0.5)
        busy = True
        pyautogui.moveTo(look4canrec)
        pyautogui.click()
        pyautogui.moveTo(416+cage[0], 965)
        busy = False
        time.sleep(1)
        while busy == True:
            time.sleep(0.5)
        busy = True
        pyautogui.moveTo(375+random.randrange(40) +
                         cage[0], 850+random.randrange(40))
        pyautogui.click()
        busy = False

        time.sleep(2)
        scrn_rgb = screen_save(cage, pos)
        scrn_hsv = cv2.cvtColor(scrn_rgb, cv2.COLOR_BGR2HSV)
        look4canrecdone = img_detect(scrn_hsv, crd_hsv, 0.99, cage)
        look4canrecbad = img_detect(scrn_hsv, crb_hsv, 0.99, cage)
        look4canrec = img_detect(scrn_hsv, cr_hsv, 0.99, cage)

        if look4canrecdone != ():
            logging.info("Found ")
            look4x = img_detect(scrn_hsv, x_hsv, 0.9, cage)
            if look4x != ():
                while busy == True:
                    time.sleep(0.5)
                busy = True
                pyautogui.moveTo(look4x)
                pyautogui.click()
                busy = False
            else:
                logging.info("Did not find X")
        elif look4canrecbad != ():
            while busy == True:
                time.sleep(0.5)
            busy = True
            pyautogui.moveTo(look4canrecbad)
            pyautogui.click()
            busy = False

    # click first friend profile
    time.sleep(1.5)
    pyautogui.moveTo(62+random.randrange(13)+cage[0], 392+random.randrange(11))
    pyautogui.click()
    time.sleep(3)

    ag_rgb = cv2.imread('templates\cant_send.png')
    ag_hsv = cv2.cvtColor(ag_rgb, cv2.COLOR_BGR2HSV)
    scrn_rgb = screen_save(cage, pos)
    scrn_hsv = cv2.cvtColor(scrn_rgb, cv2.COLOR_BGR2HSV)
    already_gifted = img_detect(scrn_hsv, ag_hsv, 0.7, cage)

    if already_gifted != ():
        while gifts_sent < 20:
            scrn_rgb = screen_save(cage, pos)
            scrn_hsv = cv2.cvtColor(scrn_rgb, cv2.COLOR_BGR2HSV)
            logging.info("gift_block check")
            gift_block = img_detect(scrn_hsv, gga_hsv, 0.8, cage)
            logging.info("giftable check")
            giftable = img_detect(scrn_hsv, ga_hsv, 0.8, cage)
            cant_send = img_detect(scrn_hsv, cs_hsv, 0.9, cage)
            if cant_send != ():
                logging.info("could not send gifts")
                break
            if gift_block != ():
                while busy == True:
                    time.sleep(0.5)
                busy = True
                pyautogui.moveTo(gift_block)
                pyautogui.rightClick()
                busy = False
                time.sleep(1)
                scrn_rgb = screen_save(cage, pos)
                scrn_hsv = cv2.cvtColor(scrn_rgb, cv2.COLOR_BGR2HSV)
                logging.info("giftable check")
                giftable = img_detect(scrn_hsv, ga_hsv, 0.7, cage)
            if giftable != ():
                while busy == True:
                    time.sleep(0.5)
                busy = True
                pyautogui.moveTo(giftable)
                pyautogui.click()
                time.sleep(1)
                pyautogui.moveTo(258+random.randrange(10) +
                                 cage[0], 365+random.randrange(10))
                pyautogui.click()
                time.sleep(1)
                pyautogui.moveTo(211+random.randrange(10) +
                                 cage[0], 770+random.randrange(10))
                pyautogui.click()
                busy = False
                time.sleep(5)
            swipe(cage)
            time.sleep(0.5)

        gifts_sent = gifts_sent + 1
    x2_rgb = cv2.imread('templates\\x2.png')
    x2_hsv = cv2.cvtColor(x2_rgb, cv2.COLOR_BGR2HSV)
    scrn_rgb = screen_save(cage, pos)
    scrn_hsv = cv2.cvtColor(scrn_rgb, cv2.COLOR_BGR2HSV)
    exit_friendlist = img_detect(scrn_hsv, x2_hsv, 0.8, cage)
    if exit_friendlist != ():
        while busy == True:
            time.sleep(0.5)
        busy = True
        logging.info("busy: "+str(busy))
        time.sleep(0.3)
        pyautogui.moveTo(exit_friendlist)
        pyautogui.click()
        busy = False
        logging.info("busy: "+str(busy))
    x2_rgb = cv2.imread('templates\\x2.png')
    x2_hsv = cv2.cvtColor(x2_rgb, cv2.COLOR_BGR2HSV)
    scrn_rgb = screen_save(cage, pos)
    scrn_hsv = cv2.cvtColor(scrn_rgb, cv2.COLOR_BGR2HSV)
    exit_friendlist = img_detect(scrn_hsv, x2_hsv, 0.8, cage)
    if exit_friendlist != ():
        while busy == True:
            time.sleep(0.5)
        busy = True
        logging.info("busy: "+str(busy))
        time.sleep(0.3)
        pyautogui.moveTo(exit_friendlist)
        pyautogui.click()
        busy = False
        logging.info("busy: "+str(busy))
    return


def swipe(cage):
    global busy
    while busy == True:
        time.sleep(0.5)
    busy = True
    logging.info("busy: "+str(busy))
    time.sleep(2)
    pyautogui.moveTo(420+random.randrange(10) +
                     cage[0], 800+random.randrange(100))
    pyautogui.dragTo(10+random.randrange(15) +
                     cage[0], 810+random.randrange(80), 0.2, button='left')
    time.sleep(1)
    busy = False
    logging.info("busy: "+str(busy))
    time.sleep(1)
    return


def open_gifts(cage, pos):
    logging.info("====================")
    logging.info("== Opening Gifts ===")
    logging.info("====================")

    global busy
    d2 = 0

    x_rgb = cv2.imread('templates\X.png')
    x_hsv = cv2.cvtColor(x_rgb, cv2.COLOR_BGR2HSV)
    sg_rgb = cv2.imread('templates\sel_gift.png')
    sg_hsv = cv2.cvtColor(sg_rgb, cv2.COLOR_BGR2HSV)
    sgu_rgb = cv2.imread('templates\sel_gift_up.png')
    sgu_hsv = cv2.cvtColor(sgu_rgb, cv2.COLOR_BGR2HSV)
    sgd_rgb = cv2.imread('templates\sel_gift_down.png')
    sgd_hsv = cv2.cvtColor(sgd_rgb, cv2.COLOR_BGR2HSV)
    ser_rgb = cv2.imread('templates\search2.png')
    ser_hsv = cv2.cvtColor(ser_rgb, cv2.COLOR_BGR2HSV)
    ok_rgb = cv2.imread('templates\ok2.png')
    ok_hsv = cv2.cvtColor(ok_rgb, cv2.COLOR_BGR2HSV)

    # Check friend sort option
    while busy == True:
        time.sleep(0.5)
    busy = True
    logging.info("busy: "+str(busy))
    pyautogui.moveTo(375+random.randrange(40) +
                     cage[0], 850+random.randrange(40))
    pyautogui.click()
    pyautogui.moveTo(416, 965)
    busy = False
    logging.info("busy: "+str(busy))
    time.sleep(2)
    scrn_rgb = screen_save(cage, pos)
    scrn_hsv = cv2.cvtColor(scrn_rgb, cv2.COLOR_BGR2HSV)

    look4selgiftdown = img_detect(scrn_hsv, sgd_hsv, 0.99, cage)
    look4selgiftup = img_detect(scrn_hsv, sgu_hsv, 0.99, cage)
    look4selgift = img_detect(scrn_hsv, sg_hsv, 0.99, cage)
    # logging.info(look4x)
    if look4selgiftdown != ():
        logging.info("Found sel_gift_down")
        look4x = img_detect(scrn_hsv, x_hsv, 0.9, cage)
        if look4x != ():
            while busy == True:
                time.sleep(0.5)
            busy = True
            logging.info("busy: "+str(busy))
            pyautogui.moveTo(look4x)
            pyautogui.click()
            busy = False
            logging.info("busy: "+str(busy))
        else:
            logging.info("Did not find X")
    elif look4selgiftup != ():
        while busy == True:
            time.sleep(0.5)
        busy = True
        logging.info("busy: "+str(busy))
        pyautogui.moveTo(look4selgiftup)
        pyautogui.click()
        busy = False
        logging.info("busy: "+str(busy))
    elif look4selgift != ():
        while busy == True:
            time.sleep(0.5)
        busy = True
        logging.info("busy: "+str(busy))
        pyautogui.moveTo(look4selgift)
        pyautogui.click()
        pyautogui.moveTo(416, 965)
        busy = False
        logging.info("busy: "+str(busy))
        time.sleep(1)
        while busy == True:
            time.sleep(0.5)
        busy = True
        logging.info("busy: "+str(busy))
        pyautogui.moveTo(375+random.randrange(40) +
                         cage[0], 850+random.randrange(40))
        pyautogui.click()
        busy = False
        logging.info("busy: "+str(busy))

        time.sleep(2)
        scrn_rgb = screen_save(cage, pos)
        scrn_hsv = cv2.cvtColor(scrn_rgb, cv2.COLOR_BGR2HSV)
        look4selgiftdown = img_detect(scrn_hsv, sgd_hsv, 0.99, cage)
        look4selgiftup = img_detect(scrn_hsv, sgu_hsv, 0.99, cage)
        look4selgift = img_detect(scrn_hsv, sg_hsv, 0.99, cage)

        if look4selgiftdown != ():
            logging.info("Found ")
            look4x = img_detect(scrn_hsv, x_hsv, 0.9, cage)
            if look4x != ():
                while busy == True:
                    time.sleep(0.5)
                busy = True
                logging.info("busy: "+str(busy))
                pyautogui.moveTo(look4x)
                pyautogui.click()
                busy = False
                logging.info("busy: "+str(busy))
            else:
                logging.info("Did not find X")
        elif look4selgiftup != ():
            while busy == True:
                time.sleep(0.5)
            busy = True
            logging.info("busy: "+str(busy))
            pyautogui.moveTo(look4selgiftup)
            pyautogui.click()
            busy = False
            logging.info("busy: "+str(busy))

    # search for interactable friends
    logging.info("Search for interactable friends")
    time.sleep(1)
    pyperclip.copy("interactable")
    scrn_rgb = screen_save(cage, pos)
    scrn_hsv = cv2.cvtColor(scrn_rgb, cv2.COLOR_BGR2HSV)
    look4search = img_detect(scrn_hsv, ser_hsv, 0.8, cage)
    if look4search != ():
        logging.info("look4search: "+str(look4search))
        while busy == True:
            time.sleep(0.5)
        busy = True
        logging.info("busy: "+str(busy))
        pyautogui.moveTo(look4search)
        pyautogui.click()
        time.sleep(0.6)
        pyautogui.typewrite(pyperclip.paste(), interval=0.1)
        busy = False
        logging.info("busy: "+str(busy))
    scrn_rgb = screen_save(cage, pos)
    scrn_hsv = cv2.cvtColor(scrn_rgb, cv2.COLOR_BGR2HSV)
    look4ok = img_detect(scrn_hsv, ok_hsv, 0.9, cage)
    if look4ok != ():
        time.sleep(0.5)
        while busy == True:
            time.sleep(0.5)
        busy = True
        logging.info("busy: "+str(busy))
        pyautogui.moveTo(look4ok)
        pyautogui.click()
        busy = False
        logging.info("busy: "+str(busy))
        time.sleep(0.6)

    # click first friend profile
    time.sleep(1)
    fhg_rgb = cv2.imread('templates\\friend_has_gift.png')
    fhg_hsv = cv2.cvtColor(fhg_rgb, cv2.COLOR_BGR2HSV)
    scrn_rgb = screen_save(cage, pos)
    scrn_hsv = cv2.cvtColor(scrn_rgb, cv2.COLOR_BGR2HSV)
    there_are_gifts = img_detect(scrn_hsv, fhg_hsv, 0.8, cage)

    if there_are_gifts != ():
        time.sleep(1.5)
        while busy == True:
            time.sleep(0.5)
        busy = True
        logging.info("busy: "+str(busy))
        pyautogui.moveTo(62+random.randrange(13) +
                         cage[0], 392+random.randrange(11))
        pyautogui.click()
        busy = False
        logging.info("busy: "+str(busy))
        time.sleep(3)

        gifts_opened = 0

        open_rgb = cv2.imread('templates\open.png')
        open_hsv = cv2.cvtColor(open_rgb, cv2.COLOR_BGR2HSV)

        while gifts_opened < 30:
            while busy == True:
                time.sleep(0.5)
            busy = True
            logging.info("busy: "+str(busy))
            pyautogui.moveTo(212+random.randrange(40) +
                             cage[0], 640+random.randrange(40))
            pyautogui.click()
            busy = False
            logging.info("busy: "+str(busy))
            time.sleep(3)
            scrn_rgb = screen_save(cage, pos)
            scrn_hsv = cv2.cvtColor(scrn_rgb, cv2.COLOR_BGR2HSV)

            look4opengift = img_detect(scrn_hsv, open_hsv, 0.99, cage)

            if look4opengift != ():
                logging.info("open found")
                while busy == True:
                    time.sleep(0.5)
                busy = True
                logging.info("busy: "+str(busy))
                pyautogui.moveTo(look4opengift)
                pyautogui.click()
                busy = False
                logging.info("busy: "+str(busy))
                gifts_opened = gifts_opened + 1
                logging.info("gifts opened: "+str(gifts_opened))
                time.sleep(20)
            while busy == True:
                time.sleep(0.5)
            busy = True
            logging.info("busy: "+str(busy))
            pyautogui.moveTo(420+random.randrange(10) +
                             cage[0], 800+random.randrange(100))
            pyautogui.dragTo(
                10+random.randrange(15)+cage[0], 810+random.randrange(80), 0.2, button='left')
            busy = False
            logging.info("busy: "+str(busy))
            time.sleep(2)

    x_rgb = cv2.imread('templates\\x_underlined.png')
    x_hsv = cv2.cvtColor(x_rgb, cv2.COLOR_BGR2HSV)
    scrn_rgb = screen_save(cage, pos)
    scrn_hsv = cv2.cvtColor(scrn_rgb, cv2.COLOR_BGR2HSV)
    clear_search = img_detect(scrn_hsv, x_hsv, 0.8, cage)
    if clear_search != ():
        while busy == True:
            time.sleep(0.5)
        busy = True
        logging.info("busy: "+str(busy))
        time.sleep(0.3)
        pyautogui.moveTo(clear_search)
        pyautogui.click()
        busy = False
        logging.info("busy: "+str(busy))

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
    logging.info("paste happens here^^")
    time.sleep(2)
    '''

    # moved to
    string_search("", bbox)

    for q in range(1000):
        sx = [80, 530]
        sy = [334, 778]
        for x in sx:
            for y in sy:
                pyautogui.moveTo(x-5+random.randrange(10),
                                 y-5+random.randrange(10))
                pyautogui.click()
                time.sleep(0.2)

        logging.info("loop: ", q)
        time.sleep(1)
        img = ImageGrab.grab(bbox)
        for p in range(4):
            evo_pos = img_detect(img, 1)
            if evo_pos != ():
                pyautogui.moveTo(evo_pos)
                pyautogui.click()
            time.sleep(1)
            img = ImageGrab.grab(bbox)

        time.sleep(1)
        img = ImageGrab.grab(bbox)
        for p in range(4):
            yes_pos = img_detect(img, 2)
            if yes_pos != ():
                pyautogui.moveTo(yes_pos)
                pyautogui.click()
            time.sleep(1)
            img = ImageGrab.grab(bbox)

        time.sleep(20)
        img = ImageGrab.grab(bbox)
        for p in range(4):
            checkmark_pos = img_detect(img, 3)
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
        evo_pos = img_detect(img,1)
        logging.info(evo_pos)
        if evo_pos != ():
            time.sleep(0.4)
            pyautogui.moveTo(evo_pos)
            pyautogui.click()
            time.sleep(1)
            img = ImageGrab.grab(bbox)
            yes_pos = img_detect(img,2)
            pyautogui.moveTo(yes_pos)
            pyautogui.click()
            time.sleep(24)
            img = ImageGrab.grab(bbox)
            checkmark_pos = img_detect(img,2)
            pyautogui.moveTo(checkmark_pos)
            pyautogui.click()
            time.sleep(3)
        else:
            logging.info("evo_pos: ")
        img = ImageGrab.grab(bbox)
        pkc = get_pcount(img)
    logging.info("last pokemon evolved")
    '''

    return


def string_search(st, bbox):
    f = open("evolve_list.txt", "r")
    sx = [38, 490]
    sy = [216, 650]

    pyperclip.copy(f.readline())
    for x in sx:
        for y in sy:
            img = ImageGrab.grab(bbox)
            while img_detect(img, 4) == ():
                pyautogui.moveTo(x-5+random.randrange(10),
                                 y-5+random.randrange(10))
                pyautogui.click()
                time.sleep(1)
                img = ImageGrab.grab(bbox)
            pyautogui.typewrite(pyperclip.paste(), interval=0.1)
            logging.info("paste happens here^^")
            time.sleep(1)
            pyautogui.moveTo(img_detect(img, 4))
            pyautogui.click()
            time.sleep(2)

    return


def check_if_ok(im):
    if_ok = 1
    im.save(r'screen.png')
    time.sleep(1)
    tm_rgb = cv2.imread('templates/ok2.png')
    scrn_rgb = screen_save(cage, pos)
    tm_hsv = cv2.cvtColor(tm_rgb, cv2.COLOR_BGR2HSV)
    scrn_hsv = cv2.cvtColor(scrn_rgb, cv2.COLOR_BGR2HSV)

    w, h = tm_rgb.shape[:-1]
    c_list = [(225, 640)]

    res = cv2.matchTemplate(scrn_hsv, tm_hsv, cv2.TM_CCOEFF_NORMED)
    #res2 = cv2.matchTemplate(scrn_hsv,tm2_hsv,cv2.TM_CCOEFF_NORMED)

    threshold = 0.60
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        if_ok = 0
        logging.info("ok found")

    return if_ok


def get_pcount(im):
    pcount = -1

    im.save(r'screen.png')
    time.sleep(1)
    tm_rgb = cv2.imread('templates/no_pokemon.png')
    scrn_rgb = screen_save(cage, pos)
    tm_hsv = cv2.cvtColor(tm_rgb, cv2.COLOR_BGR2HSV)
    scrn_hsv = cv2.cvtColor(scrn_rgb, cv2.COLOR_BGR2HSV)

    w, h = tm_rgb.shape[:-1]
    c_list = [(225, 640)]

    res = cv2.matchTemplate(scrn_hsv, tm_hsv, cv2.TM_CCOEFF_NORMED)

    threshold = 0.9
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        pcount = 1

    return pcount


def img_detect(im_hsv, j_hsv, thres, cage):
    w, h = j_hsv.shape[:-1]
    #logging.info("cage[0]: "+str(cage[0]))
    """
    tm_rgb = cv2.imread('templates\EVOLVE.png')
    tm2_rgb = cv2.imread('templates\yes2.png')
    tm3_rgb = cv2.imread('templates\checkmark.png')
    tm4_rgb = cv2.imread('templates\ok2.png')
    scrn_rgb = screen_save(cage,pos)
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
    """
    res = cv2.matchTemplate(im_hsv, j_hsv, cv2.TM_CCOEFF_NORMED)
    found_pos = ()
    threshold = thres
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        # cv2.rectangle(im_hsv,pt,(pt[0]+h2,pt[1]+w),(0,255,255),2)
        found_pos = (int(pt[0]+(h/2)+cage[0])-5+random.randrange(10),
                     int(pt[1]+(w/2))-5+random.randrange(10))
    if found_pos != ():
        logging.info("Image match found at: "+str(found_pos))
    else:
        logging.info("Image not found.")
        logging.info("cage: "+str(cage))
        logging.info("thres: "+str(thres))
    return found_pos


def delete_mons():
    return


def screen_save(cage, pos):
    if pos == 1:
        im = ImageGrab.grab(cage)
        im.save(r'screen.png')
        time.sleep(0.5)
        img = cv2.imread('screen.png')
    elif pos == 2:
        im = ImageGrab.grab(cage)
        im.save(r'screen2.png')
        time.sleep(0.5)
        img = cv2.imread('screen2.png')
    return img


def swap_accounts(cage, acc, pos):
    logging.info("====================")
    logging.info("== Swap Accounts ===")
    logging.info("====================")
    global busy
    d2 = 0
    time.sleep(2)

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
    cancel_rgb = cv2.imread('templates\cancel.png')
    cancel_hsv = cv2.cvtColor(cancel_rgb, cv2.COLOR_BGR2HSV)
    scrn_rgb = screen_save(cage, pos)
    scrn_hsv = cv2.cvtColor(scrn_rgb, cv2.COLOR_BGR2HSV)

    look4menu = img_detect(scrn_hsv, menu_hsv, 0.8, cage)

    if look4menu != ():
        logging.info("menu found")
        while busy == True:
            time.sleep(0.5)
        busy = True
        logging.info("busy: "+str(busy))
        pyautogui.moveTo(look4menu)
        pyautogui.click()
        busy = False
        logging.info("busy: "+str(busy))

    time.sleep(3)
    in_menu = True
    while in_menu == True:
        time.sleep(1)
        scrn_rgb = screen_save(cage, pos)
        scrn_hsv = cv2.cvtColor(scrn_rgb, cv2.COLOR_BGR2HSV)
        look4settings = img_detect(scrn_hsv, settings_hsv, 0.8, cage)
        if look4settings != ():
            logging.info("settings found")
            in_menu = False
            while busy == True:
                time.sleep(0.5)
            busy = True
            logging.info("busy: "+str(busy))
            pyautogui.moveTo(look4settings)
            pyautogui.click()
            busy = False
            logging.info("busy: "+str(busy))

    in_settings = True
    while in_settings == True:
        time.sleep(2)
        while busy == True:
            time.sleep(0.5)
        busy = True
        pyautogui.moveTo(320+random.randrange(20) +
                         cage[0], 730+random.randrange(30))
        pyautogui.dragTo(320+random.randrange(20) +
                         cage[0], 340+random.randrange(30), 1.5)
        busy = False
        time.sleep(3)
        # signout_hsv.save(r'test.png')
        time.sleep(1)
        scrn_rgb = screen_save(cage, pos)
        scrn_hsv = cv2.cvtColor(scrn_rgb, cv2.COLOR_BGR2HSV)
        look4signout = img_detect(scrn_hsv, signout_hsv, 0.8, cage)
        if look4signout != ():
            logging.info("signout found")
            in_settings = False
            while busy == True:
                time.sleep(0.5)
            busy = True
            logging.info("busy: "+str(busy))
            pyautogui.moveTo(look4signout)
            pyautogui.click()
            busy = False
            logging.info("busy: "+str(busy))

    time.sleep(2)
    in_yn = True
    while in_yn == True:
        time.sleep(1)
        scrn_rgb = screen_save(cage, pos)
        scrn_hsv = cv2.cvtColor(scrn_rgb, cv2.COLOR_BGR2HSV)
        look4yes = img_detect(scrn_hsv, yes_hsv, 0.9, cage)
        if look4yes != ():
            logging.info("yes found")
            in_yn = False
            while busy == True:
                time.sleep(0.5)
            busy = True
            logging.info("busy: "+str(busy))
            pyautogui.moveTo(look4yes)
            pyautogui.click()
            busy = False
            logging.info("busy: "+str(busy))

    time.sleep(2)
    in_player = True
    while in_player == True:
        time.sleep(1)
        scrn_rgb = screen_save(cage, pos)
        scrn_hsv = cv2.cvtColor(scrn_rgb, cv2.COLOR_BGR2HSV)
        look4returning = img_detect(scrn_hsv, returning_hsv, 0.8, cage)
        if look4returning != ():
            logging.info("returning found")
            in_player = False
            while busy == True:
                time.sleep(0.5)
            busy = True
            logging.info("busy: "+str(busy))
            pyautogui.moveTo(look4returning)
            pyautogui.click()
            busy = False
            logging.info("busy: "+str(busy))

    time.sleep(2)
    in_with = True
    while in_with == True:
        time.sleep(1)
        scrn_rgb = screen_save(cage, pos)
        scrn_hsv = cv2.cvtColor(scrn_rgb, cv2.COLOR_BGR2HSV)
        look4google = img_detect(scrn_hsv, google_hsv, 0.8, cage)
        if look4google != ():
            logging.info("google found")
            in_with = False
            while busy == True:
                time.sleep(0.5)
            busy = True
            logging.info("busy: "+str(busy))
            pyautogui.moveTo(look4google)
            pyautogui.click()
            # Don't want to swap windows at this point because
            # select_account() relies on it staying in focus

    time.sleep(4)
    select_account(acc)

    time.sleep(15)
    in_danger = True
    while in_danger == True:
        time.sleep(1)
        scrn_rgb = screen_save(cage, pos)
        scrn_hsv = cv2.cvtColor(scrn_rgb, cv2.COLOR_BGR2HSV)
        look4ok = img_detect(scrn_hsv, ok_hsv, 0.9, cage)
        if look4ok != ():
            logging.info("ok found")
            in_danger = False
            while busy == True:
                time.sleep(0.5)
            busy = True
            logging.info("busy: "+str(busy))
            pyautogui.moveTo(look4ok)
            pyautogui.click()
            busy = False
            logging.info("busy: "+str(busy))

    # Todo: may need to add rightClicks until it gets to "Do you want to
    # Exit?" in order to skip over accolades/news then rightClick out of it.
    in_news = True
    while in_news == True:
        pyautogui.moveTo(269+random.randrange(40) +
                         cage[0], 771+random.randrange(40))
        pyautogui.rightClick()
        time.sleep(1)
        scrn_rgb = screen_save(cage, pos)
        scrn_hsv = cv2.cvtColor(scrn_rgb, cv2.COLOR_BGR2HSV)
        look4cancel = img_detect(scrn_hsv, cancel_hsv, 0.9, cage)
        if look4cancel != ():
            logging.info("cancel found")
            in_news = False
            while busy == True:
                time.sleep(0.5)
            busy = True
            logging.info("busy: "+str(busy))
            pyautogui.moveTo(269+random.randrange(40) +
                             cage[0], 771+random.randrange(40))
            pyautogui.rightClick()
            busy = False
            logging.info("busy: "+str(busy))

    return


def select_account(n):
    global busy
    logging.info("busy: "+str(busy))
    while n > -1:
        time.sleep(0.3)
        pyautogui.press('down')
        n = n - 1
    time.sleep(1)
    pyautogui.press('space')
    busy = False
    logging.info("busy: "+str(busy))
    return


if __name__ == "__main__":
    x = threading.Thread(target=first_thread, args=(1,))
    x.start()
    y = threading.Thread(target=second_thread, args=(2,))
    y.start()
