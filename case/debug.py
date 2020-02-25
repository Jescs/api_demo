import requests
from common.get_data import ReadExcel
import re
import os
import yaml
import time


class ApiData():
    def __init__(self):
        self.excel = ReadExcel()
        self.headers = {'number': 'P2320190329'}
        file_path = os.path.abspath(os.path.dirname(__file__))
        root_path = os.path.dirname(file_path)
        data_path = root_path + '\\data'
        self.data_file = data_path + '\\data.yaml'

    def wirte_yaml(self, row, key,*dict_data):
        data = self.excel.get_param(row)
        print('----获取科室排班-----')
        url = 'http://auto-api.mobimedical.cn' + data[1]
        r = requests.get(url, params=dict_data, headers=self.headers)
        print(r.json())
        d = str(r.json())
        if len(key) >= 1:
            for i in range(len(key)):
                da = re.findall(r"'{}': '(.+?)'".format(key[i]), d)
                try:
                    if len(da) > 0:
                        d = {'{}'.format(key[i]): da[0]}
                        print(d)
                        with open(self.data_file, 'a', encoding="utf-8") as f:
                            yaml.dump(d, f, allow_unicode=True)
                except Exception as msg:
                    print(msg)



    def get_data_01(self):
        data = self.excel.get_param(3)
        self.wirte_yaml(3, ['deptId'],data[2])
        time.sleep(2)
        self.wirte_yaml(5, ['deptId', 'date', 'period'])


if __name__ == '__main__':
    api = ApiData()
    api.get_data_01()
