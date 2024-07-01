import os

def shutdown_computer():
    if os.name == 'nt':  # Windows
        os.system('shutdown /s /t 1')  # 1 sec sleep
    elif os.name == 'posix':  # Unix/Linux
        os.system('sudo shutdown now')  

shutdown_computer()
