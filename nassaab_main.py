print('بسمه الله الرحمن الرحیم')
print('salam bar mohammadreza dehghan amiri')
import copy
import datetime
import itertools
import json
import re
import time
from collections import OrderedDict
from copy import deepcopy
from curses import COLOR_BLACK

import numpy as np
import pandas as pd
import requests
import schedule
from bs2json import bs2json
from bs4 import BeautifulSoup as b
from iteration_utilities import unique_everseen
from rich import print
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from sqlalchemy import create_engine

import nassaab_get_link
import nassaab_get_meta

def get_link_name_list(page_link):
    s = requests.session()
    sg = nassaab_get_link.GETLINK(page_link,s)
    sgg = sg.get_link()
    return(nassaab_get_link.link_list)


def get_metadata(content_link):
    s = requests.session()
    sg = nassaab_get_meta.GETMETA(content_link,s)
    sgg = sg.get_meta()
    return(nassaab_get_meta.meta_data_list)


###################################################
engine = create_engine('postgresql://postgres:12344321@10.32.141.17/nassaab',pool_size=20, max_overflow=100,)
con=engine.connect()
date_a=datetime.datetime.now()

page_link=get_link_name_list('https://nassaab.com/?show=all')
for i in range(len(page_link)):
    meta=get_metadata(page_link[i])
    date_i=datetime.datetime.now()
    meta[0]['crawling_date']=str(date_i.date()).replace('-','')+str(date_i.time()).split(':')[0]
    # meta[0]['categori_name']=cat_program_name[i]
    # meta[0]['cat']='game'
    data_frame =pd.DataFrame(meta[0],index=[0])
    data_frame.to_sql('nassaab_meta'+str(date_a.date()).replace('-','')+str(date_a.time()).split(':')[0],con,if_exists='append', index=False)
    print(meta[0])
