from rest_framework import generics
from django.shortcuts import render
from rest_framework import views
from .serializers import GetSensorDataSerializer
from rest_framework.response import Response
from . import models

# Create your views here.


class GetSensorDataView(views.APIView):
    serializer_class=GetSensorDataSerializer
    allowed_methods=["POST","GET"]


    def post(self,request,*args,**kwargs):
        data=request.data
        serializer=self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(data)
        return Response(serializer.data)


class RetrieveDataView(generics.ListAPIView):
    queryset=models.Sensors.objects.all()
    serializer_class=GetSensorDataSerializer

    def get(self, request, *args, **kwargs):
        RetrieveDataView.queryset=models.Sensors.objects.all().order_by("-id")[:10]
        return self.list(request,*args,**kwargs)


class QueryData(generics.ListAPIView):
    serializer_class=GetSensorDataSerializer
    queryset=models.Sensors.objects.all()

    def get(self, request, *args, **kwargs):
        QueryData.queryset=models.Sensors.objects.filter(date_created=kwargs["date_created"])
        return self.list(request, *args, **kwargs)                                                                                 