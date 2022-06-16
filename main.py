from google.cloud import storage
from flask import escape
import functions_framework
import json
from random import randrange

# get GCS bucket for storing data
BUCKET_NAME = 'func-data'
storage_client = storage.Client.from_service_account_json('faas-hw-074966470cb7.json')
BUCKET = storage_client.get_bucket(BUCKET_NAME)

# generate random file name
filename = 'data-' + str(randrange(1000)) +".json"


@functions_framework.http
def func_http(request):
    """
    This function reads json file from Cloud Storage and saves data from function call to it. 
    """
    blob = BUCKET.blob(filename)

    # processing of the input request from user
    request_json = request.get_json(silent=True)
    
    # upload data to the file
    blob.upload_from_string(
    data=json.dumps(request_json),
    content_type='application/json'
        )

    return 'Hello {}! Your request has been save to Cloud Storage object'.format(escape(request_json['name']))
