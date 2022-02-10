from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ImageSerializer
class ImageViewSet(viewsets.ModelViewSet):

    @api_view(['POST'])
    def create(request):
        try:
            print(request.get_host())
            serializer = ImageSerializer(data = request.data)
            if(serializer.is_valid()):
                serializer.save()

            print("serializer.data",serializer.data['image'])
            return Response({
            'status' : True,
            'images' : "{}{}".format(request.get_host(), serializer.data['image'])  
            })
        except Exception as e:
            print("e",e)