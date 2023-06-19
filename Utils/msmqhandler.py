import os

import pythoncom
import win32com

from Utils.receiverhandler import IDataRetriever
from Utils.senderhandler import IDataSender


class MsmqRetriever(IDataRetriever):
    def __init__(self, queue_name):
        self.queue_name = queue_name
    def get_data(self):
        queue_info = win32com.client.Dispatch("MSMQ.MSMQQueueInfo")
        computer_name = os.getenv('COMPUTERNAME')
        queue_name = self.queue_name
        queue_info.FormatName = f'direct=os:{computer_name}\\PRIVATE$\\{queue_name}'
        msg_list = []
        queue = queue_info.Open(1, 0)
        while True:
            msgs = queue.Peek(pythoncom.Empty, pythoncom.Empty, 1000)
            if not msgs:
                #print(f'No more messages in {queue_name}')
                break
            msg = queue.Receive()
            #print(f'Got Message from {queue_name}: {msg.Label} - {msg.Body}')
            msg_list.append({int(msg.label):msg.body})
        return (msg_list)



class MsmqSender(IDataSender):
    def __init__(self, queue_name):
        self.queue_name = queue_name + ("_out")
    def set_data(self, data):
        for item in data:
            result = [value.strip() for value in item.split(':')]
            label = result[0]
            message = result[1] + " - Moderation Flag: " + result [2]
            queue_info = win32com.client.Dispatch("MSMQ.MSMQQueueInfo")
            computer_name = os.getenv('COMPUTERNAME')
            queue_name = self.queue_name
            queue_info.FormatName = f'direct=os:{computer_name}\\PRIVATE$\\{queue_name}'
            queue = queue_info.Open(2, 0)
            msg = win32com.client.Dispatch("MSMQ.MSMQMessage")
            msg.Label = label
            msg.Body = message
            msg.Send(queue)
            queue.close()