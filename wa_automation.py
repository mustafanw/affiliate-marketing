from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
import datetime
import os
import argparse
import platform
import pathlib
from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# chrome_driv = webdriver.Chrome(ChromeDriverManager().install())

BASE_DIR = pathlib.Path(__file__).parent.absolute()
user_data = os.path.join(BASE_DIR, "User_Data")

# chrome_driv = os.path.join(BASE_DIR, "chromedriver.exe")
browser = None
Contact = ['"Musaira Deals 99"', '"Musaira Deals 101"'] #"Musaira Deals 99"','"Selenium"','"Musaira Deals 3"','
message = "Test4"
Link = "https://web.whatsapp.com/"
mode="server"

def testing():
    print("inside testing")
def whatsapp_login():
    print("inside whatsapp login")
    global wait, browser, Link, mode
    if mode=='local':
        options = Options()
        options = webdriver.ChromeOptions()
        # options.headless = True
        # execute_path=r"D:\Projects\whpip install chromedriver-binary-autoatsapp\whatsapp_automation\chromedriver.exe"
        # execute_path=r"D:\Projects\chromedriver.exe"

        execute_path=r"D:\Projects\whatsapp\chromedriver.exe"
    else:
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        execute_path=os.environ.get("CHROMEDRIVER_PATH")
    print(user_data)
    options.add_argument('--user-data-dir='+user_data)#D:\\Projects\\whatsapp\\whatsapp_automation\\User_Data')
    # options.add_argument('window-size=1200x600')    
    options.add_argument("user-agent=User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36")
    browser = webdriver.Chrome(executable_path=execute_path,options=options)
    wait = WebDriverWait(browser, 600)
    browser.get(Link)    
    browser.maximize_window()
    print("QR scanned")

def send_attachment(image_path):
    # Attachment Drop Down Menu
    #browser.find_element_by_xpath("//div[@id='main']/footer/div/div/div[2]/div/div/span").click()
    # browser.find_element_by_xpath("//div[@id='main']/footer/div/div/div/div/div[2]/div/div/span").click()
    browser.find_element_by_xpath("//div[@id='main']/footer/div/div/span[2]/div/div/div[2]/div/span/div/div/ul/li/button/span").click()
    time.sleep(1)
    #browser.find_element_by_xpath("//div[@id='main']/footer/div/div/div[2]/div/span/div/div/ul/li/button/span").click()
    # browser.find_element_by_xpath("//div[@id='main']/footer/div/div/div/div/div[2]/div/span/div/div/ul/li/button/span").click()
    browser.find_element_by_xpath("//div[@id='main']/footer/div/div/span[2]/div/div/div[2]/div/span/div/div/ul/li/button/span").click()
    time.sleep(3)
    # browser.find_element_by_xpath("//input[@type='file']").clear()
    # browser.find_element_by_xpath("//input[@type='file']").send_keys(image_path)
    # autoit.control_focus("Open", "Edit1")
    # autoit.control_set_text("Open", "Edit1", image_path)
    # autoit.control_click("Open", "Button1")
    browser.find_element_by_xpath("//input[@type='file']").send_keys(image_path)
    time.sleep(3)
    #browser.find_element_by_xpath("//div[@id='app']/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div").click()
    browser.find_element_by_xpath("//div[@id='app']/div/div/div[3]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div/span").click()

def send_message(target,new_message,image_path):
    global message, wait, browser
    print("inside send message")
    
    # print(browser)
    try:
        x_arg = '//span[contains(@title,' + target + ')]'
        ct = 0
        while ct != 5:
            try:
                group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
                group_title.click()
                break
            except Exception as e:
                print("Retry Send Message Exception", e)
                ct += 1
                time.sleep(3)
        # input_box = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        # input_box = browser.find_element_by_xpath("//div[@id='main']/footer/div/div[2]/div/div/div/div[2]")
        input_box = browser.find_element_by_xpath("//div[@id='main']/footer/div/div/span[2]/div/div[2]/div/div/div")
        
        # browser.save_screenshot(r"D:\Projects\whatsapp\test3.png")
        start_t=time.time()
        new_message = new_message.split("\n")
        for ch in new_message:
            input_box.send_keys(ch)
            ActionChains(browser).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(
                    Keys.SHIFT).key_up(Keys.BACKSPACE).perform()

        if image_path:
            send_attachment(image_path)
            
        # breakpoint()
        time.sleep(13)
            
        input_box.send_keys(Keys.ENTER)
        
        end_t=time.time()
        print(f"Total time {end_t-start_t}")
        print("Message sent successfully")
        time.sleep(5)
                
    except NoSuchElementException as e:
        print("send message exception: ", e)
        return

async def sender(new_message,image_path=None):
    global Contact, choice, docChoice, unsaved_Contacts

    print(Contact)
    for i in Contact:
        try:
            send_message(i,new_message,image_path)
            print("Message sent to ", i)
        except Exception as e:
            print("Msg to {} send Exception {}".format(i, e))
        
# if __name__ == "__main__":
#     print("Web Page Open") 
#     # Let us login and Scan
#     print("SCAN YOUR QR CODE FOR WHATSAPP WEB")
#     whatsapp_login()
#     message="boAt Rockerz 245v2 Bluetooth Wireless in Ear Earphones with Upto 8 Hours Playback, 12mm Drivers,  IPX5, Magnetic Eartips, Integrated Controls and Lightweight Design with Mic (Navy Blue)\nDeal Price:  ₹799.00\n\n🛒 Amazon https://amzn.to/431yKVa"
#     wa_message= ''.join(c for c in message if c <= '\uFFFF')
#     sender(wa_message,"D:\Projects\affiliate-marketing\img.jpeg")
#     browser.quit()
#     print("Task Completed")
