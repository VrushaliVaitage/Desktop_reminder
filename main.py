import time
from plyer import notification

while True:
    notification.notify(title ="hello ! good morning Vrushali !!",
                        message = "Have a nice day !!",
                        timeout = 10
                        )
    time.sleep(6*6)