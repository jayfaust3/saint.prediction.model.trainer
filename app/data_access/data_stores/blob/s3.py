from typing import Any
from os import getenv
from boto3 import client
from botocore.client import BaseClient
from botocore.response import StreamingBody
from data_access.data_stores.blob.base import BaseBlobClient


class S3Client(BaseBlobClient):

    # def __init__(self,
    #              s3_client: BaseClient) -> None:
    #     self.__s3_client: BaseClient = s3_client

    def __init__(self) -> None:
        self.__s3_client: BaseClient = client('s3',
                                              region_name=getenv('AWS_REGION'),
                                              aws_access_key_id=getenv('AWS_ACCESS_KEY_ID'),
                                              aws_secret_access_key=getenv('AWS_SECRET_ACCESS_KEY'),
                                              endpoint_url=getenv('S3_ENDPOINT'),
                                              use_ssl=False,
                                              verify=False)

    def get_blob(self, blob_directory: str, blob_name: str) -> bytes:
        response: Any = self.__s3_client.get_object(Bucket=blob_directory, Key=blob_name)

        stream: StreamingBody = response['Body']

        return stream.read()

    def post_blob(self, blob_directory: str, blob_name: str, data: Any) -> None:
        self.__s3_client.put_object(Bucket=blob_directory, Key=blob_name, Body=data)

        return
