from django.shortcuts import render

# Create your views here.
from clustering.models import FileInfo
from clustering.models import FaceInfo
from clustering.models import UserInfo
from clustering.models import GroupInfo
from clustering.serializers import AddFaceSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import boto3
from datetime import datetime
from PIL import Image, ImageDraw
import requests
from io import BytesIO
import io


class faces(APIView):
    def post(self, request):
        if request.method == 'POST':
            data = request.data
            file_id = data['file_id']
            user_id = data['user_id']
            client = boto3.client('rekognition')
            print(file_id,user_id)
            # get file address using file id
            file_address = FileInfo.objects.values('file_address').distinct().filter(file_id=file_id, user_id=user_id)
            serializer = AddFaceSerializer(file_address)
            file_address = file_address[0]['file_address']

            # file_address format : object URL
            proc = file_address[8:]
            bucket = proc[:proc.find('.')]
            file_path = proc[proc.find('/') + 1:]
            print(bucket, file_path)
            if file_path.find('/') != -1:
                file_name = file_path
                while (file_name.find('/') != -1):
                    file_name = file_name[file_name.find('/') + 1:]
            else:
                file_name = file_path

            if file_name.find('/') != -1:
                file_name = file_name[file_name.find('/') + 1:]

            # get collection id using user id
            collection_id = UserInfo.objects.values('collection_id').distinct().filter(user_id=user_id)
            collection_id = collection_id[0]['collection_id']

            # set max number of face to add
            add_max_faces = 3

            # add faces to collection
            response = client.index_faces(CollectionId=collection_id,
                                          Image={'S3Object': {'Bucket': bucket, 'Name': file_path}},
                                          ExternalImageId=file_name,
                                          MaxFaces=add_max_faces,
                                          QualityFilter="AUTO",
                                          DetectionAttributes=['ALL'])
            # process result
            face_records = response['FaceRecords']
            unindex_faces = response['UnindexedFaces']

            if (len(face_records) == 0):
                # case1 : There is no person in this image
                print('No Person in Photo')
            else:
                print('Faces indexed:')
                for faceRecord in face_records:
                    # case2 : There is people in this image

                    print('  Face ID: ' + faceRecord['Face']['FaceId'])
                    print('  Location: {}'.format(faceRecord['Face']['BoundingBox']))

                    ## Check if there is already the same person

                    # Set threshold for similarity
                    threshold = 95

                    # Set max result number to find in a collection
                    max_faces = 1
                    client = boto3.client('rekognition')

                    face_id = faceRecord['Face']['FaceId']
                    location = faceRecord['Face']['BoundingBox']
                    response = client.search_faces(CollectionId=collection_id,
                                                   FaceId=face_id,
                                                   FaceMatchThreshold=threshold,
                                                   MaxFaces=max_faces)

                    face_matches = response['FaceMatches']

                    # Even if input face id is in the collection, results do not include input face id
                    if (len(face_matches) == 0):
                        # case2-1 : There is no same person in collection
                        print('New Person')
                        s3_client = boto3.client('s3')

                        ## set initial name of new group
                        timestamp = datetime.now().strftime('%y%m%d%H%M%S')
                        group_name_prefix = user_id
                        new_group_id = group_name_prefix + timestamp

                        add_new_face = FaceInfo.objects.create(face_id=face_id, group_id=new_group_id, user_id=user_id, file_id=file_id)

                        print(file_address)
                        img_response = requests.get(file_address)
                        img = Image.open(BytesIO(img_response.content))
                        width, height = img.size
                        left = width * location['Left']
                        top = height * location['Top']
                        crop_loc = (left, top, left + (width * location['Width']), top + (height * location['Height']))
                        crop_img = img.crop(crop_loc)
                        # crop_img.show()
                        # save crop image
                        rep_img = io.BytesIO()
                        img_format = "JPEG"
                        crop_img.save(rep_img, img_format)
                        rep_img.seek(0)

                        url_gen = new_group_id + '.' + img_format

                        s3_prefix = 'https://f4cloudtest1.s3.amazonaws.com/'
                        s3_client.upload_fileobj(
                            rep_img,
                            bucket,
                            url_gen,
                            ExtraArgs={
                                "ContentType": 'image/jpeg'
                            }
                        )
                        rep_faceaddress = s3_prefix + url_gen
                        rep_faceid = face_id
                        create_group = GroupInfo.objects.create(group_id = new_group_id, user_id=user_id,rep_faceid=rep_faceid, rep_faceaddress=rep_faceaddress)
                    else:
                        # case2-2 : There is same person in collection
                        print('add into existing group')
                        for match in face_matches:
                            print('FaceId:' + match['Face']['FaceId'])
                            print('Similarity: ' + "{:.2f}".format(match['Similarity']) + "%")
                            match_face_id = match['Face']['FaceId']

                            get_group_id = FaceInfo.objects.values('group_id').distinct().filter(face_id = match_face_id,user_id=user_id)
                            group_id = get_group_id[0]['group_id']
                            add_new_face = FaceInfo.objects.create(face_id=face_id, group_id=group_id,
                                                                   user_id=user_id, file_id=file_id)

            if (len(unindex_faces) != 0):
                print('Faces not indexed:')
                for unindexedFace in unindex_faces:
                    print(' Location: {}'.format(unindexedFace['FaceDetail']['BoundingBox']))
                    print(' Reasons:')
                    for reason in unindexedFace['Reasons']:
                        print('   ' + reason)

        return Response({'msg':'complete'})
