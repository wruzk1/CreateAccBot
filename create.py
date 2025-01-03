import requests,re,redis,threading,asyncio,os,sys,gc,json,time,stem.process,random
from random import randint
import subprocess as sp

TYPECR = "PYRO"
try:
    TYPECR = sys.argv[1]
except:
    print("NO TYPECR")
    
PHONE = ""
try:
    PHONE = sys.argv[2]
except:
    print("NO PHONE")     

IDS = ""
try:
    IDS = sys.argv[3]
except:
    print("NO IDS")   

OPRX = ""
try:
    OPRX = sys.argv[4]
except:
    print("NO OPR")  
   
CHATID = ""
try:
    CHATID = sys.argv[5]
except:
    print("NO CHATID") 

THE = ""
try:
    THE = sys.argv[6]
except:
    print("NO THE")  

APIID = ""
try:
    APIID = sys.argv[7]
except:
    print("NO APIID") 

APIHASH = ""
try:
    APIHASH = sys.argv[8]
except:
    print("NO APIHASH") 
    
SITE = ""
try:
    SITE = sys.argv[9]
except:
    print("NO SITE")      
db = None
while not db :
    db = redis.StrictRedis(host='localhost', port=6379, db=0,decode_responses=True)
    
from pyrogram import Client
from pyrogram import filters
from pyrogram import idle
from pyrogram import errors
from pyrogram.types import InlineKeyboardButton as button
from pyrogram.types import InlineKeyboardMarkup as markup
from pyrogram.types import ForceReply as reply
from pyrogram.raw import functions
from pyrogram import enums
from telethon import TelegramClient, events, functions, types
from telethon import errors as errors2
from telethon.errors import SessionPasswordNeededError
if db.get("SATOKEN"):
    SATOKEN = db.get("SATOKEN")
else:
    SATOKEN = ""
if db.get("S5TOKEN"):
    S5TOKEN = db.get("S5TOKEN")
else:
    S5TOKEN = ""
if db.get("SCTOKEN"):
    SCTOKEN = db.get("SCTOKEN")
else:
    SCTOKEN = ""
if db.get("SMTOKEN"):
    SMTOKEN = db.get("SMTOKEN")
else:
    SMTOKEN = ""
from time import sleep
global step
step= 'None'
SORP = "SERI"
SOSK = 0
NASK = 0
def print_bootstrap_lines(line):
    print(line)
def changeIP(PORT):
    if db.get("WEBSH"):
        PROXY = ""
        if db.scard("WEBSHL") > 0:
            PROXY = db.srandmember("WEBSHL")
            db.srem("WEBSHL",PROXY)
        else:
            try:
                t = requests.get("https://graph.tuxweb.ir/?token=XXXXX&service=XXX&wsh=" + str(db.get("WEBSH")) + "&gall=true")
                print(t)
                for xi in t.json():
                    db.sadd("WEBSHL",xi)
                PROXY = db.srandmember("WEBSHL")
                db.srem("WEBSHL",PROXY)
            except Exception as e:
                print(e)
        print(PROXY)
        return PROXY
    else:
        os.system("sudo fuser -k " + str(PORT) + "/tcp")
        result = None
        try:
            tor_process = stem.process.launch_tor_with_config(config = {'SocksPort': str(PORT),'DataDirectory': './.tordatach' + str(PORT),},init_msg_handler = print_bootstrap_lines,)
            result = "Yes"
        except:
            pass
        return "OK"
def trytoban(TOKEN, ID):
    if SITE == "5sim":
        headers = {'Authorization': 'Bearer ' + TOKEN,'Accept': 'application/json',}
        DELETE = requests.get(f"https://5sim.net/v1/user/ban/{ID}", headers=headers)
        try:
            while DELETE.status_code != 200:
                DELETE = requests.get(f"https://5sim.net/v1/user/ban/{ID}", headers=headers)
        except Exception as e: print(e)
    elif SITE == "sa":
        DELETE = requests.get(f"https://sms-activate.ru/stubs/handler_api.php?api_key={TOKEN}&action=setStatus&status=8&id={ID}")
        try:
            while DELETE.status_code != 200:
                DELETE = requests.get(f"https://sms-activate.ru/stubs/handler_api.php?api_key={TOKEN}&action=setStatus&status=8&id={ID}")
        except Exception as e: print(e)
    elif SITE == "sm":
        DELETE = requests.get(f"https://api.sms-man.com/control/set-status?token={TOKEN}&request_id={ID}&status=used")
        try:
            while DELETE.status_code != 200:
                DELETE = requests.get(f"https://api.sms-man.com/control/set-status?token={TOKEN}&request_id={ID}&status=used")
        except Exception as e: print(e)
    else:
        DELETE = requests.get(f"https://sms-code.store/stubs/handler_api.php?api_key={TOKEN}&action=setStatus&status=8&id={ID}")
        try:
            while DELETE.status_code != 200:
                DELETE = requests.get(f"https://sms-code.store/stubs/handler_api.php?api_key={TOKEN}&action=setStatus&status=8&id={ID}")
        except Exception as e: print(e)
        
