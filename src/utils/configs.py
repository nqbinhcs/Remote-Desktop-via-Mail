import json


def get_configs():
    """Get configurations from configs.json

    :return: (str,str,list) username, password, trusted sender list
    """
    with open('configs/configs.json') as json_file:
        data = json.load(json_file)
        USERNAME = data['account'][0]['username']
        PASSWORD = data['account'][0]['credential']
        TRUSTED_SENDERS = [_data['mail'] for _data in data['trusted_sender']]
        return USERNAME, PASSWORD, TRUSTED_SENDERS
