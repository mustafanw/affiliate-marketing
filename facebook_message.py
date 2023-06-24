import facebook
import re
import requests
import os
FB_TOKEN = os.environ.get("FB_TOKEN")
graph = facebook.GraphAPI(access_token=FB_TOKEN)

async def send_facebook_page(message, image_path=None):
    try:
        global graph
        if image_path:
            photo=open(image_path,'rb')
            new_message = message + '\n #deal #deals #DealoftheDay #DailyDeals #sale #affiliate'
            graph.put_photo(photo,message=new_message)
            print("Photo Posted on facebook successfully")
        else:
            my_link=re.search("(?P<url>https?://[^\s]+)", message).group("url")
            new_message=message.replace(my_link,'')
            new_message = new_message + '\n #deal #deals #DealoftheDay #DailyDeals #sale #affiliate'
            
            graph.put_object(
            parent_object=102888708318630,
            connection_name="feed",
            message=new_message,
            link=my_link
            )        
            print("Posted on facebook successfully")
    except Exception as ex:
        print(str(ex))
        report = {}
        report["value1"] = "Musaira Deals Facebook Publish Failed"
        requests.post("https://maker.ifttt.com/trigger/Facebook_Musaira_Deals/with/key/bMKgwR-VK-tw8rRpt-HM53pfeyhpQITaQIapwlZ1QZs", data=report)

