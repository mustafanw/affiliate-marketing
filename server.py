import os
from telethon.sync import TelegramClient
from telethon import events
from telethon.errors import ChannelInvalidError
from affiliates import TeleGramAffiliate
import pathlib
import bitlyshortener
import sys
import shutil
import requests
import facebook_bot
from datetime import datetime

BASE_DIR = pathlib.Path(__file__).parent.absolute()
HEADERS={
    "accept": "text/html, */*; q=0.01",
"accept-encoding": "gzip, deflate, br",
"accept-language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
"cookie": 's_fid=6B251727A4AE01B9-0410BDC245B4A668; ubid-acb,in=258-2514721-3045447; __utmv=164013664.freecashkaroi-21; lc-acbin=en_IN; __utma=164013664.416634750.1603992697.1603992697.1607111018.2; i18n-prefs=INR; s_nr=1641913239783-Repeat; s_vnum=2041231568450%26vn%3D2; s_dslv=1641913239787; csd-key=eyJ3YXNtVGVzdGVkIjp0cnVlLCJ3YXNtQ29tcGF0aWJsZSI6dHJ1ZSwid2ViQ3J5cHRvVGVzdGVkIjpmYWxzZSwidiI6MSwia2lkIjoiNjNjMGEzIiwia2V5IjoiQjhVZU43Ym9SUXVEYlRIZWVIeGlqRWJiK0xTeTkrazVmMTFsZisydjBONTdoNkFoTk9YcnpGY2VjZTdPaUtNVXpBNmpXRXpFcldMRkVMc1I3ZGQwQXdxNzRMaE13NmdXbG5IL0xmVUh6NnRBT0d6SnBNNmZkUW1kY1hyYXBrN0I2YllEbS9ITDhYcXV2ZGlGZFFxOGh5ejBxSS9nd1RraXR1V0VlMlpaSmxsS3dFTWRBend1S1hLTUo1SnM3L1lXK0dBYXJITjhFdFoxQVdDM3d1NUxka0kwL2NtbThlalVyVHlqd2MwK0FxTTY3cFRzZXg0QWVkUVlIMm5IK3VnYzNidjdseE5ZNFp5d0F3YjN5TU1TY2xpVmQxT0YvS2czaXZ4MEwvaXo4U1dqdll0QjVxRCtpYWFPVXlxdDNVbUhaWi9jRHpIMnN2ZWF4MmRPSmJpOVBnPT0ifQ==; session-id=258-9230251-8654434; s_cc=true; x-acbin="4gED4O5v42IW3TOrT@gGv9hbN97zptUTO12TB5Lgoosmry1UbVWb?tXpkfAfsmFh"; at-acbin=Atza|IwEBILjHJCxvpcQfMPoBN62wILg-Rb4HdhixybUALakEH4qMLGsIwoshfqCE0eLh7-36sFdm0tSa5onXY9hKgr0hCoJoUtbCnJkXBC5LbLaZvkN7c8p5wUt8DXm0x0ErxHad0kPI9Ts3o7E1Gf10dOucVBqrbNYhjW3MP8_o26YP-fkjvQFd2sJ2vfDnocneWvAUapr2k2RkstxYOfKowWO1fr-9; sess-at-acbin="Led3UeUOi9r90uAPKARKU4WwiA9EKANjoKBHJUKvGwE="; sst-acbin=Sst1|PQH37QI4iuRs9ozuCMXcudwHDPh45bFAOtQZ62XBmLjjtWv_VL2VQ6Fl90sL8X5H3v6GAYDh2meqjAmj1wqd6VVTr8MBArYwfSj0jNqTOTTkWI5Xtog7AA_hiUaCj7wCs27A00DD5HtAi9eqSOfbjNaJfa7GS7nGMM-Q_zpZTnsPV_NHLAbDbPE2ms2T1ZlulgqdbQxV_8PFEDoAaJRDqeiGZOtCERj29uTc2os1Uehlbd41XZSW8bISV2-ZFjn6kCRh097GTGybikPoB7KlWvZgpc3uB8Qz_qNMCleZKaxf2LYsVsrz8XbjBx91ajiAftBpXB2zzqTmoeT2Q2Uoqtlk6p-XmdGTxS5J-3YYlgJmkQg; session-token=914IDUFDs6qlDJwYy7Pd1HM/tCH74eN98H4eIzpkL8OpCEA9V2cjJtdcaTKg3iq2fDwmjDqeGAVNo+kfxpWc/SW6bqTA8HLn+eApgXWb5o9GWCsqL4kU6mk0E0MAtV94ccLXbOIt8HnRPD43U8e+vCYF7qqygZVQ3aMoKEb8VBK/YzJExqUPtauifPL/7UhI7vjBezZ5Hd21cjmJim9WA3J3CfiaqdpaM5g76qvUK4A; AMCVS_A7493BC75245ACD20A490D4D%40AdobeOrg=1; AMCV_A7493BC75245ACD20A490D4D%40AdobeOrg=1585540135%7CMCIDTS%7C19025%7CMCMID%7C31716134902656058773627870595029714843%7CMCAAMLH-1644342791%7C12%7CMCAAMB-1644342791%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1643745191s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.4.0; gpv_pn=IN%3ASD%3AHomepage; s_vnc365=1675273992813%26vn%3D1; s_ivc=true; s_tp=7498; s_ips=609; s_nr365=1643738033608-New; s_ppv=IN%253ASD%253AHomepage%2C42%2C8%2C3115%2C5%2C12; _rails-root_session=MjgvUmpOZW4zdjFIT0hCa3EvZVJ0bG5VSjY1Mjd6RTQxVlVoZm9XL3Rzamprb1ZwS2lMS3hlUWRuMFh1cDF2TXByY3Q5Y0dROEY1SFRpaGVZdjlNOXZQYjdjcDc1d0cxQVd0U1NId2ZlWEE3K2NPZ29aSHB6VnFzcGRUclRYc0xMSUMvZDZ0Q2RWVzZYTlFvak1Td1A5MEN1a3BMd0RidE5hOUQrV0ZkU3ZxY2JxMFBQRjFyNUxnTzVObENtUlFuLS0yVlY0aWRQNUJ1MUVXNjZUcmE0TS93PT0%3D--c0d3f5d9d5dbe77cd87354c6415b8b6091ce3d15; s_sq=%5B%5BB%5D%5D; visitCount=44; session-id-time=2082787201l; csm-hit=tb:s-1AGN0V719N7TQ0XZ6748|1643739078663&t:1643739078986&adb:adblk_no',
"downlink": "6.85",
"ect": "4g",
"referer": "https://www.amazon.in/deal/3f208be8?showVariations=true&smid=A14CZOWI0VEHLG&pf_rd_r=W8J2BCJNKJ0VNS0TECV9&pf_rd_p=f690369a-7bb4-48bb-9349-f68a447ef06d&pd_rd_r=9231ef26-9e98-47e5-a073-5b676304627d&pd_rd_w=Ux6J2&pd_rd_wg=68ffP&ref_=pd_gw_unk",
"rtt": "200",
"sec-ch-ua-mobile": "?0",
"sec-ch-ua-platform": "Windows",
"sec-fetch-dest": "empty",
"sec-fetch-mode": "cors",
"sec-fetch-site": "same-origin",
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
"x-requested-with": "XMLHttpRequest"
}
class TelegramMessageForwarder:
    def __init__(self, api_id, api_hash, source_channel, dest_chn1, dest_chn2, test_chn):
        self.api_id = api_id
        self.api_hash = api_hash
        self.source_channel = source_channel
        self.dest_chn1 = dest_chn1
        self.dest_chn2 = dest_chn2
        self.test_chn = test_chn
        self.client = TelegramClient('9589625153server', api_id, api_hash)
        self.telegram_affiliate = TeleGramAffiliate()

    async def forward_messages(self, event):
       
        message=event.message.message
        message,first_link, file_path = self.telegram_affiliate.modify_message(message, event)  
        message = message.replace("stealsales", "musairadeals")
        message = message.replace("steal", "musairadeals") 
        if file_path:  
            path = await self.client.download_media(event.message)
            file_path = os.path.join(BASE_DIR, path)
            print(file_path)
        event.message.message = message
        wa_message= ''.join(c for c in event.message.message if c <= '\uFFFF')

        try:
            if first_link and "error" not in first_link:    
                await self.client.send_file('@musaira_deals',first_link[0],caption=event.message.message) #musaira_deals
                await self.client.send_file('@musairadeals',first_link[0],caption=event.message.message)     
                response = requests.get(first_link[0], stream=True, headers=HEADERS)
                with open('img.png', 'wb') as file_loc:
                    shutil.copyfileobj(response.raw, file_loc)
                    file_path = os.path.join(BASE_DIR, 'img.png')
                del response
                print(file_path)
                
            else:
                await self.client.send_message('@musaira_deals',event.message) #musaira_deals
                await self.client.send_message('@musairadeals',event.message)
            
            await facebook_bot.send_facebook_page(wa_message,file_path)   
            if file_path:
                    os.remove(file_path)
            print(f'Deals Published at {datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}')
        except Exception as e:
            print(f"Failed to forward message: {str(e)}")
    

        # try:
        #     await self.client.send_message(self.dest_chn1, message)
        #     await self.client.send_message(self.dest_chn2, message)
        #     await facebook_bot.send_facebook_page(wa_message,file_path)  
        #     print(f"Message forwarded: {message}")
        # except Exception as e:
        #     print(f"Failed to forward message: {str(e)}")

    def start(self):
        print("Start")
        self.client.add_event_handler(self.forward_messages, events.NewMessage(chats=self.source_channel))
        self.client.add_event_handler(self.forward_messages, events.NewMessage(chats=self.test_chn))
        self.client.start()
        self.client.run_until_disconnected()

# Usage example
api_id = 1958908
api_hash = '21d35d34c158be29142b85527b4128ab'
source_channel = 'FRCP_Official'
test_chn = 'testgmnw'
dest_chn1 = 'musaira_deals'
dest_chn2 = 'musairadeals'


forwarder = TelegramMessageForwarder(api_id, api_hash, source_channel, dest_chn1, dest_chn2, test_chn)
forwarder.start()