PORTX = 9051
async def TELETHON1(clientT,PHONE,PORTX,ID,OPR,TOKEN,chat_id,SITE):
    global OUTED
    print("IN CREATE THON")
    global NASK
    global SORP
    global SOSK
    phone_code = False
    try:
        if SITE == "5sim":
            # headers = {'Authorization': 'Bearer ' + TOKEN,'Accept': 'application/json',}
            # READY = requests.get(f"https://5sim.net/v1/user/check/{ID}", headers=headers)
            pass
        elif SITE == "sa":
            READY = requests.get(f"https://sms-activate.ru/stubs/handler_api.php?api_key={TOKEN}&action=setStatus&status=1&id={ID}")
        elif SITE == "sm":
            # READY = requests.get(f"http://api.sms-man.com/stubs/handler_api.php?api_key={TOKEN}&action=setStatus&status=1&id={ID}")
            READY = requests.get(f"https://api.sms-man.com/control/set-status?token={TOKEN}&request_id={ID}&status=ready")
            print(READY.json())
            READY = requests.get(f"http://api.sms-man.com/stubs/handler_api.php?action=setStatus&api_key={TOKEN}&id={ID}&status=1")
            print(READY.content)
        else:
            READY = requests.get(f"https://sms-code.store/stubs/handler_api.php?api_key={TOKEN}&action=setStatus&status=1&id={ID}")
        try:
            await clientT.connect()
            print("CONNECT TELEGRAM")
            try:
                phone_code_hash1 = await clientT.send_code_request(f"+{PHONE}",force_sms=True)
                if phone_code_hash1.type and "SentCodeTypeSms" in str(phone_code_hash1.type):
                    db.sadd("BANNED",f"{PHONE}")
                    trytoban(TOKEN, ID)
                    OUTED = True
                    sys.exit()
                print(phone_code_hash1)
                phone_code = True
            except Exception as e:
                print(e)
                db.sadd("BANNED",f"{PHONE}")
                trytoban(TOKEN, ID)
                OUTED = True
                sys.exit()
        except errors2.PhoneNumberInvalidError:
            print("PhoneNumberInvalid")
            db.sadd("BANNED",f"{PHONE}")
            # if SITE == "5sim":
                # headers = {'Authorization': 'Bearer ' + TOKEN,'Accept': 'application/json',}
                # DELETE = requests.get(f"https://5sim.net/v1/user/ban/{ID}", headers=headers)
            # elif SITE == "sa":
                # DELETE = requests.get(f"https://sms-activate.ru/stubs/handler_api.php?api_key={TOKEN}&action=setStatus&status=8&id={ID}")
            # elif SITE == "sm":
                # DELETE = requests.get(f"https://api.sms-man.com/control/set-status?token={TOKEN}&request_id={ID}&status=reject")
            # else:
                # DELETE = requests.get(f"https://sms-code.store/stubs/handler_api.php?api_key={TOKEN}&action=setStatus&status=8&id={ID}")
            trytoban(TOKEN, ID)
          #  sys.exit()
            OUTED = True
            # try:
                # await clientT.disconnect()
            # except: pass
            sys.exit()
        except Exception as e: 
            print(type(e).__name__,e,e.__traceback__.tb_lineno)
            db.sadd("BANNED",f"{PHONE}")
            trytoban(TOKEN, ID)
            OUTED = True
            # try:
                # await clientT.disconnect()
            # except: pass
            sys.exit()
        except:
            print("EXCEPT")
            db.sadd("BANNED",f"{PHONE}")
            trytoban(TOKEN, ID)
            OUTED = True
            # try:
                # await clientT.disconnect()
            # except: pass
            sys.exit()
        if phone_code == True:
            CodeGo = ""
            TIMETC = 0
            while True:
                if TIMETC < 35:
                    TIMETC += 1
                    STATUS = ""
                    if SITE == "5sim":
                        headers = {'Authorization': 'Bearer ' + TOKEN,'Accept': 'application/json',}
                        STATUS = requests.get(f"https://5sim.net/v1/user/check/{ID}", headers=headers)
                        try:
                            print(STATUS.content)
                        except:
                            print(STATUS)
                        try:
                            STATUSC = STATUS.json()["status"]
                            if (STATUSC == "FINISHED" or STATUSC == "RECEIVED") and len(STATUS.json()["sms"]) > 0:
                                for XCODE in STATUS.json()["sms"]:
                                    CodeGo = XCODE["code"]
                                break
                        except Exception as e: print(e)
                        except: pass
                    elif SITE == "sa":
                        STATUS = requests.get(f"https://api.sms-activate.org/stubs/handler_api.php?api_key={TOKEN}&action=getStatus&id={ID}")
                        STATUSC = ""
                        try:
                            STATUSC = str(STATUS.content)
                        except: 
                            STATUSC = str(STATUS)
                        print(STATUSC)
                        if "STATUS_OK" in STATUSC:
                            CodeGo = STATUSC.replace("\n","").replace("STATUS_OK:","").replace("b'","").replace("'","")
                            break
                    elif SITE == "sm":
                        # STATUS = requests.get(f"http://api.sms-man.com/stubs/handler_api.php?api_key={TOKEN}&action=getStatus&id={ID}")
                        STATUS = requests.get(f"http://api.sms-man.com/control/get-sms?token={TOKEN}&request_id={ID}")
                        STATUSC = ""
                        try:
                            STATUSC = STATUS.json()
                            print(STATUSC)
                            if STATUSC["sms_code"]:
                                STATUSC = "STATUS_OK:" + str(STATUSC["sms_code"])
                            else:
                                STATUSC = "STATUS_WAITING"
                        except Exception as e:
                            print(type(e).__name__,e,e.__traceback__.tb_lineno)
                            STATUSC = "STATUS_WAITING"
                        except:
                            print("Except")
                            STATUSC = "STATUS_WAITING"
                        # STATUSC = ""
                        # try:
                            # STATUSC = str(STATUS.content)
                        # except: 
                            # STATUSC = str(STATUS)
                        # print(STATUSC)
                        if "STATUS_OK" in STATUSC:
                            CodeGo = STATUSC.replace("\n","").replace("STATUS_OK:","").replace("b'","").replace("'","")
                            break
                    else:
                        STATUS = requests.get(f"https://sms-code.store/stubs/handler_api.php?api_key={TOKEN}&action=getStatus&id={ID}")
                        STATUSC = ""
                        try:
                            STATUSC = str(STATUS.content)
                        except: 
                            STATUSC = str(STATUS)
                        print(STATUSC)
                        if "STATUS_OK" in STATUSC:
                            CodeGo = STATUSC.replace("\n","").replace("STATUS_OK:","").replace("b'","").replace("'","")
                            break
                else:
                    db.sadd("AFTERTIME",f"{PHONE}")
                    print("NO CODE")
                    break
                await asyncio.sleep(1)
            if CodeGo == "":
                print("FUCK IT")
                db.sadd("BANNED",f"{PHONE}")
                trytoban(TOKEN, ID)
                OUTED = True
                # try:
                    # await clientT.disconnect()
                # except: pass
                sys.exit()
            try:
                print("SIGN IN")
                RESULTA = await clientT.sign_in(phone=f"+{PHONE}", code=CodeGo)
                print(RESULTA)
            except errors2.PhoneNumberUnoccupiedError:
                print("REG")
                try:
                    if db.get("NASK"):
                        NASK = int(db.get("NASK"))
                    if db.get("ATITLE"):
                        TNN = 0
                        ATITLE = str(db.get("ATITLE"))
                        if NASK >= db.scard("NAMES" + ATITLE):
                            NASK = 0
                            db.set("NASK","0")
                        for GNAME in db.smembers("NAMES" + ATITLE):
                            TNN += 1
                            if TNN > NASK:
                                NASK = TNN
                                db.set("NASK",str(TNN))
                                break
                        GNAME = GNAME
                        GNAMES = GNAME.split(" ")
                        FNAME = GNAMES[0]
                        LNAME = GNAMES[1]
                    else:
                        FNAME = "Torsten"
                        LNAME = "Eichmann"
                    RESULTA = await clientT.sign_up(code=CodeGo, first_name=str(FNAME), last_name=str(LNAME)) 
                    print(RESULTA)
                except Exception as e: 
                    print(e)
                    db.sadd("BANNED",f"{PHONE}")
                    trytoban(TOKEN, ID)
                    OUTED = True
                    sys.exit()
            except Exception as e:
                db.sadd("BANNED",f"{PHONE}")
                print(type(e).__name__,e,e.__traceback__.tb_lineno)
                trytoban(TOKEN, ID)
                OUTED = True
                # try:
                    # await clientT.disconnect()
                # except: pass
                sys.exit()
            except:
                db.sadd("BANNED",f"{PHONE}")
                print("EXCEPT")
                trytoban(TOKEN, ID)
                OUTED = True
                # try:
                    # await clientT.disconnect()
                # except: pass
                sys.exit()
            db.sadd("PHONESALL",PHONE)
            db.set(PHONE,"THON")
            db.sadd("CREATED",f"{PHONE}:TELETHON:{CodeGo}")
            try:
                print("PHOTO")
                if db.get("SOSK"):
                    SOSK = int(db.get("SOSK"))
                if db.get("SORP"):
                    SORP = db.get("SORP")
                if SORP == "SERI":
                    if db.get("ATITLE"):
                        ATITLE = str(db.get("ATITLE"))
                        TIN = 0
                        if SOSK >= db.scard("SERI" + ATITLE):
                            SORP = "PHOT"
                            db.set("SORP","PHOT")
                            SOSK = 0
                            db.set("SOSK","0")
                        for GPHOTO1 in db.smembers("SERI" + ATITLE):
                            TIN += 1
                            if TIN > SOSK:
                                SOSK = TIN
                                db.set("SOSK",str(TIN))
                                break
                        GPHOTO1 = GPHOTO1
                        MSPH = db.scard(GPHOTO1)
                        for SPH in range(1,MSPH + 1):
                            for URLPH in db.smembers(GPHOTO1):
                                GETSA = str(SPH) + "-+"
                                if GETSA in str(URLPH):
                                    URLPH = str(URLPH).replace(GETSA,"")
                                    try:
                                        NO = await clientT(functions.photos.UploadProfilePhotoRequest(await clientT.upload_file(URLPH)))
                                    except: pass
                        # for URLPH in db.smembers(GPHOTO1):
                            # URLPH = URLPH
                            # try:
                                # NO = await clientT(functions.photos.UploadProfilePhotoRequest(await clientT.upload_file(URLPH)))
                            # except: pass
                    else:
                        if db.get("ATITLE"):
                            ATITLE = str(db.get("ATITLE"))
                            TIN = 0
                            if SOSK >= db.scard("PHOTOS" + ATITLE):
                                SORP = "SERI"
                                db.set("SORP","SERI")
                                SOSK = 0
                                db.set("SOSK","0")
                            for GPHOTO in db.smembers("PHOTOS" + ATITLE):
                                TIN += 1
                                if TIN > SOSK:
                                    SOSK = TIN
                                    db.set("SOSK",str(TIN))
                                    break
                            GPHOTO = GPHOTO
                            try:
                                NO = await clientT(functions.photos.UploadProfilePhotoRequest(await clientT.upload_file(GPHOTO)))
                            except: pass
                elif SORP == "PHOT":
                    if db.get("ATITLE"):
                        ATITLE = str(db.get("ATITLE"))
                        TIN = 0
                        if SOSK >= db.scard("PHOTOS" + ATITLE):
                            SORP = "SERI"
                            db.set("SORP","SERI")
                            SOSK = 0
                            db.set("SOSK","0")
                        for GPHOTO in db.smembers("PHOTOS" + ATITLE):
                            TIN += 1
                            if TIN > SOSK:
                                SOSK = TIN
                                db.set("SOSK",str(TIN))
                                break
                        GPHOTO = GPHOTO
                        try:
                            NO = await clientT(functions.photos.UploadProfilePhotoRequest(await clientT.upload_file(GPHOTO)))
                        except: pass
                    else:
                        TIN = 0
                        if SOSK >= db.scard("SERI"):
                            SORP = "PHOT"
                            db.set("SORP","PHOT")
                            SOSK = 0
                            db.set("SOSK","0")
                        for GPHOTO1 in db.smembers("SERI"):
                            TIN += 1
                            if TIN > SOSK:
                                SOSK = TIN
                                db.set("SOSK",str(TIN))
                                break
                        GPHOTO1 = GPHOTO1
                        # for URLPH in db.smembers(GPHOTO1):
                            # URLPH = URLPH
                            # try:
                                # NO = await clientT(functions.photos.UploadProfilePhotoRequest(await clientT.upload_file(URLPH)))
                            # except: pass
                        MSPH = db.scard(GPHOTO1)
                        for SPH in range(1,MSPH + 1):
                            for URLPH in db.smembers(GPHOTO1):
                                GETSA = str(SPH) + "-+"
                                if GETSA in str(URLPH):
                                    URLPH = str(URLPH).replace(GETSA,"")
                                    try:
                                        NO = await clientT(functions.photos.UploadProfilePhotoRequest(await clientT.upload_file(URLPH)))
                                    except: pass
                OUTED = True
                print("END CREATE")
                # try:
                    # await clientT.disconnect()
                # except: pass
                sys.exit()
            except Exception as e: 
                print(e)
                db.sadd("BANNED",f"{PHONE}")
                trytoban(TOKEN, ID)
                OUTED = True
                sys.exit()
            except:
                db.sadd("BANNED",f"{PHONE}")
                trytoban(TOKEN, ID)
                OUTED = True
                sys.exit()
            OUTED = True
            # try:
                # await clientT.disconnect()
            # except: pass
        else:
            print("FUCK IT")
            db.sadd("BANNED",f"{PHONE}")
            trytoban(TOKEN, ID)
        OUTED = True
        sys.exit()
    except Exception as e:
        print(type(e).__name__,e,e.__traceback__.tb_lineno)
        print("FUCK IT")
        db.sadd("BANNED",f"{PHONE}")
        trytoban(TOKEN, ID)
        OUTED = True

