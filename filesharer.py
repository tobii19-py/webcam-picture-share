import os
from filestack import Client


class FileSharer:

    def __init__(self, filepath):
        self.filepath = filepath
        self.api_key = os.getenv("FILESTACK")

    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url

