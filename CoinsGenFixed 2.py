def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)
  
text = 'AminoCoinGen'
text2 = 'Fixed by 3looy'
colored_text = colored(255, 0, 0, text)
print(colored_text)
from box import tzFilter
from aminofix import Client 
from aminofix import SubClient
from aminofix.lib.util.exceptions import * 
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from os import path
import json
from hashlib import sha1
from hmac import new
import os
import time
def deviee():
    identifierr = bytes.fromhex("42") + os.urandom(20)
    macc = new(bytes.fromhex("02B258C63559D8804321C5D5065AF320358D366F"), identifierr, sha1)
    return f"{identifierr.hex()}{macc.hexdigest()}".upper()
deviceII = deviee()
THIS_FOLDER = path.dirname(path.abspath(__file__))
emailfile=path.join(THIS_FOLDER,"accounts.json")
dictlist=[]
clientt = Client(deviceId=deviee())
cid="" # community id here's
#keep_alive()
with open(emailfile) as f: 
    dictlist = json.load(f) 

def magicnum(): 
    toime={"start":int(datetime.timestamp(datetime.now())),"end":int(datetime.timestamp(datetime.now()))+300}
    return toime 

def sendobj(sub : SubClient):
    timer=[
    magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum(),magicnum()
    ] 
    sub.send_active_obj(timers=timer,
tz=tzFilter()) 

def log(cli : Client(deviceId=deviee()),email : str, password : str):
    try:  
        cli.login(email=email,password=password)
        print(f"logged into {email}\n")
    except VerificationRequired:
        print(f"Verification required for {email}")
    except InvalidPassword or InvalidAccountOrPassword:
        print(f"Incorrect password for {email}")
    except: 
        print(f"An unkown error has occoured for {email}")
        pass # Passes 

def task(sub : SubClient,email : str,i : int):
    try:
        time.sleep(1)
        sendobj(sub) 
        print(f"Sent coin generating object for {email} times :- {i+1}")
    except Exception as e:
        print(e)
        return None

def threadit(acc : dict):
    email=acc["email"]
    #device= deviceII
    password=acc["password"]
    client=Client(deviceId=deviceII)
    log(cli=client,email=email,password=password)
    #client.join_community(cid)
    subclient=SubClient(comId=cid,profile=client.profile, deviceId=deviee())
    print("Done")
    with ThreadPoolExecutor(max_workers=1) as executorx:
        _ = [executorx.submit(task, subclient,email,i)for i in range(25)]
    time.sleep(35)
    client.logout()
    print(f"FINISHED MINING {email}")

def main():
    print(f"{len(dictlist)} accounts loaded")
    for amp in dictlist:
    	threadit(amp)
    print("Mining with all accounts finished")
 
if __name__ == '__main__': 
    main()