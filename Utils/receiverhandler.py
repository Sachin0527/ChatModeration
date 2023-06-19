import os
import json
import requests
import pythoncom
import win32com.client

class IDataRetriever:
    def get_data(self):
        pass

# class ApiRetriever(IDataRetriever):
#     def __init__(self, api_url):
#         self.api_url = api_url
#     def get_data(self):
#         return requests.get(self.api_url)

# class FileRetriever(IDataRetriever):
#     def __init__(self, file_path):
#         self.file_path = file_path
#     def get_data(self):
#         with open(self.file_path, 'r') as file:
#             return file.read()

# class MsmqRetriever(IDataRetriever):
#     def __init__(self, queue_name):
#         self.queue_name = queue_name
#     def get_data(self):
#         queue_info = win32com.client.Dispatch("MSMQ.MSMQQueueInfo")
#         computer_name = os.getenv('COMPUTERNAME')
#         queue_name = self.queue_name
#         queue_info.FormatName = f'direct=os:{computer_name}\\PRIVATE$\\{queue_name}'
#         msg_list = []
#         queue = queue_info.Open(1, 0)
#         while True:
#             msgs = queue.Peek(pythoncom.Empty, pythoncom.Empty, 1000)
#             if not msgs:
#                 #print(f'No more messages in {queue_name}')
#                 break
#             msg = queue.Receive()
#             #print(f'Got Message from {queue_name}: {msg.Label} - {msg.Body}')
#             msg_list.append({int(msg.label):msg.body})
#         return (msg_list)

# Example usage
"""
api_retriever = ApiRetriever('http://127.0.0.1:8080/djangoapi/apisample/')
api_data = api_retriever.get_data()
print(api_data)
"""

"""
file_retriever = FileRetriever('../TestData/messages.txt')
file_data = file_retriever.get_data()
print(file_data)
"""

"""
msmq_retriever = MsmqRetriever('one')
msmq_data = msmq_retriever.get_data()
print(msmq_data)
"""


