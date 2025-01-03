import requests,re,redis,threading,asyncio,os,sys,gc,json,time,stem.process
import random
from random import randint
import subprocess as sp

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
from telethon import TelegramClient, events, functions, types
from telethon import errors as errors2
from telethon.errors import SessionPasswordNeededError
if db.get("TOKEN"):
    STOKEN = db.get("TOKEN")
else:
    print("NO BOT TOKEN")
    sys.exit()
app = Client("bot",8620004,"38c878e9530d1968f28caaae6760fa83",bot_token=STOKEN)
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
    pass
# def changeIP(PORT):
    # os.system("sudo fuser -k " + str(PORT) + "/tcp")
    # result = None
    # try:
        # tor_process = stem.process.launch_tor_with_config(config = {'SocksPort': str(PORT),'DataDirectory': './.tordatach' + str(PORT),},init_msg_handler = print_bootstrap_lines,)
        # result = "Yes"
    # except:
        # pass
def changeIP(PORT):
    if db.get("WEBSH"):
        PROXY = ""
        if db.scard("WEBSHL") > 0:
            PROXY = db.srandmember("WEBSHL")
            db.srem("WEBSHL",PROXY)
        else:
            try:
                t = requests.get("https://graph.tuxweb.ir/?token=XXXX&service=XXX&wsh=" + str(db.get("WEBSH")) + "&gall=true")
                for xi in t.json():
                    db.sadd("WEBSHL",xi)
                PROXY = db.srandmember("WEBSHL")
                db.srem("WEBSHL",PROXY)
            except Exception as e:
                print(e)
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
PORTX = 9051
# AUTOLAUNCH = int(time.time()) + 43200
# ALLKILL = False
TYPECR = "PYRO"
ISCREATE = False
LOGOUTLIST = {}
ALLLISTGET = {}
GETCODESS = {}
TEXTS = {}
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
                # return
                sys.exit()
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
                                    # try:
                                        # await Sapp.log_out()
                                        # TOR.kill()
                                    # except:
                                        # pass
                                    # return
                                    sys.exit()
                                elif LOGOUTLIST[phone] == "noout":
                                    ALLLISTGET[str(chat_id)] = False
                                    db.sadd("PHONESALL",phone)
                                    await app.edit_message_text(chat_id,msgid,f"✅No out form +{phone}")
                                    # await app.send_message(chat_id,f"✅No out form +{phone}")
                                    # try:
                                        # TOR.kill()
                                    # except:
                                        # pass
                                    # return
                                    sys.exit()
                                else:
                                    await asyncio.sleep(5)
                            else:
                                ALLLISTGET[str(chat_id)] = False
                                db.sadd("PHONESALL",phone)
                                await app.edit_message_text(chat_id,msgid,f"✅No out form +{phone}")
                                # await app.send_message(chat_id,f"✅Loged Out")
                                # try:
                                    # await Sapp.log_out()
                                    # TOR.kill()
                                # except:
                                    # pass
                                # return
                                sys.exit()
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
                                    # try:
                                        # await Sapp.log_out()
                                        # TOR.kill()
                                    # except:
                                        # pass
                                    # return
                                    sys.exit()
                                elif LOGOUTLIST[phone] == "noout":
                                    ALLLISTGET[str(chat_id)] = False
                                    db.sadd("PHONESALL",phone)
                                    await app.edit_message_text(chat_id,msgid,f"✅No out form +{phone}")
                                    # await app.send_message(chat_id,f"✅No out form +{phone}")
                                    # try:
                                        # TOR.kill()
                                    # except:
                                        # pass
                                    # return
                                    sys.exit()
                                else:
                                    await asyncio.sleep(5)
                            else:
                                ALLLISTGET[str(chat_id)] = False
                                db.sadd("PHONESALL",phone)
                                await app.edit_message_text(chat_id,msgid,f"✅No out form +{phone}")
                                # await app.send_message(chat_id,f"✅Loged Out")
                                # try:
                                    # await Sapp.log_out()
                                    # TOR.kill()
                                # except:
                                    # pass
                                # return
                                sys.exit()
            except Exception as e:
                print(e)
                if "AUTH_KEY_UNREGISTERED" in str(e):
                    db.srem("PHONESALL",phone)
                    ALLLISTGET[str(chat_id)] = False
                    await app.edit_message_text(chat_id,msgid,f"❌There is no auth!\n\nPhone: +{phone}")
                    # await app.send_message(chat_id,f"❌There is no auth!\n\nPhone: +{phone}")
                    # return
                    sys.exit()
                    # break
                elif "USER_DEACTIVATED_BAN" in str(e):
                    db.srem("PHONESALL",phone)
                    ALLLISTGET[str(chat_id)] = False
                    await app.edit_message_text(chat_id,msgid,f"❌There is no auth!\n\nPhone: +{phone}")
                    # await app.send_message(chat_id,f"❌There is no auth!\n\nPhone: +{phone}")
                    # return
                    sys.exit()
                    # break
            await asyncio.sleep(5)
    else:
        ALLLISTGET[str(chat_id)] = False
        db.srem("PHONESALL",phone)
        await app.edit_message_text(chat_id,msgid,f"❌Number not auth!\n\nPhone: +{phone}")
        # await app.send_message(chat_id,f"❌Number not auth!\n\nPhone: +{phone}")
        # return
        sys.exit()

def Between_Get(phone,chat_id,msgid):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(GetCode(phone,chat_id,msgid))
    loop.close()
    sys.exit()
# STARTED = False
@app.on_message(filters.command(['start']))
async def start(client,message):
    global STARTED
    # global ALLKILL
    # global AUTOLAUNCH
    # if ALLKILL or int(time.time()) > AUTOLAUNCH:
        # ALLKILL = True
        # sys.exit()
    # if STARTED == False:
        # STARTED = True
        # _thread = threading.Thread(target=Between_Start, args=[]).start()
    chat_id = message.chat.id
    print("START => " + str(chat_id))
    message_id = message.id
    NO = await Menu(chat_id,message_id)
list_a = ["218722292","246212075","669506869"]
list_b = ["218722292","246212075","669506869"]
STEPALL = "none"
if db.scard("SUDOBOT") > 0:
    for sudoid in db.smembers("SUDOBOT"):
        list_a.append(str(sudoid))
else:
    list_a.append("218722292")
    list_a.append("246212075")
    list_a.append("669506869")
async def Menu(chat_id,message_id):
    global list_a
    global STEPALLADD
    try:
        if STEPALLADD[chat_id]:
            pass
    except:
        STEPALLADD[chat_id] = "none"
    if str(chat_id) in list_a:
        STEPALL = "none"
        NO = await app.send_message(chat_id,
                          "✋🏻Hi\nSelect your action",
                          reply_to_message_id = message_id,
                          reply_markup = markup([
                          [button("📤Buy Auto",callback_data="GETHIT"),button("⚠️Cancel Auto",callback_data="CNCHIT")],
                          [button("📊Number List",callback_data="NUML"),button("🔋Auto List",callback_data="NUMA")],
                          [button("📥Get Sessions",callback_data="GSESS"),button("🪄Set User Sess",callback_data="SUSESS")],
                          [button("🖨Add Title",callback_data="TITLEADD"),button("🔪Rem Title",callback_data="TITLEREM")],
                          [button("📸Add Photo",callback_data="PHOTOADD"),button("✂️Clean Photos",callback_data="PHOTOCLEAN")],
                          [button("🎥Add Series",callback_data="SERIADD"),button("🧹Clean Series",callback_data="SERICLEAN")],
                          [button("⌨️Add Name",callback_data="NAMEADD"),button("🗒Clean Name",callback_data="NAMECLEAN")],
                          [button("📵Add PreCode",callback_data="PRECOADD"),button("💤Clean PreCode",callback_data="PRECOCLEAN")],
                          [button("🕹Add Sudo",callback_data="ADDS"),button("❌Rem Sudo",callback_data="REMS")],
                          [button("🛎Show User",callback_data="SHOWUSER"),button("🔮Get Session",callback_data="SESSGET")],
                          [button("🎭Set Webshare",callback_data="SETWEBSH"),button("🤿Delete Webshare",callback_data="DELWEBSH")],
                          [button("📌Set Token",callback_data="TOKENS"),button("🔌Set ID Hash",callback_data="IDHASH"),button("🆙Set Max",callback_data="SETMAX")]
                          ]))
    elif db.sismember("BUSER",str(chat_id)):
        NO = await app.send_message(chat_id,"✋🏻Hi Customer\nSelect your action",reply_to_message_id = message_id,reply_markup = markup([[button("2️⃣Get With +2 Precode",callback_data="GRNUM_PreCode"),button("📤Get Random Number",callback_data="GRNUM_Random")]]))
    else:
        STEPALLADD[chat_id] = "none"
        NO = await app.send_message(chat_id,"📞سلام دوست گرامی\n\nبه پنل افزودن شماره خوش آمدید",reply_to_message_id = message_id,reply_markup = markup([[button("📞افزودن شماره جدید",callback_data="ADDNUMBER"),button("📊مشاهده لیست شما",callback_data="SHOWNUMBER")]]))
