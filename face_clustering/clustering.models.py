# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class FaceInfo(models.Model):
    face_id = models.CharField(primary_key=True, max_length=255)
    user_id = models.CharField(max_length=255)
    file_id = models.CharField(max_length=255)
    group_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'face_info'


class FileInfo(models.Model):
    file_id = models.CharField(primary_key=True, max_length=255)
    file_address = models.CharField(max_length=225)
    user_id = models.CharField(max_length=255)
    file_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'file_info'


class GroupInfo(models.Model):
    group_id = models.CharField(primary_key=True, max_length=255)
    user_id = models.CharField(max_length=255)
    rep_faceid = models.CharField(max_length=255)
    rep_faceaddress = models.CharField(max_length=255)
    custom_groupname = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'group_info'


class UserInfo(models.Model):
    user_id = models.CharField(primary_key=True, max_length=255)
    collection_id = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'user_info'
