import requests

from Utils.receiverhandler import IDataRetriever
from Utils.senderhandler import IDataSender


class ApiSender(IDataSender):
    def __init__(self, rest_api_url):
        self.rest_api_url = rest_api_url
    def set_data(self, data):
        url_orig = self.rest_api_url
        for element in data:
            msg_id = int(element['msg_id'])
            msg_desc = element['msg_desc']
            msg_moderate_status = element['msg_moderate_status']
            msg_processed = element['msg_processed']
            data = {
                'msg_moderate_status': msg_moderate_status,
                'msg_processed': msg_processed
            }
            url = url_orig + f'{msg_id}/'
            print(url)
            response = requests.put(url, data=data)
            print(response.status_code)

class ApiRetriever(IDataRetriever):
    def __init__(self, rest_api_url):
        self.rest_api_url = rest_api_url
    def get_data(self):
        return requests.get(self.rest_api_url)