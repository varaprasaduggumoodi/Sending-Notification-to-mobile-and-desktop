import requests
from plyer import notification
import time
time.sleep(10)
#below code sends the notification to the same desktop where the code is running
notification.notify(title='Notifications for the Desktop',message=input("Enter the message : "),app_icon='image.ico',timeout=20,)
#below code sends the notification to the mobile device which contains the app myNotifier.
requests.post('https://api.mynotifier.app', {
    "apiKey": ' #provide the api key here ',
    "message": "Python internship project!",
    "description": "Task1:Sending notification through python for mobile is successfully completed",
    "type": "success", 
})

