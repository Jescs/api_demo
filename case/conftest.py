import pytest
from common.get_data import *

excel = ReadExcel()
row = excel.get_max_row()
all_data = excel.get_all_param(row)
data = all_data[0]
path = all_data[1]


@pytest.fixture(params=all_data)
def is_data(request):
    return request.param
print(all_data)