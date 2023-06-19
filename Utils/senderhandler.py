import os
import json
import requests
import pythoncom
import win32com.client

class IDataSender:
    def set_data(self, data):
        pass

# class ApiSender(IDataSender):
#     def __init__(self, api_url):
#         self.api_url = api_url
#     def set_data(self, data):
#         url_orig = self.api_url
#         for element in data:
#             msg_id = int(element['msg_id'])
#             msg_desc = element['msg_desc']
#             msg_moderate_status = element['msg_moderate_status']
#             msg_processed = element['msg_processed']
#             data = {
#                 'msg_moderate_status': msg_moderate_status,
#                 'msg_processed': msg_processed
#             }
#             url = url_orig + f'{msg_id}/'
#             print(url)
#             response = requests.put(url, data=data)
#             print(response.status_code)


# class FileSender(IDataSender):
#     def __init__(self, file_path):
#         self.file_path = file_path.replace(".","_out.")
#     def set_data(self, data):
#         with open(self.file_path, 'w') as file:
#             for item in data:
#                 file.write(item + '\n')

# class MsmqSender(IDataSender):
#     def __init__(self, queue_name):
#         self.queue_name = queue_name + ("_out")
#     def set_data(self, data):
#         for item in data:
#             result = [value.strip() for value in item.split(':')]
#             label = result[0]
#             message = result[1] + " - Moderation Flag: " + result [2]
#             queue_info = win32com.client.Dispatch("MSMQ.MSMQQueueInfo")
#             computer_name = os.getenv('COMPUTERNAME')
#             queue_name = self.queue_name
#             queue_info.FormatName = f'direct=os:{computer_name}\\PRIVATE$\\{queue_name}'
#             queue = queue_info.Open(2, 0)
#             msg = win32com.client.Dispatch("MSMQ.MSMQMessage")
#             msg.Label = label
#             msg.Body = message
#             msg.Send(queue)
#             queue.close()

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