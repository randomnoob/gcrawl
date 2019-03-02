# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException
import platform



class CollectLinks:
    """
    Deprecated class, deprecated chromedriver in favor of pure requests
    """

    def __init__(self):
        executable = ''

        if platform.system() == 'Windows':
            print('Detected OS : Windows')
            executable = './chromedriver/chromedriver_win.exe'
        elif platform.system() == 'Linux':
            print('Detected OS : Linux')
            executable = './chromedriver/chromedriver_linux'
        elif platform.system() == 'Darwin':
            print('Detected OS : Darwin')
            executable = './chromedriver/chromedriver_mac'
        else:
            assert False, 'Unknown OS Type'

        self.executable = executable



    def gcrawl_list(self, keyword_list, proxified_ssh=''):
        
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        # set the window size
        chrome_options.add_argument('window-size=1200x600')
        chrome_options.add_argument('disable-gpu')
        if proxified_ssh:
            chrome_options.add_argument('--proxy-server=socks5://127.0.0.1:{}'.format(proxified_ssh))
            chrome_options.add_argument('--host-resolver-rules="MAP * ~NOTFOUND , EXCLUDE 127.0.0.1"')
            self.browser = webdriver.Chrome(executable_path=self.executable, options=chrome_options)
        else:
            self.browser = webdriver.Chrome(executable_path=self.executable, options=chrome_options)
        result = []
        for index, keyword in enumerate(keyword_list):
            # print('KEYWORD_LIST_FOUND')
            self.browser.get("https://www.google.com/search?q={}&source=lnms&tbm=isch".format(keyword))
            photo_meta = self.browser.find_elements(By.XPATH, '//div[@class="rg_meta notranslate"]')
            print('Scraping links, keyword {} of {}.............'.format(index+1, len(keyword_list)))
            metadata = [x.get_attribute('innerHTML') for x in photo_meta]
            # If I see less than 50 images, I quit and switch the proxy
            if len(metadata) < 50:
                print ('Result doesn\'t seem right, I\'m quitting')
                break
            else:
                result.append(metadata)
                print('Googling done, Keyword: {}, Total: {}'.format(keyword, len(metadata)))
        self.browser.close()
        return result


