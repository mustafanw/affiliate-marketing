import facebook
import re
import requests
graph = facebook.GraphAPI(access_token="EAACpTRXZBREcBAIj6xse6F7xyZALKV7JH1ZC5KMrT8sZCwYaoXI5B5UFuzTn5CZCVAzCeuZB4NHi0WKWnIZCJ6PTYNRRXhLVlpbgIRZApUZB030ZAkCcFWDITgU4ZAOnolBzEtAdVBZAUEbseFH8cZB6J7MgSbyae1kI2Qgq6U4ZAnrrZCjudLtyIRAG0AO")

def send_facebook_page(message, image_path=None):
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



send_facebook_page("https://l.facebook.com/l.php?u=https%3A%2F%2Famzn.to%2F3KjbxV9%3Ffbclid%3DIwAR2HsopLGdEejJJJIBmkyKMTxLUXXkY5jS5Yj9uJwed1paw7uSwAd5BEeXo&h=AT1pT8ZemtFPkBby6RJliWkGvGIAnOuTMKgJ7DGtxFYaEmr8iud6pAbgXehHicUjhns7fwfJA31aMXATIVpnOkiG3wNIq4jJBn7i2mBx5zGlS4qOsC4Us0fZgJxJBv5Osyf_Ckjd9E9VTDC6_3wn&__tn__=H-R&c[0]=AT28_Af87gNvbtB8rYeKogSu7eYnxr1BwOmgxFFovV_WoasRrGfWDbtO_uXewPZmkKAVPxZr9SED9lpgdQTUsVXpb9vurZDNORfqqrsVeVehWIDFm5BwwyE2joLzo6q66vAu3D-_ufjsWFjyKMvTev2ZVckiSB2Yrl2xiBp_vncrBznDWsKuFZQuBIS6aHq8NtZNlvf4OvMD")

# Get New Access token
# curl -i -X GET "https://graph.facebook.com/102888708318630?fields=access_token&access_token=EAACpTRXZBREcBAFfwXFdJC9VVuzZCpsozryrwccrnZAcLHYHRkhMEOFMGkzJU7qPVmWqCixbgqiw7Rgcnz75WXCjZCYp76HR38CaveGUeC5lJVh8puhfAdRHhotOkHUny3gZAxewg3RUPxW3lCzKLZBg5lb7pGBrlMamUpanE4UhKxFAOPr4DD"

# curl -i -X POST "https://graph.facebook.com/102888708318630/feed?message=HelloFans!&access_token=EAACpTRXZBREcBAK1z6JTxZB6mCGMCpZCr4crUlGzWta0hzUxa33G2pNmfx1MqpEm2E0aipuSZARQdKotxnV0dDKFQFyRbWtFORBs54IC1bVavVMfHNZBaxaM9z3SZA2ctTBmAjHb3wLBTssZBZAL1R2zluxgAiiduA7bMxfXl2m7UnwVkA6yCA91"