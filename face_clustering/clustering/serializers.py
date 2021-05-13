from rest_framework import serializers
from clustering.models import FileInfo

class AddFaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileInfo
        fields = ['file_address']

