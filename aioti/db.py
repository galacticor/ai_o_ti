import os
import boto3

client = None


def _get_client():
    global client
    if client is None:
        client = boto3.client('dynamodb')

    return client


# {'Lat': -6.329598542338873, 'Long': 106.72983194993282, 'DeviceId': 1, 'Humidity': 44.200001, 'Temp': 29.6, 'Fire': 1.695236}
def put_data(data):
    if not os.getenv('APP_ENV'):
        print(data)
        return

    table = _get_client().Table('gemastik_aioti')
    response = table.put_item(Item=data)
    return response
