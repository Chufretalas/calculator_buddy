import subprocess
import pyautogui as pgui

def main():
    calcPID = subprocess.Popen(r"C:\Windows\System32\calc.exe")
    print(calcPID.pid)

    screenWidth, screenHeight = pgui.size()

if __name__ == "__main__":
    main()