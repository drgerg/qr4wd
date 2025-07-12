# qrtool - no camera, no Internet needed.

### Handle QR codes on Windows desktop using the clipboard and this app.

"qrtool" is a utility to get text in and out of QR codes on the Windows desktop.
It does this by reading the current contents of the clipboard then doing one of two things:

 - If it finds text in the clipboard, it generates a QR code of that text
        and pops that into the clipboard.
 - If it finds an image in the clipboard, it tries to read it as a QR code.  If successful, 
        it converts the QR code and pops the resulting text into the clipboard.

This tool does not try to send the qr code data anywhere.  It simply copies it to the
clipboard so you can paste it.

There are many ways to use it. Snip a QR code on the screen, or right-click on a QR and 'Copy Image'.
Run qrtool.exe (I have the icon pinned to my Taskbar) and then CTRL-V paste the text into an application 
like Notepad. I have my most consistent positive results when using Windows' Snipping tool.

In reverse, CTRL-C copy text, then run qrtool.exe.  The CTRL-V paste into a graphics 
application like Paint or AutoCAD or your PDF editor.

NOTE: There is no feedback. You'll know it worked when you paste. That's exactly
what I wanted.