async def TELETHON2(clientT,PHONE,PORTX,chat_id):
    global OUTED
    print("IN CREATE THON2")
    global NASK
    global SORP
    global SOSK
    phone_code = False
    try:
        try:
            await clientT.connect()
            print("CONNECT TELEGRAM")
            try:
                phone_code_hash1 = await clientT.send_code_request(f"+{PHONE}",force_sms=True)
                print(phone_code_hash1)
                phone_code = True
            except Exception as e:
                print(e)
        except errors2.PhoneNumberInvalidError:
            print("PhoneNumberInvalid")
            db.sadd(f"ACTION{chat_id}",f"ELOGGING{PHONE}")
            OUTED = True
            sys.exit()
        except Exception as e: 
            print(type(e).__name__,e,e.__traceback__.tb_lineno)
            db.sadd(f"ACTION{chat_id}",f"ELOGGING{PHONE}")
            OUTED = True
            sys.exit()
        except:
            print("EXCEPT")
            db.sadd(f"ACTION{chat_id}",f"ELOGGING{PHONE}")
            OUTED = True
            sys.exit()
        if phone_code == True:
            db.sadd(f"ACTION{chat_id}",f"SCODE{PHONE}")
            CodeGo = ""
            TIMETC = 0
            while True:
                if TIMETC < 100:
                    TIMETC += 1
                    STATUS = ""
                    if db.get(f"CODE{chat_id}"):
                        CodeGo = db.get(f"CODE{chat_id}")
                        db.delete(f"CODE{chat_id}")
                        break
                else:
                    db.sadd(f"ACTION{chat_id}",f"AFTERTIME{PHONE}")
                    print("NO CODE")
                    break
                await asyncio.sleep(1)
            if CodeGo == "":
                print("FUCK IT")
                db.sadd(f"ACTION{chat_id}",f"ELOGGING{PHONE}")
                OUTED = True
                sys.exit()
            try:
                print("SIGN IN")
                RESULTA = await clientT.sign_in(phone=f"+{PHONE}", code=CodeGo)
                print(RESULTA)
            except errors2.PhoneNumberUnoccupiedError:
                print("REG")
                try:
                    if db.scard("TITLE") > 0:
                        GNAME1 = db.srandmember("TITLE")
                        GNAME = db.srandmember("NAMES" + str(GNAME1))
                        GNAMES = GNAME.split(" ")
                        FNAME = GNAMES[0]
                        LNAME = GNAMES[1]
                    else:
                        FNAME = "Torsten"
                        LNAME = "Eichmann"
                    RESULTA = await clientT.sign_up(code=CodeGo, first_name=str(FNAME), last_name=str(LNAME)) 
                    print(RESULTA)
                except Exception as e: print(e)
            except errors2.SessionPasswordNeededError as e:
                db.sadd(f"ACTION{chat_id}",f"PASSWORD{PHONE}")
                PassGo = ""
                while True:
                    if TIMETC < 100:
                        TIMETC += 1
                        STATUS = ""
                        if db.get(f"PASS{chat_id}"):
                            PassGo = db.get(f"PASS{chat_id}")
                            db.delete(f"PASS{chat_id}")
                            break
                    else:
                        db.sadd(f"ACTION{chat_id}",f"AFTERTIME{PHONE}")
                        print("NO PASS")
                        break
                    await asyncio.sleep(1)
                if PassGo == "":
                    print("FUCK IT")
                    db.sadd(f"ACTION{chat_id}",f"ELOGGING{PHONE}")
                    OUTED = True
                    sys.exit()
                else:
                    try:
                        GETPASS = await clientT.sign_in(password=PassGo)
                        try:
                            await clientT.edit_2fa(password=PassGo)
                        except Exception as e: print(e)
                    except Exception as e:
                        db.sadd(f"ACTION{chat_id}",f"ELOGGING{PHONE}")
                        print(type(e).__name__,e,e.__traceback__.tb_lineno)
                        OUTED = True
                        sys.exit()
            except Exception as e:
                db.sadd(f"ACTION{chat_id}",f"ELOGGING{PHONE}")
                print(type(e).__name__,e,e.__traceback__.tb_lineno)
                OUTED = True
                sys.exit()
            except:
                db.sadd(f"ACTION{chat_id}",f"ELOGGING{PHONE}")
                print("EXCEPT")
                OUTED = True
                sys.exit()
            db.sadd("RECIVER",PHONE)
            db.sadd(f"ACTION{chat_id}",f"CREATED{PHONE}")
            OUTED = True
            sys.exit()
        else:
            print("FUCK IT")
            db.sadd(f"ACTION{chat_id}",f"ELOGGING{PHONE}")
        OUTED = True
        sys.exit()
    except Exception as e:
        print(type(e).__name__,e,e.__traceback__.tb_lineno)
        print("FUCK IT")
        db.sadd(f"ACTION{chat_id}",f"ELOGGING{PHONE}")
        OUTED = True
        sys.exit()
        
