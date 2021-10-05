import requests
import os
from typing import Any, Dict, Tuple
from json.decoder import JSONDecodeError
from dataclasses import dataclass

DEFAULT_HTTP_TIMEOUT = 30
API_KEY = os.getenv("API_KEY")


@dataclass
class Result:
    status: int
    data: Dict[str, Any] = None
    error_message: str = None


def get_request(uri: str, headers: Dict[str, Any], timeout: int = DEFAULT_HTTP_TIMEOUT, params: Dict[str, Any] = None) -> Result:
    response = requests.get(uri, timeout=timeout, headers=headers, params=params)
    status = response.status_code
    json_response = None
    try:
        if status < 300:
            json_response = response.json()
    except JSONDecodeError:
        json_response = None

    return Result(
        status=status,
        data=json_response,
        error_message=response.reason if response.status_code >= 400 else None
    )


def get_default_headers() -> Dict[str, str]:
    return {
        "accept": "application/json",
        "Content-Type": "application/json"
    }


def get_wind_and_rain(lat: float, lon: float) -> Tuple[float, float]:
    # api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
    url = "http://api.openweathermap.org/data/2.5/weather"

    headers = get_default_headers()
    params = {"lat": round(lat, 2), "lon": round(lon, 2), "appid": API_KEY}

    response = get_request(url, headers, params=params)
    if response.status == 200:
        wind = response.data.get("wind", {}).get("speed")
        rain = response.data.get("rain", {}).get("1h")
        return wind, rain

    raise Exception("Error when get_wind_and_rain")


def save_data(data):
    print(data)
