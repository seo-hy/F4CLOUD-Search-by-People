#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3
from botocore.exceptions import ClientError
from os import environ

def create_collection(collection_id):

    client=boto3.client('rekognition')

    #Create a collection
    print('Creating collection:' + collection_id)
    response=client.create_collection(CollectionId=collection_id)
    print('Collection ARN: ' + response['CollectionArn'])
    print('Status code: ' + str(response['StatusCode']))
    print('Done...')


def list_collections():
    max_results = 2

    client = boto3.client('rekognition')

    # Display all the collections
    print('Displaying collections...')
    response = client.list_collections(MaxResults=max_results)
    collection_count = 0
    done = False

    while done == False:
        collections = response['CollectionIds']

        for collection in collections:
            print(collection)
            collection_count += 1
        if 'NextToken' in response:
            nextToken = response['NextToken']
            response = client.list_collections(NextToken=nextToken, MaxResults=max_results)

        else:
            done = True

    return collection_count


def delete_collection(collection_id):
    print('Attempting to delete collection ' + collection_id)
    client = boto3.client('rekognition')
    status_code = 0
    try:
        response = client.delete_collection(CollectionId=collection_id)
        status_code = response['StatusCode']

    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceNotFoundException':
            print('The collection ' + collection_id + ' was not found ')
        else:
            print('Error other than Not Found occurred: ' + e.response['Error']['Message'])
        status_code = e.response['ResponseMetadata']['HTTPStatusCode']
    return (status_code)

def main():
    #Create a collection
    collection_id='<collection_id>'
    create_collection(collection_id)

    #List Collections
    #collection_count=list_collections()
    #print("collections: " + str(collection_count))

    #Delete a collection
    #collection_id = '<collection_id>'
    #status_code = delete_collection(collection_id)
    #print('Status code: ' + str(status_code))

if __name__ == "__main__":
    main()