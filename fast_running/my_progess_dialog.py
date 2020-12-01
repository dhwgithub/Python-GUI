from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QProgressBar

from utils import resource_path


class MyProgressDialog(QDialog):
    """
    进度条会话类
    """
    def __init__(self):
        super(MyProgressDialog, self).__init__()

        self.__max_length = None  # 进度条最大长度
        self.__main_layout = QVBoxLayout()  # 主界面

        # 文本显示框
        self.__label = QLabel("处理中，请稍等...")
        self.__label.setAlignment(Qt.AlignCenter)

        # 进度条框
        self.__progress_bar = QProgressBar()

        """
        会话框全局设置
        """
        # 组件
        self.__main_layout.addWidget(self.__label)
        self.__main_layout.addWidget(self.__progress_bar)
        self.setLayout(self.__main_layout)

        # 背景
        palette = QPalette()
        palette.setColor(self.backgroundRole(), QColor(255, 255, 255))
        self.setPalette(palette)
        self.setAutoFillBackground(True)

        # 大小
        self.setMinimumSize(250, 50)
        self.setWindowIcon(QIcon(resource_path("icons/choice.png")))
        self.setWindowFlags(Qt.CustomizeWindowHint)

    def set_max_length(self, length):
        self.__max_length = length
        self.__progress_bar.setMaximum(length)

    def get_step(self, step):
        self.__progress_bar.setValue(step)

        if step >= self.__max_length:
            self.close()