async def GetCode(phone,chat_id,msgid):
    Sapp = ""
    global PORTX
    # global ALLKILL
    # global AUTOLAUNCH
    global app
    global ALLLISTGET
    global LOGOUTLIST
    global GETCODESS
    global TEXTS
    TELTHON = False
    if db.get(phone):
        TELTHON = True
    while True:
        try:
            sessionx = f'sessions/+{phone}'
            PORTX += 1
            if int(PORTX) > 9100:
                PORTX = 9051
            TOR = changeIP(PORTX)
            api_id, api_hash = 16623,"8c9dbfe58437d1739540f5d53c72ae4b"
            if db.get("WEBSH"): 
                TOR = TOR.split(":")
                if TELTHON == True:
                    proxy = proxy = {'proxy_type': 'socks5','addr': TOR[0],'port': int(TOR[1]),'username': TOR[2],'password': TOR[3],'rdns': True}
                    Sapp = TelegramClient(sessionx, api_id, api_hash, proxy=proxy)
                else:
                    proxy = {"scheme": "socks5","hostname": TOR[0],"port": int(TOR[1]),"username": TOR[2],"password": TOR[3]}
                    Sapp = Client(sessionx,api_id,api_hash,proxy=proxy)  
                break
            else:
                if TELTHON == True:
                    Sapp = TelegramClient(sessionx, api_id, api_hash, proxy=("socks5", "127.0.0.1", int(PORTX)))
                else:
                    proxy = {"scheme": "socks5","hostname": "127.0.0.1","port": int(PORTX),"username": "","password": ""}
                    Sapp = Client(sessionx,api_id,api_hash,proxy=proxy)  
                break
        except:
            await asyncio.sleep(1)
    is_auth = False
    # await app.edit_message_text(chat_id,msgid,f"♻️Wait for getting code in 30 sec later...\nEnter phone number +{phone} in your telegram to get your code")
    # await asyncio.sleep(30)
    try:
        if TELTHON == True:
            is_auth2 = await Sapp.connect()
            is_auth = await Sapp.is_user_authorized()
        else:
            is_auth = await Sapp.connect()
    except Exception as e: print(e)
    except: print("EXCEPT")
    if is_auth:
        TRYTIME= 0
        GETCODESS[phone] = False
        while True:
            TRYTIME += 1
            if TRYTIME > 50:
                ALLLISTGET[str(chat_id)] = False
                # await app.send_message(chat_id,f"❌You have reach max time 100 sec")
                await app.edit_message_text(chat_id,msgid,f"❌You have reach max time 100 sec")
                db.sadd("PHONESALL",phone)
                try:
                    await Sapp.disconnect()
                except: pass
                try:
                    await Sapp.stop()
                except: pass
                return
                # sys.exit()
                # break
            try:
                if TELTHON == True:
                    # GETCODESS[phone] = False
                    TEXTS[phone] = {}
                    TEXTS[phone]["temp"] = ""
                    TEXTS[phone]["gen"] = ""
                    async for message in Sapp.iter_messages(777000,limit=10):
                        TEXTS[phone]["temp"] = str(message.raw_text)
                        print(TEXTS[phone]["temp"])
                        if len(TEXTS[phone]["temp"]) < 310 :
                            TEXTS[phone]["temp"] = TEXTS[phone]["temp"].replace("1","1️⃣").replace("2","2️⃣").replace("3","3️⃣").replace("4","4️⃣").replace("5","5️⃣").replace("6","6️⃣").replace("7","7️⃣").replace("8","8️⃣").replace("9","9️⃣").replace("0","0️⃣")
                            db.decr(str(chat_id))
                            # ALLLISTGET[str(chat_id)] = False
                            GETCODESS[phone] = True
                            try:
                                TEXTX = TEXTS[phone]["temp"].split("\n\n")
                                TEXTS[phone]["gen"] = TEXTS[phone]["gen"] + "\n\n" + TEXTX[0]
                            except:
                                TEXTS[phone]["gen"] = TEXTS[phone]["gen"] + "\n\n" + TEXTS[phone]["temp"]
                    if GETCODESS[phone] == True:
                        GETCODESS[phone] = False
                        LOGOUTLIST[phone] = "wait"
                        # await app.send_message(chat_id,f"✅Code received\n\nPhone: +{phone}\nMessage: {TEXT}",reply_markup = markup([[button("✅Logout",callback_data=f"LOGOUT_{phone}"),button("❌No Logout",callback_data=f"NOOUT_{phone}")]]))
                        await app.edit_message_text(chat_id,msgid,f"✅Code received\n\nPhone: +{phone}\nMessage: "  + str(TEXTS[phone]["gen"]),reply_markup = markup([[button("✅Logout",callback_data=f"LOGOUT_{phone}"),button("❌No Logout",callback_data=f"NOOUT_{phone}")]]))
                        TIMELG = 0
                        TRYTIME = TRYTIME + 30
                        while True:
                            TIMELG += 1
                            if TIMELG < 30:
                                if LOGOUTLIST[phone] == "logout":
                                    ALLLISTGET[str(chat_id)] = False
                                    # await app.send_message(chat_id,f"✅Logout form +{phone}")
                                    await app.edit_message_text(chat_id,msgid,f"✅Logout form +{phone}")
                                    try:
                                        await Sapp.log_out()
                                        TOR.kill()
                                    except:
                                        pass
                                    return
                                    # sys.exit()
                                elif LOGOUTLIST[phone] == "noout":
                                    ALLLISTGET[str(chat_id)] = False
                                    db.sadd("PHONESALL",phone)
                                    await app.edit_message_text(chat_id,msgid,f"✅No out form +{phone}")
                                    # await app.send_message(chat_id,f"✅No out form +{phone}")
                                    try:
                                        TOR.kill()
                                    except:
                                        pass
                                    return
                                    # sys.exit()
                                else:
                                    await asyncio.sleep(5)
                            else:
                                ALLLISTGET[str(chat_id)] = False
                                db.sadd("PHONESALL",phone)
                                await app.edit_message_text(chat_id,msgid,f"✅No out form +{phone}")
                                # await app.send_message(chat_id,f"✅Loged Out")
                                try:
                                    # await Sapp.log_out()
                                    TOR.kill()
                                except:
                                    pass
                                return
                                # sys.exit()
                else:
                    # GETCODESS[phone] = False
                    # TEXT = ""
                    TEXTS[phone] = {}
                    TEXTS[phone]["temp"] = ""
                    TEXTS[phone]["gen"] = ""
                    async for message in Sapp.get_chat_history(777000):
                        TEXTS[phone]["temp"] = str(message.text)
                        print(TEXTS[phone]["temp"])
                        if len(TEXTS[phone]["temp"]) < 310:
                            TEXTS[phone]["temp"] = TEXTS[phone]["temp"].replace("1","1️⃣").replace("2","2️⃣").replace("3","3️⃣").replace("4","4️⃣").replace("5","5️⃣").replace("6","6️⃣").replace("7","7️⃣").replace("8","8️⃣").replace("9","9️⃣").replace("0","0️⃣")
                            db.decr(str(chat_id))
                            # ALLLISTGET[str(chat_id)] = False
                            GETCODESS[phone] = True
                            try:
                                TEXTX = TEXTS[phone]["temp"].split("\n\n")
                                TEXTS[phone]["gen"] = TEXTS[phone]["gen"] + "\n\n" + TEXTX[0]
                            except:
                                TEXTS[phone]["gen"] = TEXTS[phone]["gen"] + "\n\n" + TEXTS[phone]["temp"]
                            # TEXTS[phone] = TEXTS[phone] + str("\n\n\n\n")
                    if GETCODESS[phone] == True:
                        GETCODESS[phone] = False
                        LOGOUTLIST[phone] = "wait"
                        # await app.send_message(chat_id,f"✅Code received\n\nPhone: +{phone}\nMessage: {TEXT}",reply_markup = markup([[button("✅Logout",callback_data=f"LOGOUT_{phone}"),button("❌No Logout",callback_data=f"NOOUT_{phone}")]]))
                        await app.edit_message_text(chat_id,msgid,f"✅Code received\n\nPhone: +{phone}\nMessage: " + str(TEXTS[phone]["gen"]),reply_markup = markup([[button("✅Logout",callback_data=f"LOGOUT_{phone}"),button("❌No Logout",callback_data=f"NOOUT_{phone}")]]))
                        TIMELG = 0
                        TRYTIME = TRYTIME + 30
                        while True:
                            TIMELG += 1
                            if TIMELG < 30:
                                if LOGOUTLIST[phone] == "logout":
                                    ALLLISTGET[str(chat_id)] = False
                                    await app.edit_message_text(chat_id,msgid,f"✅Logout form +{phone}")
                                    # await app.send_message(chat_id,f"✅Logout form +{phone}")
                                    try:
                                        await Sapp.log_out()
                                        TOR.kill()
                                    except:
                                        pass
                                    return
                                    # sys.exit()
                                elif LOGOUTLIST[phone] == "noout":
                                    ALLLISTGET[str(chat_id)] = False
                                    db.sadd("PHONESALL",phone)
                                    await app.edit_message_text(chat_id,msgid,f"✅No out form +{phone}")
                                    # await app.send_message(chat_id,f"✅No out form +{phone}")
                                    try:
                                        TOR.kill()
                                    except:
                                        pass
                                    return
                                    # sys.exit()
                                else:
                                    await asyncio.sleep(5)
                            else:
                                ALLLISTGET[str(chat_id)] = False
                                db.sadd("PHONESALL",phone)
                                await app.edit_message_text(chat_id,msgid,f"✅No out form +{phone}")
                                # await app.send_message(chat_id,f"✅Loged Out")
                                try:
                                    # await Sapp.log_out()
                                    TOR.kill()
                                except:
                                    pass
                                return
                                # sys.exit()
            except Exception as e:
                print(e)
                if "AUTH_KEY_UNREGISTERED" in str(e):
                    db.srem("PHONESALL",phone)
                    ALLLISTGET[str(chat_id)] = False
                    await app.edit_message_text(chat_id,msgid,f"❌There is no auth!\n\nPhone: +{phone}")
                    # await app.send_message(chat_id,f"❌There is no auth!\n\nPhone: +{phone}")
                    return
                    # sys.exit()
                    # break
                elif "USER_DEACTIVATED_BAN" in str(e):
                    db.srem("PHONESALL",phone)
                    ALLLISTGET[str(chat_id)] = False
                    await app.edit_message_text(chat_id,msgid,f"❌There is no auth!\n\nPhone: +{phone}")
                    # await app.send_message(chat_id,f"❌There is no auth!\n\nPhone: +{phone}")
                    return
                    # sys.exit()
                    # break
            await asyncio.sleep(5)
    else:
        ALLLISTGET[str(chat_id)] = False
        db.srem("PHONESALL",phone)
        await app.edit_message_text(chat_id,msgid,f"❌Number not auth!\n\nPhone: +{phone}")
        # await app.send_message(chat_id,f"❌Number not auth!\n\nPhone: +{phone}")
        return
        
