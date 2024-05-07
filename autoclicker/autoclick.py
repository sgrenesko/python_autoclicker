import pyautogui
import time

def auto_clicker(interval, clicks):
    print("Auto Clicker will start in 10 seconds. Move the mouse to the desired position.")
    time.sleep(10)
    print("Auto Clicker started.")
    
    # Get current mouse position
    initial_position = pyautogui.position()
    
    # Sends mouse_down and mouse_up events with a 50ms pause
    for _ in range(clicks):
        pyautogui.mouseDown(initial_position[0], initial_position[1])
        time.sleep(0.05)  # Pause for 50 ms
        pyautogui.mouseUp(initial_position[0], initial_position[1])
        time.sleep(interval)

    print("Auto Clicker finished.")

print("Welcome to Autoclicker by SRG!\n")

# Asks user for interval time (sec) between clicks and number of clicks
interval=input("Please enter the interval (seconds) between clicks: ")
interval = int(interval)
clicks=input("\nPlease enter the total amount of clicks: ")
clicks = int(clicks)

# Click function call
auto_clicker(interval, clicks)
