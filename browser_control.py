import serial                                      # add Serial library for serial communication
import pyautogui                                   # add pyautogui library for programmatically controlling the mouse and keyboard.
import time 
import statistics
 
Arduino_Serial = serial.Serial('COM4',9600)       # Initialize serial and Create Serial port object called Arduino_Serial
 
data1 = []

 
def cal_std(data):
    length_data = len(data)
    sorted_data = sorted(data)
    return statistics.stdev(sorted_data[int(length_data/4) : int(3*length_data/4)])
 
while True:
    start_time = time.time()
    while True:
        current_time = time.time()  
        elapsed_time = current_time - start_time
        
        incoming_data = str(Arduino_Serial.readline())
        print(incoming_data)
        incoming_data = (incoming_data.split("\\")[0][2:])
        print(incoming_data)
        incoming_data=incoming_data.split(':')
        incoming_data=incoming_data[1]
        print(incoming_data)
        if incoming_data != "":
            data1.append(int(float(incoming_data)))
 
        if elapsed_time >= 2: 
            mean = statistics.mean(data1)
            std = cal_std(data1)
            print(mean)
            print(std)
            if std < 3:
                if (mean >= 0 and mean <=10):
                     pyautogui.hotkey('fn','win','prtsc')
                if (mean > 10 and mean <= 20):
                     pyautogui.press('pgup')
                if (mean > 20 and mean <= 30):
                    pyautogui.press('pgdn')
                if (mean > 20 and mean <= 30):
                    pyautogui.alert('Did you enjoy our presentation?')
                
                
            data1 = []
            break
