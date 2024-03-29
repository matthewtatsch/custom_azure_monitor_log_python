import os
from azure.core.exceptions import HttpResponseError
from azure.identity import DefaultAzureCredential
from azure.monitor.ingestion import LogsIngestionClient

endpoint = os.environ['DATA_COLLECTION_ENDPOINT']
credential = DefaultAzureCredential()

client = LogsIngestionClient(endpoint=endpoint, credential=credential)

rule_id = os.environ['LOGS_DCR_RULE_ID']
body = [
      {
        "Message": "Another informational log.",
        "Level": "info"
      },
      {
        "Message": "Another warning log.",
        "Level": "warning"
      },
      {
        "Message": "Another error log.",
        "Level": "error"
      }
    ]

try:
    client.upload(rule_id=rule_id, stream_name=os.environ['LOGS_DCR_STREAM_NAME'], logs=body)
except HttpResponseError as e:
    print(f"Upload failed: {e}")