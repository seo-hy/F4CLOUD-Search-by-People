from rest_framework import serializers
from f4people.models import FileInfo
from f4people.models import GroupInfo
class AddFaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileInfo
        fields = ['file_address']

class GroupListSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupInfo
        fields = ['group_id','rep_fileid','rep_faceaddress','display_name','user_id','rep_faceid']

class GroupDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileInfo
        fields = ['file_address','file_id','user_id','file_name']

