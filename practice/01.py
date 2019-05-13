# -*- coding: utf-8 -*-
from tkinter import *
from http.client import HTTPSConnection
from http.server import BaseHTTPRequestHandler, HTTPServer
import requests

import smtplib
from email.mime.text import MIMEText
ser=smtplib.SMTP("smtp.gmail.com",587)


ser.ehlo()
ser.starttls()



connect=None
Detail_url='http://openapi.tour.go.kr/openapi/service/TourismResourceService/getTourResourceDetail'
List_url="http://openapi.tour.go.kr/openapi/service/TourismResourceService/getTourResourceList"
Key='cYtnsiDywOollKA9No97lS%2B7V3H1tl2gq5F%2BJyzAxQ70dhlac0M8D84OwUrJkVVy5wC7NwpkGa05zzXUIl3BWA%3D%3D'


def connectOpenAPIServer():
    global conn, server
    conn = HTTPSConnection(server)
    conn.set_debuglevel(1)

def userURLBuilder(url, **user):
    str = url + "?"
    for key in user.keys():
        str += key + "=" + user[key] + "&"
    return str

url = userURLBuilder(List_url,ServiceKey=Key, SIDO="서울특별시", GUNGU="종로구", RES_NM="")
url_D=userURLBuilder(Detail_url,ServiceKey=Key, SIDO="서울특별시", GUNGU="종로구", RES_NM="경복궁")
res=requests.get(url_D)


print(url_D)
print(res.text)