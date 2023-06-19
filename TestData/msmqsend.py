# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 19:35:40 2023

@author: 244262
"""

import win32com.client
import os
import time
import random

queue_info = win32com.client.Dispatch("MSMQ.MSMQQueueInfo")
computer_name = os.getenv('COMPUTERNAME')

queues = ['myqueue2']


def send_message(queue_name: str, label: str, message: str):

    queue_info.FormatName = f'direct=os:{computer_name}\\PRIVATE$\\{queue_name}'
    queue = None

    try:
        queue = queue_info.Open(2, 0)

        msg = win32com.client.Dispatch("MSMQ.MSMQMessage")
        msg.Label = label
        msg.Body = message

        msg.Send(queue)

    except Exception as e:
        print(f'Error! {e}')

    finally:
        queue.Close()


def main():
    i = 0
    while i<1:
        i += 1
        send_message(random.choice(queues), 1, 'this shit not happen again ')
        send_message(random.choice(queues), 2,  'I will kill you ')
        print(f'{i}: Message sent!')
        time.sleep(0.5)


if __name__ == '__main__':
    main()
