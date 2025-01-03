import requests,re,redis,threading,asyncio,os,sys,gc,json,time,stem.process
from random import randint
 
db = None
while not db :
    db = redis.StrictRedis(host='localhost', port=6379, db=0)
    
from pyrogram import Client
from pyrogram import filters
from pyrogram import idle
from pyrogram import errors
from pyrogram.types import InlineKeyboardButton as button
from pyrogram.types import InlineKeyboardMarkup as markup
from pyrogram.types import ForceReply as reply
from pyrogram.raw import functions
if db.get("TOKEN"):
    STOKEN = db.get("TOKEN").decode('utf-8')
else:
    print("NO BOT TOKEN")
    sys.exit()
app = Client("bot",8620004,"38c878e9530d1968f28caaae6760fa83",bot_token=STOKEN)
if db.get("STOKEN"):
    TOKEN = db.get("STOKEN").decode('utf-8')
else:
    print("NO SMS TOKEN")
    sys.exit()
from time import sleep
global step
step= 'None'
SORP = "SERI"
SOSK = 0
NASK = 0
def print_bootstrap_lines(line):
    pass
def changeIP(PORT):
    os.system("sudo fuser -k " + str(PORT) + "/tcp")
    result = None
    try:
        tor_process = stem.process.launch_tor_with_config(config = {'SocksPort': str(PORT),'DataDirectory': './.tordatach' + str(PORT),},init_msg_handler = print_bootstrap_lines,)
        result = "Yes"
    except:
        pass
