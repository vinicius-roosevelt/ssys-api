from django.shortcuts import render
from .models import Employee

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token

from django.db.models import Avg, Min
from .serializers import EmployeeSerializer

from datetime import datetime
from django.http import HttpResponse

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    

class ReportViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    @action(detail=False)
    def age(self, request):
        
        #FUNCION FOR CALCULATING THE AGES AVERAGE OF THE ENTIRE DATABASE
        def calcAverageAges(countAges, birthDates):
            sumAges = 0
            for x in range(countAges):
                year = birthDates[x]['birth_date'].split('-')[2]
                age = 2020-int(year)
                sumAges += age
            return (sumAges/countAges)

        youngerData = Employee.objects.all().order_by('-birth_date')
        younger = self.get_serializer(youngerData, many=True)
        younger = younger.data[0]

        olderData = Employee.objects.all().order_by('birth_date')
        older = self.get_serializer(olderData, many=True)
        older = older.data[0]

        allAgesData = Employee.objects.all()
        allAges = self.get_serializer(allAgesData, many=True)

        birthDate = allAges.data
        sumAges=0

        avgAges = calcAverageAges(allAgesData.count(), birthDate)
        
        response = {
            "younger":younger,
            "older":older,
            "average":avgAges 
        }

        return Response(response)
    
    @action(detail=False)
    def salary(self, request):
        lowestData = Employee.objects.all().order_by('salary')
        lowest = self.get_serializer(lowestData, many=True)
        lowest = lowest.data[0]

        highestData = Employee.objects.all().order_by('-salary')
        highest = self.get_serializer(highestData, many=True)
        highest = highest.data[0]
        
        average = Employee.objects.all().aggregate(Avg('salary'))
        
        response = {
            "lowest":lowest,
            "highest":highest,
            "average":average['salary__avg']
        }
        
        # serializer = self.get_serializer(recent_users, many=True)
        return Response(response)
# Create your views here.
