# github.com/tb-net
# Library for network connections

import os, requests, json
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



# --------- requests functions ---------

def get(url, opt, wait=67):
    v = {}
    r = requests.get(url, timeout=wait)
    v['status'] = r.status_code
    if opt=='html':
        v['data'] = bs(r.text, 'html.parser')
    elif opt=='json':
        v['data'] = json.loads(r.text)
    return v




# -------- selenium functions ---------


def browser(wait=67, visible=False):
    chrome_opt = Options()
    if not visible: chrome_opt.add_argument('--headless')
    chrome_pref = {'download.prompt_for_download': False,
                   'download.directory_upgrade': True,
                   'safebrowsing.enabled': False,
                   'safebrowsing.disable_download_protection': True}
    chrome_opt.add_experimental_option('prefs', chrome_pref)
    exec_path =  '/usr/lib/chromium-browser/chromedriver'
    brw = webdriver.Chrome(executable_path = exec_path, chrome_options = chrome_opt)
    brw.set_page_load_timeout(wait)
    brw.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
    params = {'cmd': 'Page.setDownloadBehavior', 'params': \
            {'behavior': 'allow', 'downloadPath': '/Downloads/chrome/'}}
    brw.execute("send_command", params)
    return brw


