from django.shortcuts import render

from main.models import Collection
from .forms import CollectionForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . serializer import CollectionSerializer

def Home(request):
    if request.method=='POST':
        form=CollectionForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    form=CollectionForm()
    data=Collection.objects.all()
    return render(request,'index.html',{'form':form,'data':data})

class HomeClass(APIView):
    def post(self,request,format=None):
        serializer=CollectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data is successfully posted','status':'success','data':serializer.data},status=status.HTTP_201_CREATED)

    def get(self,request,format=None):
        data=Collection.objects.all()
        serializer=CollectionSerializer(data,many=True)
        return Response({'msg':'Data is successfully retrived','status':'success','data':serializer.data},status=status.HTTP_200_OK)


    
