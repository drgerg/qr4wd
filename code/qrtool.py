#!/usr/bin/env python3
# 
# qrtool.py - 2024,2025 by Gregory A. Sanders (dr.gerg@drgerg.com)
# Read clipboard contents and generate QR from clipboard text. 
##
## NOTE: cv2 is installed by 'pip install opencv-python'
#
import tkinter as tk
import cv2  
from PIL import ImageGrab, Image
from pathlib import Path
from io import BytesIO
import win32clipboard

version = "1.4.1"

def clipIsImag():
    im = ImageGrab.grabclipboard()
    gotone = isinstance(im, Image.Image)
    if gotone == True:
        im.save('somefile.png','PNG')
    return gotone

def readImag():
    image = cv2.imread('somefile.png')
    detector = cv2.QRCodeDetector()
    data, vertices_array, binary_qrcode = detector.detectAndDecode(image)
    try:
        if vertices_array is not None:
            print("QRCode data:")
            print(data)
        else:
            print("There was some error")
    except:
        print("There was some error")
    Path.unlink('somefile.png')
    return data

def getClipboardText():
    root = tk.Tk()
    root.withdraw()  # keep the window from showing
    gctReturn = root.clipboard_get()
    root.quit()
    if gctReturn == None or gctReturn == "":
        gctReturn = "notText"
    gctReturn = gctReturn.replace('"',"")
    return gctReturn

def send_to_clipboard(clip_type, data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(clip_type, data)
    win32clipboard.CloseClipboard()

def send_text_to_clipboard(data, fmt):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(data, fmt)
    win32clipboard.CloseClipboard()

def makeqrcode(textPath):
    import qrcode
    img = qrcode.make(textPath)
    print(type(img))
    print(img.size)
    output = BytesIO()
    img.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]
    output.close()
    send_to_clipboard(win32clipboard.CF_DIB, data)

def main():
    itsanimage = clipIsImag()
    if itsanimage == True:
        print("Headed to readImag()")
        data = readImag()
        print(data)
        # subprocess.Popen(r'explorer /select,' + '"' + data + '"')
        send_text_to_clipboard(data,win32clipboard.CF_TEXT)
    else:
        print("The clipboard did not hold an image.")
        theText = getClipboardText()
        print('The text retrieved is {}'.format(theText))
        if theText != None and theText != "notText":
            makeqrcode(theText)
            print("Made the QR image.")


if __name__ == '__main__':
    try:
        main()
    except SystemExit as e:
        print('Error:\n{}'.format(e))
        endit = input("a thing")
        