async def THONCHECK(clientT,PHONE,PORTX,chat_id):
    global OUTED
    print("IN THONCHECK")
    global NASK
    global SORP
    global SOSK
    phone_code = False
    try:
        try:
            await clientT.connect()
            print("CONNECT TELEGRAM")
            if await clientT.is_user_authorized():
                try:
                    result = await clientT(functions.account.GetAuthorizationsRequest())
                    XKILL = 0
                    for XAU in result.authorizations:
                        XKILL += 1
                    if XKILL <= 1:
                        db.sadd(f"CHECK{chat_id}",f"OK{PHONE}")
                        try:
                            if db.scard("TITLE") > 0:
                                GNAME1 = db.srandmember("TITLE")
                                GNAME = db.srandmember("NAMES" + str(GNAME1))
                                GNAMES = GNAME.split(" ")
                                FNAME = GNAMES[0]
                                LNAME = GNAMES[1]
                            else:
                                FNAME = "Torsten"
                                LNAME = "Eichmann"
                            result = await clientT(functions.account.UpdateProfileRequest(first_name=str(FNAME),last_name=str(LNAME)))
                            print(RESULTA)
                        except Exception as e: 
                            print(e)
                            db.set("lasterr",str(e))
                        try:
                            dfile = await clientT.get_profile_photos('me')
                            for XPH in dfile:
                                file_dir = await clientT(functions.photos.DeletePhotosRequest(id=[types.InputPhoto(id=XPH.id,access_hash=XPH.access_hash,file_reference=XPH.file_reference)]))
                        except Exception as e:
                            print(e)
                        try:
                            if db.scard("TITLE") > 0:
                                GPHOTOX = db.srandmember("TITLE")
                                if db.scard("SERI" + str(GPHOTOX)) > 0:
                                    GPHOTO1 = db.srandmember("SERI" + str(GPHOTOX))
                                    MSPH = db.scard(GPHOTO1)
                                    for SPH in range(1,MSPH + 1):
                                        for URLPH in db.smembers(GPHOTO1):
                                            GETSA = str(SPH) + "-+"
                                            if GETSA in str(URLPH):
                                                URLPH = str(URLPH).replace(GETSA,"")
                                                try:
                                                    NO = await clientT(functions.photos.UploadProfilePhotoRequest(await clientT.upload_file(URLPH)))
                                                except Exception as e: 
                                                    print(e)
                                                    db.set("lasterr",str(e))
                                else:
                                    if db.scard("PHOTOS" + str(GPHOTOX)) > 0:
                                        GPHOTOX = db.srandmember("TITLE")
                                        GPHOTO = db.srandmember("PHOTOS" + str(GPHOTOX))
                                        try:
                                            NO = await clientT(functions.photos.UploadProfilePhotoRequest(await clientT.upload_file(GPHOTO)))
                                        except Exception as e: 
                                            print(e)
                                            db.set("lasterr",str(e))
                            OUTED = True
                            print("END CREATE")
                            sys.exit()
                        except Exception as e: 
                            print(e)
                            db.set("lasterr",str(e))
                        except:
                            pass
                    else:
                        db.sadd(f"CHECK{chat_id}",f"NO{PHONE}")
                    OUTED = True
                    sys.exit()
                except Exception as e:
                    print(type(e).__name__,e,e.__traceback__.tb_lineno)
                    db.sadd(f"CHECK{chat_id}",f"BAN{PHONE}")
                    OUTED = True
                    sys.exit()
            else:
                db.sadd(f"CHECK{chat_id}",f"BAN{PHONE}")
                OUTED = True
                sys.exit()
        except Exception as e: 
            print(type(e).__name__,e,e.__traceback__.tb_lineno)
            db.sadd(f"CHECK{chat_id}",f"BAN{PHONE}")
            OUTED = True
            sys.exit()
    except Exception as e:
        print(type(e).__name__,e,e.__traceback__.tb_lineno)
        print("FUCK IT")
        db.sadd(f"CHECK{chat_id}",f"BAN{PHONE}")
        OUTED = True
        sys.exit()

