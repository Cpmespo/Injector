import httpx
import json
import random as rdm

Vhost = "us-central1-cp-multiplayer.cloudfunctions.net"
Vheader = {
    "Content-Type": "application/json",
    "X-Android-Package": "com.olzhas.carparking.multyplayer",
    "X-Android-Cert": "D4962F8124C2E09A66B97C8E326AFF805489FE39",
    "Accept-Language": "in-ID, en-US",
    "X-Client-Version": "Android/Fallback/X21001000/FirebaseCore-Android",
    "X-Firebase-GMPID": "1:581727203278:android:af6b7dee042c8df539459f",
    "X-Firebase-Client": "H4sIAAAAAAAAAKtWykhNLCpJSk0sKVayio7VUSpLLSrOzM9TslIyUqoFAFyivEQfAAAA",
    "User-Agent": f"Dalvik/2.1.0 (Linux; U; Android 8.1.0; ASUS_X00TD MIUI/16.2017.2009.087-20{rdm.randint(111111,999999)})",
    "Host": "www.googleapis.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip"
}
# for cekdata in ["data"]:
#     if cekdata not in Vdata:
#         Vdata[cekdata]=input(f"{cekdata} : ")
Vdata = {}
Vdata["idToken"] = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjNmNjcyNDYxOTk4YjJiMzMyYWQ4MTY0ZTFiM2JlN2VkYTY4NDZiMzciLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vY3AtbXVsdGlwbGF5ZXIiLCJhdWQiOiJjcC1tdWx0aXBsYXllciIsImF1dGhfdGltZSI6MTY2Njk2NzcxNywidXNlcl9pZCI6InIybnBPekpuaTloWXU1WWZEbWduamZUUVVhSjMiLCJzdWIiOiJyMm5wT3pKbmk5aFl1NVlmRG1nbmpmVFFVYUozIiwiaWF0IjoxNjY2OTY3NzE3LCJleHAiOjE2NjY5NzEzMTcsImVtYWlsIjoidHNiMDEwQGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJlbWFpbCI6WyJ0c2IwMTBAZ21haWwuY29tIl19LCJzaWduX2luX3Byb3ZpZGVyIjoicGFzc3dvcmQifX0.gztM8gzOpNdW6PmmA_hfJDpxh8hCVC1RgAeKcBeVs5-sZnALK3gOtA85ip8khJyhC0N7i0iPwN9TsJqMGvqPb6qHGtuoe9agXWyPdqiztmKEBsJpJrvjPKJj24PmmoREnDnJq8cZHgX7BPyPoD25ZqhCC1pEkjz_XSoQF4qwLhM7-BR8BjcVYkWxxKxJPzfjMc3WfaW2ehHbYEjx8RcOQvsW6yp1zgGXYlbMavbyjHE2Zbl5ameRwic47WD_C6ugH4vtIf7XJWxbAF02CBHicJqLAkCQt0ioxtQpsYu_yq6khnNOA7vqCIn3G8kfmLIZvTNH9kQ-q7X59ePUwgvrmA"
Vdata["key"] = "AIzaSyBW1ZbMiUeDZHYUO2bY8Bfnf5rRgrQGPTM"
Vdata["firebase-instance-id-token"] = "fdEMFcKoR2iSrZAzViyFkh:APA91bEQsP8kAGfBuPTL_ATg25AmnqpssGTkc7IAS2CgLiILjBbneFuSEzOJr2a97eDvQOPGxlphSIV7gCk2k4Wl0UxMK5x298LrJYa5tJmVRqdyz0j3KDSKLCtCbldkRFwNnjU3lwfP"
Vdata["data"] = "9FD07A11C3494803B517F92545ED5A6702AD0AD2"


def verifyPassword(email, password):
    uri = f"https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key={Vdata['key']}"
    data = {"email": email, "password": password, "returnSecureToken": True}
    req = httpx.post(uri, data=json.dumps(data), headers=Vheader)
    if req.status_code == 200:
        ress = json.loads(req.text)
        print(f"verifyPassword : {len(ress)}")
        Vdata["idToken"] = ress["idToken"]
        # print(Vdata["idToken"])
        return True


def getAccountInfo():
    uri = f"https://www.googleapis.com/identitytoolkit/v3/relyingparty/getAccountInfo?key={Vdata['key']}"
    data = {"idToken": Vdata["idToken"]}
    req = httpx.post(uri, data=json.dumps(data), headers=Vheader)
    if req.status_code == 200:
        ress = json.loads(req.text)
        print(f"getAccountInfo : {len(ress)}")