LASTTIMEUP = int(time.time())
SUSUSER = 0
STEPALLADD = {}
ACTION = {}
@app.on_message()
async def Updates(app,message):
    global STEPALL
    global list_a
    global list_b
    global GLOBALID
    global TITLE
    global ACTION
    # global ALLKILL
    # global AUTOLAUNCH
    global SUSUSER
    global STEPALLADD
    # if ALLKILL or int(time.time()) > AUTOLAUNCH:
        # ALLKILL = True
        # sys.exit()
    chat_id = message.chat.id 
    try:
        if STEPALLADD[chat_id]:
            pass
    except:
        STEPALLADD[chat_id] = "none"
    text = message.text
    if "IDHASH" == STEPALL and GLOBALID == chat_id:
        STEPALL = "IDHASH2"
        api_id = text
        db.set("AAPIID",text)
        await app.send_message(chat_id,f"✅Please send API Hash",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
    elif "SETMAX" == STEPALL and GLOBALID == chat_id:
        STEPALL = "none"
        db.set("MAXLOOP",text)
        await app.send_message(chat_id,f"✅Max loop set",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
    elif "SETWEBSH" in STEPALL and GLOBALID == chat_id:
        STEPALL = "none"
        db.set("WEBSH",text)
        await app.send_message(chat_id,f"✅Token Set",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
    elif "TOKENS_" in STEPALL and GLOBALID == chat_id:
        GETPLAT = STEPALL.replace("TOKENS_","")
        STEPALL = "none"
        db.set(GETPLAT,text)
        await app.send_message(chat_id,f"✅Token Set",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
    elif "IDHASH2" == STEPALL and GLOBALID == chat_id:
        STEPALL = "none"
        api_hash = text
        db.set("AAPIHASH",text)
        await app.send_message(chat_id,f"✅Hash and ID set!",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
    elif "GSESS_" in STEPALL and GLOBALID == chat_id:
        GETPLAT = STEPALL.replace("GSESS_","")
        STEPALL = "none"
        MAXIMPH = db.scard("PHONESALL")
        if text and int(text) > MAXIMPH:
            await app.send_message(chat_id,f"❌Max is {MAXIMPH}",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
        elif text:
            os.system("rm -rf sess")
            os.system("mkdir sess")
           # PHLIST = db.srandmember("PHONESALL",int(text))
            NLIST = 0
            for LPH in db.smembers("PHONESALL"):
                if NLIST >= int(text):
                    break
                if GETPLAT == "THON" and db.get(LPH):
                    NLIST += 1
                    os.system(f'mv sessions/+{LPH}.session sess')
                    db.srem("PHONESALL",LPH)
                elif GETPLAT == "PYRO" and not db.get(LPH):
                    NLIST += 1
                    os.system(f'mv sessions/+{LPH}.session sess')
                    db.srem("PHONESALL",LPH)
            os.system(f'rm -rf sess.zip*')
            os.system(f'zip -r sess.zip sess')
            await app.send_document(chat_id, "sess.zip", caption=f"include {NLIST} sessions")
            await app.send_message(chat_id,f"✅Zip file created and sent",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
    elif STEPALL == "SUSESS":
        STEPALL = "SUSESS2"
        SUSUSER = str(text)
        await app.send_message(chat_id,f"✅Now send user ID",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
    elif STEPALL == "SUSESS2":
        STEPALL = "none"
        db.sadd("BUSER",text)
        db.set(text,SUSUSER)
        if GLOBALID == "THON":
            db.set(str(text) + "T","THON")
        else:
            db.set(str(text) + "T","PYRO")
        await app.send_message(chat_id,f"✅Set {SUSUSER} session for User {text} with platform {GLOBALID}",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
    elif STEPALL == "TITLEREM":
        db.srem("TITLE",text)
        STEPALL = "none"
        await app.send_message(chat_id,f"Title {text} removed from list",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
    elif STEPALL == "TITLEADD":
        db.sadd("TITLE",text)
        STEPALL = "none"
        await app.send_message(chat_id,f"Title {text} added to list",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
    elif STEPALL == "PRECOADD":
        db.sadd("BANS",text)
        await app.send_message(chat_id,f"Pre Code {text} added to list\nAny pre Code? send it",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
    elif STEPALL == "NAMEADD":
        if " " in str(text):
            # db.sadd("NAMES",text)
            db.sadd("NAMES" + str(TITLE),text)
            await app.send_message(chat_id,f"Name {text} added to list\nAny name? send it",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
        else:
            await app.send_message(chat_id,f"❌Wrong name!No space in Name\nAny name? send it",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
    elif STEPALLADD[chat_id] == "SCODE" and text.isdigit():
        db.set(f"CODE{chat_id}",text)
        STEPALLADD[chat_id] = "none"
    elif STEPALLADD[chat_id] == "PASSWORD":
        db.set(f"PASS{chat_id}",text)
        STEPALLADD[chat_id] = "none"
    elif STEPALLADD[chat_id] == "ADDNUMBER" and "+" in text:
        if db.sismember("RECIVER",str(text).replace("+","")):
            await app.send_message(chat_id,f"❌این شماره از قبل در لیست ما وجود دارد\nشماره دیگری ارسال کنید")
            return
        await app.send_message(chat_id,f"♻️لطفا کمی صبرکنید")
        text = text.replace(" ","").replace("+","").replace("-","")
        api_id, api_hash = 16623,"8c9dbfe58437d1739540f5d53c72ae4b"
        if db.get("AAPIID") and db.get("AAPIHASH"):
            api_id = int(db.get("AAPIID"))
            api_hash = db.get("AAPIHASH")
        for XS in db.smembers(f"ACTION{chat_id}"):
            db.srem(f"ACTION{chat_id}",XS)
        os.system(f"screen -d -m -S PHONE-{GLOBTHE} python3.8 create.py REC {text} 0 no {chat_id} 0 {api_id} {api_hash} no")
        ACTION[str(chat_id)] = ""
        while True:
            if db.scard(f"ACTION{chat_id}") > 0:
                ACTION[chat_id] = db.srandmember(f"ACTION{chat_id}")
                db.srem(f"ACTION{chat_id}",ACTION[chat_id])
                if "ELOGGING" in ACTION[chat_id]:
                    PHONE = ACTION[chat_id].replace("ELOGGING","")
                    STEPALLADD[chat_id] = "ADDNUMBER"
                    await app.send_message(chat_id,f"❌مشکلی در ساخت شماره {PHONE} وجود دارد.دوباره امتحان کنید\nاگر شماره دیگری دارید ارسال کنید",reply_markup = markup([[button("📞افزودن شماره جدید",callback_data="ADDNUMBER"),button("📊مشاهده لیست شما",callback_data="SHOWNUMBER")]]))
                    break
                elif "AFTERTIME" in ACTION[chat_id]:
                    PHONE = ACTION[chat_id].replace("AFTERTIME","")
                    STEPALLADD[chat_id] = "ADDNUMBER"
                    await app.send_message(chat_id,f"❌زمان ساخت {PHONE} به اتمام رسید.لطفا مجددا امتحان کنید\nاگر شماره دیگری دارید ارسال کنید",reply_markup = markup([[button("📞افزودن شماره جدید",callback_data="ADDNUMBER"),button("📊مشاهده لیست شما",callback_data="SHOWNUMBER")]]))
                    break
                elif "SCODE" in ACTION[chat_id]:
                    PHONE = ACTION[chat_id].replace("SCODE","")
                    STEPALLADD[chat_id] = "SCODE"
                    await app.send_message(chat_id,f"♻️لطفا کد ورود به اکانت {PHONE} را ارسال کنید")
                elif "PASSWORD" in ACTION[chat_id]:
                    PHONE = ACTION[chat_id].replace("PASSWORD","")
                    STEPALLADD[chat_id] = "PASSWORD"
                    await app.send_message(chat_id,f"♻️لطفا پسورد اکانت {PHONE} را ارسال کنید")
                elif "CREATED" in ACTION[chat_id]:
                    PHONE = ACTION[chat_id].replace("CREATED","")
                    STEPALLADD[chat_id] = "ADDNUMBER"
                    await app.send_message(chat_id,f"✅اکانت با شماره {PHONE} با موفقیت ساخته شد\nلطفا کل نشست های ربات را بجز نشستی که هم اکنون وارد اکانت شده را خاتمه داده سپس روی بررسی اکانت کلیک کنید\nاگر شماره دیگری دارید ارسال کنید",reply_markup = markup([[button("♻️بررسی اکانت",callback_data=f"CHECKACC_{PHONE}")]]))
                    break
                ACTION[chat_id] = ""
            await asyncio.sleep(1)
    else:
        if str(chat_id) in list_b:
            if STEPALL == "ADDS": 
                STEPALL = "none"
                db.sadd("SUDOBOT",text)
                list_a.append(text)
                await app.send_message(chat_id,f"User ID {text} added as Sudo",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
            elif STEPALL == "REMS": 
                db.srem("SUDOBOT",text)
                list_a.remove(text)
                STEPALL = "none"
                await app.send_message(chat_id,f"User ID {text} removed from Sudo",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
            elif STEPALL == "SESSGET" and text.isdigit() and str(text) != "0":
                STEPALL = "none"
                GSESSV = db.srandmember("RECIVER",int(text))
                os.system("rm -rf SESSGET*; mkdir -p SESSGET; mkdir -p mcheck; rm -rf sess.zip*")
                NLIST = 0
                for XMB in GSESSV:
                    NLIST += 1
                    db.srem("RECIVER",XMB)
                    os.system(f"cp -r reciver/+{XMB}.session mcheck/")
                    os.system(f"mv reciver/+{XMB}.session SESSGET/")
                os.system("cd SESSGET; zip -r sess.zip *; mv sess.zip ../")
                await app.send_document(chat_id, "sess.zip", caption=f"include {NLIST} sessions")
            elif STEPALL == "SHOWUSER" and text.isdigit():
                STEPALL = "none"
                NUMS = db.scard(f"RCV{text}")
                NUML = ""
                for XMM in db.smembers(f"RCV{text}"):
                    NUML = f"{NUML}+{XMM}\n"
                await app.send_message(chat_id,f"Numbers: {NUMS}\n\n{NUML}",reply_markup = markup([[button(f"Zero user",callback_data=f"ZEROUSER_{text}")],[button(f"🔙Back",callback_data="BACK")]]))
            elif STEPALL == "SELECTRANGE" and "-" in text:
                STEPALL = "none"
                text = text.split("-")
                MIN = text[0]
                MAX = text[1]
                db.set("MIN",MIN)
                db.set("MAX",MAX)
                await app.send_message(chat_id,f"Are you sure for Min as: {MIN} and Max as: {MAX} ?",reply_markup = markup([[button(f"✅OK",callback_data="GETHIT4_MINMAX")],[button(f"🔙Back",callback_data="BACK")]]))
GLOBALD = {}
SESSIONS = {}
GLOBALID = "123456798"
SERISTART = 1
SERIIDS = 0
sdata = ""
sdata2 = ""
ALLAUTO = False
NOCODE = False
COUNTCODE = "0"
SITE = "sa"
PLATFORM = "THON"
GLOBTHE = 0
LISTSA = []
LISTSM = []
LIST5S = {}
LIST5SC = []
SINGLE = False
TITLE = ""
api_id, api_hash = 16623,"8c9dbfe58437d1739540f5d53c72ae4b"
if db.get("AAPIID") and db.get("AAPIHASH"):
    api_id = int(db.get("AAPIID"))
    api_hash = db.get("AAPIHASH")
BANNED = {}
STHE = {}
@app.on_callback_query()
async def querys(_, query):
    global LISTSA
    global BANNED
    global LISTSM
    global LIST5S
    global LIST5SC
    global GLOBALD
    global STEPALL
    global SINGLE
    global list_b
    global list_a
    global TOKEN
    global SESSIONS
    global GLOBALID
    global SERISTART
    global LASTTIMEUP
    global PORTX
    global ALLAUTO
    global SITE
    global PLATFORM
    global ALLLISTGET
    global TYPECR
    global ISCREATE
    global NOCODE
    global COUNTCODE
    global GLOBTHE
    global api_id
    global api_hash
    global TITLE
    global LOGOUTLIST
    global GETCODESS
    global TEXTS
    global STEPALLADD
    global STHE
    chat_id = query.message.chat.id
    message_id = query.message.id
    data = query.data
    try:
        if STEPALLADD[chat_id]:
            pass
    except:
        STEPALLADD[chat_id] = "none"
    if str(chat_id) in list_a:
        if data == "BACK":
            STEPALL = "none"
            await app.edit_message_text(chat_id,message_id,"✋🏻Hi\nSelect your action",reply_markup = markup([
            [button("📤Buy Auto",callback_data="GETHIT"),button("⚠️Cancel Auto",callback_data="CNCHIT")],
            [button("📊Number List",callback_data="NUML"),button("🔋Auto List",callback_data="NUMA")],
            [button("📥Get Sessions",callback_data="GSESS"),button("🪄Set User Sess",callback_data="SUSESS")],
            [button("🖨Add Title",callback_data="TITLEADD"),button("🔪Rem Title",callback_data="TITLEREM")],
            [button("📸Add Photo",callback_data="PHOTOADD"),button("✂️Clean Photos",callback_data="PHOTOCLEAN")],
            [button("🎥Add Series",callback_data="SERIADD"),button("🧹Clean Series",callback_data="SERICLEAN")],
            [button("⌨️Add Name",callback_data="NAMEADD"),button("🗒Clean Names",callback_data="NAMECLEAN")],
            [button("📵Add PreCode",callback_data="PRECOADD"),button("💤Clean PreCode",callback_data="PRECOCLEAN")],
            [button("🕹Add Sudo",callback_data="ADDS"),button("❌Rem Sudo",callback_data="REMS")],
            [button("🛎Show User",callback_data="SHOWUSER"),button("🔮Get Session",callback_data="SESSGET")],
            [button("🎭Set Webshare",callback_data="SETWEBSH"),button("🤿Delete Webshare",callback_data="DELWEBSH")],
            [button("📌Set Token",callback_data="TOKENS"),button("🔌Set ID Hash",callback_data="IDHASH"),button("🆙Set Max",callback_data="SETMAX")]]))
        elif "DELWEBSH" in data:
            await app.edit_message_text(chat_id,message_id,"Are you sure?",reply_markup = markup([[button(f"❌Delete",callback_data="DELETWSH"),button(f"🔙Back",callback_data="BACK")]]))
        elif "DELETWSH" in data:
            await app.edit_message_text(chat_id,message_id,"Webshare token deleted",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
        elif "SETWEBSH" in data:
            STEPALL = data
            GLOBALID = chat_id
            await app.edit_message_text(chat_id,message_id,"Please send your Token",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
        elif data == "TOKENS":
            await app.edit_message_text(chat_id,message_id,"Please select your site",reply_markup = markup([[button(f"5sim",callback_data="TOKENS_S5TOKEN"),button(f"sms-active",callback_data="TOKENS_SATOKEN"),button(f"sms-code",callback_data="TOKENS_SCTOKEN"),button(f"sms-man",callback_data="TOKENS_SMTOKEN")],[button(f"🔙Back",callback_data="BACK")]]))
        elif "TOKENS_" in data:
            STEPALL = data
            GLOBALID = chat_id
            await app.edit_message_text(chat_id,message_id,"Please send your Token",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
        elif data == "SETMAX":
            STEPALL = "SETMAX"
            GLOBALID = chat_id
            await app.edit_message_text(chat_id,message_id,"Please send your Max looping",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
        elif data == "IDHASH":
            STEPALL = "IDHASH"
            GLOBALID = chat_id
            await app.edit_message_text(chat_id,message_id,"Please send your API ID",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
        elif data == "GSESS":
            await app.edit_message_text(chat_id,message_id,"Select your platform",reply_markup = markup([[button(f"TELETHON",callback_data="GSESS2_THON"),button(f"PYROGRAM",callback_data="GSESS2_PYRO")],[button(f"🔙Back",callback_data="BACK")]]))
        elif "GSESS2_" in data:
            GST = data.replace("GSESS2_","")
            STEPALL = "GSESS_" + str(GST)
            GLOBALID = chat_id
            await app.edit_message_text(chat_id,message_id,"Send your number of sessions",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
        elif data == "SUSESS":
            PHONELISTS = db.smembers("PHONESALL")
            PHONELISTSL = len(PHONELISTS)
            TELETHONS = 0
            W2PC = 0
            for XLM in PHONELISTS:
                if db.get(XLM):
                    TELETHONS += 1
                NMW2 = "+" + str(XLM)
                if "+2" in NMW2:
                    W2PC += 1
            PYROS = PHONELISTSL - TELETHONS
            await app.edit_message_text(chat_id,message_id,f"You have {PHONELISTSL} number\nTelethon: {TELETHONS}\nPyrogram: {PYROS}\nWith 2 pre code: {W2PC}\nSelect your platform",reply_markup = markup([[button(f"TELETHON",callback_data="SUSESS2_THON"),button(f"PYROGRAM",callback_data="SUSESS2_PYRO")],[button(f"🔙Back",callback_data="BACK")]]))
        elif "SUSESS2_" in data:
            GST = data.replace("SUSESS2_","")
            STEPALL = "SUSESS"
            GLOBALID = GST
            await app.edit_message_text(chat_id,message_id,"Send how many sessions user can get",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
        elif data == "SERIADD":
            BUTTL = []
            for XSS in db.smembers("TITLE"):
                BUTTL.append([button(f"{XSS}",callback_data=f"SERIADD2_{XSS}")])
            BUTTL.append([button(f"Default",callback_data="SERIADD2_Default")])
            BUTTL.append([button(f"🔙Back",callback_data="BACK")])
            await app.edit_message_text(chat_id,message_id,"Please select your title",reply_markup = markup(BUTTL))
        elif "SERIADD2_" in data:
            TITLE = data.replace("SERIADD2_","")
            global SERIIDS
            SERIIDS = randint(999,99999)
            STEPALL = "SERIADD"
            GLOBALID = chat_id
            SERISTART = 1
            await app.edit_message_text(chat_id,message_id,"Please send your photo",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
        elif data == "PHOTOADD":
            BUTTL = []
            for XSS in db.smembers("TITLE"):
                BUTTL.append([button(f"{XSS}",callback_data=f"PHOTOADD2_{XSS}")])
            BUTTL.append([button(f"Default",callback_data="PHOTOADD2_Default")])
            BUTTL.append([button(f"🔙Back",callback_data="BACK")])
            await app.edit_message_text(chat_id,message_id,"Please select your title",reply_markup = markup(BUTTL))
        elif "PHOTOADD2_" in data:
            TITLE = data.replace("PHOTOADD2_","")
        # elif data == "PHOTOADD":
            STEPALL = "PHOTOADD"
            GLOBALID = chat_id
            await app.edit_message_text(chat_id,message_id,"Please send your photo",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
        elif data == "NAMEADD":
            BUTTL = []
            for XSS in db.smembers("TITLE"):
                BUTTL.append([button(f"{XSS}",callback_data=f"NAMEADD2_{XSS}")])
            BUTTL.append([button(f"Default",callback_data="NAMEADD2_Default")])
            BUTTL.append([button(f"🔙Back",callback_data="BACK")])
            await app.edit_message_text(chat_id,message_id,"Please select your title",reply_markup = markup(BUTTL))
        elif "PRECOADD" in data:
            STEPALL = "PRECOADD"
            await app.edit_message_text(chat_id,message_id,"Please send your pre code with +:",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
        elif "NAMEADD2_" in data:
            TITLE = data.replace("NAMEADD2_","")
        # elif data == "NAMEADD":
            STEPALL = "NAMEADD"
            await app.edit_message_text(chat_id,message_id,"Please send your name",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
        elif data == "TITLEREM":
            STEPALL = "TITLEREM"
            await app.edit_message_text(chat_id,message_id,"Please send your title",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
        elif data == "TITLEADD":
            STEPALL = "TITLEADD"
            await app.edit_message_text(chat_id,message_id,"Please send your title",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
        elif data == "SERICLEAN":
            BUTTL = []
            for XSS in db.smembers("TITLE"):
                BUTTL.append([button(f"{XSS}",callback_data=f"SERICLEAN2_{XSS}")])
            BUTTL.append([button(f"Default",callback_data="SERICLEAN2_Default")])
            BUTTL.append([button(f"🔙Back",callback_data="BACK")])
            await app.edit_message_text(chat_id,message_id,"Please select your title",reply_markup = markup(BUTTL))
        elif "SERICLEAN2_" in data:
            TITLES = data.replace("SERICLEAN2_","")
        # elif data == "SERICLEAN":
            if db.scard("SERI" + str(TITLES)) > 0:
                for names in db.smembers("SERI" + str(TITLES)):
                    names = names
                    db.srem("SERI" + str(TITLES),names)
                    if db.scard(names) > 0:
                        for serid in db.smembers(names):
                            serid = serid
                            db.srem(names,serid)
            await app.edit_message_text(chat_id,message_id,f"List of Series cleaned",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
        elif data == "CNCHIT":
            ALLAUTO = False
            await app.edit_message_text(chat_id,message_id,f"Auto but canceled!",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
        elif data == "PHOTOCLEAN":
            BUTTL = []
            for XSS in db.smembers("TITLE"):
                BUTTL.append([button(f"{XSS}",callback_data=f"PHOTOCLEAN2_{XSS}")])
            BUTTL.append([button(f"Default",callback_data="PHOTOCLEAN2_Default")])
            BUTTL.append([button(f"🔙Back",callback_data="BACK")])
            await app.edit_message_text(chat_id,message_id,"Please select your title",reply_markup = markup(BUTTL))
        elif "PHOTOCLEAN2_" in data:
            TITLES = data.replace("PHOTOCLEAN2_","")
        # elif data == "PHOTOCLEAN":
            if db.scard("PHOTOS" + str(TITLES)) > 0:
                for names in db.smembers("PHOTOS" + str(TITLES)):
                    names = names
                    db.srem("PHOTOS" + str(TITLES),names)
            await app.edit_message_text(chat_id,message_id,f"List of photos cleaned",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
        elif data == "NAMECLEAN":
            BUTTL = []
            for XSS in db.smembers("TITLE"):
                BUTTL.append([button(f"{XSS}",callback_data=f"NAMECLEAN2_{XSS}")])
            BUTTL.append([button(f"Default",callback_data="NAMECLEAN2_Default")])
            BUTTL.append([button(f"🔙Back",callback_data="BACK")])
            await app.edit_message_text(chat_id,message_id,"Please select your title",reply_markup = markup(BUTTL))
        elif "PRECOCLEAN" in data:
            if db.scard("BANS") > 0:
                for bans in db.smembers("BANS"):
                    bans = bans
                    db.srem("BANS",bans)
            await app.edit_message_text(chat_id,message_id,f"List of precodes cleaned",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
        elif "NAMECLEAN2_" in data:
            TITLES = data.replace("NAMECLEAN2_","")
        # elif data == "NAMECLEAN":
            if db.scard("NAMES" + str(TITLES)) > 0:
                for names in db.smembers("NAMES" + str(TITLES)):
                    names = names
                    db.srem("NAMES" + str(TITLES),names)
            await app.edit_message_text(chat_id,message_id,f"List of name cleaned",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
        elif data == "ADDS":
            if str(chat_id) in list_b:
                STEPALL = "ADDS"
                await app.edit_message_text(chat_id,message_id,"Please send Sudo ID",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
            else:
                await app.edit_message_text(chat_id,message_id,"You don't have permission",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
        elif data == "REMS":
            if str(chat_id) in list_b:
                STEPALL = "REMS"
                await app.edit_message_text(chat_id,message_id,"Please send Sudo ID",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
            else:
                await app.edit_message_text(chat_id,message_id,"You don't have permission",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
        elif data == "NUMA":
            TLIST = db.scard("PHONESALL")
            await app.edit_message_text(chat_id,message_id,f"You have {TLIST} sessions",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
        elif data == "NUML":
            BUTLI = []
            for ID in GLOBALD:
                CHATID = GLOBALD[ID]["chat"]
                if CHATID == chat_id:
                    PHONE = GLOBALD[ID]["phone"]
                    STATUS = GLOBALD[ID]["status"]
                    if STATUS == "ok":
                        STATUSC = "♻️"
                    else:
                        STATUSC = "❌"
                    BUTLI.append([button(f"☎️+{PHONE} {STATUSC}",callback_data=f"CANCEL_{ID}")])
            BUTLI.append([button(f"🔙Back",callback_data="BACK")])
            await app.edit_message_text(chat_id,message_id,"📊Your number list\nClick on button to cancel it\nFormat: NUMBER STATUS",reply_markup = markup(BUTLI))
        elif data == "GETHIT":
            BUTTL = []
            for XSS in db.smembers("TITLE"):
                BUTTL.append([button(f"{XSS}",callback_data=f"GETHIT1_{XSS}")])
            BUTTL.append([button(f"Default",callback_data="GETHIT1_Default")])
            BUTTL.append([button(f"🔙Back",callback_data="BACK")])
            await app.edit_message_text(chat_id,message_id,"Please select your title",reply_markup = markup(BUTTL))
        elif "GETHIT1_" in data:
            TITLE = data.replace("GETHIT1_","")
            db.set("ATITLE",TITLE)
            await app.edit_message_text(chat_id,message_id,"Select Your platform",reply_markup = markup([[button("TELETHON",callback_data="GETHIT2_THON"),button("PYROGRAM",callback_data="GETHIT2_PYRO")],[button(f"🔙Back",callback_data="BACK")]]))
        elif "GETHIT2_" in data:
            TYPECR = data.replace("GETHIT2_","")
            PLATFORM = TYPECR
            await app.edit_message_text(chat_id,message_id,"Select Your site",reply_markup = markup([[button("5 SIM",callback_data="GETHIT3_5sim"),button("SMS ACTIVE",callback_data="GETHIT3_sa")],[button("SMS MAN",callback_data="GETHIT3_sm"),button("SMS CODE",callback_data="GETHIT3_sc")],[button(f"🔙Back",callback_data="BACK")]]))
        elif "GETHIT3_" in data:
            SITE = data.replace("GETHIT3_","")
            await app.edit_message_text(chat_id,message_id,"In range or one country?",reply_markup = markup([[button("Select your range",callback_data="SELECTRANGE")],[button("One Country",callback_data="GETHIT4_one")],[button("Pre Code +2",callback_data="GETHIT4_precode")],[button(f"🔙Back",callback_data="BACK")]]))
        elif "SELECTRANGE" in data:
            STEPALL = "SELECTRANGE"
            await app.edit_message_text(chat_id,message_id,"Please send you range as min-max in Ruble",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
        elif "GETHIT4_" in data:
            if ALLAUTO:
                await app.edit_message_text(chat_id,message_id,"❌Is active...\nCancel it",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
                return
            LISTSM = []
            LISTSA = []
            LIST5S = []
            LIST5SC = []
            if SITE == "5sim":
                TOKEN = S5TOKEN
            elif SITE == "sa":
                TOKEN = SATOKEN
            elif SITE == "sm":
                TOKEN = SMTOKEN
            else:
                TOKEN = SCTOKEN
            SINGLE = data.replace("GETHIT4_","")
            if SINGLE != "one" and SINGLE != "precode" and db.get("MIN") and db.get("MAX"):
                MIN = db.get("MIN")
                MAX = db.get("MAX")
                if SITE == "sa":
                    ALLCONP = {}
                    try:
                        ALLCON = requests.get(f"https://api.sms-activate.org/stubs/handler_api.php?api_key={TOKEN}&action=getPrices&service=tg")
                        ALLCONP = ALLCON.json()
                        await asyncio.sleep(0.1)
                    except: pass
                    for COT in ALLCONP:
                        COUNT = ALLCONP[COT]["tg"]["count"]
                        COST = ALLCONP[COT]["tg"]["cost"]
                        if int(COUNT) > 0 and int(float(COST)) <= int(MAX) and int(float(COST)) >= int(MIN):
                            LISTSA.append(COT)
                    getl = len(LISTSA)
                    await app.edit_message_text(chat_id,message_id,f"📤Start with {getl} country?\n{MIN} < Ruble < {MAX}",reply_markup = markup([[button(f"✅Start",callback_data="BUY_RANGE")],[button(f"🔙Back",callback_data="BACK")]]))
                elif SITE == "sm":
                    ALLCONP = {}
                    try:
                        # ALLCON = requests.get(f"http://api.sms-man.com/stubs/handler_api.php?action=getPrices&api_key={TOKEN}&service=tg")
                        ALLCON = requests.get(f"http://api.sms-man.com/control/get-prices?token={TOKEN}")
                        ALLCONP = ALLCON.json()
                        await asyncio.sleep(0.1)
                    except: pass
                    for COT in ALLCONP:
                        # COUNT = ALLCONP[COT]["tg"]["count"]
                        # COST = ALLCONP[COT]["tg"]["cost"]
                        try:
                            if str(COT) != "8" and str(COT) != "7" and str(COT) != "1" and ALLCONP[COT]["3"]:
                                COUNT = ALLCONP[COT]["3"]["count"]
                                COST = ALLCONP[COT]["3"]["cost"]
                                if int(COUNT) > 0 and int(float(COST)) <= int(MAX) and int(float(COST)) >= int(MIN):
                                    LISTSM.append(COT)
                        except Exception as e: print(e)
                        except: pass
                    getl = len(LISTSM)
                    await app.edit_message_text(chat_id,message_id,f"📤Start with {getl} country?\n{MIN} < Ruble < {MAX} ",reply_markup = markup([[button(f"✅Start",callback_data="BUY_RANGE")],[button(f"🔙Back",callback_data="BACK")]]))
                elif SITE == "5sim":
                    try:
                        PRICES = requests.get("https://5sim.net/v1/guest/prices?product=telegram")
                        PRICES = PRICES.json()["telegram"]
                        for COUNTR in PRICES:
                            for OPRS in PRICES[COUNTR]:
                                COSTS = PRICES[COUNTR][OPRS]["cost"]
                                COUNT = PRICES[COUNTR][OPRS]["count"]
                                if int(float(COSTS)) >= int(MIN) and int(float(COSTS)) <= int(MAX) and int(COUNT) > 0: 
                                    try:
                                        LIST5S[COUNTR].append(OPRS)
                                    except:
                                        LIST5S[COUNTR] = []
                                        LIST5S[COUNTR].append(OPRS)
                                    if not str(COUNTR) in LIST5SC:
                                        LIST5SC.append(COUNTR)
                    except: pass
                    getl = len(LIST5S)
                    await app.edit_message_text(chat_id,message_id,f"📤Start with {getl} country?\n{MIN} < Ruble < {MAX}",reply_markup = markup([[button(f"✅Start",callback_data="BUY_RANGE")],[button(f"🔙Back",callback_data="BACK")]]))
                else:
                    await app.edit_message_text(chat_id,message_id,f"📤Start with 1 country?\n{MIN} < Ruble < {MAX}",reply_markup = markup([[button(f"✅Start",callback_data="BUY_RANGE")],[button(f"🔙Back",callback_data="BACK")]]))
            elif SINGLE == "precode":
                if SITE == "sm":
                    ALLCONP = {}
                    LCHECK = [137,153,190,194,196,197,121,200,122,203,102,177,105,109,212,148,214,219,110,118,227,145,96,236,237,297,101,240,146,245,246,117,157,251,255,103,265,139,317,167,113,320,315,313,176,166,152,15,173]
                    try:
                        ALLCON = requests.get(f"http://api.sms-man.com/control/get-prices?token={TOKEN}")
                        ALLCONP = ALLCON.json()
                        await asyncio.sleep(0.1)
                    except: pass
                    for COT in LCHECK:
                        try:
                            COT = str(COT)
                            COUNT = ALLCONP[COT]["3"]["count"]
                            COST = ALLCONP[COT]["3"]["cost"]
                            if int(COUNT) > 0 and int(float(COST)) < 14:
                                LISTSM.append(COT)
                        except: pass
                    getl = len(LISTSM)
                    await app.edit_message_text(chat_id,message_id,f"📤Start with {getl} country?\nUnder {SINGLE} Ruble",reply_markup = markup([[button(f"✅Start",callback_data="BUY_RANGE")],[button(f"🔙Back",callback_data="BACK")]]))
                else:
                     await app.edit_message_text(chat_id,message_id,"❌No available for other sites")
            else:
                TYPECR = PLATFORM
                LISTBUT = []
                RAWBUT = []
                await app.edit_message_text(chat_id,message_id,"Try to get number...")
                try:
                    if SITE == "sa":
                        Brazil = {"73":{"tg":{"cost":0,"count":0}}}
                        Algeria = {"58":{"tg":{"cost":0,"count":0}}}
                        Argentina = {"39":{"tg":{"cost":0,"count":0}}}
                        Philippines = {"4":{"tg":{"cost":0,"count":0}}}
                        Indonesia = {"6":{"tg":{"cost":0,"count":0}}}
                        Pakistan = {"66":{"tg":{"cost":0,"count":0}}}
                        Vietnam = {"10":{"tg":{"cost":0,"count":0}}}
                        Pakistan = {"66":{"tg":{"cost":0,"count":0}}}
                        ALLCONP = ""
                        try:
                            ALLCON = requests.get(f"https://api.sms-activate.org/stubs/handler_api.php?api_key={TOKEN}&action=getPrices&service=tg")
                            ALLCONP = ALLCON.json()
                            await asyncio.sleep(0.1)
                        except: pass
                        BrazilP = ALLCONP["73"]["tg"]["cost"]
                        BrazilC = ALLCONP["73"]["tg"]["count"]
                        AlgeriaP = ALLCONP["58"]["tg"]["cost"]
                        AlgeriaC = ALLCONP["58"]["tg"]["count"]
                        ArgentinaP = ALLCONP["39"]["tg"]["cost"]
                        ArgentinaC = ALLCONP["39"]["tg"]["count"]
                        PhilippinesP = ALLCONP["4"]["tg"]["cost"]
                        PhilippinesC = ALLCONP["4"]["tg"]["count"]
                        IndonesiaP = ALLCONP["6"]["tg"]["cost"]
                        IndonesiaC = ALLCONP["6"]["tg"]["count"]
                        PakistanP = ALLCONP["66"]["tg"]["cost"]
                        PakistanC = ALLCONP["66"]["tg"]["count"]
                        VietnamP = ALLCONP["10"]["tg"]["cost"]
                        VietnamC = ALLCONP["10"]["tg"]["count"]
                        PapuaP = ALLCONP["79"]["tg"]["cost"]
                        PapuaC = ALLCONP["79"]["tg"]["count"]
                        LISTBUT = [[button(f"🇧🇷Brazil-{BrazilP}-{BrazilC}",callback_data=f"BUY_73"),button(f"🇩🇿Algeria-{AlgeriaP}-{AlgeriaC}",callback_data=f"BUY_58")],
                        #[button(f"🇦🇷Argentina-{ArgentinaP}-{ArgentinaC}",callback_data=f"BUY_39"),
                        [button(f"🇵🇭Philippines-{PhilippinesP}-{PhilippinesC}",callback_data=f"BUY_4")],
                        [button(f"🇮🇩Indonesia-{IndonesiaP}-{IndonesiaC}",callback_data=f"BUY_6"),button(f"🇵🇰Pakistan-{PakistanP}-{PakistanC}",callback_data=f"BUY_66")],
                        [button(f"🇻🇳Vietnam-{VietnamP}-{VietnamC}",callback_data=f"BUY_10"),button(f"🇵🇬Papua-{PapuaP}-{PapuaC}",callback_data=f"BUY_79")],
                        [button(f"🔙Back",callback_data="BACK")]
                        ]
                        await app.edit_message_text(chat_id,message_id,"Please select your country\nFormat: NAME-PRICE-COUNT",reply_markup = markup(LISTBUT))
                    elif SITE == "sm":
                        # Mozambique = {"157":{"tg":{"cost":0,"count":0}}}
                        # Kenya = {"96":{"tg":{"cost":0,"count":0}}}
                        # Nigeria = {"103":{"tg":{"cost":0,"count":0}}}
                        # Algeria = {"137":{"tg":{"cost":0,"count":0}}}
                        # Senegal = {"139":{"tg":{"cost":0,"count":0}}}
                        # Ethiopia = {"148":{"tg":{"cost":0,"count":0}}}
                        # SouthAfrica = {"113":{"tg":{"cost":0,"count":0}}}
                        # Morocco = {"117":{"tg":{"cost":0,"count":0}}}
                        # Zimbabwe = {"173":{"tg":{"cost":0,"count":0}}}
                        # Madagascar = {"101":{"tg":{"cost":0,"count":0}}}
                        # ALLCONP = ""
                        # try:
                            # ALLCON = requests.get(f"http://api.sms-man.com/stubs/handler_api.php?action=getPrices&api_key={TOKEN}&service=tg")
                            # ALLCONP = ALLCON.json()
                            # await asyncio.sleep(0.1)
                        # except: pass
                        # MozambiqueP = ALLCONP["157"]["tg"]["cost"]
                        # MozambiqueC = ALLCONP["157"]["tg"]["count"]
                        # KenyaP = ALLCONP["96"]["tg"]["cost"]
                        # KenyaC = ALLCONP["96"]["tg"]["count"]
                        # NigeriaP = ALLCONP["103"]["tg"]["cost"]
                        # NigeriaC = ALLCONP["103"]["tg"]["count"]
                        # AlgeriaP = ALLCONP["137"]["tg"]["cost"]
                        # AlgeriaC = ALLCONP["137"]["tg"]["count"]
                        # SenegalP = ALLCONP["139"]["tg"]["cost"]
                        # SenegalC = ALLCONP["139"]["tg"]["count"]
                        # EthiopiaP = ALLCONP["148"]["tg"]["cost"]
                        # EthiopiaC = ALLCONP["148"]["tg"]["count"]
                        # SouthAfricaP = ALLCONP["113"]["tg"]["cost"]
                        # SouthAfricaC = ALLCONP["113"]["tg"]["count"]
                        # MoroccoP = ALLCONP["117"]["tg"]["cost"]
                        # MoroccoC = ALLCONP["117"]["tg"]["count"]
                        # ZimbabweP = ALLCONP["173"]["tg"]["cost"]
                        # ZimbabweC = ALLCONP["173"]["tg"]["count"]
                        # MadagascarP = ALLCONP["101"]["tg"]["cost"]
                        # MadagascarC = ALLCONP["101"]["tg"]["count"]
                        # LISTBUT = [[button(f"🇲🇿Mozambique-{MozambiqueP}-{MozambiqueC}",callback_data=f"BUY_80"),button(f"🇰🇪Kenya-{KenyaP}-{KenyaC}",callback_data=f"BUY_8")],
                        # [button(f"🇳🇬Nigeria-{NigeriaP}-{NigeriaC}",callback_data=f"BUY_19"),button(f"🇩🇿Algeria-{AlgeriaP}-{AlgeriaC}",callback_data=f"BUY_58")],
                        # [button(f"🇸🇳Senegal-{SenegalP}-{SenegalC}",callback_data=f"BUY_61"),button(f"🇪🇹Ethiopia-{EthiopiaP}-{EthiopiaC}",callback_data=f"BUY_71")],
                        # [button(f"🇿🇼Zimbabwe-{ZimbabweP}-{ZimbabweC}",callback_data=f"BUY_96"),button(f"🇵🇬Morocco-{MoroccoP}-{MoroccoC}",callback_data=f"BUY_37")],
                        # [button(f"🇿🇦SouthAfrica-{SouthAfricaP}-{SouthAfricaC}",callback_data=f"BUY_31"),button(f"🇲🇬Madagascar-{MadagascarP}-{MadagascarC}",callback_data=f"BUY_37")],
                        # [button(f"🔙Back",callback_data="BACK")]
                        # ]
                        # await app.edit_message_text(chat_id,message_id,"Please select your country\nFormat: NAME-PRICE-COUNT",reply_markup = markup(LISTBUT))
                        
                        try:
                            PRICES = requests.get(f"http://api.sms-man.com/control/get-prices?token={TOKEN}")
                            PRICES = PRICES.json()
                            INTWO = []
                            COUNTS = requests.get(f"http://api.sms-man.com/control/countries?token={TOKEN}")
                            COUNTS = COUNTS.json()
                            for COUNTR in PRICES:
                                try:
                                    if PRICES[COUNTR]["3"]:
                                        COSTS = PRICES[COUNTR]["3"]["cost"]
                                        COUNT = PRICES[COUNTR]["3"]["count"]
                                        if int(float(COSTS)) < 15 and int(COUNT) > 0: 
                                            if len(INTWO) == 2:
                                                RAWBUT.append(INTWO)
                                                INTWO = []
                                                COUNTRS = COUNTS[COUNTR]["title"]
                                                INTWO.append(button(f"🇺🇳{COUNTRS}-{COSTS}-{COUNT}",callback_data=f"BUY_{COUNTR}"))
                                            else:
                                                COUNTRS = COUNTS[COUNTR]["title"]
                                                INTWO.append(button(f"🇺🇳{COUNTRS}-{COSTS}-{COUNT}",callback_data=f"BUY_{COUNTR}"))
                                except Exception as e: print(e)
                                except: pass
                            if len(INTWO) > 0: 
                                RAWBUT.append(INTWO)
                                INTWO = []
                            try:
                                COSTS = PRICES["136"]["3"]["cost"]
                                COUNT = PRICES["136"]["3"]["count"]
                                RAWBUT.append([button(f"🇮🇷Iran-{COSTS}-{COUNT}",callback_data=f"BUY_136")])
                            except Exception as e: print(e)
                            except: pass
                            RAWBUT.append([button(f"🔙Back",callback_data=f"BACK")])
                        except Exception as e: print(e)
                        except: print("Except")
                        await app.edit_message_text(chat_id,message_id,"Please select your country\nFormat: NAME-PRICE-COUNT",reply_markup = markup(RAWBUT))
                    elif SITE == "5sim":
                        try:
                            PRICES = requests.get("https://5sim.net/v1/guest/prices?product=telegram")
                            PRICES = PRICES.json()["telegram"]
                            INTWO = []
                            for COUNTR in PRICES:
                                for OPRS in PRICES[COUNTR]:
                                    COSTS = PRICES[COUNTR][OPRS]["cost"]
                                    COUNT = PRICES[COUNTR][OPRS]["count"]
                                    if int(float(COSTS)) < 16 and int(COUNT) > 0: 
                                        if len(INTWO) == 2:
                                            RAWBUT.append(INTWO)
                                            INTWO = []
                                            INTWO.append(button(f"🇺🇳{COSTS}-{COUNT}-{OPRS}-{COUNTR}",callback_data=f"BUY_{COUNTR}:{OPRS}"))
                                        else:
                                            INTWO.append(button(f"🇺🇳{COSTS}-{COUNT}-{OPRS}-{COUNTR}",callback_data=f"BUY_{COUNTR}:{OPRS}"))
                                            # RAWBUT.append([button(f"🇺🇳{COSTS}-{COUNT}-{OPRS}-{COUNTR}",callback_data=f"BUY_{COUNTR}:{OPRS}")])
                            if len(INTWO) > 0: 
                                RAWBUT.append(INTWO)
                                INTWO = []
                            RAWBUT.append([button(f"🔙Back",callback_data=f"BACK")])
                        except Exception as e: print(e)
                        except: print("Except")
                        await app.edit_message_text(chat_id,message_id,"Please select your country\nFormat: PRICE-COUNT-OPR-NAME",reply_markup = markup(RAWBUT))
                    else:
                        try:
                            PRICES = requests.get(f"https://sms-code.store/stubs/handler_api.php?api_key={TOKEN}&action=getNumbersStatus")
                            PRICES = str(PRICES.json()["tg_0"])
                            print(PRICES)
                            LISTBUT = [[button(f"🇺🇳USA|CANADA-{PRICES}",callback_data=f"BUY_all")],[button(f"🔙Back",callback_data=f"BACK")]]
                            await app.edit_message_text(chat_id,message_id,"Please select your country\nFormat: NAME-COUNT",reply_markup = markup(LISTBUT))
                        except Exception as e: print(e)
                        except: pass
                except Exception as e: print(e)
                except:
                    await app.edit_message_text(chat_id,message_id,"❌Have problem to get data",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
        # elif "receive_" in str(data):
            # try:
                # PHONE = str(data).replace("receive_","")
                # ALLLISTGET[str(chat_id)] = True
                # _thread = threading.Thread(target=Between_Get, args=[PHONE,chat_id,message_id]).start()
                # await app.edit_message_text(chat_id,message_id,f"♻️Ready for getting code\nEnter phone number +{PHONE} in your telegram to get your code and after that click on GET CODE button",reply_markup = markup([[button("♻️Receive Code",callback_data=f"receive_{PHONE}")]]))
            # except:
                # await app.edit_message_text(chat_id,message_id,f"❌There is a problem to get code for phone number +{PHONE}\n Try after a while",reply_markup = markup([[button("♻️Receive Code",callback_data=f"receive_{PHONE}")]]))
        elif "BUY_" in str(data):
            for XN in db.smembers("SERI"):
                db.srem("SERI",XN)
            for XN in db.smembers("PHOTOS"):
                db.srem("PHOTOS",XN)
            for XN in db.smembers("NAMES"):
                db.srem("NAMES",XN)
            for XN in db.smembers("SERI" + str(TITLE)):
                db.sadd("SERI",XN)
            for XN in db.smembers("PHOTOS" + str(TITLE)):
                db.sadd("PHOTOS",XN)
            for XN in db.smembers("NAMES" + str(TITLE)):
                db.sadd("NAMES",XN)
            for XNX in db.smembers("LISTTHE"):
                db.srem("LISTTHE",XNX)
                os.system(f"screen -S PHONE-{XNX} -X kill")
            COUNTBUY = COUNTCODE#
            GDATA = str(data).replace("BUY_","")
            ACTIVEOP = "any"
            if GDATA != "RANGE":
                if SITE == "sm":
                    ACTIVEOP = "any"
                    COUNTBUY = GDATA
                elif SITE == "sa":
                    ACTIVEOP = "any"
                    COUNTBUY = GDATA
                elif SITE == "5sim":
                    GDATA = GDATA.split(":")
                    ACTIVEOP = GDATA[1]
                    COUNTBUY = GDATA[0]
                else:
                    ACTIVEOP = "any"
                    COUNTBUY = "12"
            ALLAUTO = True
            await app.edit_message_text(chat_id,message_id,f"♻️Creating Loop started!",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
            THELASTOP = 0
            MAXLOOP = 5
            if db.get("MAXLOOP"):
                MAXLOOP = int(db.get("MAXLOOP"))
            ISNONUM = False
            TLISX = 0
            while True:
                if ALLAUTO == False:
                    break
                if db.scard("CREATED") > 0:
                    try:
                        for XC in db.smembers("CREATED"):
                            db.srem("CREATED",XC)
                            XC = XC.split(":")
                            PHONEC1 = XC[0]
                            TYPEC1 = XC[1]
                            CODEC1 = XC[2]
                            await app.send_message(chat_id,f"✅One number created!\nPhone: {PHONEC1}\nCode: {CODEC1}\nPlatform: {TYPEC1}")
                    except: pass
                if db.scard("BANNED") > 0:
                    try:
                        for XC in db.smembers("BANNED"):
                            db.srem("BANNED",XC)
                            await app.send_message(chat_id,f"❌One number is ban\nPhone: {XC}")
                    except: pass
                if db.scard("AFTERTIME") > 0:
                    try:
                        for XC in db.smembers("AFTERTIME"):
                            db.srem("AFTERTIME",XC)
                            await app.send_message(chat_id,f"⚠️One number is timeout\nPhone: {XC}")
                    except: pass
                LISTTHEX = db.scard("LISTTHE")
                if LISTTHEX > 0:
                    for XLT in db.smembers("LISTTHE"):
                        if db.get(f"THE{XLT}"):
                            XLTS = db.get(f"THE{XLT}")
                            XLTS = XLTS.split(":")
                            TIMS = int(XLTS[0])
                            if TIMS < int(float(time.time())):
                                IDMS = XLTS[1]
                                SITS = XLTS[2]
                                PHNS = XLTS[3]
                                if SITS == "5sim":
                                    headers = {'Authorization': 'Bearer ' + S5TOKEN,'Accept': 'application/json',}
                                    DELETE = requests.get(f"https://5sim.net/v1/user/ban/{IDMS}", headers=headers)
                                elif SITS == "sa":
                                    DELETE = requests.get(f"https://sms-activate.ru/stubs/handler_api.php?api_key={SATOKEN}&action=setStatus&status=8&id={IDMS}")
                                elif SITS == "sm":
                                    DELETE = requests.get(f"https://api.sms-man.com/control/set-status?token={SMTOKEN}&request_id={IDMS}&status=reject")
                                else:
                                    DELETE = requests.get(f"https://sms-code.store/stubs/handler_api.php?api_key={SCTOKEN}&action=setStatus&status=8&id={IDMS}")
                                db.srem("LISTTHE",XLT)
                                os.system(f"screen -S PHONE-{XLT} -X kill")
                                db.delete(f"THE{XLT}")
                                await app.send_message(chat_id,f"⚠️One number is timeout\nPhone: {PHNS}")
                if LISTTHEX < MAXLOOP:
                    if GDATA == "RANGE":
                        if SITE == "sm":
                            ACTIVEOP = "any"
                            if db.scard("LISTSM") == 0:
                                for CB in LISTSM:
                                    db.sadd("LISTSM",CB)
                            COUNTBUY = db.srandmember("LISTSM")
                            db.srem("LISTSM",COUNTBUY)
                            # XT = 0
                            # for CB in LISTSM:
                                # XT += 1
                                # if TLISX >= len(LISTSM) - 1:
                                    # TLISX = 0
                                # if XT >= TLISX:
                                    # TLISX = XT
                                    # COUNTBUY = CB
                                    # break
                            # COUNTBUY = random.choice(LISTSM)
                        elif SITE == "sa":
                            ACTIVEOP = "any"
                            if db.scard("LISTSA") == 0:
                                for CB in LISTSA:
                                    db.sadd("LISTSA",CB)
                            COUNTBUY = db.srandmember("LISTSA")
                            db.srem("LISTSA",COUNTBUY)
                            # COUNTBUY = random.choice(LISTSA)
                            # XT = 0
                            # for CB in LISTSA:
                                # XT += 1
                                # if TLISX >= len(LISTSA) - 1:
                                    # TLISX = 0
                                # if XT >= TLISX:
                                    # TLISX = XT
                                    # COUNTBUY = CB
                                    # break
                        elif SITE == "5sim":
                            if db.scard("LIST5S") == 0:
                                for CB in list(LIST5SC):
                                    db.sadd("LIST5S",CB)
                            COUNTBUY = db.srandmember("LIST5S")
                            db.srem("LIST5S",COUNTBUY)
                            # COUNTBUY = random.choice(list(LIST5S))
                            # XT = 0
                            # for CB in list(LIST5S):
                                # XT += 1
                                # if TLISX >= len(list(LIST5S)) - 1:
                                    # TLISX = 0
                                # if XT >= TLISX:
                                    # TLISX = XT
                                    # COUNTBUY = CB
                                    # break
                            ACTIVEOP = random.choice(LIST5S[COUNTBUY])
                        else:
                            ACTIVEOP = "any"
                            COUNTBUY = "12"
                    try:
                        BUYSC = ""
                        if SITE != "5sim":
                            if SITE == "sa":
                                BUYS = requests.get(f"https://api.sms-activate.org/stubs/handler_api.php?api_key={TOKEN}&action=getNumber&service=tg&country={COUNTBUY}")
                                BUYSC = str(BUYS.content)
                            elif SITE == "sc":
                                BUYS = requests.get(f"https://sms-code.store/stubs/handler_api.php?api_key={TOKEN}&action=getNumber&service=tg&country={COUNTBUY}")
                                BUYSC = str(BUYS.content)
                            elif SITE == "sm":
                                BUYS = requests.get(f"https://api.sms-man.com/control/get-number?token={TOKEN}&country_id={COUNTBUY}&application_id=3")
                                # BUYS = requests.get(f"http://api.sms-man.com/stubs/handler_api.php?api_key={TOKEN}&action=getNumber&service=tg&country={COUNTBUY}")
                                # BUYSC = str(BUYS.content)
                                BUYSC = ""
                                try:
                                    BUYSC = BUYS.json()
                                    # print(BUYSC)
                                    if BUYSC["number"]:
                                        BUYSC = "ACCESS_NUMBER:" + str(BUYSC["request_id"]) + ":" + str(BUYSC["number"])
                                    else:
                                        BUYSC = "NO_NUMBERS"
                                except Exception as e:
                                    print(e)
                                    BUYSC = "NO_NUMBERS"
                                except:
                                    print("Except")
                                    BUYSC = "NO_NUMBERS"
                            # print(BUYSC)
                            if "ACCESS_NUMBER" in BUYSC:
                                DATAS = BUYSC.split(":")
                                ID = DATAS[1]
                                PHONE = DATAS[2]
                                PHONE = PHONE.replace("'","").replace("+","")
                                await app.edit_message_text(chat_id,message_id,f"♻️Looping!\n♻️Checking: {PHONE}\n🏛Country: {COUNTBUY}")#,reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
                                print(PHONE)
                                BANNED[PHONE] = False
                                CHPHO = "+" + str(PHONE)
                                for PHO in db.smembers("BANS"):
                                    if str(PHO) in CHPHO:
                                        BANNED[PHONE] = True
                                if BANNED[PHONE] == True:
                                    await app.send_message(chat_id,f"⚠️One number is forbidden pre code\nPhone: {XC}")
                                    if SITE == "sa":
                                        DELETE = requests.get(f"https://sms-activate.ru/stubs/handler_api.php?api_key={SATOKEN}&action=setStatus&status=8&id={ID}")
                                    elif SITE == "sm":
                                        DELETE = requests.get(f"https://api.sms-man.com/control/set-status?token={SMTOKEN}&request_id={ID}&status=reject")
                                    else:
                                        DELETE = requests.get(f"https://sms-code.store/stubs/handler_api.php?api_key={SCTOKEN}&action=setStatus&status=8&id={ID}")
                                else:
                                    if "no such column: number" in str(PHONE):
                                        ISNONUM = True
                                        try:
                                            print("FUCK IT\nNo number")
                                            await app.edit_message_text(chat_id,message_id,f"♻️Looping!\n❌No number!\n🏛Country: {COUNTBUY}")
                                        except: pass
                                    else:
                                        if GLOBTHE > 50:
                                            GLOBTHE = 0
                                        GLOBTHE = GLOBTHE + 1
                                        await app.send_message(chat_id,f"♻️Start thread {GLOBTHE}:\nPhone: {PHONE}\nPlatform: {TYPECR}")
                                        db.set(f"THE{GLOBTHE}",str(int(float(time.time())) + 200) + ":" + str(ID) + ":" + str(SITE) + ":" + str(PHONE))
                                        # print(f"screen -d -m -S PHONE-{GLOBTHE} python3.8 create.py {TYPECR} {PHONE} {ID} {ACTIVEOP} {chat_id} {GLOBTHE} {api_id} {api_hash} {SITE}")
                                        os.system(f"screen -d -m -S PHONE-{GLOBTHE} python3.8 create.py {TYPECR} {PHONE} {ID} {ACTIVEOP} {chat_id} {GLOBTHE} {api_id} {api_hash} {SITE}")
                            elif "NO_BALANCE" in BUYSC:
                                ISNONUM = True
                                try:
                                    await app.edit_message_text(chat_id,message_id,f"♻️Looping!\n❌No balance!\n🏛Country: {COUNTBUY}")
                                except: pass
                            elif "NO_NUMBERS" in BUYSC:
                                ISNONUM = True
                                try:
                                    await app.edit_message_text(chat_id,message_id,f"♻️Looping!\n❌No number!\n🏛Country: {COUNTBUY}")
                                except: pass
                            else:
                                ISNONUM = True
                                # print(BUYSC)
                                try:
                                    await app.edit_message_text(chat_id,message_id,f"♻️Looping!\n❌Error!\n🏛Country: {COUNTBUY}")
                                except: pass
                        else:
                            headers = {'Authorization': 'Bearer ' + TOKEN,'Accept': 'application/json',}
                            BUYS = requests.get(f"https://5sim.net/v1/user/buy/activation/{COUNTBUY}/{ACTIVEOP}/telegram", headers=headers)
                            BUYSC = BUYS.json()
                            # print(BUYS.content)
                            if BUYSC["status"] == "PENDING" or BUYSC["status"] == "RECEIVED":
                                ID = BUYSC["id"]
                                PHONE = str(BUYSC["phone"]).replace("+","")
                                BANNED = False
                                CHPHO = "+" + str(PHONE)
                                for PHO in db.smembers("BANS"):
                                    if str(PHO) in CHPHO:
                                        BANNED = True
                                if BANNED == True:
                                    headers = {'Authorization': 'Bearer ' + S5TOKEN,'Accept': 'application/json',}
                                    DELETE = requests.get(f"https://5sim.net/v1/user/ban/{ID}", headers=headers)
                                else:
                                    await app.edit_message_text(chat_id,message_id,f"♻️Looping!\n♻️Checking: {PHONE}\n🪄Operator: {ACTIVEOP}\n🏛Country: {COUNTBUY}")#,reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
                                    print(PHONE)
                                    if "no such column: number" in str(PHONE):
                                        print("FUCK IT\nNo number")
                                        ISNONUM = True
                                    else:
                                        if GLOBTHE > 50:
                                            GLOBTHE = 0
                                        GLOBTHE = GLOBTHE + 1
                                        await app.send_message(chat_id,f"♻️Start thread {GLOBTHE}:\nPhone: {PHONE}\nPlatform: {TYPECR}\n🏛Country: {COUNTBUY}")
                                        db.set(f"THE{GLOBTHE}",str(int(float(time.time())) + 200) + ":" + str(ID) + ":" + str(SITE) + ":" + str(PHONE))
                                        # print(f"screen -d -m -S PHONE-{GLOBTHE} python3.8 create.py {TYPECR} {PHONE} {ID} {ACTIVEOP} {chat_id} {GLOBTHE} {api_id} {api_hash} {SITE}")
                                        os.system(f"screen -d -m -S PHONE-{GLOBTHE} python3.8 create.py {TYPECR} {PHONE} {ID} {ACTIVEOP} {chat_id} {GLOBTHE} {api_id} {api_hash} {SITE}")
                            else:
                                ISNONUM = True
                                # print(BUYS.content)
                    except Exception as e:
                        print(type(e).__name__,e,e.__traceback__.tb_lineno)
                        try:
                            await app.edit_message_text(chat_id,message_id,f"❌No number\n🏛Country: {COUNTBUY}",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
                        except: pass
                    except:
                        try:
                            await app.edit_message_text(chat_id,message_id,f"❌No number\n🏛Country: {COUNTBUY}",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
                        except: pass
                else:
                    await asyncio.sleep(5)
                if ISNONUM == True:
                    ISNONUM = False
                    await asyncio.sleep(2)
                else:
                    await asyncio.sleep(5)
        elif "CANCEL_" in str(data):
            try:
                ID = str(data).replace("CANCEL_","")
                PHONE = GLOBALD[ID]["phone"]
                client = SESSIONS[PHONE]
                CANCEL = requests.get(f"https://sms-activate.ru/stubs/handler_api.php?api_key={TOKEN}&action=setStatus&status=8&id={ID}")
                del GLOBALD[ID]
                await app.edit_message_text(chat_id,message_id,f"❌Number Canceled\n\nPhone: +{PHONE}\nID: {ID}",reply_markup = markup([[button(f"📤Go to buy list",callback_data="GETHIT")],[button(f"🔙Back",callback_data="BACK")]]))
                try:
                    await client.disconnect()
                except: pass
                try:
                    await client.stop()
                except: pass
                TOR = GLOBALD[ID]["tor"]
                TOR.kill()
            except:
                await app.edit_message_text(chat_id,message_id,"❌Have problem to get data",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
        elif "SHOWUSER" in str(data):
            STEPALL = "SHOWUSER"
            await app.edit_message_text(chat_id,message_id,"Send user ID",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
        elif "SESSGET" in str(data):
            STEPALL = "SESSGET"
            GSESSV = db.scard("RECIVER")
            await app.edit_message_text(chat_id,message_id,f"How many of {GSESSV} telethon session do you want?",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
        elif "ZEROUSER_" in str(data):
            ID = str(data).replace("ZEROUSER_","")
            for xds in db.smembers(f"RCV{ID}"):
                db.srem(f"RCV{ID}",xds)
            await app.edit_message_text(chat_id,message_id,"User numbers set as zero",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
    elif "BACKADD" in data:
        await app.edit_message_text(chat_id,message_id,"📞سلام دوست گرامی\n\nبه پنل افزودن شماره خوش آمدید",reply_markup = markup([[button("📞افزودن شماره جدید",callback_data="ADDNUMBER"),button("📊مشاهده لیست شما",callback_data="SHOWNUMBER")]]))
    elif "SHOWNUMBER" in data:
        NUMS = db.scard(f"RCV{chat_id}")
        NUML = ""
        for XMM in db.smembers(f"RCV{chat_id}"):
            NUML = f"{NUML}+{XMM}\n"
        await app.edit_message_text(chat_id,message_id,f"📊آمار شما:\n\n تعداد شماره ها: {NUMS}\nایدی عددی شما: {chat_id}\n\nلیست شماره ها:\n{NUML}",reply_markup = markup([[button(f"🪄تسویه حساب",callback_data="CHECKOUT")],[button(f"🔙برگشت",callback_data="BACKADD")]]))
    elif "CHECKOUT" in data:
        NUMS = db.scard(f"RCV{chat_id}")
        if NUMS > 0:
            await app.edit_message_text(chat_id,message_id,f"🪄درخواست تسویه حساب ارسال شد",reply_markup = markup([[button(f"🔙برگشت",callback_data="BACKADD")]]))
            for SUDO in list_b:
                try:
                    await app.send_message(SUDO,f"🪄Checkout for user\n\nID: {chat_id}\nNumbers: {NUMS}",reply_markup = markup([[button(f"🪄Checkout and zero",callback_data=f"ZEROUSER_{chat_id}")]]))
                except: pass
        else:
            await app.edit_message_text(chat_id,message_id,f"🪄موجودی شما کافی نمیباشد",reply_markup = markup([[button(f"🔙برگشت",callback_data="BACKADD")]]))
    elif "ADDNUMBER" in data:
        STEPALLADD[chat_id] = "ADDNUMBER"
        await app.edit_message_text(chat_id,message_id,"☎️لطفا شماره خود همراه با پیش شماره ارسال کنید",reply_markup = markup([[button(f"🔙برگشت",callback_data="BACKADD")]]))
    elif "CHECKACC_" in data:
        await app.edit_message_text(chat_id,message_id,f"♻️لطفا کمی صبرکنید")
        data = data.replace("CHECKACC_","")
        api_id, api_hash = 16623,"8c9dbfe58437d1739540f5d53c72ae4b"
        if db.get("AAPIID") and db.get("AAPIHASH"):
            api_id = int(db.get("AAPIID"))
            api_hash = db.get("AAPIHASH")
        os.system(f"screen -d -m -S PHONE-{GLOBTHE} python3.8 create.py CHK {data} 0 no {chat_id} 0 {api_id} {api_hash} no")
        while True:
            if db.scard(f"CHECK{chat_id}") > 0:
                CHECK = db.srandmember(f"CHECK{chat_id}")
                db.srem(f"CHECK{chat_id}",CHECK)
                if "NO" in CHECK:
                    PHONE = CHECK.replace("NO","")
                    STEPALLADD[chat_id] = "none"
                    try:
                        await app.edit_message_text(chat_id,message_id,f"❌لطفا نشست های {PHONE} را خاتمه داده سپس اقدام به تایید اکانت کنید",reply_markup = markup([[button("♻️بررسی اکانت",callback_data=f"CHECKACC_{PHONE}")]]))
                    except: pass
                    break
                elif "BAN" in CHECK:
                    PHONE = CHECK.replace("BAN","")
                    STEPALLADD[chat_id] = "none"
                    db.srem(f"RECIVER",PHONE)
                    await app.edit_message_text(chat_id,message_id,f"❌شماره {PHONE} بن میباشد")
                    break
                elif "OK" in CHECK:
                    PHONE = CHECK.replace("OK","")
                    STEPALLADD[chat_id] = "none"
                    db.sadd(f"RCV{chat_id}",PHONE)
                    await app.edit_message_text(chat_id,message_id,f"✅اکانت با شماره {PHONE} با موفقیت به لیست شما اضافه شد")
                    break
            await asyncio.sleep(1)
    elif "GRNUM_" in data:
        pcode = data.replace("GRNUM_","")
        if db.sismember("BUSER",str(chat_id)) and db.get(str(chat_id)) and db.scard("PHONESALL") > 0:
            if int(db.get(str(chat_id))) == 0:
                db.srem("BUSER",str(chat_id))
                await app.edit_message_text(chat_id,message_id,"⚠️Your capacity is over",reply_markup = markup([[button(f"🔙Back",callback_data="BOOK")]]))
                return 
            try:
                if ALLLISTGET[str(chat_id)] and ALLLISTGET[str(chat_id)] == True:
                    await app.edit_message_text(chat_id,message_id,"⚠️You have an number in waiting...",reply_markup = markup([[button(f"🔙Back",callback_data="BOOK")]]))
                    return 
            except: pass
            try:
                GETPLAT = db.get(str(chat_id) + "T")
                if not GETPLAT:
                    GETPLAT = "PYRO"
                PHONE = ""
                for XPH in db.srandmember("PHONESALL", 100):
                    PCO = "+" + str(XPH)
                    if pcode == "PreCode" and "+2" in PCO:
                        if GETPLAT == "THON" and db.get(XPH):
                            PHONE = XPH
                        elif GETPLAT == "PYRO" and not db.get(XPH):   
                            PHONE = XPH
                        break
                    else:
                        if GETPLAT == "THON" and db.get(XPH):
                            PHONE = XPH
                        elif GETPLAT == "PYRO" and not db.get(XPH):   
                            PHONE = XPH
                        break
                if PHONE == "":
                    await app.edit_message_text(chat_id,message_id,f"❌Sorry\nNo number available!",reply_markup = markup([[button(f"🔙Back",callback_data="BOOK")]]))
                else:
                    LOGOUTLIST[PHONE] = ""
                    GETCODESS[PHONE] = False
                    TEXTS[PHONE] = {}
                    TEXTS[PHONE]["temp"] = ""
                    TEXTS[PHONE]["gen"] = ""
                    # db.srem("PHONESALL",PHONE)
                    # _thread = threading.Thread(target=Between_Get, args=[PHONE,chat_id,message_id]).start()
                    await app.edit_message_text(chat_id,message_id,f"♻️Ready for getting code\n☎️Number: +{PHONE}\n\nEnter phone number in your telegram to get your code then click on GET CODE button",reply_markup = markup([[button("📥GET CODE",callback_data=f"GETCODESR_{PHONE}")]]))
            except Exception as e:
                print(type(e).__name__,e,e.__traceback__.tb_lineno)
                await app.edit_message_text(chat_id,message_id,f"❌There is a problem\n Try after a while",reply_markup = markup([[button("♻️Try again",callback_data=f"BOOK")]]))
            except:
                await app.edit_message_text(chat_id,message_id,f"❌There is a problem\n Try after a while",reply_markup = markup([[button("♻️Try again",callback_data=f"BOOK")]]))
        else:
            await app.edit_message_text(chat_id,message_id,"⚠️Something going wrong")
    elif "GETCODESR_" in data:
        ALLLISTGET[str(chat_id)] = True
        PHONE = data.replace("GETCODESR_","")
        db.srem("PHONESALL",PHONE)
        STHE[chat_id] = False
        if STHE[chat_id] == False:
            STHE[chat_id] = True
            LOGOUTLIST[PHONE] = "none"
            _thread = threading.Thread(target=Between_Get, args=[PHONE,chat_id,message_id]).start()
        await app.edit_message_text(chat_id,message_id,f"♻️Ready for getting code\n☎️Number: +{PHONE}")
    elif db.sismember("BUSER",str(chat_id)) and data == "BOOK":
        NO = await app.send_message(chat_id,"✋🏻Hi Customer\nSelect your action",reply_to_message_id = message_id,reply_markup = markup([[button("2️⃣Get With +2 Precode",callback_data="GRNUM_PreCode"),button("📤Get Random Number",callback_data="GRNUM_Random")]]))
    elif "LOGOUT_" in data:
        LG = data.replace("LOGOUT_","")
        LOGOUTLIST[LG] = "logout"
        # await app.edit_message_text(chat_id,message_id,f"✅Logout form +{LG}")
        # return
    elif "NOOUT_" in data:
        LG = data.replace("NOOUT_","")
        LOGOUTLIST[LG] = "noout"
        # await app.edit_message_text(chat_id,message_id,f"✅No Logout form +{LG}")
        # return
    else:
        await app.edit_message_text(chat_id,message_id,"You can not use this robot")
        
@app.on_message(filters.photo, group=2)
async def get_file(cli, message):
    global STEPALL
    global GLOBALID
    global TITLE
    global SERIIDS
    global SERISTART
    global STEPALLADD
    chat_id = message.chat.id 
    try:
        if STEPALLADD[chat_id]:
            pass
    except:
        STEPALLADD[chat_id] = "none"
    if STEPALL == "PHOTOADD" and GLOBALID == chat_id:
        file_dir = await app.download_media(message) 
        # db.sadd("PHOTOS",str(file_dir))
        db.sadd("PHOTOS" + str(TITLE),str(file_dir))
        await app.send_message(chat_id,f"Photo with local address {file_dir} added to list\nAny photo? send it",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
    elif STEPALL == "SERIADD" and GLOBALID == chat_id:
        file_dir = await app.download_media(message) 
        # if not db.sismember("SERI",str(SERIIDS)):
            # db.sadd("SERI",str(SERIIDS))
        if not db.sismember("SERI" + str(TITLE),str(SERIIDS)):
            db.sadd("SERI" + str(TITLE),str(SERIIDS))
        db.sadd(str(SERIIDS),str(SERISTART) + "-+" + str(file_dir))
        await app.send_message(chat_id,f"Photo with local address {file_dir} added to seri {SERIIDS} with ID {SERISTART}\nAny photo? send it",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
        SERISTART += 1
app.start()
print("Running Bot...")
ME=app.get_me()
print(ME)
idle()
app.stop()