PORTX = 9051
async def AUTOL():
    global GLOBALD
    global app
    global TOKEN
    global SESSIONS
    global SORP
    global SOSK
    global NASK
    global PORTX
    while True:
        try:
            for ID in GLOBALD:
                TIMETC = GLOBALD[ID]["time"]
                if TIMETC < 60:
                    GLOBALD[ID]["time"] = TIMETC + 1
                    STATUS = requests.get(f"https://sms-activate.ru/stubs/handler_api.php?api_key={TOKEN}&action=getStatus&id={ID}")
                    STATUSC = str(STATUS.content)
                    print(STATUSC)
                    if "STATUS_OK" in STATUSC:
                        CodeGo = STATUSC.replace("\n","").replace("STATUS_OK:","").replace("b'","").replace("'","")
                        PHONE = GLOBALD[ID]["phone"]
                        chat_id = GLOBALD[ID]["chat"]
                        HASH = GLOBALD[ID]["hash"]
                        await app.send_message(chat_id,f"📥Creating account!\n\nPhone: +{PHONE}\nID: {ID}\nCode: {CodeGo}")
                        client = SESSIONS[PHONE]
                        OKTRUE = 0
                        try:
                            RESULTA = await client.sign_in(phone_number=f"+{PHONE}",phone_code_hash=HASH, phone_code=CodeGo)
                            try:
                                IDX = RESULTA.id
                                RESULT = await client.accept_terms_of_service(terms_of_service_id=str(IDX))
                            except Exception as e:
                                print(e)
                                pass
                            try:
                                if db.scard("NAMES") > 0:
                                    TNN = 0
                                    if NASK >= db.scard("NAMES"):
                                        NASK = 0
                                    for GNAME in db.smembers("NAMES"):
                                        TNN += 1
                                        if TNN > NASK:
                                            NASK = TNN
                                            break
                                    GNAME = GNAME.decode("utf-8")
                                    GNAMES = GNAME.split(" ")
                                    FNAME = GNAMES[0]
                                    LNAME = GNAMES[1]
                                else:
                                    FNAME = "Torsten"
                                    LNAME = "Eichmann"
                                RESULT = await client.sign_up(phone_number=f"+{PHONE}",phone_code_hash= HASH, first_name= str(FNAME) , last_name= str(LNAME))
                                OKTRUE += 1
                            except Exception as e:
                                print(e)
                            await app.send_message(chat_id,f"✋✅Account created!\n\nPhone: +{PHONE}\nID: {ID}\nCode: {CodeGo}\n\nNow you can select receive button to get your login code",reply_markup = markup([[button("♻️Receive Code",callback_data=f"receive_{PHONE}")]]))
                            try:
                                if SORP == "SERI":
                                    if db.scard("SERI") > 0:
                                        TIN = 0
                                        if SOSK >= db.scard("SERI"):
                                            SORP = "PHOT"
                                            SOSK = 0
                                        for GPHOTO1 in db.smembers("SERI"):
                                            TIN += 1
                                            if TIN > SOSK:
                                                SOSK = TIN
                                                break
                                        GPHOTO1 = GPHOTO1.decode("utf-8")
                                        for URLPH in db.smembers(GPHOTO1):
                                            URLPH = URLPH.decode('utf-8')
                                            await client.set_profile_photo(photo=str(URLPH))
                                    else:
                                        if db.scard("PHOTOS") > 0:
                                            TIN = 0
                                            if SOSK >= db.scard("PHOTOS"):
                                                SORP = "SERI"
                                                SOSK = 0
                                            for GPHOTO in db.smembers("PHOTOS"):
                                                TIN += 1
                                                if TIN > SOSK:
                                                    SOSK = TIN
                                                    break
                                            GPHOTO = GPHOTO.decode("utf-8")
                                            await client.set_profile_photo(photo=str(GPHOTO))
                                elif SORP == "PHOT":
                                    if db.scard("PHOTOS") > 0:
                                        TIN = 0
                                        if SOSK >= db.scard("PHOTOS"):
                                            SORP = "SERI"
                                            SOSK = 0
                                        for GPHOTO in db.smembers("PHOTOS"):
                                            TIN += 1
                                            if TIN > SOSK:
                                                SOSK = TIN
                                                break
                                        GPHOTO = GPHOTO.decode("utf-8")
                                        await client.set_profile_photo(photo=str(GPHOTO))
                                    else:
                                        TIN = 0
                                        if SOSK >= db.scard("SERI"):
                                            SORP = "PHOT"
                                            SOSK = 0
                                        for GPHOTO1 in db.smembers("SERI"):
                                            TIN += 1
                                            if TIN > SOSK:
                                                SOSK = TIN
                                                break
                                        GPHOTO1 = GPHOTO1.decode("utf-8")
                                        for URLPH in db.smembers(GPHOTO1):
                                            URLPH = URLPH.decode('utf-8')
                                            await client.set_profile_photo(photo=str(URLPH))
                            except:
                                pass
                            OKTRUE += 1
                        except Exception as e:
                            print(e)
                        if OKTRUE == 0:
                            await app.send_message(chat_id,f"❌There is a problem to create account!\n\nPhone: +{PHONE}\nID: {ID}\nCode: {CodeGo}")
                        TOR = GLOBALD[ID]["tor"]
                        del GLOBALD[ID]
                        try:
                            await client.disconnect()
                        except: pass
                        del client
                        try:
                            TOR.kill()
                        except: pass
                    elif "STATUS_CANCEL" in STATUSC:
                        del GLOBALD[ID]
                    else:
                        pass
                else:
                    CANCEL = requests.get(f"https://sms-activate.ru/stubs/handler_api.php?api_key={TOKEN}&action=setStatus&status=8&id={ID}")
                    PHONE = GLOBALD[ID]["phone"]
                    chat_id = GLOBALD[ID]["chat"]
                    del GLOBALD[ID]
                    await app.send_message(chat_id,f"❌Your number canceled after 100 time request!\n\nPhone: +{PHONE}\nID: {ID}")
                    
        except:
            await asyncio.sleep(10)
        await asyncio.sleep(5)
def Between_Start():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(AUTOL())
    loop.close()
