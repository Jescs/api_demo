import os
import xlrd
from xlutils.copy import copy

file_path = os.path.abspath(os.path.dirname(__file__))  # 获取当前文件目录
print(file_path)
root_path = os.path.dirname(file_path)   # 获取文件上级目录
data_path = root_path + '\\data'  # 拼接data文件夹地址
data_file = data_path + '\\api.xlsx'   # 拼接excel文件地址
data = xlrd.open_workbook(data_file)  # 读取文件
sheet = data.sheet_by_index(0)   # 切换到第一个sheet


def write_excel_xls(row, col, value):
    """
    excel 写入
    :param row:
    :param col:
    :param value:
    :return:
    """
    book_r = xlrd.open_workbook(data_file)
    book_w = copy(book_r)  # 复制原表格
    sheet_1 = book_w.get_sheet(0)  # 以编辑方式得到文件的第一个工作表
    sheet_1.write(row, col, value)   # 把内容写入表格
    os.remove(data_file)  # 删除原文件
    book_w.save(data_file)  # 保存修改的文件为原文件


def get_excel(row, col):
    """
    excel 单元格读取
    :param row:
    :param col:
    :return:
    """
    rows = sheet.nrows  # 获取最大行号
    cols = sheet.ncols  # 获取最大列号
    path_name = sheet.cell_value(row, col)   # 获取单元格值
    return rows,cols,path_name
