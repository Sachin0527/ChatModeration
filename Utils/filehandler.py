import os
import json
import requests
import pythoncom
import win32com.client

from Utils.receiverhandler import IDataRetriever
from Utils.senderhandler import IDataSender


class FileRetriever(IDataRetriever):
    def __init__(self, file_path):
        self.file_path = file_path
    def get_data(self):
        with open(self.file_path, 'r') as file:
            return file.read()

class FileSender(IDataSender):
    def __init__(self, file_path):
        self.file_path = file_path.replace(".","_out.")
    def set_data(self, data):
        with open(self.file_path, 'w') as file:
            for item in data:
                file.write(item + '\n')
