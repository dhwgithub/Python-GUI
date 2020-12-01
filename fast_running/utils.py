import os
import sys


def resource_path(relative_path):
    """ 返回绝对路径
    """
    # if hasattr(sys, 'frozen'):
    #     os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
    # base_path = os.path.abspath("")  # 获取当前路径的绝对路径
    if getattr(sys, 'frozen', False):  # 使用pyinstaller时保证资源文件可用
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath("")  # 获取当前路径的绝对路径

    return os.path.join(base_path, relative_path)
