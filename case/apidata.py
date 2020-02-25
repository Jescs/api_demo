import requests
from common.get_data import ReadExcel
import time
import yaml
import re
import os


class ApiData():
    def __init__(self):
        self.excel = ReadExcel()
        self.headers = {'number': 'P2320190329'}
        file_path = os.path.abspath(os.path.dirname(__file__))
        root_path = os.path.dirname(file_path)
        data_path = root_path + '\\data'
        self.data_file = data_path + '\\data.yaml'
    # def get_api_data(self, r, title, id, name):
    #     response = r.json()['data']
    #     if len(response) > 0:
    #         response_id = response[0][id]
    #         response_name = response[0][name]
    #     else:
    #         print('------获取{}失败------'.format(title))
    #         raise Exception
    #     return response_id, response_name
    #
    # def get_data_01(self):
    #     data = self.excel.get_param(3)
    #     print('----获取科室排班-----')
    #     url = 'http://auto-api.mobimedical.cn' + data[1]
    #     r = requests.get(url, params=data[2], headers=self.headers)
    #     self.excel.write_excel_xls(3, 3, r.json()['data'][0]['deptId'])
    #     self.excel.write_excel_xls(5, 3, r.json()['data'][0]['deptId'])
    #     dept_name = r.json()['data'][0]['name']
    #     time.sleep(2)
    #     data = self.excel.get_param(4)
    #     url = 'http://auto-api.mobimedical.cn' + data[1]
    #     print('获取{}科室排班时间'.format(dept_name))
    #     r = requests.get(url, params=data[2], headers=self.headers)
    #     print(r.json())
    #     self.excel.write_excel_xls(5, 5, r.json()['data'][0]['date'])
    #     self.excel.write_excel_xls(5, 7, r.json()['data'][0]['period'][0])
    #     time.sleep(2)
    #     data = self.excel.get_param(6)
    #     url = 'http://auto-api.mobimedical.cn' + data[1]
    #     print('获取{}科室排班医生'.format(dept_name))
    #     r = requests.get(url, params=data[2], headers=self.headers)
    #     print(r.json())
    #     self.excel.write_excel_xls(6, 3, r.json()['data'][0]['scheduleId'])
    #     time.sleep(2)

    def wirte_yaml(self, row, *args):
        data = self.excel.get_param(row)
        print('----获取科室排班-----')
        url = 'http://auto-api.mobimedical.cn' + data[1]
        r = requests.get(url, params=data[2], headers=self.headers)
        print(r.json())
        d = str(r.json())
        da = re.findall(r"'{}': '(.+?)'".format(args), d)
        try:
            if len(da) > 0:
                deptId = {'{}'.format(args): da[0]}
                print(deptId)
                with open(self.data_file, 'w', encoding="utf-8") as f:
                    yaml.dump(deptId, f, allow_unicode=True)
        except Exception as msg:
            print(msg)

    def get_data_01(self):
        self.wirte_yaml(3, 'name','deptId')


if __name__ == '__main__':
    api = ApiData()
    api.get_data_01()
