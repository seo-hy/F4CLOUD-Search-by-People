
## F4CLOUD-Search-by-People

### AWS - IAM Access
   -  AmazonS3FullAccess
   -  AmazonRekognitionFullAccess

### Implementation
![image](https://user-images.githubusercontent.com/68395698/120573645-dedb1d00-c458-11eb-853e-0b78f7904236.png)


###  API
* Create collection
   * Create AWS Rekognition Collection
* Add faces
   * Create face Id after extracting faces from photos
   * Test similarity
   * Existing face -> Set face group
   * New face -> Create face group and set
* List all face groups
* List members of the face group 
* Set display name of the face group
* Search by people
    * Search by display name      
* Delete face
   * Delete the face group if there is no member of the face group to which it belongs 
* Delete collection
         
### Sample : Face Group
![KakaoTalk_20210521_000054973](https://user-images.githubusercontent.com/68395698/119002258-ae5ea200-b9c7-11eb-80bc-155df0218856.gif)

