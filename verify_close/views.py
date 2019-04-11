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

@csrf_exempt
def verify_close(name):
    print("verify_close 호출")
    # url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query='+str(name)
    # headers = {
    #     'user-agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
    # }
    # try:
    #     response = requests.get(url, headers=headers)
    #     if(response.status_code != 200):
    #         response.raise_for_status()
    # except HTTPError:
    #     return JsonResponse({'message' : 'Error at crawling' + name})
    # html = response.text
    # soup = BeautifulSoup(html, 'html.parser')
    # list = soup.select('.biz_name')
    # list2 = soup.select('#sp_local_1 > div.tit_area > a > strong')
    # list3 = soup.select('#sp_local_1 > dl > dt > a')
    # if (not list) and (not list2) and (not list3):
    #     sleep(0.5)
    #     return name
    # else:
    #     sleep(0.5)
    #     return 'open'

@csrf_exempt
def main(request):
    print("test")
    # rest_response = requests.get('https://devbotfood.jellylab.io:6001/api/v1/users/get_all_restaurant')
    # rest = json.loads((rest_response.text))
    # print(rest)
    # p = Pool(3)
    # result = p.map(verify_close, rest)
    # p.close()
    # p.join()
    # # result = map(verify_close, rest)
    # print(result)
    # result = [x for x in result if x != 'open']
    # print(result)
    # for i in result:
    #     print(i)
    #     subway, res_name = i.split(None,maxsplit=1)
    #     query_header = {
    #     'Content-Type': 'application/json'}
    #     data = {"res_name" : res_name,"subway" : subway}
    #     try:
    #         query_response = requests.post('https://devbotfood.jellylab.io:6001/api/v1/users/update_closedown', headers=query_header, data=json.dumps(data))
    #         if(query_response.status_code != 200):
    #             query_response.raise_for_status()
    #     except HTTPError:
    #         return JsonResponse({'message' : 'Error at updating query' + subway + res_name})
    #     sleep(0.5)
    return JsonResponse({'message' : 'success'})


#
# if __name__ == '__main__':
#     main()
