import requests
import json
from enum import Enum

class ResultEnum(Enum):
    JSON = 0


class APIHandler:
    def __init__(self):
        pass
    def GET(self, url = "", queryParameters = {}, headers = {}, returnType = ResultEnum.JSON):
        queryString = "?"
        for parameter, value in queryParameters.items():
            queryString += f"{parameter}={value}"
            queryString += "&"
        # print(url + queryString)
        try:
            result = requests.get(url + queryString)
        except Exception as e:
            if returnType == ResultEnum.JSON:
                return {"status": -10000, "Message": f"GET API Failed! Error is:{str(e)}"}
            else:
                return str(e)
        else:
            if returnType == ResultEnum.JSON:
                resultJSON = json.loads(result.text)
            return {"status": 0, "data": resultJSON}