import boto3
from PIL import Image
import requests
from io import BytesIO
import io
import boto3


def extract_and_save_face(fileAddress, collectionId):
    client = boto3.client('rekognition')
    s3_client = boto3.client('s3')
    # process file address
    # file_address format : object URL
    file_address = fileAddress
    tmp = file_address[8:]
    bucket = tmp[:tmp.find('.')]
    file_path = tmp[tmp.find('/')+1:]
    print(bucket, file_path)
    if file_path.find('/') != -1:
        file_name = file_path
        while (file_name.find('/') != -1):
            file_name = file_name[file_name.find('/') + 1:]
    else:
        file_name = file_path

    if file_name.find('/') != -1:
        file_name = file_name[file_name.find('/')+1:]
    # set max face num
    max_faces = 3

    collection_id = collectionId
    # print(bucket, file_path, file_name)

    response = client.index_faces(CollectionId=collection_id,
                                  Image={'S3Object': {'Bucket': bucket, 'Name': file_path}},
                                  ExternalImageId=file_name,
                                  MaxFaces=max_faces,
                                  QualityFilter="AUTO",
                                  DetectionAttributes=['ALL'])

    # print output
    print('Results for ' + file_name)

    face_records = response['FaceRecords']
    unindex_faces = response['UnindexedFaces']
    if(len(face_records)==0):
        print('No Person in Photo')
    else:
        print('Faces indexed:')
        for faceRecord in face_records:
            print('  Face ID: ' + faceRecord['Face']['FaceId'])
            print('  Location: {}'.format(faceRecord['Face']['BoundingBox']))
            face_id = faceRecord['Face']['FaceId']
            location = faceRecord['Face']['BoundingBox']

            #get original image
            response = requests.get(file_address)
            img = Image.open(BytesIO(response.content))

            #get location of the face
            width, height = img.size
            left = width * location['Left']
            top = height * location['Top']

            #crop image
            crop_loc = (left,top, left + (width * location['Width']), top +(height * location['Height']))
            crop_img = img.crop(crop_loc)
            #crop_img.show()

            # save crop image in s3
            rep_img = io.BytesIO()
            img_format = "JPEG" # set file format
            crop_img.save(rep_img,img_format)
            rep_img.seek(0)
            url_gen = face_id + '.'+img_format # set file url
            s3_client.upload_fileobj(
                rep_img,
                bucket,
                url_gen,
                ExtraArgs={
                    "ContentType": 'image/jpeg'
                }
            )




    if(len(unindex_faces)!=0):
        print('Faces not indexed:')
        for unindexedFace in unindex_faces:
            print(' Location: {}'.format(unindexedFace['FaceDetail']['BoundingBox']))
            print(' Reasons:')
            for reason in unindexedFace['Reasons']:
                print('   ' + reason)

    return len(face_records)


def main():
    collection_id = '<collection_id>'
    file_address = '<file_address>' # s3 object URL
    indexed_faces_count = extract_and_save_face(file_address, collection_id)
    print("Faces indexed count: " + str(indexed_faces_count))


if __name__ == "__main__":
    main()