#!/usr/bin/python3
#-*-coding:utf-8-*-
# Update V1.6

### Import Module
import requests,bs4,sys,os,random,time,re,json,uuid,subprocess,platform,base64
from random import randint
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from bs4 import BeautifulSoup as par
from datetime import date
from datetime import datetime
from urllib.parse import quote


### Perumpamaan Module & Syntax
_req_ses_  = requests.Session()
_req_get_  = requests.get
_req_post_ = requests.post
_js_lo_    = json.loads
_cici_azimvau_    = input
_azimvau_dapunta_ = open
_cici_cici_       = exit

### Warna
Z = "\033[1;30m" # Hitam
P = "\033[1;37m" # Putih
M = "\033[1;31m" # Merah
H = "\033[1;32m" # Hijau
K = "\033[1;33m" # Kuning
B = "\033[1;34m" # Biru
U = "\033[1;35m" # Ungu
O = "\033[1;36m" # Biru Muda
N = "\033[0m"    # Warna Mati

### Host & Penampungan
host = "https://mbasic.facebook.com"
ok = []
cp = []
ttl = []
count = 1
data_1 = {}
data_2 = {}
data_change_1 = {}
data_change_2 = {}
data_user = []
header_grup = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
header_nama = {"origin": "https://mbasic.facebook.com","accept-language": "en-GB,en-US;q=0.9,en;q=0.8,bn;q=0.7","accept-encoding": "gzip, deflate","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","user-agent": "Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Host": "".join(bs4.re.findall("://(.*?)$","https://m.facebook.com")),"referer": "https://m.facebook.com/login/?next&ref=dbl&fl&refid=8","cache-control": "max-age=0","upgrade-insecure-requests": "1","content-type": "application/x-www-form-urlencoded"}
header_hashtag = {'authority': 'mbasic.facebook.com','method': 'GET','path': '/favicon.ico','scheme': 'https','accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8','accept-encoding': 'gzip, deflate','accept-language': 'en-US,en;q=0.9','user-agent': 'Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36','origin': 'https://www.facebook.com','referer': 'https://www.facebook.com'}

r = str(random.randint(1,9999))
rx = r.replace("1","A").replace("2","C").replace("3","B").replace("4","E").replace("5","H").replace("6","I").replace("7","Y")
plist = (platform.uname())[2]
basex = plist
basex1 = basex.encode('ascii')
basex2 = base64.b64encode(basex1)
basex3 = basex2.decode('ascii')
base4 = (basex3).upper()
basesplit = base4.replace('=', 'N').replace('A', '3').replace('B', '9').replace('C', '7').replace('D', '1').replace('E', '4').replace('M', '2').replace('L', '6').replace('F', '8').replace('N', 'E').replace('T', 'R').replace("5","X").replace("1","X")

try:
    rq = requests.get('https://github.com/Shuvo-BBHH/premiouM/blob/main/requirements.txt').text
except requests.exceptions.ConnectionError:
    print('\nNO INTERNET CONNECTION\n')
    exit()
