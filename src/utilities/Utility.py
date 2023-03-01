import platform
from openpyxl import load_workbook
import json


class Utility:
    def __init__(self):
        pass

    @staticmethod
    def is_windows():
        if platform.platform().lower() == 'windows':
            return True
        return False

    @staticmethod
    def is_linux():
        if platform.platform().lower() == 'linux':
            return True
        return False

    @staticmethod
    def read_json(json_file_path):
        with open(json_file_path) as f:
            json_file = json.load(f)
        # return the object from JSON
        return json_file

    @staticmethod
    def get_app_path_from_env():
        return False

    @staticmethod
    def search_file_recursively(file_name, base_path) -> any:
        return False


class PageLocatorDict(dict):
    def __getattr__(self, item):
        return self[item]

    def __dir__(self):
        return super().__dir__() + [str(k) for k in self.keys()]


class ReadExcel:
    def __init__(self, file_name, sheet_name):
        self.workbook = load_workbook(file_name)
        self.worksheet = self.workbook[sheet_name]

    def read_from_excel(self, column, row):
        cell = "{}{}".format(column, row)
        cell_value = self.worksheet[cell].value
        return cell_value
