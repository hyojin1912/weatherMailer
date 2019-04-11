# # -*- coding:utf-8 -*-
import requests
from requests import HTTPError
from bs4 import BeautifulSoup
from multiprocessing import Pool
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from time import sleep
import json
import smtplib, ssl

@csrf_exempt
def main(request):

    # 날씨정보 크롤링
    url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8&oquery=%EC%9B%90%EC%A3%BC+%EB%82%A0%EC%94%A8&tqi=U6xA5dp0JXVssA9WTuGssssstmZ-432536'
    res = requests.get(url)
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    found = soup.find("div",{"class": "sc cs_weather _weather"})
    found2 = found.find("div", {"class": "info_data"})
    found3 = found2.find("p", {"class": "cast_txt"})
    wt_summary = found3.text

    # 파이썬 메일 보내기 템플릿
    port = 465  # For SSL
    senderEmail = "chaosjin1912@gmail.com"
    password = input("Type your password and press enter: ")
    subject = "python mail test"
    message = 'Subject: {}\n\n{}'.format(subject, wt_summary).encode('utf-8')

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("chaosjin1912@gmail.com", password)
        server.sendmail("chaosjin1912@gmail.com", "chaosjin1912@gmail.com", message)

    return JsonResponse({'message' : 'success'})

# if __name__ == '__main__':
#     main()
