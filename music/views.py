from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import MusicSerializer
from .models import Music



@api_view(['GET', 'POST'])
def music_list(request):

    if request.method == 'GET':
        music = Music.objects.all()
        serializer = MusicSerializer(music, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MusicSerializer(data=request.data)
        if serializer.is_valid() == True:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def music_detail(request, pk):
    try:
        music = Music.objects.get(pk=pk)
    except Music.DoesNotExist:
        return Response (status=status.HTTP_404_NOT_FOUND)

    return Response(pk)

# BELOW is what the above code COULD BE changed to in order to have a minimal way of coding the functionality
# ABOVE POST section we imported the status calls from the rest_framework in order to send the HTTP message requests as needed
#   if request.method == 'GET':
#         music = Music.objects.all()
#         serializer = MusicSerializer(music, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = MusicSerializer(data=request.data)
#         serializer.is_valid( raise_exception = True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#        
            


