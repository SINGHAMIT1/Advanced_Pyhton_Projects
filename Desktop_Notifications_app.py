import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title="Alert !!!!",
            message="It's already 1 hour! take break for sometime",
            timeout=10
        )
        time.sleep(3600)
# # sleep() suspends execution for the given number of second
