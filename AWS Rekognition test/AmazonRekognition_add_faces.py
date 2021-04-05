import boto3


def add_faces_to_collection(bucket, photo, collection_id):
    client = boto3.client('rekognition')
    # Processing files in folders
    if photo.find('/') != -1:
        photo_key = photo[photo.find('/')+1:]
    else:
        photo_key = photo
    #print(photo_key)

    response = client.index_faces(CollectionId=collection_id,
                                  Image={'S3Object': {'Bucket': bucket, 'Name': photo}},
                                  ExternalImageId=photo_key,
                                  MaxFaces=1,
                                  QualityFilter="AUTO",
                                  DetectionAttributes=['ALL'])

    print('Results for ' + photo)
    print('Faces indexed:')
    for faceRecord in response['FaceRecords']:
        print('  Face ID: ' + faceRecord['Face']['FaceId'])
        print('  Location: {}'.format(faceRecord['Face']['BoundingBox']))

    print('Faces not indexed:')
    for unindexedFace in response['UnindexedFaces']:
        print(' Location: {}'.format(unindexedFace['FaceDetail']['BoundingBox']))
        print(' Reasons:')
        for reason in unindexedFace['Reasons']:
            print('   ' + reason)
    return len(response['FaceRecords'])


def main():
    bucket = '<bucket>'

    collection_id = '<collectoin_id>'
    photo = '<photo>'
    indexed_faces_count = add_faces_to_collection(bucket, photo, collection_id)
    print("Faces indexed count: " + str(indexed_faces_count))


if __name__ == "__main__":
    main()