import requests
from plyer import notification
import schedule
import time


def generator():
    url="https://zenquotes.io/api/random"
 
    response=requests.get(url)
                    
    q=response.json()
                    
    quote=q[0]['q']
    author=q[0]['a']
                    
    print(quote)
    print(f"-'{author}'")
                    
    notification_title = "Quote of the day"
    notification_message = quote+"\n"+"- "+author

    notification.notify(
                        title=notification_title,
                        message=notification_message,
                        app_name="Quote",
                        timeout=15 #secs
                )
       
     
schedule.every().minute.at(":01").do(generator)


while True:
    schedule.run_pending()
    time.sleep(1)