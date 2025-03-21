import requests

class Api:
    """
    提供HTTP request 呼叫API的快速類別
    """

    # 要呼叫的API URL位置
    url = 'https://opendata.cwa.gov.tw'

    # API版本
    version = 'v1'

    # API路由
    path = f'api/{version}/rest/datastore'

    # token
    apiAuth ={'Authorization': 'CWA-5B306D7D-A5ED-4639-8532-D1C274899F48'}

    # 定義請求標頭
    headers = {
        'User-Agent': 'python work',
        'Accept': '*/*',
        'Connection': 'keep-alive'
    }

    # 要呼叫的API端點
    apis = [
        'O-A0003-001', # 現在天氣觀測
        'F-C0032-001', # 臺灣各縣市天氣預報資料及國際都市天氣預報
        'A-B0062-001', # 日出日落
        'E-A0014-001', # 海嘯
        'E-A0016-001', # 小區域有感地震
        'E-A0015-001', # 顯著有感地震
        'E-A0016-001', # 小區域顯著有感地震
    ]

    def setHeader(self, params = {}):
        """
        配置request http header要傳遞的內容
        """
        self.headers = {**self.headers, **params}
        return None

    def get(self, api, params = {}):
        """
        TODO 使用get方法呼叫API
        Args:
            self
            api (string): 要呼叫的API端點
            params (dict): {參數名稱1：參數值1， 參數名稱2：參數值2....}

        Returns:
            json

        Example:
            import Api from Api
            api = Api()
            api.get("{url}", {name: "Hi"})
        """
        uri = f"{self.url}/{self.path}/{api}"
        return self.send('get', uri, params)

    def send(self, method, api, params):
        """
        proxy 代理方法，對應方法發調用request對應的方法
        """
        response = {"status": False, "code":0, "message":None, "data": None}
        try:
            if(method.upper() == 'GET'):
                _r = requests.get(api, headers=self.headers, params={**params, **self.apiAuth})
            elif(method.upper() == 'POST'):
                _r = requests.post(api, headers=self.headers, data=params, params=self.apiAuth)
            else:
                response["message"] = f"錯誤的方法{method}"
                return response
                
            response["status"] = _r.status_code == 200
            response["code"] = _r.status_code
            response["message"] = "呼叫成功" if _r.status_code == 200 else "呼叫失敗"
            response["data"] = _r.json()
            return response

        except requests.exceptions.HTTPError as errh:
            response["message"] = f"HTTP錯誤: {errh}"
            return response
        except requests.exceptions.ConnectionError as errc:
            response["message"] = f"連接錯誤: {errc}"
            return response
        except requests.exceptions.Timeout as errt:
            response["message"] = f"超時錯誤: {errt}"
            return response
        except requests.exceptions.RequestException as err:
            response["message"] = f"無法預期的錯誤: {err}"
            return response

