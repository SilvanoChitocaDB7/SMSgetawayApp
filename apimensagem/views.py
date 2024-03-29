from django.shortcuts import render, redirect
from django.http import HttpResponse
from os import name
import json
import requests




def index(request):

    if request.POST:
        mensagem=str(request.POST.get('mensagem'))
        telefone=str(request.POST.get('telefone'))
        url = "https://api.useombala.ao/v1/messages"
        data = {"message":mensagem,"from":"924680610","to":telefone}
        token = 'c570185f-ac81-4da1-a03f-85e85d5c8656'
        headers ={'Authorization':f'Token {token}','Content-Type': 'application/json'}
        response=requests.post(url,headers=headers,data=json.dumps(data))
        print(response.text)
        print(response.status_code)

    
    return render(request,'index.html')


