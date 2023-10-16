from win10toast import ToastNotifier
import time


def send_notification(title, message):
    toaster = ToastNotifier()
    toaster.show_toast(title, message, duration=10)


# Example usage
send_notification('Time Tracking App', 'You have a meeting at 2:00 PM')

# To keep the app running and display notifications periodically
while True:
    # Check if it's time to display a notification
    # and call send_notification with the appropriate details
    # based on your time tracking app's logic
    send_notification('Time Tracking App', 'Time to log your hours!')
    time.sleep(3600)  # Repeat every hour (3600 seconds)
