from urllib.request import Request, urlopen
import json
import re
import time
import datetime
from win10toast import ToastNotifier
import os
import cowin_v2

pause = False

def get_data():
    current_time = datetime.datetime.now() 
    print("running... ",current_time)
    today = str(current_time.day) +"-"+ str(current_time.month)  +"-"+ str(current_time.year) 
    first_url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=571&date="+today

    # print(first_url)
    data = {}
    
    # time.sleep(1)
   
    req = Request(first_url, headers={'User-Agent': 'Mozilla/5.0'} )
    inp = urlopen(req)
    resp = json.load(inp)

    for i in resp['centers']:
        if i['fee_type'] == "Paid":
            for j in i['sessions']:
                if j["min_age_limit"] == 18:
                    if j["vaccine"] == "COVAXIN":    
                        # data[i['name']] [j["date"]] = j["available_capacity"]
                        # print( j["date"] , j["available_capacity"] )
                        if j["available_capacity_dose2"] > 0:
                            # print("Slots Avaialble")
                            print(j["date"] +" "+ i["name"]  +" "+ str(j["available_capacity"]) )
                            toast.show_toast("Notification","Vacant",duration=4)
                            # os.system('python cowin_v2.py')
                            cowin_v2.main(i["pincode"])
                            input("proceed?")
                            pause = True
        
    return False

toast = ToastNotifier()

while not pause:
    get_data()
    time.sleep(5)