async def GetCode(phone,chat_id):
    Sapp = ""
    global PORTX
    while True:
        try:
            sessionx = f'sessions/+{phone}'
            PORTX += 1
            if int(PORTX) > 9100:
                PORTX = 9051
            TOR = changeIP(PORTX)
            api_id, api_hash = 16623,"8c9dbfe58437d1739540f5d53c72ae4b"
            Sapp = Client(sessionx,api_id,api_hash,proxy=dict(hostname="127.0.0.1",port=int(PORTX),username="",password=""))  
            break
        except:
            await asyncio.sleep(1)
    is_auth = await Sapp.connect()
    if is_auth:
        while True:
            try:
                async for message in Sapp.iter_history(777000):
                    TEXT = str(message.text)
                    print(TEXT)
                    if "Login code" in TEXT:
                        TEXT = TEXT.replace("1","1️⃣").replace("2","2️⃣").replace("3","3️⃣").replace("4","4️⃣").replace("5","5️⃣").replace("6","6️⃣").replace("7","7️⃣").replace("8","8️⃣").replace("9","9️⃣").replace("0","0️⃣")
                        await app.send_message(chat_id,f"✅Code received\n\nPhone: +{phone}\nMessage: {TEXT}")
                        try:
                            await Sapp.log_out()
                            TOR.kill()
                        except:
                            pass
                        sys.exit()
            except Exception as e:
                print(e)
                if "AUTH_KEY_UNREGISTERED" in str(e):
                    await app.send_message(chat_id,f"❌There is no auth!\n\nPhone: +{phone}")
                    sys.exit()
                    break
            await asyncio.sleep(1)
    else:
        await app.send_message(chat_id,f"❌Number not auth!\n\nPhone: +{phone}")
        sys.exit()

def Between_Get(phone,chat_id):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(GetCode(phone,chat_id))
    loop.close()
STARTED = False
@app.on_message(filters.command(['start']))
async def start(client,message):
    global STARTED
    if STARTED == False:
        STARTED = True
        _thread = threading.Thread(target=Between_Start, args=[]).start()
    chat_id = message.chat.id
    print("START => " + str(chat_id))
    message_id = message.message_id
    NO = await Menu(chat_id,message_id)
list_a = ["218722292","246212075"]
list_b = ["218722292","246212075"]
STEPALL = "none"
if db.scard("SUDOBOT") > 0:
    for sudoid in db.smembers("SUDOBOT"):
        list_a.append(str(sudoid.decode("utf-8")))
else:
    list_a.append("218722292")
    list_a.append("246212075")
async def Menu(chat_id,message_id):
    global list_a
    if str(chat_id) in list_a:
        NO = await app.send_message(chat_id,
                          "✋🏻Hi\nSelect your action",
                          reply_to_message_id = message_id,
                          reply_markup = markup([
                          [button("📤Buy and Check",callback_data="GETHIT")],
                          [button("📊Your Number List",callback_data="NUML")],
                          [button("📸Add Photo",callback_data="PHOTOADD"),button("✂️Clean Photos",callback_data="PHOTOCLEAN")],
                          [button("🎥Add Series",callback_data="SERIADD"),button("🧹Clean Series",callback_data="SERICLEAN")],
                          [button("⌨️Add Name",callback_data="NAMEADD"),button("🗒Clean Name",callback_data="NAMECLEAN")],
                          [button("🕹Add Sudo",callback_data="ADDS"),button("❌Rem Sudo",callback_data="REMS")]
                          ]))
    else:
        NO = await app.send_message(chat_id,"You can not use this robot",parse_mode='html')
