import pytest
import os
from case.apidata import ApiData
import time

api = ApiData()
api.get_data_01()

file_path = os.path.abspath(os.path.dirname(__file__))
root_path = os.path.dirname(file_path)
date = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime())


def run_test():
    report_path = os.path.join(root_path, 'reports', str(date))
    allure_report_path = os.path.join(root_path, 'allurereport', str(date))
    test_folder = os.path.join(root_path, 'case')
    # print(test_folder)
    pytest.main([test_folder, '--alluredir=%s' % (report_path), '-o log_cli=true -o log_cli_level=INFO'])
    os.system('allure generate %s -o %s/html --clean' % (report_path, allure_report_path))  # 替换为本地的 allure 安装路径


run_test()
