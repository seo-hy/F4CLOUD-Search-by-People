<!-- TABLE OF CONTENTS -->
### Table of Contents
<ol>
  <li>
    <a href="#about-the-project">About The Project</a>
  </li>
  <li>
    <a href="#getting-started">Getting Started</a>
    <ul>
      <li><a href="#AWS-Setting">AWS Setting</a></li>
      <li><a href="#installation">Installation</a></li>
    </ul>
  </li>
  <li><a href="#usage">Usage</a></li>
  <li><a href="#license">License</a></li>
  <li><a href="#contact">Contact</a></li>
  <li><a href="#acknowledgements">Acknowledgements</a></li>
</ol>

<!-- GETTING STARTED -->
## Getting Started

### AWS Setting
1. IAM Access
    * AmazonS3FullAccess
    * AmazonRekognitionFullAccess


2. Install AWS CLI
   <br>Run the msiexec command to run the MSI installer
    ```sh
    msiexec.exe /i https://awscli.amazonaws.com/AWSCLIV2.msi
    ```
   Confirm the installation
    ```sh
    aws --version
    ```
3. Install AWS SDK for Python (Boto3)
    ```sh
    pip install boto3
    ```

4. Configure the credentials
   ```sh
    aws configure
   ```
   Input your Access key id and secret access key<br>
   Input your aws region (ex: us-east-1)
  
### Installation
* boto3
