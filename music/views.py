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


@api_view(['GET', 'PUT','DELETE', 'PATCH'])
def music_detail(request, pk):
    music = get_object_or_404(Music, pk=pk)

    if request.method == 'GET':
        serializer = MusicSerializer(music)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MusicSerializer(music, data=request.data)
        serializer = is_valid(raise_exception=True)
        serializer = save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    elif request.method == 'DELETE':
        custom_response = {
            'Music Deleted': music.title
        }
        music.delete()
        return Response(custom_response, status=status.HTTP_200_OK)

    elif request.method == 'PATCH':
        if music.likes >= 0:
            music.likes += 1
        serializer = MusicSerializer(music, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    # try:
    #     music = Music.objects.get(pk=pk)
    # except Music.DoesNotExist:
    #     return Response (status=status.HTTP_404_NOT_FOUND)

    # return Response(pk)

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
            


