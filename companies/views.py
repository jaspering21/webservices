from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Stock
from .serializers import StockSerializer
from django.http import HttpResponse
from django.shortcuts import render, HttpResponse

def homepage(request):
    #return HttpResponse('Home Page')
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'companies/ticker.html')

'''class StockList(APIView):

    def homepage(request):
        return HttpResponse('Home Page')
        #return render(request, 'companies/ticker.html')

    def get (self, request):
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks, many=True)
        return Response(serializer.data)

    def post(self):
        pass
'''