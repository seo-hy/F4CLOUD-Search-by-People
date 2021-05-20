
## F4CLOUD : 사진에서 인물 검색

### AWS - IAM Access
   -  AmazonS3FullAccess
   -  AmazonRekognitionFullAccess

###  API Usage
1. Collection 생성
      * AWS Rekognition Collection 생성
2. Face 추가
      * 사진 속 얼굴 추출 후 Face Id 생성, 유사도 테스트
      * 존재하는 Face -> Face Group 지정
      * 새로운 Face -> Face Group 생성 후 지정
3. 전체 Face Group 리스트
4. 특정 Face Group 멤버 리스트 
5. 특정 Face Group의 display name 설정
6. 인물 검색
      * display name 검색      
8. Face 삭제
      * 해당 Face가 속한 Face Group의 멤버가 없을 시 Face Group 삭제 
         
### Sample
![KakaoTalk_20210521_000054973](https://user-images.githubusercontent.com/68395698/119002258-ae5ea200-b9c7-11eb-80bc-155df0218856.gif)

