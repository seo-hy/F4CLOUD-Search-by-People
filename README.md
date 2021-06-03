
## F4CLOUD-Search-by-People

### AWS - IAM Access
   -  AmazonS3FullAccess
   -  AmazonRekognitionFullAccess

### Implementation
![image](https://user-images.githubusercontent.com/68395698/120574037-85272280-c459-11eb-8000-a83762a292d7.png)


###  API
* Create collection
   * Create AWS Rekognition Collection
* Add faces
   * Create face Id after extracting faces from photos
   * Test similarity
   * Existing face -> Add to face group
   * New face -> Create new face group
* List all face groups
* List members of the face group 
* Set display name of the face group
* Search by people
    * Search by display name      
* Delete face
   * Delete the face group if there is no member of the face group to which it belongs 
* Delete collection
         
### Sample : Face Group List and Detail
![KakaoTalk_20210521_000054973](https://user-images.githubusercontent.com/68395698/119002258-ae5ea200-b9c7-11eb-80bc-155df0218856.gif)

