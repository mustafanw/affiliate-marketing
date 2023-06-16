from telethon import TelegramClient, events, sync
import re
import requests
import pyshorteners
from datetime import datetime
import os
import re
# import wa_automation
# import twitter_bot
# import facebook_bot
from bs4 import BeautifulSoup
import unicodedata
import json
import pathlib
import bitlyshortener
import sys
import shutil

tokens_pool = ['9d1ccd972fb5efa7f164d959d30c8922063126b8','1f9827a1d22a98dc7d06ebbfab4e22b476ed3236','ed2526d19a1e682ac14a0284bbd0fb9e9f40c034','1e0297f6e7a70f1e1b8a1b15770d0c80839acd46','6efffab60065ad40092f5d3acf909ff5c7dfb4ce'] 
SHORT_URL = bitlyshortener.Shortener(tokens=tokens_pool, max_cache_size=256)

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

class TeleGramAffiliate:

    def longer_exception(self, input_object, method_name):
        """
            Prints Exception

            Parameters:
            Input Object

            Returns:
            None

        """
        exc_type, exc_obj, exc_tb = input_object
        print("Exception type:%s", exc_type)
        print("Method name     :%s", method_name)
        print("Line number   :%s", exc_tb.tb_lineno)

    def take_image_amazon(self, soup):
        try:
            img_div = soup.find(id="imgTagWrapperId")
            imgs_str = img_div.img.get('data-a-dynamic-image')  # a string in Json format
            # convert to a dictionary
            imgs_dict = json.loads(imgs_str)
            #each key in the dictionary is a link of an image, and the value shows the size (print all the dictionay to inspect)

            first_link = list(imgs_dict.keys())
            return first_link
        except Exception as ex:
            print("-----Exception take_image_amazon")
            print('Take Image Error ' + str(ex))
            self.longer_exception(sys.exc_info(), "take_image_amazon")
            return ["error"]

    def take_image_flipkart(self, response):
        try:
            soup=BeautifulSoup(response.content,'html.parser')
            for a in soup.findAll("script",attrs={"id":"jsonLD"})[0]:
                first_link = [json.loads(a)[0]["image"]]
                break
            return first_link
        except Exception as ex:
            print("-----Exception take_image_flipkart")
            print('Take Image Error ' + str(ex))
            return ["error"]

    def amazon_links(self, url, old_url):
        try:
            if 'tag' in old_url:
                new_url = re.sub('tag=[a-zA-Z0-9._-]+', 'tag=freecashkaroi-21', old_url)
                # new_short_url=SHORT_URL.tinyurl.short(new_url)
                new_short_url = SHORT_URL.shorten_urls([new_url])[0].replace('j.mp', 'bit.ly')
                new_short_url="🛒 Amazon "+new_short_url
            else:
                new_url = old_url + '&tag=freecashkaroi-21'
                # new_short_url = SHORT_URL.tinyurl.short(new_url)
                new_short_url = SHORT_URL.shorten_urls([new_url])[0].replace('j.mp', 'bit.ly')
                new_short_url = "🛒 Amazon " + new_short_url
            self.message = self.message.replace(url,new_short_url)
            
            if len(self.urls) ==1:                
                url=old_url
                response = requests.get(url, headers=HEADERS)
                soup=BeautifulSoup(response.content,'lxml')
                # self.first_link = self.take_image_amazon(soup)
                mrp_message=soup.find("span", attrs={'id':'productTitle'}).string.strip()
                # try:
                #     # mrp_price = soup.find("span", attrs={'class':'a-price a-text-price a-size-base'}).string.strip()
                #     mrp_price = soup.find_all('span', attrs={'class':'a-offscreen'})[1].string.strip()
                    
                #     mrp_message = mrp_message + "\n\nM.R.P.  " + str(mrp_price)                    
                # except Exception as ex:
                #     self.longer_exception(sys.exc_info(), "MRP PRICE")
                #     print(str(ex))
                try:
                    # deal_price = soup.find("span", attrs={'id':'priceblock_dealprice'}).string.strip()
                    deal_price = soup.find_all('span', attrs={'class':'a-offscreen'})[0].string.strip()
                    mrp_message = mrp_message + "\nDeal Price:  " + str(deal_price)
                except:
                    print("-----Exception dEAL PRICE")
                    self.longer_exception(sys.exc_info(), "dEAL PRICE")
                    deal_price = soup.find("span", attrs={'id':'priceblock_ourprice'}).string.strip()
                    deal_price = unicodedata.normalize("NFKD",deal_price)
                    mrp_message = mrp_message + "\nDeal Price " + str(deal_price)  
                # try:
                #     # mrp_price = soup.find("span", attrs={'class':'a-price a-text-price a-size-base'}).string.strip()
                #     offer_percent = soup.find('span', attrs={'class' : 'a-size-large a-color-price savingPriceOverride aok-align-center savingsPercentage'}).string.strip()
                    
                #     mrp_message = mrp_message + "\nDiscount:   " + str(offer_percent)                    
                # except Exception as ex:
                #     self.longer_exception(sys.exc_info(), "Discount")
                #     print(str(ex)) 

                mrp_message = '🛍 '+mrp_message + "\n\n" + new_short_url  
                self.message = mrp_message    
        except Exception as ex:
            print("-----Exception amazon_links")
            print(str(ex))
            self.longer_exception(sys.exc_info(), "amazon_links")

    def flipkart_links(self, url, old_url): 
        try:
            if 'affid' in old_url:
                new_url = re.sub('affid=[a-zA-Z0-9]+', 'affid=mustafanw', old_url)
                # new_short_url=SHORT_URL.tinyurl.short(new_url)
                new_short_url = SHORT_URL.shorten_urls([new_url])[0].replace('j.mp', 'bit.ly')
                new_short_url = "🛒 Flipkart " + new_short_url
            else:
                new_url = old_url + '&affid=mustafanw'
                # new_short_url = SHORT_URL.tinyurl.short(new_url)
                new_short_url = SHORT_URL.shorten_urls([new_url])[0].replace('j.mp', 'bit.ly')
                new_short_url = "🛒 Flipkart " + new_short_url
            self.message=self.message.replace(url,new_short_url)
            if len(self.urls) ==1:
                url=old_url
                response = requests.get(url, headers=HEADERS)
                soup=BeautifulSoup(response.content,'lxml')
                # self.first_link = self.take_image_flipkart(response)
                mrp_message=soup.find("span", attrs={'class':'B_NuCI'}).text.strip()
                try:
                    mrp_price = soup.find("div", attrs={'class':'_3I9_wc _2p6lqe'}).text.strip()
                    mrp_message = mrp_message + "\n\nM.R.P. " + str(mrp_price)                    
                except Exception as ex:
                    print("-----Exception mrp_price")
                    print(str(ex))
                try:
                    deal_price = soup.find("div", attrs={'class':'_30jeq3 _16Jk6d'}).text.strip()
                    mrp_message = mrp_message + "\nDeal Price " + str(deal_price)
                except Exception as ex:
                    print("-----Exception deal_price")
                    print(str(ex))   
                mrp_message = '🛍 '+mrp_message + "\n\n" + new_short_url 
                self.message = mrp_message
        except Exception as ex:
            print("-----Exception flipkart")
            print(str(ex))
            self.longer_exception(sys.exc_info(), "flipkart")

    def modify_message(self, message, event):
        self.message = message
        self.first_link = False
        self.urls = re.findall("(?P<url>https?://[^\s]+)", message)
        file_path=False
        if self.urls:
            if "ekaro" in self.urls[0]:
                # new_short_url = SHORT_URL.tinyurl.short(self.urls[0])
                new_short_url = SHORT_URL.shorten_urls(self.urls)[0]
                new_short_url = new_short_url.replace('j.mp', 'bit.ly')
                self.message=self.message.replace(self.urls[0], new_short_url)
                file_path = True
            else:
                for url in self.urls:
                    session = requests.Session()  
                    session.max_redirects = 5
                    resp = session.head(url, allow_redirects=True)
                    old_url = resp.url
                    if "amazon" in old_url:
                        self.amazon_links(url, old_url)                                   
                    elif "flipkart" in old_url:
                        self.flipkart_links(url, old_url)
                    
                    
        return self.message, self.first_link, file_path