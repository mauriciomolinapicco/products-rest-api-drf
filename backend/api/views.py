import json
from django.forms.models import model_to_dict
from products.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer

@api_view(['POST'])  #drf api view
def api_home(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):  #This gives 
        #instance = serializer.save()
        print(serializer.data)
        return Response(serializer.data)
    
    
    #return Response({'invalid': 'not valid data'}) 
        #this would go only if i didnt use the raise_exception on is_valid