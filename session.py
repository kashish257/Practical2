import boto3 

client = boto3.client("s3",aws_access_key_id="AKIAZVOSVHEFZRIKIJVU",aws_secret_access_key="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")

# response=client.create_bucket(Bucket="kjkhj")
response=client.list_buckets()

for i in response['Buckets']:
    print(i)