async def PYROG(PHONE,api_id, api_hash, PORTX, OPR,ID,TOKEN,chat_id,SITE,TOR):
    global OUTED
    print("IN CREATE PYRO")
    global NASK
    global SORP
    global SOSK
    session = f'sessions/+{PHONE}'
    proxy = {"scheme": "socks5","hostname": "127.0.0.1","port": int(PORTX),"username": "","password": ""}
    if db.get("WEBSH"): 
        TOR = TOR.split(":")
        proxy = {"scheme": "socks5","hostname": TOR[0],"port": int(TOR[1]),"username": TOR[2],"password": TOR[3]}
    client = ""
    if SITE == "5sim":
        # headers = {'Authorization': 'Bearer ' + TOKEN,'Accept': 'application/json',}
        # READY = requests.get(f"https://5sim.net/v1/user/check/{ID}", headers=headers)
        pass
    elif SITE == "sa":
        READY = requests.get(f"https://sms-activate.ru/stubs/handler_api.php?api_key={TOKEN}&action=setStatus&status=1&id={ID}")
    elif SITE == "sm":
        # READY = requests.get(f"http://api.sms-man.com/stubs/handler_api.php?api_key={TOKEN}&action=setStatus&status=1&id={ID}")
        READY = requests.get(f"https://api.sms-man.com/control/set-status?token={TOKEN}&request_id={ID}&status=ready")
        print(READY.json())
        READY = requests.get(f"http://api.sms-man.com/stubs/handler_api.php?action=setStatus&api_key={TOKEN}&id={ID}&status=1")
        print(READY.content)
    else:
        READY = requests.get(f"https://sms-code.store/stubs/handler_api.php?api_key={TOKEN}&action=setStatus&status=1&id={ID}")
    try:
        client = Client(session,api_id,api_hash,proxy=proxy)
        await client.connect()
        print("CONNECT TELEGRAM")
        phone_code_hash1 = await client.send_code(f"+{PHONE}")
        print(phone_code_hash1)
        phone_code_hash = phone_code_hash1.phone_code_hash
        # phone_code_hash2 = ""
        if phone_code_hash1.next_type and phone_code_hash1.next_type == enums.NextCodeType.SMS:
            db.sadd("BANNED",f"{PHONE}")
            trytoban(TOKEN, ID)
            OUTED = True
            print("NO SMS")
            try:
                await client.disconnect()
            except: pass
            try:
                await client.stop()
            except: pass
            return False
        else:
            print("Ready")
            TIMETC = 0
            CodeGo = ""
            RESEND = False
            while True:
                if TIMETC < 35:
                    # if TIMETC > 100 and RESEND == False:
                        # RESEND = True
                        # try:
                            # phone_code_hash1 = await client.resend_code(phone_number=f"+{PHONE}",phone_code_hash=phone_code_hash)
                            # print(phone_code_hash1)
                            # phone_code_hash2 = phone_code_hash1.phone_code_hash
                        # except Exception as e:
                            # print(e)
                        # except: pass
                    TIMETC += 1
                    STATUSC = ""
                    if SITE == "5sim":
                        headers = {'Authorization': 'Bearer ' + TOKEN,'Accept': 'application/json',}
                        STATUS = requests.get(f"https://5sim.net/v1/user/check/{ID}", headers=headers)
                        try:
                            print(STATUS.content)
                        except: 
                            print(STATUS)
                        try:
                            STATUSC = STATUS.json()["status"]
                            if (STATUSC == "FINISHED" or STATUSC == "RECEIVED") and len(STATUS.json()["sms"]) > 0:
                                for XCODE in STATUS.json()["sms"]:
                                    CodeGo = XCODE["code"]
                                    print(CodeGo)
                                break
                        except Exception as e: print(e)
                        except: pass
                    elif SITE == "sa":
                        STATUS = requests.get(f"https://api.sms-activate.org/stubs/handler_api.php?api_key={TOKEN}&action=getStatus&id={ID}")
                        STATUSC = ""
                        try:
                            STATUSC = str(STATUS.content)
                        except: 
                            STATUSC = str(STATUS)
                        print(STATUSC)
                        if "STATUS_OK" in STATUSC:
                            CodeGo = STATUSC.replace("\n","").replace("STATUS_OK:","").replace("b'","").replace("'","")
                            break
                    elif SITE == "sm":
                        # STATUS = requests.get(f"http://api.sms-man.com/stubs/handler_api.php?api_key={TOKEN}&action=getStatus&id={ID}")
                        STATUS = requests.get(f"http://api.sms-man.com/control/get-sms?token={TOKEN}&request_id={ID}")
                        STATUSC = ""
                        try:
                            STATUSC = STATUS.json()
                            print(STATUSC)
                            if STATUSC["sms_code"]:
                                STATUSC = "STATUS_OK:" + str(STATUSC["sms_code"])
                            else:
                                STATUSC = "STATUS_WAITING"
                        except Exception as e:
                            print(e)
                            STATUSC = "STATUS_WAITING"
                        except:
                            print("Except")
                            STATUSC = "STATUS_WAITING"
                        # try:
                            # STATUSC = str(STATUS.content)
                        # except: 
                            # STATUSC = str(STATUS)
                        # print(STATUSC)
                        if "STATUS_OK" in STATUSC:
                            CodeGo = STATUSC.replace("\n","").replace("STATUS_OK:","").replace("b'","").replace("'","")
                            break
                    else:
                        STATUS = requests.get(f"https://sms-code.store/stubs/handler_api.php?api_key={TOKEN}&action=getStatus&id={ID}")
                        STATUSC = ""
                        try:
                            STATUSC = str(STATUS.content)
                        except: 
                            STATUSC = str(STATUS)
                        print(STATUSC)
                        if "STATUS_OK" in STATUSC:
                            CodeGo = STATUSC.replace("\n","").replace("STATUS_OK:","").replace("b'","").replace("'","")
                            break
                    print(CodeGo)
                else:
                    db.sadd("AFTERTIME",f"{PHONE}")
                    trytoban(TOKEN, ID)
                    print("After Time")
                    OUTED = True
                    try:
                        await client.disconnect()
                    except: pass
                    try:
                        await client.stop()
                    except: pass
                    return False
                await asyncio.sleep(2)
            if CodeGo != "":
                print("SIGN IN")
                # if phone_code_hash2 != "":
                    # HASH = phone_code_hash2
                # else:
                HASH = phone_code_hash
                OKTRUE = 0
                try:
                    RESULTA = await client.sign_in(phone_number=f"+{PHONE}",phone_code_hash=HASH, phone_code=CodeGo)
                    print(RESULTA)
                    try:
                        IDX = RESULTA.id
                        RESULT = await client.accept_terms_of_service(terms_of_service_id=str(IDX))
                    except Exception as e: print(e)
                    try:
                        print("NAME")
                        if db.get("NASK"):
                            NASK = int(db.get("NASK"))
                        if db.get("ATITLE"):
                            ATITLE = str(db.get("ATITLE"))
                            TNN = 0
                            if NASK >= db.scard("NAMES" + ATITLE):
                                NASK = 0
                                db.set("NASK", "0")
                            for GNAME in db.smembers("NAMES" + ATITLE):
                                TNN += 1
                                if TNN > NASK:
                                    NASK = TNN
                                    db.set("NASK", str(TNN))
                                    break
                            GNAME = GNAME
                            GNAMES = GNAME.split(" ")
                            FNAME = GNAMES[0]
                            LNAME = GNAMES[1]
                        else:
                            FNAME = "Torsten"
                            LNAME = "Eichmann"
                        RESULT = await client.sign_up(phone_number=f"+{PHONE}",phone_code_hash= HASH, first_name= str(FNAME) , last_name= str(LNAME))
                        OKTRUE += 1
                    except Exception as e: print(e)
                    db.sadd("PHONESALL",PHONE)
                    db.sadd("CREATED",f"{PHONE}:PYROGRAM:{CodeGo}")
                    try:
                        print("PHOTO")
                        if db.get("SOSK"):
                            SOSK = int(db.get("SOSK"))
                        if db.get("SORP"):
                            SORP = db.get("SORP")
                        if SORP == "SERI":
                            if db.get("ATITLE"):
                                ATITLE = str(db.get("ATITLE"))
                                TIN = 0
                                if SOSK >= db.scard("SERI" + ATITLE):
                                    SORP = "PHOT"
                                    db.set("SORP","PHOT")
                                    SOSK = 0
                                    db.set("SOSK","0")
                                for GPHOTO1 in db.smembers("SERI" + ATITLE):
                                    TIN += 1
                                    if TIN > SOSK:
                                        SOSK = TIN
                                        db.set("SOSK",str(TIN))
                                        break
                                GPHOTO1 = GPHOTO1
                                MSPH = db.scard(GPHOTO1)
                                for SPH in range(1,MSPH + 1):
                                    for URLPH in db.smembers(GPHOTO1):
                                        GETSA = str(SPH) + "-+"
                                        if GETSA in str(URLPH):
                                            URLPH = str(URLPH).replace(GETSA,"")
                                            await client.set_profile_photo(photo=str(URLPH))
                            else:
                                if db.get("ATITLE"):
                                    ATITLE = str(db.get("ATITLE"))
                                    TIN = 0
                                    if SOSK >= db.scard("PHOTOS" + ATITLE):
                                        SORP = "SERI"
                                        db.set("SORP","SERI")
                                        SOSK = 0
                                        db.set("SOSK","0")
                                    for GPHOTO in db.smembers("PHOTOS" + ATITLE):
                                        TIN += 1
                                        if TIN > SOSK:
                                            SOSK = TIN
                                            db.set("SOSK",str(TIN))
                                            break
                                    GPHOTO = GPHOTO
                                    await client.set_profile_photo(photo=str(GPHOTO))
                        elif SORP == "PHOT":
                            if db.get("ATITLE"):
                                ATITLE = str(db.get("ATITLE"))
                                TIN = 0
                                if SOSK >= db.scard("PHOTOS" + ATITLE):
                                    SORP = "SERI"
                                    db.set("SORP","SERI")
                                    SOSK = 0
                                    db.set("SOSK","0")
                                for GPHOTO in db.smembers("PHOTOS" + ATITLE):
                                    TIN += 1
                                    if TIN > SOSK:
                                        SOSK = TIN
                                        db.set("SOSK",str(TIN))
                                        break
                                GPHOTO = GPHOTO
                                await client.set_profile_photo(photo=str(GPHOTO))
                            else:
                                TIN = 0
                                if db.get("ATITLE"):
                                    ATITLE = str(db.get("ATITLE"))
                                    if SOSK >= db.scard("SERI" + ATITLE):
                                        SORP = "PHOT"
                                        db.set("SORP","PHOT")
                                        SOSK = 0
                                        db.set("SOSK","0")
                                    for GPHOTO1 in db.smembers("SERI" + ATITLE):
                                        TIN += 1
                                        if TIN > SOSK:
                                            SOSK = TIN
                                            db.set("SOSK",str(TIN))
                                            break
                                    GPHOTO1 = GPHOTO1
                                    # for URLPH in db.smembers(GPHOTO1):
                                        # URLPH = URLPH
                                        # await client.set_profile_photo(photo=str(URLPH))
                                    MSPH = db.scard(GPHOTO1)
                                    for SPH in range(1,MSPH + 1):
                                        for URLPH in db.smembers(GPHOTO1):
                                            GETSA = str(SPH) + "-+"
                                            if GETSA in str(URLPH):
                                                URLPH = str(URLPH).replace(GETSA,"")
                                                await client.set_profile_photo(photo=str(URLPH))
                        OUTED = True
                        print("END CREATE")
                        try:
                            await client.disconnect()
                        except: pass
                        try:
                            await client.stop()
                        except: pass
                        return True
                    except Exception as e: 
                        print(e)
                        db.sadd("BANNED",f"{PHONE}")
                        trytoban(TOKEN, ID)
                        OUTED = True
                        sys.exit()
                    except: pass
                    OUTED = True
                    try:
                        await client.disconnect()
                    except: pass
                    try:
                        await client.stop()
                    except: pass
                    return False
                except Exception as e: 
                    db.sadd("BANNED",f"{PHONE}")
                    print(e)
                    trytoban(TOKEN, ID)
                    print("EXCEPTION")
                    OUTED = True
                    try:
                        await client.disconnect()
                    except: pass
                    try:
                        await client.stop()
                    except: pass
                    return False
    except errors.PhoneNumberInvalid as error:
        db.sadd("BANNED",f"{PHONE}")
        print("PhoneNumberInvalid")
        trytoban(TOKEN, ID)
        print("No phone")
        OUTED = True
        try:
            await client.disconnect()
        except: pass
        try:
            await client.stop()
        except: pass
        return False
    except Exception as e: 
        db.sadd("BANNED",f"{PHONE}")
        print(e)
        trytoban(TOKEN, ID)
        OUTED = True
        print("Exception 2")
        try:
            await client.disconnect()
        except:
            pass
        return False
        
