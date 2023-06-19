import json
import os

def format_input(messages,type):
    messages_formatted_json = []
    if type == 'msmq':
        return messages
    elif type == 'file':
        messages_list = messages.split("\n")
        for key, value in [elem.split(': ') for elem in messages_list]:
            messages_formatted_json.append({int(key):value})
        return messages_formatted_json
    elif type == 'api':
        messages_json = json.loads(messages.text)
        for obj in messages_json:
            if obj['msg_processed'] == False:
                messages_formatted_json.append({obj['msg_id']:obj['msg_desc']})
        print(messages_formatted_json)
        return messages_formatted_json
    else:
        raise Exception("Source Not Supported")

def format_output(messages,formatted_messages,output, type):
    temp = []
    if type == 'api':
        messages_temp = messages.json()
        i = 0
        for element1 in messages.json():
            for key, value in element1.items():
                for element2 in output:
                    for key1, value1 in element2.items():
                        if value == key1:
                            messages_temp[i]['msg_moderate_status'] = element2['moderation_status']
                            messages_temp[i]['msg_processed'] = True
            i = i + 1
        return messages_temp
    elif type == 'msmq' or type == 'file':
        for msg in formatted_messages:
            arr = list(msg.keys())
            temp.append(str(arr[0]) + " : " + msg[arr[0]] + " : " + str(msg['moderation_status']))
        return temp



