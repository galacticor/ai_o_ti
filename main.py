from aioti.models import predict
from aioti.utils import get_wind_and_rain


def handler(event, context):
    # {'Lat': -6.329598542338873, 'Long': 106.72983194993282, 'DeviceId': 1, 'Humidity': 44.200001, 'Temp': 29.6, 'Fire': 1.695236}
    wind, rain = get_wind_and_rain(event['Lat'], event['Long'])
    event['rain'] = rain
    event['wind'] = wind
    risiko = predict(event)
