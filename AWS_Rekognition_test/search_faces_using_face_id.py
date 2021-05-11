import boto3


def search_face_using_face_id(faceId, collectionId):
    threshold = 90
    max_faces = 5 # max result number to find in a collection
    client = boto3.client('rekognition')

    face_id = faceId
    collection_id = collectionId

    response = client.search_faces(CollectionId=collection_id,
                                   FaceId=face_id,
                                   FaceMatchThreshold=threshold,
                                   MaxFaces=max_faces)

    face_matches = response['FaceMatches']
    # Even if input face id is in the collection, results do not include input face id
    print('Matching faces')
    for match in face_matches:
        print('FaceId:' + match['Face']['FaceId'])
        print('Similarity: ' + "{:.2f}".format(match['Similarity']) + "%")
        print()

    return len(face_matches)


def main():
    face_id = '<xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx>'
    collection_id = '<collection_id>'


    faces_count = search_face_using_face_id(face_id, collection_id)
    print("faces found: " + str(faces_count))


if __name__ == "__main__":
    main()