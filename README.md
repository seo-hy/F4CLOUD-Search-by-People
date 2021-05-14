## F4CLOUD : 사진에서 인물 검색

### AWS - IAM Access
   -  AmazonS3FullAccess
   -  AmazonRekognitionFullAccess

###  API Usage
1. Collection 생성
      * AWS Rekognition Collection 생성
2. 사진 업로드
      * 사진 속 얼굴 추출 후 Face Id 생성, Face Group 지정
      ```
      curl -d "{""file_id"":""<file_id>"", ""user_id"":""<user_id>""}" -H "Content-Type: application/json" -X POST http://localhost:8000/faces/      
      ```
3. 인물 검색
4. Face Group의 display name 설정
      
5. 사진 삭제
         
### Demo