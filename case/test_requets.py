import pytest
import requests
import allure
from common.logger import *


def get_request(data):
    logger.info('----准备测试数据{}'.format(data[2]))

    logger.info('This is info message，获取接口地址{}'.format(url))
    headers = {'number': 'P2320190329'}
    logger.info('----开始接口测试')
    if data[0] == 'get':
        r = requests.get(url, params=data[2], headers=headers)
    else:
        r = requests.post(url, data=data[2], headers=headers)
    logger.info('----接口请求完成response{}'.format(r.json()))
    response = str(r.json()['data'])
    try:
        logger.info('response:expect-{}'.format(data[3]))
        assert data[3] in response
    except Exception as msg:
        logger.info('-------fail:{}------'.format(msg))
        raise
    print(r.json()['data'])
    return r.status_code


@allure.feature('测试http请求')
def test_get_request(is_data):
    allure.dynamic.title(is_data[0])
    logger.info('-------状态码断言------')
    assert get_request(is_data) == 200
    logger.info('-------测试完成------')


if __name__ == "__main__":
    pytest.main()
