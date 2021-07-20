import psutil
from time import sleep
import os

sleep(60)
while 1:
    sleep(1)
    if "orderbot.exe" not in [x.name() for x in psutil.process_iter()]:
        os.system('shutdown -s')

#pyinstaller --noconfirm --onefile --windowed --name "helperbot"  "C:/Users/youss/PycharmProjects/bot-helper/main.py"