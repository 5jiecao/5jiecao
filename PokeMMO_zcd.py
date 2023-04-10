import time
from tkinter import messagebox
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton,  QPlainTextEdit
import pyautogui
import tkinter as tk
import win32gui as pwin
import win32con
import pygetwindow
import ctypes
import ctypes.wintypes
import asyncio

#创建一个名为 PokeMMO_zcd 的类
user32 = ctypes.windll.user32
FindWindow = user32.FindWindowW  # 使用Unicode编码的版本
FindWindow.restype = ctypes.wintypes.HWND
FindWindow.argtypes = (ctypes.wintypes.LPCWSTR, ctypes.wintypes.LPCWSTR)

class PokeMMO_zcd:
    
    def __init__(self):
        
        ## 初始化 Qt 的应用程序
        self.app = QApplication([])
        # 创建一个名为 window 的主窗口，并设置大小和位置
        self.window = QMainWindow()
        self.window.resize(500, 400)
        self.window.move(300, 310)
        # 设置窗口的标题
        self.window.setWindowTitle('猫男pokemmo辅助')
        # 创建一个名为 text_edit 的文本框，并设置位置和大小
        self.text_edit = QPlainTextEdit(self.window)
        self.text_edit.move(50, 180)
        self.text_edit.resize(400, 200)
        
        # 添加一个按钮
        self.button = QPushButton('一键浇水', self.window)
        self.button.move(200, 100)
        self.button.resize(100, 50)
        self.button.clicked.connect(self.jiaoshui)

        self.window.show()

    def _get_window_handle(self, timeout=10):
        """获取窗口句柄"""
        start_time = time.time()
        while True:
            # 枚举所有顶级窗口，找到标题为 'PokeMMO' 的窗口
            hwnd = pwin.FindWindow(None, "PokeMMO")
            if hwnd != 0:
                return hwnd
            if time.time() - start_time >= timeout:
                return None
            time.sleep(1)

    async def jiaoshui(self):
        # 获取游戏窗口对象
        
        print("我进入了浇水里面判断")
        # 查找窗口句柄
        time.sleep(1)
        #hwnd = pwin.GetForegroundWindow()
        hwnd = 199736
        print(hwnd)
        await asyncio.sleep(2)
        # 模拟按键按下
        pwin.PostMessage(hwnd, win32con.WM_KEYDOWN, ord('Z'), 0)

        # 模拟按键释放
        pwin.PostMessage(hwnd, win32con.WM_KEYUP, ord('Z'), 0)

        #pyautogui.typewrite('z')
        #pyautogui.typewrite('z')
        print("我按了次Z")
        time.sleep(1)
        found_pos = pyautogui.locateCenterOnScreen('image/zzpd.png')
        if found_pos is not None:
            print("我进入了if里面判断")
            print("找到dl2.1.png，等待0.5秒后搜索是.png")
            time.sleep(0.5)  # 等待0.5秒
            found_pos_2 = pyautogui.locateCenterOnScreen('image/是.png')
            x_2, y_2 = found_pos_2     
            print("找到是.png，我要移动鼠标过去了")
            print("小飞棍来咯")
            #pyautogui.moveTo(x_2, y_2, 0.1)
            pyautogui.click(button='z')
    
    def run(self):
        # 创建一个事件循环对象
        loop = asyncio.get_event_loop()

        # 将异步函数加入到事件循环中并执行
        loop.run_until_complete(jiaoshui())

        # 关闭事件循环
        loop.close()
        
    def start(self):
        self.app.exec_()
        
if __name__ == "__main__":
    poke = PokeMMO_zcd()
    poke.start()