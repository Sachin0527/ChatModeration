import os
import json
import requests
from dotenv import load_dotenv
from os.path import join, dirname

from Utils.msmqhandler import MsmqRetriever, MsmqSender
from Utils.receiverhandler import IDataRetriever
from Utils.restapihandler import ApiRetriever, ApiSender
from Utils.senderhandler import IDataSender
from Utils.filehandler import FileSender, FileRetriever

"""Setup to read env file for various parameters"""
dotenv_path = join(dirname(__file__), '../var.env')
load_dotenv(dotenv_path)
"""Read Parameters from env file"""
source_type = os.getenv('source_type')

def get_env(call_flag):
    if call_flag == "retriever":
        if source_type == 'msmq':
            handler = MsmqRetriever(os.getenv('queue_name'))
        elif source_type == 'file':
            handler = FileRetriever(os.getenv('file_path'))
        elif source_type == 'api':
            handler = ApiRetriever(os.getenv('src_api_url'))
        else:
            raise Exception("Source Not Supported")
    elif call_flag == "sender":
        if source_type == 'msmq':
            handler = MsmqSender(os.getenv('queue_name'))
        elif source_type == 'file':
            handler = FileSender(os.getenv('file_path'))
        elif source_type == 'api':
            handler =ApiSender(os.getenv('src_api_url'))
        else:
            raise Exception("Source Not Supported")
    return handler

def get_input():
    return call_retriever(get_env("retriever")), source_type

def call_retriever(retriever: IDataRetriever):
    return retriever.get_data()

def set_output(output):
    return call_sender(get_env("sender"),output)

def call_sender(sender: IDataSender,output):
    return sender.set_data(output)