OUTED = False
First = False
while True:
    if OUTED == True:
        break
    STOKEN = ""
    if SITE == "5sim":
        STOKEN = S5TOKEN
    elif SITE == "sa":
        STOKEN = SATOKEN
    elif SITE == "sm":
        STOKEN = SMTOKEN
    else:
        STOKEN = SCTOKEN
    db.sadd("LISTTHE" , str(THE))
    os.system(f"rm -rf sessions/+{PHONE}.session")
    os.system(f"mkdir -p sessions; mkdir -p reciver;")
    if First == False:
        if TYPECR == "PYRO":
            First = True
            try:
                PORTX = 9050 + int(THE)
                TOR = changeIP(PORTX)
                # loop = asyncio.new_event_loop()
                # asyncio.set_event_loop(loop)
                asyncio.run(PYROG(PHONE,APIID, APIHASH, PORTX, OPRX,IDS,STOKEN,CHATID,SITE,TOR))
                # loop.run_until_complete(PYROG(PHONE,APIID, APIHASH, PORTX, OPRX,IDS,STOKEN,CHATID,SITE))
                # loop.close()
            except Exception as e: print(e)
            except: pass
        elif TYPECR == "THON":
            First = True
            try:
                PORTX = 9050 + int(THE)
                TOR = changeIP(PORTX)
                proxy = {'proxy_type': 'socks5','addr': '127.0.0.1','port': int(PORTX),'username': '','password': '','rdns': True}
                if db.get("WEBSH"): 
                    TOR = TOR.split(":")
                    proxy = proxy = {'proxy_type': 'socks5','addr': TOR[0],'port': int(TOR[1]),'username': TOR[2],'password': TOR[3],'rdns': True}
                clientT = TelegramClient(f'sessions/+{PHONE}', APIID, APIHASH, proxy=proxy)
                clientT.loop.run_until_complete(TELETHON1(clientT,PHONE,PORTX,IDS,OPRX,STOKEN,CHATID,SITE,TOR))
                clientT.start()
                clientT.run_until_disconnected()
            except Exception as e: 
                print(type(e).__name__,e,e.__traceback__.tb_lineno)
            except: pass
        elif TYPECR == "REC":
            First = True
            try:
                PORTX = 9050
                TOR = changeIP(PORTX)
                proxy = {'proxy_type': 'socks5','addr': '127.0.0.1','port': int(PORTX),'username': '','password': '','rdns': True}
                if db.get("WEBSH"): 
                    TOR = TOR.split(":")
                    proxy = proxy = {'proxy_type': 'socks5','addr': TOR[0],'port': int(TOR[1]),'username': TOR[2],'password': TOR[3],'rdns': True}
                MODELS = ["Galaxy J1 Ace",  "Joe",  "Huawei Y7",  "Huawei Enjoy 5S",  "Huawei Mate 10",  "Huawei P20",  "Galaxy J5",  "Galaxy M30",  "Huawei P9 Lite",  "Galaxy J4",  "Galaxy Note 8",  "Galaxy J52 Pro",  "Huawei Y336",  "Huawei Honor 7A",  "Huawei Y221",  "Huawei Nova Lite",  "Galaxy A8s",  "Galaxy Core Plus",  "Honor 6A",  "Galaxy A3",  "Galaxy i7500", "Asus ZenFone Go"]
                MODEL = random.choice(MODELS)
                db.set("MODEL" + str(PHONE), MODEL) 
                SYSTEMS = ["Galaxy J1 Ace",  "Android 8.1 O MR1 (27)",  "Android 6.0",  "Android 8.0 O (26)",  "Android 8.0.0",  "Android 10 Q (29)",  "Android 4.2.2",  "Android 9 P (28)"]
                SYSTEM = random.choice(SYSTEMS)
                db.set("SYSTEM" + str(PHONE), SYSTEM)
                APPL = [1,2,3,4,5,6,7,8,9,0]
                APPVER = str(random.choice(APPL)) + "." + str(random.choice(APPL)) + "." + str(random.choice(APPL))
                db.set("APPVER" + str(PHONE), APPVER)
                clientT = TelegramClient(f'reciver/+{PHONE}', APIID, APIHASH,device_model=MODEL,system_version=SYSTEM,app_version=APPVER,use_ipv6 = False, timeout=10,request_retries=2,connection_retries=2,retry_delay=5,flood_sleep_threshold=120, proxy=proxy)
                clientT.loop.run_until_complete(TELETHON2(clientT,str(PHONE).replace("+",""),PORTX,CHATID))
                clientT.start()
                clientT.run_until_disconnected()
            except Exception as e: 
                print(type(e).__name__,e,e.__traceback__.tb_lineno)
            except: pass
        elif TYPECR == "CHK":
            First = True
            try:
                PORTX = 9050
                TOR = changeIP(PORTX)
                proxy = {'proxy_type': 'socks5','addr': '127.0.0.1','port': int(PORTX),'username': '','password': '','rdns': True}
                if db.get("WEBSH"): 
                    TOR = TOR.split(":")
                    proxy = proxy = {'proxy_type': 'socks5','addr': TOR[0],'port': int(TOR[1]),'username': TOR[2],'password': TOR[3],'rdns': True}
                APPVER = ""
                MODEL = ""
                SYSTEM = ""
                if db.get("MODEL" + str(PHONE)):
                    MODEL = db.get("MODEL" + str(PHONE))
                if db.get("SYSTEM" + str(PHONE)):
                    SYSTEM = db.get("SYSTEM" + str(PHONE))
                if db.get("APPVER" + str(PHONE)):
                    APPVER = db.get("APPVER" + str(PHONE))
                clientT = ""
                if APPVER != "" and SYSTEM != "" and MODEL != "":
                    clientT = TelegramClient(f'reciver/+{PHONE}', APIID, APIHASH,device_model=MODEL,system_version=SYSTEM,app_version=APPVER,use_ipv6 = False, timeout=10,request_retries=2,connection_retries=2,retry_delay=5,flood_sleep_threshold=120, proxy=proxy)
                else:
                    clientT = TelegramClient(f'reciver/+{PHONE}', APIID, APIHASH, proxy=proxy)
                clientT.loop.run_until_complete(THONCHECK(clientT,str(PHONE).replace("+",""),PORTX,CHATID))
                clientT.start()
                clientT.run_until_disconnected()
            except Exception as e: 
                print(type(e).__name__,e,e.__traceback__.tb_lineno)
            except: pass
        
    sleep(5)
db.srem("LISTTHE" , str(THE))
print("END")