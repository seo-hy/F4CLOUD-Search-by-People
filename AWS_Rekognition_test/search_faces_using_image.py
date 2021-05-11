
import boto3

def search_faces_using_image(fileAddress, collectionId):
    # process file address
    file_address = fileAddress
    tmp = file_address[5:]
    bucket = tmp[:tmp.find('/')]
    file_path = tmp[tmp.find('/') + 1:]

    print(bucket, file_address)
    collection_id = collectionId

    # set max face num
    max_faces = 100 # result number to find in a collection
    threshold = 70

    client = boto3.client('rekognition')

    response = client.search_faces_by_image(CollectionId=collection_id,
                                            Image={'S3Object': {'Bucket': bucket, 'Name': file_path}},
                                            FaceMatchThreshold=threshold,
                                            MaxFaces=max_faces)

    face_matches = response['FaceMatches']
    if(len(face_matches)==0):
        print('No Matching faces')
    else:
        print('Matching faces : '+str(len(face_matches)))
        for match in face_matches:
            print('ImageId: '+match['Face']['ExternalImageId'])
            print('FaceId:' + match['Face']['FaceId'])
            print('Similarity: ' + "{:.2f}".format(match['Similarity']) + "%")
            print()

if __name__ == "__main__":
    collection_id = '<collection_id>'
    file_address = '<file_address>'

    search_faces_using_image(file_address, collection_id)
