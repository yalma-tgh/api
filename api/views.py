from rest_framework import generics

from .models import Item, Location
from . serilaizers import ItemSerializer , LocationSerializer



class ItemList(generics.ListCreateAPIView):
    serializer_class = ItemSerializer


    def get_queryset(self):
        queryset = Item.objects.all()
        location = self.request.query_params.get('Location')
        if location is not None:
            queryset = queryset.filter(itemLocatin=location)
        return queryset
    
class ItemDetail(generics.RetrieveUpdateAPIView):
    serializer_class = ItemSerializer
    queryset = Location.objects.all()


 
class LocationList(generics.ListCreateAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()



 
class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()