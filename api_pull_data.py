import os
import requests
import pandas as pd
from google.cloud import storage

project_id = 'GCS_PROJECT_ID'
bucket_name = 'BUCKET_NAME'
bucket_file = 'user_demo_data.csv'
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= 'API_KEY.json'


def get_api_data(url):
 response = requests.get(url)
 df = pd.read_json(response.text)
 return df

def gcs_write_pandas(data):

 client = storage.Client(project_id)
 bucket = client.get_bucket(bucket_name)
 blob = bucket.blob(bucket_file)
 blob.upload_from_string(data.to_csv(), 'text/csv')


url = 'https://sheet.best/api/sheets/2f759380-b49d-4d22-b3a4-ac370122f9e1'
data_df = get_api_data(url)
gcs_write_pandas(data_df)



