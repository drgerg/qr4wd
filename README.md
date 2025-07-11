# qrtool - no camera needed.

### Handle QR codes on Windows desktop using the clipboard and this app.

"qrtool" is a utility to read the current contents of the clipboard then do one of two things:

 - If it finds text in the clipboard, it generates a QR code of that text
        and pops it into the clipboard.
 - If it finds an image in the clipboard, it tries to read it as a QR code.  If successful, 
        it converts the QR code and pops the resulting text into the clipboard.

There are many ways to use it. Snip a screenshot, or right-click on a QR and copy image.
Run qrtool.exe and then CTRL-V paste the text into an application like Notepad.

In reverse, CTRL-C copy text, then run qrtool.exe.  The CTRL-V paste into a graphics 
application like Paint or AutoCAD or your PDF editor.

NOTE: There is no feedback. You'll know it worked when you paste. That's exactly
what I wanted.
