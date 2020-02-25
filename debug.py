import requests
import json

host = 'http://auto-api.mobimedical.cn'
pathname = '/card/patient'
data = {'cardId': '1904236007', 'cardType': 6}
headers = {'number': 'P2320190329'}
url = host + pathname
r = requests.get(url, params=data, headers=headers)
json_data = r.json()
try:
    assert json_data['data']['cardName'] == '陈凤'
    print('------success------')
except Exception as msg:
    print('-------fail:{}--------'.format(msg))
# dict_data = json.dumps(r.json(), ensure_ascii=False)  # json转换为dict
