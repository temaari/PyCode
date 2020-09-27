import os
import time
import ctypes
import threading 

LF_FACESIZE = 32
STD_OUTPUT_HANDLE = -11

class COORD(ctypes.Structure):
    _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

class CONSOLE_FONT_INFOEX(ctypes.Structure):
    _fields_ = [("cbSize", ctypes.c_ulong),
                ("nFont", ctypes.c_ulong),
                ("dwFontSize", COORD),
                ("FontFamily", ctypes.c_uint),
                ("FontWeight", ctypes.c_uint),
                ("FaceName", ctypes.c_wchar * LF_FACESIZE)]

font = CONSOLE_FONT_INFOEX()
font.cbSize = ctypes.sizeof(CONSOLE_FONT_INFOEX)
font.nFont = 12
font.dwFontSize.X = 11
font.dwFontSize.Y = 18
font.FontFamily = 54
font.FontWeight = 400
font.FaceName = "Lucida Console"

handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
ctypes.windll.kernel32.SetCurrentConsoleFontEx(
        handle, ctypes.c_long(False), ctypes.pointer(font))

#This is where the counting begins
clear = lambda: os.system('cls')
def countUp():
	min=0
	while (min < 10):
		for sec in range(60):
			if (sec == 59):
				min+= 1
			if min < 10 and sec < 10:
				print('0'+str(min) + ':0' + str(sec))
			elif sec < 10:
				print(str(min) + ':0' + str(sec))
			elif min < 10:
				print('0'+str(min) + ':' + str(sec))
			else:
				print(str(min) + ':' + str(sec))
			print("")
			time.sleep(0.001)
			clear()
def countDown(): #doesn't quite work popperly
	min=10
	while (min > 0):
		for sec in range(0,-59,-1):
			if (sec == -58 or min == 10):
				min-= 1
			else:
				print(str(min) + ':' + str(abs(sec)))
			print("")
			time.sleep(0.1)
			clear()

threading.Thread(target=countUp()).start()
threading.Thread(target=countDown()).start()