LASTTIMEUP = int(time.time())
@app.on_message()
async def Updates(app,message):
    global STEPALL
    global list_a
    global list_b
    chat_id = message.chat.id 
    text = message.text
    if STEPALL == "NAMEADD":
        if " " in str(text):
            db.sadd("NAMES",text)
            await app.send_message(chat_id,f"Name {text} added to list\nAny name? send it",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
        else:
            await app.send_message(chat_id,f"❌Wrong name!No space in Name\nAny name? send it",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
    
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
GLOBALD = {}
SESSIONS = {}
GLOBALID = "123456798"
SERIIDS = 0
sdata = ""
sdata2 = ""
@app.on_callback_query()
async def querys(_, query):
    global GLOBALD
    global STEPALL
    global list_b
    global list_a
    global TOKEN
    global SESSIONS
    global GLOBALID
    global LASTTIMEUP
    global PORTX
    chat_id = query.message.chat.id
    message_id = query.message.message_id
    if str(chat_id) in list_a:
        data = query.data
        if data == "BACK":
            STEPALL = "none"
            await app.edit_message_text(chat_id,message_id,"✋🏻Hi\nSelect your action",reply_markup = markup([
            [button("📤Buy and Check",callback_data="GETHIT")],
            [button("📊Your Number List",callback_data="NUML")],
            [button("📸Add Photo",callback_data="PHOTOADD"),button("✂️Clean Photos",callback_data="PHOTOCLEAN")],
            [button("🎥Add Series",callback_data="SERIADD"),button("🧹Clean Series",callback_data="SERICLEAN")],
            [button("⌨️Add Name",callback_data="NAMEADD"),button("🗒Clean Names",callback_data="NAMECLEAN")],
            [button("🕹Add Sudo",callback_data="ADDS"),button("❌Rem Sudo",callback_data="REMS")]]))
        elif data == "SERIADD":
            global SERIIDS
            SERIIDS = randint(999,99999)
            STEPALL = "SERIADD"
            GLOBALID = chat_id
            await app.edit_message_text(chat_id,message_id,"Please send your photo",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
        elif data == "PHOTOADD":
            STEPALL = "PHOTOADD"
            GLOBALID = chat_id
            await app.edit_message_text(chat_id,message_id,"Please send your photo",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
        elif data == "NAMEADD":
            STEPALL = "NAMEADD"
            await app.edit_message_text(chat_id,message_id,"Please send your name",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
        elif data == "SERICLEAN":
            if db.scard("SERI") > 0:
                for names in db.smembers("SERI"):
                    names = names.decode('utf-8')
                    db.srem("SERI",names)
                    if db.scard(names) > 0:
                        for serid in db.smembers(names):
                            serid = serid.decode('utf-8')
                            db.srem(names,serid)
            await app.edit_message_text(chat_id,message_id,f"List of Series cleaned",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
        elif data == "PHOTOCLEAN":
            if db.scard("PHOTOS") > 0:
                for names in db.smembers("PHOTOS"):
                    names = names.decode('utf-8')
                    db.srem("PHOTOS",names)
            await app.edit_message_text(chat_id,message_id,f"List of photos cleaned",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
        elif data == "NAMECLEAN":
            if db.scard("NAMES") > 0:
                for names in db.smembers("NAMES"):
                    names = names.decode('utf-8')
                    db.srem("NAMES",names)
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
            await app.edit_message_text(chat_id,message_id,"Try to get number...")
            TIMENOW = int(time.time())
            global sdata
            global sdata2
            if LASTTIMEUP < TIMENOW:
                LASTTIMEUP = int(time.time()) + 300
                while True:
                    try:
                        S1 = requests.get(f"https://sms-activate.ru/stubs/handler_api.php?api_key={TOKEN}&action=getPrices&service=tg")
                        S2 = requests.get(f"https://sms-activate.ru/stubs/handler_api.php?api_key={TOKEN}&action=getCountries")
                        sdata = S1.json()
                        sdata2 = S2.json()
                        break
                    except:
                        await app.edit_message_text(chat_id,message_id,"❌Have problem to get data\nWaiting...",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
                     #   return 
                    sleep(1)
            try:
                LISTBUT = []
                for key in sdata.keys(): 
                    try:
                        COST = sdata[key]["tg"]["cost"]
                        NAME = sdata2[key]["eng"]
                        if COST <= 17 and sdata[key]["tg"]["count"] > 0:
                            LISTBUT.append([button(f"🇺🇳 {NAME} - {COST}",callback_data=f"BUY_{key}")])
                    except:
                        pass
                LISTBUT.append([button(f"🔙Back",callback_data="BACK")])
                await app.edit_message_text(chat_id,message_id,"Please select your country\nFormat: NAME - PRICE",reply_markup = markup(LISTBUT))
            except:
                await app.edit_message_text(chat_id,message_id,"❌Have problem to get data",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
        elif "receive_" in str(data):
            try:
                PHONE = str(data).replace("receive_","")
                _thread = threading.Thread(target=Between_Get, args=[PHONE,chat_id]).start()
                await app.edit_message_text(chat_id,message_id,f"♻️Ready for getting code\nEnter phone number +{PHONE} in your telegram to get your code")
            except:
                await app.edit_message_text(chat_id,message_id,f"❌There is a problem to get code for phone number +{PHONE}\n Try after a while",reply_markup = markup([[button("♻️Receive Code",callback_data=f"receive_{PHONE}")]]))
        elif "BUY_" in str(data):
            try:
                COUNTBUY = str(data).replace("BUY_","")
                BUYS = requests.get(f"https://sms-activate.ru/stubs/handler_api.php?api_key={TOKEN}&action=getNumber&service=tg&operator=any&country={COUNTBUY}")
                BUYSC = str(BUYS.content)
                if "ACCESS_NUMBER" in BUYSC:
                    DATAS = BUYSC.split(":")
                    ID = DATAS[1]
                    PHONE = DATAS[2]
                    PHONE = PHONE.replace("'","")
                    GLOBALD[ID] = {"chat":chat_id,"phone":PHONE,"status":"no","time":0}
                    await app.edit_message_text(chat_id,message_id,f"Number created\n\nPhone: +{PHONE}\nID: {ID}\n\n♻️Wait to check number")
                    PORTX += 1
                    if int(PORTX) > 9100:
                        PORTX = 9051
                    TOR = changeIP(PORTX)
                    session = f'sessions/+{PHONE}'
                    api_id, api_hash = 16623,"8c9dbfe58437d1739540f5d53c72ae4b"
                    client = Client(session,api_id,api_hash,proxy=dict(hostname="127.0.0.1",port=int(PORTX),username="",password=""))
                    await client.connect()
                    try:
                        phone_code_hash1 = await client.send_code(f"+{PHONE}")
                        print(phone_code_hash1)
                        phone_code_hash = phone_code_hash1.phone_code_hash
                        GLOBALD[ID]["hash"] = phone_code_hash
                        GLOBALD[ID]["tor"] = TOR
                        SESSIONS[PHONE] = client
                #        await app.edit_message_text(chat_id,message_id,f"✅Number is OK\n\nPhone: +{PHONE}\nID: {ID}\n\n💤Wait for 30 seconds to this message edit automatically and showing OK button\nYou can cancel it too")
                #        await asyncio.sleep(30)
                        await app.edit_message_text(chat_id,message_id,f"✅Number is OK\n\nPhone: +{PHONE}\nID: {ID}\n\n♻Please confirm it to ready for get code",reply_markup = markup([[button(f"✅OK",callback_data=f"OK_{ID}"),button(f"❌Cancel",callback_data=f"CANCEL_{ID}")]]))
                    #    await client.disconnect()
                    except errors.PhoneNumberInvalid as error:
                        print("PhoneNumberInvalid")
                        try:
                            TOR = GLOBALD[ID]["tor"]
                            TOR.kill()
                            del GLOBALD[ID]
                        except:
                            pass
                        DELETE = requests.get(f"https://sms-activate.ru/stubs/handler_api.php?api_key={TOKEN}&action=setStatus&status=8&id={ID}")
                        await app.edit_message_text(chat_id,message_id,f"❌Number had problem\n\nPhone: +{PHONE}\nID: {ID}",reply_markup = markup([[button(f"♻️Buy from this country again",callback_data=f"BUY_{COUNTBUY}")],
                        [button(f"📤Buy from another country",callback_data="GETHIT")],
                        [button(f"🔙Back",callback_data="BACK")]]))
                        del client
                    except Exception as e:
                        print(e)
                        try:
                            TOR = GLOBALD[ID]["tor"]
                            TOR.kill()
                            del GLOBALD[ID]
                        except:
                            pass
                        DELETE = requests.get(f"https://sms-activate.ru/stubs/handler_api.php?api_key={TOKEN}&action=setStatus&status=8&id={ID}")
                        await app.edit_message_text(chat_id,message_id,f"❌Number had problem\n\nPhone: +{PHONE}\nID: {ID}",reply_markup = markup([[button(f"♻️Buy from this country again",callback_data=f"BUY_{COUNTBUY}")],
                        [button(f"📤Buy from another country",callback_data="GETHIT")],
                        [button(f"🔙Back",callback_data="BACK")]]))
                        del client
                elif "NO_BALANCE" in BUYSC:
                    await app.edit_message_text(chat_id,message_id,"There is no Balance",reply_markup = markup([[button(f"♻️Buy from this country again",callback_data=f"BUY_{COUNTBUY}")],
                        [button(f"📤Buy from another country",callback_data="GETHIT")],
                        [button(f"🔙Back",callback_data="BACK")]]))
                elif "NO_NUMBERS" in BUYSC:
                    await app.edit_message_text(chat_id,message_id,"There is no Number for this country",reply_markup = markup([[button(f"♻️Buy from this country again",callback_data=f"BUY_{COUNTBUY}")],
                        [button(f"📤Buy from another country",callback_data="GETHIT")],
                        [button(f"🔙Back",callback_data="BACK")]]))
                else:
                    await app.edit_message_text(chat_id,message_id,"There is an unknown error",reply_markup = markup([[button(f"♻️Buy from this country again",callback_data=f"BUY_{COUNTBUY}")],
                        [button(f"📤Buy from another country",callback_data="GETHIT")],
                        [button(f"🔙Back",callback_data="BACK")]]))
            except:
                await app.edit_message_text(chat_id,message_id,"❌Have problem to get data",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
        elif "OK_" in str(data):
            try:
                ID = str(data).replace("OK_","")
                PHONE = GLOBALD[ID]["phone"]
                GLOBALD[ID]["status"] = "ok"
                READY = requests.get(f"https://sms-activate.ru/stubs/handler_api.php?api_key={TOKEN}&action=setStatus&status=1&id={ID}")
                await app.edit_message_text(chat_id,message_id,f"✅Ready for getting code\n\nPhone: +{PHONE}\nID: {ID}",reply_markup = markup([[button(f"❌Cancel",callback_data=f"CANCEL_{ID}")],[button(f"🔙Back",callback_data="BACK")]]))
            except:
                await app.edit_message_text(chat_id,message_id,"❌Have problem to get data",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
        elif "CANCEL_" in str(data):
            try:
                ID = str(data).replace("CANCEL_","")
                PHONE = GLOBALD[ID]["phone"]
                client = SESSIONS[PHONE]
                CANCEL = requests.get(f"https://sms-activate.ru/stubs/handler_api.php?api_key={TOKEN}&action=setStatus&status=8&id={ID}")
                TOR = GLOBALD[ID]["tor"]
                TOR.kill()
                del GLOBALD[ID]
                await app.edit_message_text(chat_id,message_id,f"❌Number Canceled\n\nPhone: +{PHONE}\nID: {ID}",reply_markup = markup([[button(f"📤Go to buy list",callback_data="GETHIT")],[button(f"🔙Back",callback_data="BACK")]]))
                await client.disconnect()
            except:
                await app.edit_message_text(chat_id,message_id,"❌Have problem to get data",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
    else:
        await app.edit_message_text(chat_id,message_id,"You can not use this robot")
        
@app.on_message(filters.photo, group=2)
async def get_file(cli, message):
    global STEPALL
    global GLOBALID
    chat_id = message.chat.id 
    if STEPALL == "PHOTOADD" and GLOBALID == chat_id:
        file_dir = await app.download_media(message) 
        db.sadd("PHOTOS",str(file_dir))
        await app.send_message(chat_id,f"Photo with local address {file_dir} added to list\nAny photo? send it",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
    elif STEPALL == "SERIADD" and GLOBALID == chat_id:
        global SERIIDS
        file_dir = await app.download_media(message) 
        if not db.sismember("SERI",str(SERIIDS)):
            db.sadd("SERI",str(SERIIDS))
        db.sadd(str(SERIIDS),str(file_dir))
        await app.send_message(chat_id,f"Photo with local address {file_dir} added to seri {SERIIDS}\nAny photo? send it",reply_markup = markup([[button(f"🔙Back",callback_data="BACK")]]))
    
app.start()
print("Running Bot...")
idle()
app.stop()