import boto3

s3 = boto3.client('s3')
bucket_name = 'proyecto-final-epico'
file_name = 'ejemplo.txt'

s3.upload_file(file_name, bucket_name, file_name)
print(f"Archivo {file_name} subido a {bucket_name}")
