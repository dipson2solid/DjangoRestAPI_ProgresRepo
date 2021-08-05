from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from CustomerApp.models import Customers
from CustomerApp.serializers import CustomerSerializer



# Create your views here.

@csrf_exempt
def customerApi(request,id=0):
    if request.method=='GET':
        customers = Customers.objects.all()
        customers_serializer=CustomerSerializer(customers,many=True)
        return JsonResponse(customers_serializer.data,safe=False)
    elif request.method=='POST':
        customer_data=JSONParser().parse(request)
        customers_serializer=CustomerSerializer(data=customer_data)
        if customers_serializer.is_valid():
            customers_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        customer_data=JSONParser().parse(request)
        customer=Customers.objects.get(CustomerId=customer_data['CustomerId'])
        customers_serializer=CustomerSerializer(customer,data=customer_data)
        if customers_serializer.is_valid():
            customers_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        customer=Customers.objects.get(CustomerId=id)
        customer.delete()
        return JsonResponse("Deleted Successfully",safe=False)
