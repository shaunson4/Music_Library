from rest_framework import serializers
from .models import Music

class MusicSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Music
        fields = ['id','title', 'artist', 'album', 'release_date', 'genry', 'likes']