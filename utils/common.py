import requests
import json
from utils.set_cookies import get_cookies

host="xdata.jcloud.com"
cookies=get_cookies()
class commonHttpClient:

    def http_request(self, method, uri, params=None, files=None, headers=None):
        if (method == "POST"):
            hc = requests.post("https://{0}/{1}".format(host, uri), cookies=cookies, params=params,files=files,headers=headers)
        elif (method == "GET"):
            hc = requests.get("https://{0}/{1}".format(host, uri), cookies=cookies, params=params)
        res = json.loads(hc.content)
        status = hc.status_code
        return res, status

