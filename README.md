
## F4CLOUD-Search-by-People

### AWS - IAM Access
   -  AmazonS3FullAccess
   -  AmazonRekognitionFullAccess

### Implementation
![image](https://user-images.githubusercontent.com/68395698/120728514-0e049380-c518-11eb-8faa-792f752536c5.png)
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
   * Delete the face group if there is no member of the face group to which the face id deleted belongs 
* Delete collection
         
### Sample1 : Face Group List and Detail
![KakaoTalk_20210521_000054973](https://user-images.githubusercontent.com/68395698/119002258-ae5ea200-b9c7-11eb-80bc-155df0218856.gif)


### Sample2 : Upload and Delete
1. I'm going to upload these two images

![test](https://user-images.githubusercontent.com/68395698/120960103-1ec23d00-c796-11eb-890a-9f32acee6308.png)

2. Fisrt, Upload the first image. The results are as follow. A new person(face) is uploaded and new face group is created

![KakaoTalk_20210607_134812714](https://user-images.githubusercontent.com/68395698/120960601-29c99d00-c797-11eb-88c3-56e065b59976.gif)


3. Then upload the second image. A new person and the person on the drive(F4CLOUD) are uploaded. 
 * A new person(face) is uploaded and new face group is created
 * The person(face) on the drive is added. So add it to the matched face group
 
![KakaoTalk_20210607_134812714_01](https://user-images.githubusercontent.com/68395698/120961048-03f0c800-c798-11eb-8ef1-a45b5d977d8f.gif)


4. Delete the previously uploaded image(second image). In the second face group there is no member, so delete that face group.

![KakaoTalk_20210607_134812714](https://user-images.githubusercontent.com/68395698/120961241-6053e780-c798-11eb-8429-2ec877cb018d.gif)
   




