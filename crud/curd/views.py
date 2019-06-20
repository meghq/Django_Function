# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from curd.models import Register

@api_view(['POST'])
def adding(request):
    print(request.data,"dataaa")
    obj=Register()
    obj.eid = request.data['eid']
    obj.ename = request.data['ename']
    obj.eaddress = request.data['eaddress']
    obj.save()
    return Response("hello")

@api_view(['GET'])
def get(request):
   print(request.data, "hell***************************************************888")
   details = Register.objects.all().values()
   print(request.data,"hell")

   return Response(details)

@api_view(['POST'])
def onedata(request):
    print(request.data,"onlyone")
    id=request.data['eid']
    print("gdshcfdshgc",id)
    single=Register.objects.filter(eid=id).values('ename','eaddress')

    return Response(single)

@api_view(['POST'])
def update(request):
    id=request.data['eid']
    getdata=Register.objects.filter(eid=id)
    if getdata:
        getdata.update(ename=request.data['ename'])
        return Response(getdata)



@api_view(['POST'])
def delete(request):
    id=request.data['eid']
    print (id)
    data=Register.objects.filter(eid=id)

    if data:
        data.delete()
        data={"message":"delete"}
        return Response(data)
    else:
        data={"message":"not deleted"}
        return Response(data)




