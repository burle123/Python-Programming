'''
Drink Water Reminder App

Write a python program which reminds you of drinking water every hour or two. Your program can either beep or send desktop notifications for a specific operating system
'''

import time
import winsound  # For beep sound
from plyer import notification  # For desktop notifications

def drink_water_reminder(interval=30, use_notification=True):
 
    while True:
        if use_notification:
            notification.notify(
                title="💧 Drink Water Reminder",
                message="Time to drink a glass of water!",
                timeout=5  # Notification stays for 5 seconds
            )
        else:
            # Beep sound (frequency, duration)
            winsound.Beep(1000, 500)  # 1000 Hz for 0.5 sec

        print("Reminder: Drink Water!")
        time.sleep(interval)


# Run the reminder every 30 seconds (for testing)
if __name__ == "__main__":
    drink_water_reminder(interval=10, use_notification=True)
    # drink_water_reminder(interval=10, use_notification=False)
