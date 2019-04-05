import boto3
import requests
from requests_aws4auth import AWS4Auth

host = 'https://search-okram-dev-es-dryn3bngfu.us-east-2.es.amazonaws.com/' # include https:// and trailing /
region = 'us-east-2' # e.g. us-west-1
service = 'es'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

# Register repository

path = '_snapshot/ava-dev-snapshot-repo' # the Elasticsearch API endpoint
url = host + path
print(url)

payload = {
  "type": "s3",
  "settings": {
    "bucket": "es-snapshot-okram",
    "region": "us-east-2",              #"endpoint": "s3.amazonaws.com" (if you are in us-east-1 region)
    "role_arn": "arn:aws:iam::874311019960:role/TheSnapshotRole"
  }
}

headers = {"Content-Type": "application/json"}

r = requests.put(url, auth=awsauth, json=payload, headers=headers)

print(r.status_code)
print(r.text)

# # Take snapshot
#
# path = '_snapshot/my-snapshot-repo/my-snapshot'
# url = host + path
#
# r = requests.put(url, auth=awsauth)
#
# print(r.text)
#
# # Delete index
#
# path = 'my-index'
# url = host + path
#
# r = requests.delete(url, auth=awsauth)
#
# print(r.text)
#
# # Restore snapshots (all indices)
#
# path = '_snapshot/my-snapshot-repo/my-snapshot/_restore'
# url = host + path
#
# r = requests.post(url, auth=awsauth)
#
# print(r.text)
#
# # Restore snapshot (one index)
#
# path = '_snapshot/my-snapshot-repo/my-snapshot/_restore'
# url = host + path
#
# payload = {"indices": "my-index"}
#
# headers = {"Content-Type": "application/json"}
#
# r = requests.post(url, auth=awsauth, json=payload, headers=headers)
#
# print(r.text)