def GetPlayerRecords():
    uri = f"https://{Vhost}/GetPlayerRecords2"
    heder = {
        "Host": Vhost,
        "authorization": f'Bearer {Vdata["idToken"]}',
        "firebase-instance-id-token": Vdata["firebase-instance-id-token"],
        "content-type": "application/json; chatset=utf-8",
        "accept-encoding": "gzip",
        "User-Agent": f"Dalvik/2.1.0 (Linux; U; Android 8.1.0; ASUS_X00TD MIUI/16.2017.2009.087-20{rdm.randint(111111,999999)})"
    }
    data = {"data": Vdata["data"]}
    req = httpx.post(uri, data=json.dumps(data), headers=heder)
    if req.status_code == 200:
        ress = json.loads(req.text)
        resss = json.loads(ress["result"])
        with open('player/data.json', 'w', encoding='utf-8') as f:
            json.dump({"data": resss}, f, ensure_ascii=False, indent=4)
        print(f"Data Player : {len(resss)}")
        return resss


def GetCarHash():
    uri = f"https://{Vhost}/GetCarHash"
    heder = {
        "Host": Vhost,
        "authorization": f'Bearer {Vdata["idToken"]}',
        "firebase-instance-id-token": Vdata["firebase-instance-id-token"],
        "content-type": "application/json; chatset=utf-8",
        "accept-encoding": "gzip",
        "User-Agent": f"Dalvik/2.1.0 (Linux; U; Android 8.1.0; ASUS_X00TD MIUI/16.2017.2009.087-20{rdm.randint(111111,999999)})"
    }
    data = {"data": ""}
    req = httpx.post(uri, data=json.dumps(data), headers=heder)
    if req.status_code == 200:
        ress = json.loads(req.text)
        resss = json.loads(ress["result"])
        with open('player/carhash.json', 'w', encoding='utf-8') as f:
            json.dump({"result": resss}, f, ensure_ascii=False, indent=4)
        print(f"Car Hash : {len(resss)}")


def SavePlayerRecords7(dataakun):
    uri = f"https://{Vhost}/SavePlayerRecords10"
    heder = {
        "Host": Vhost,
        "authorization": f'Bearer {Vdata["idToken"]}',
        "firebase-instance-id-token": Vdata["firebase-instance-id-token"],
        "content-type": "application/json; chatset=utf-8",
        "accept-encoding": "gzip",
        "User-Agent": f"Dalvik/2.1.0 (Linux; U; Android 8.1.0; ASUS_X00TD MIUI/16.2017.2009.087-20{rdm.randint(111111,999999)})"
    }
    pipit = json.dumps(dataakun["data"])
    data = {"data": pipit}
    req = httpx.post(uri, data=json.dumps(data), headers=heder)
    # print(req.status_code)
    # print(req.text)
    if req.status_code == 200:
        ress = json.loads(req.text)
        print(f"Save Account Info {ress}")
        resss = json.loads(ress["result"])
        if resss == 1:
            return True
        return True
    return False
    
    def SetUserRatingCall(isidata):
        print('SetUserRatingCall')
        uri = f"https://{'us-central1-cp-multiplayer.cloudfunctions.net'}/SetUserRatingCall"
        heder = {'Host': 'us-central1-cp-multiplayer.cloudfunctions.net', 'authorization': f"Bearer {dat['idToken']}", 'firebase-instance-id-token': dat['firebase-instance-id-token'], 'content-type': 'application/json; chatset=utf-8', 'accept-encoding': 'gzip', 'User-Agent': f'Dalvik/2.1.0 (Linux; U; Android 8.1.0; ASUS_X00TD MIUI/16.2017.2009.087-20{random.randint(111111, 999999)})'}
        data = {'data': json.dumps(isidata)}
        req = httpx.post(uri, data=json.dumps(data), headers=heder, timeout='1000')
        if req.status_code == '200':
            ress = json.loads(req.text)
            return True
        return False

    def clear():
        try:
            os.system('cls')
            os.system('clear')
        except:
            pass


def SaveCarHash(dataakun):
    uri = f"https://{Vhost}/SaveCarHash"
    heder = {
        "Host": Vhost,
        "authorization": f'Bearer {Vdata["idToken"]}',
        "firebase-instance-id-token": Vdata["firebase-instance-id-token"],
        "content-type": "application/json; chatset=utf-8",
        "accept-encoding": "gzip",
        "User-Agent": f"Dalvik/2.1.0 (Linux; U; Android 8.1.0; ASUS_X00TD MIUI/16.2017.2009.087-20{rdm.randint(111111,999999)})"
    }
    pipit = json.dumps(dataakun["result"])
    data = {"data": pipit}
    req = httpx.post(uri, data=json.dumps(data), headers=heder)
    # print(req.status_code)
    # print(req.text)
    if req.status_code == 200:
        ress = json.loads(req.text)
        resss = json.loads(ress["result"])
        print(f"Save Car Hash : {ress}")
        if resss == 1:
            return True
    return False


