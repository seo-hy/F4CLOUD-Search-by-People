import boto3

def add_faces_to_collection(fileAddress, collectionId):
    client = boto3.client('rekognition')

    # process file address
    # file address format : S3 URI
    file_address = fileAddress
    tmp = file_address[5:]
    bucket = tmp[:tmp.find('/')]
    file_path = tmp[tmp.find('/')+1:]

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

    if(len(unindex_faces)!=0):
        print('Faces not indexed:')
        for unindexedFace in unindex_faces:
            print(' Location: {}'.format(unindexedFace['FaceDetail']['BoundingBox']))
            print(' Reasons:')
            for reason in unindexedFace['Reasons']:
                print('   ' + reason)

    return len(face_records)


def main():
    #collection_id = '<collection_id>'
    #file_address = '<file_address>'

    indexed_faces_count = add_faces_to_collection(file_address, collection_id)
    print("Faces indexed count: " + str(indexed_faces_count))


if __name__ == "__main__":
    main()