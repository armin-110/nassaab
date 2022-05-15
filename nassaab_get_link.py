from curses import meta
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
import pandas as pd
import numpy as np
from bs2json import bs2json
import re
import json
import copy
from copy import deepcopy
import requests
from collections import OrderedDict
from iteration_utilities import unique_everseen
import time
import itertools
link_list=[]

class GETLINK():
    def __init__ (self,page_link,s):
        self.page_link =page_link
        self.s=s
        ##################################################################################

    def get_link(self):
        link_list.clear()
        response = self.s.get(self.page_link, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36"})
        page_html=response.text
        page_html_soup = b(page_html, 'html.parser')

        converter = bs2json()
        print(page_html_soup)
        class_find_name= page_html_soup.findAll('div', {'class': 'app_block'}) 
        json_class_find_name = converter.convertAll(class_find_name)
        for i in range(len(json_class_find_name)):
            link_list.append(json_class_find_name[i]['div'][0]['a']['attributes']['href'])
        print(json_class_find_name[0]['div'][0]['a']['attributes']['href'])
        # meta_dic['content_name']=json_class_find_name[0]['text']#title
        print(link_list)
        print(len(link_list))