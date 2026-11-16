# # Excercise 11... Question... Drink Water Reminder...  


# WAP in python which reminds you of drinking water every hour or two. Your program can either beep or send desktop notifications for a specific operating system...










# # *** For 1 Hour ***



# import os
# import platform
# import time
# import pyttsx3


# def speak_reminder(text):
#     """Speaks the reminder text aloud using Text-to-Speech."""
#     engine = pyttsx3.init()
#     engine.setProperty("rate", 165)  # Speed of speech
#     engine.say(text)
#     engine.runAndWait()


# def send_notification(title, message):
#     """Speaks the reminder and triggers a native desktop notification based on the OS."""
#     speak_reminder("Hey Prafull, drink water")

#     current_os = platform.system()

#     if current_os == "Windows":
#         ps_script = f'''
#         Add-Type -AssemblyName System.Windows.Forms
#         $notification = New-Object System.Windows.Forms.NotifyIcon
#         $notification.Icon = [System.Drawing.SystemIcons]::Information
#         $notification.BalloonTipTitle = "{title}"
#         $notification.BalloonTipText = "{message}"
#         $notification.Visible = $true
#         $notification.ShowBalloonTip(5000)
#         '''
#         os.system(f'powershell -Command "{ps_script}"')

#     elif current_os == "Darwin":  # macOS
#         os.system(
#             f'osascript -e \'display notification "{message}" with title "{title}"\''
#         )

#     elif current_os == "Linux":
#         os.system(f'notify-send "{title}" "{message}"')

#     else:
#         print(f"\n[{title}] {message}")


# def water_reminder(interval_hours=1):
#     """Runs an infinite loop reminding the user to drink water at set intervals."""
#     interval_seconds = interval_hours * 3600
#     print(f"Drink Water Reminder started! You will be reminded every {interval_hours} hour(s).")
#     print("Press Ctrl+C in the terminal to stop.\n")

#     try:
#         while True:
#             time.sleep(interval_seconds)
#             timestamp = time.strftime("%I:%M %p")
#             print(f"[{timestamp}] Reminder sent: Hey Prafull, drink water!")
#             send_notification(
#                 title="Drink Water Reminder",
#                 message="Hey Prafull, drink water!",
#             )
#     except KeyboardInterrupt:
#         print("\nReminder stopped. Stay hydrated!")


# if __name__ == "__main__":
#     # Change to 2 for every 2 hours, or 0.002 (~7 seconds) to test immediately
#     hours = float(input("Enter reminder interval in hours (e.g., 1 or 2): ") or 1)
#     water_reminder(interval_hours=hours)








# *** For 1 Minute ***




import os
import platform
import time
import pyttsx3


def speak_reminder(text):
    """Speaks the reminder text aloud using Text-to-Speech."""
    engine = pyttsx3.init()
    engine.setProperty("rate", 165)  # Speed of speech
    engine.say(text)
    engine.runAndWait()


def send_notification(title, message):
    """Speaks the reminder and triggers a desktop notification based on the OS."""
    # Speak the voice alert instead of a beep
    speak_reminder("Hey Prafull, drink water")

    current_os = platform.system()

    if current_os == "Windows":
        ps_script = f'''
        Add-Type -AssemblyName System.Windows.Forms
        $notification = New-Object System.Windows.Forms.NotifyIcon
        $notification.Icon = [System.Drawing.SystemIcons]::Information
        $notification.BalloonTipTitle = "{title}"
        $notification.BalloonTipText = "{message}"
        $notification.Visible = $true
        $notification.ShowBalloonTip(5000)
        '''
        os.system(f'powershell -Command "{ps_script}"')

    elif current_os == "Darwin":  # macOS
        os.system(
            f'osascript -e \'display notification "{message}" with title "{title}"\''
        )

    elif current_os == "Linux":
        os.system(f'notify-send "{title}" "{message}"')

    else:
        print(f"\n[{title}] {message}")


def water_reminder_minutes(interval_minutes=1):
    """Sends a water reminder at the specified interval in minutes."""
    interval_seconds = interval_minutes * 60  # Convert minutes to seconds
    print(f"Reminder started! You will be notified every {interval_minutes} minute(s).")
    print("Press Ctrl + C in the terminal to stop.\n")

    try:
        while True:
            time.sleep(interval_seconds)  # Wait for 60 seconds
            timestamp = time.strftime("%I:%M:%S %p")
            print(f"[{timestamp}] Reminder: Hey Prafull, drink water!")
            send_notification(
                title="Drink Water Reminder",
                message="Hey Prafull, drink water!",
            )
    except KeyboardInterrupt:
        print("\nReminder stopped. Stay hydrated!")


if __name__ == "__main__":
    # Setting 1 means the reminder will trigger every 1 minute (60 seconds)
    water_reminder_minutes(interval_minutes=1)