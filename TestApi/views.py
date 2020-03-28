from django.shortcuts import render
import requests


def home(request):
    req=requests.get('https://api.kawalcorona.com/indonesia/provinsi')
    data=req.json()

    return render (request,'TestApi/home.html',{ 
    "name" : data,
    })

