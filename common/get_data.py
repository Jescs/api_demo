import xlrd
import os
from xlutils.copy import copy


class ReadExcel():
    def __init__(self):
        file_path = os.path.abspath(os.path.dirname(__file__))
        root_path = os.path.dirname(file_path)
        data_path = root_path + '\\data'
        self.data_file = data_path + '\\api.xlsx'
        data = xlrd.open_workbook(self.data_file)
        self.sheet = data.sheet_by_index(0)

    def write_excel_xls(self, row, col, value):
        book_r = xlrd.open_workbook(self.data_file)
        book_w = copy(book_r)
        sheet_1 = book_w.get_sheet(0)
        sheet_1.write(row, col, value)
        os.remove(self.data_file)
        book_w.save(self.data_file)

    def get_max_row(self):
        rows = self.sheet.nrows
        return rows

    def get_max_col(self):
        return self.sheet.ncols

    def get_path(self, rows):
        """
        获取path
        :param rows:
        :return:
        """
        path_name = self.sheet.cell_value(rows - 1, 1)  # 2,3,4
        return path_name

    def get_expect(self, rows):
        """
        获取期望值
        :param rows:
        :return:
        """
        expect = self.sheet.cell_value(rows - 1, 10)
        return expect

    def get_method(self, rows):
        """
        获取请求方式
        :param rows:
        :return:
        """
        return self.sheet.cell_value(rows - 1, 0)

    def get_param(self, rows):
        """
        获取单行的path与param，该行的path、param（key，values组成字典）组成list
        :param rows:
        :return:
        """
        get_data = []
        for i in range(rows):
            keys = []
            values = []
            for i in range(2, 10):
                if i % 2 == 0:
                    key = self.sheet.cell_value(rows - 1, i)
                    keys.append(key)
                    keys = [i for i in keys if i != '']
                else:
                    value = self.sheet.cell_value(rows - 1, i)
                    values.append(value)
                    values = [i for i in values if i != '']
            datas = dict(zip(keys, values))

            get_data.append(self.get_method(rows))
            get_data.append(self.get_path(rows))
            get_data.append(datas)
            get_data.append(self.get_expect(rows))
            return get_data

    def get_all_param(self, rows):
        """
        获取所有的path与params，每行的path与param组成一个list
        :param rows:
        :return:
        """
        all_data = []
        for j in range(2, rows + 1):
            all_data.append(self.get_param(j))
        return all_data


if __name__ == '__main__':
    excel = ReadExcel()
    path = excel.get_path(4)
    row = excel.get_max_row()
    data = excel.get_param(row)
    all_data = excel.get_all_param(row)
    excel.write_excel_xls(7, 7, 'yeyds1a')
    print(row, all_data)