def SaveCars(data):
    uri = f"https://{Vhost}/SaveCars"
    heder = {
        "Host": Vhost,
        "authorization": f'Bearer {Vdata["idToken"]}',
        "firebase-instance-id-token": Vdata["firebase-instance-id-token"],
        "content-type": "application/json; chatset=utf-8",
        "accept-encoding": "gzip",
        "User-Agent": f"Dalvik/2.1.0 (Linux; U; Android 8.1.0; ASUS_X00TD MIUI/16.2017.2009.087-20{rdm.randint(111111,999999)})"
    }
    # pipit=json.dumps(data["data"])
    # data=json.dumps(data)
    data = json.dumps({"data": json.dumps(data["data"])})
    req = httpx.post(uri, data=data, headers=heder)
    if req.status_code == 400:
        ress = json.loads(req.text)
        resss = json.loads(ress["result"])
        # print(resss)
        return True
    print(req.status_code)
    print(req.text)
    return False


def TestGetAllCars():
    uri = f"https://{Vhost}/TestGetAllCars"
    heder = {
        "Host": Vhost,
        "authorization": f'Bearer {Vdata["idToken"]}',
        "firebase-instance-id-token": Vdata["firebase-instance-id-token"],
        "content-type": "application/json; chatset=utf-8",
        "accept-encoding": "gzip",
        "User-Agent": f"Dalvik/2.1.0 (Linux; U; Android 8.1.0; ASUS_X00TD MIUI/16.2017.2009.087-20{rdm.randint(111111,999999)})"
    }
    data = {"data": Vdata["data"]}
    req = httpx.post(uri, data=json.dumps(data), headers=heder, timeout=1000)
    if req.status_code == 200:
        ress = json.loads(req.text)
        resss = json.loads(ress["result"])
        urutan = ""
        for itr in range(len(resss)):
            urutan += str(resss[itr]["CarID"])+","
            with open(f'player/cars/{resss[itr]["CarID"]}', 'w', encoding='utf-8') as f:
                json.dump({"data": resss[itr]}, f,
                          ensure_ascii=False, indent=4)
        print(urutan)
        print(f"Data : {len(resss)}")


# World Sale
def GetCarListWorldSale2(wsvalue):
    # print("Get Car List WorldSale2")
    uri = f"https://{Vhost}/GetCarListWorldSale2"
    heder = {
        "Host": Vhost,
        "authorization": f'Bearer {Vdata["idToken"]}',
        "firebase-instance-id-token": Vdata["firebase-instance-id-token"],
        "content-type": "application/json; chatset=utf-8",
        "accept-encoding": "gzip",
        "User-Agent": f"Dalvik/2.1.0 (Linux; U; Android 8.1.0; ASUS_X00TD MIUI/16.2017.2009.087-20{rdm.randint(111111,999999)})"
    }
    data = json.dumps({"data": {
                      "@type": "type.googleapis.com/google.protobuf.Int64Value", "value": wsvalue}})
    req = httpx.post(uri, data=data, headers=heder, timeout=10)
    # print(req.text)
    if req.status_code == 200:
        ress = json.loads(req.text)
        return ress["result"]


def TestGetOneCarFromWorldSale(ownerAccountID, carid, wsvalue):
    print("Get Car From WorldSale")
    uri = f"https://{Vhost}/TestGetOneCarFromWorldSale"
    heder = {
        "Host": Vhost,
        "authorization": f'Bearer {Vdata["idToken"]}',
        "firebase-instance-id-token": Vdata["firebase-instance-id-token"],
        "content-type": "application/json; chatset=utf-8",
        "accept-encoding": "gzip",
        "User-Agent": f"Dalvik/2.1.0 (Linux; U; Android 8.1.0; ASUS_X00TD MIUI/16.2017.2009.087-20{rdm.randint(111111,999999)})"
    }
    data = json.dumps(
        {"data": [str(ownerAccountID), str(carid), str(wsvalue)]})
    print(data)
    req = httpx.post(uri, data=data, headers=heder, timeout=10)
    print(req.text)
    if req.status_code == 200:
        ress = json.loads(req.text)
        return ress["result"]


def signupNewUser(email, password):
    uri = f"https://www.googleapis.com/identitytoolkit/v3/relyingparty/signupNewUser?key={Vdata['key']}"
    data = {"email": email, "password": password}
    req = httpx.post(uri, data=json.dumps(data), headers=Vheader)
    if req.status_code == 200:
        ress = json.loads(req.text)
        print(f"signupNewUser : {len(ress)}")
        Vdata["idToken"] = ress["idToken"]
        return True
    print(req.text)
    return False
