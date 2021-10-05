from main import handler


dummy_event = {'Lat': -6.329598542338873, 'Long': 106.72983194993282, 'DeviceId': 1, 'Humidity': 44.200001, 'Temp': 29.6, 'Fire': 1.695236}


if __name__ == "__main__":
    handler(dummy_event, None)
