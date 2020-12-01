import glob
import os

from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtWidgets import QTextBrowser
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QMessageBox

from utils import resource_path
from setting import pushbutton_css
from setting import font_css
from setting import border_css
from my_progess_dialog import MyProgressDialog
from main_algorithm.det_eval_2013_for_PESNet import MyAlgorithm


class MainWindow(QMainWindow):
    """ 主界面
    """
    def __init__(self):
        super(MainWindow, self).__init__()

        self.__main_widget = QWidget()  # 总布局
        self.__info_layout = QVBoxLayout()

        # ==============================================================
        self.__label_layout = QHBoxLayout()

        self.__label_info = QLabel()
        self.__label_info.setText("标注文件路径：")
        self.__label_info.setStyleSheet(font_css)
        self.__label_info.setMinimumSize(120, 25)

        self.__label_show = QLineEdit()
        self.__label_show.setPlaceholderText("请选择标注文件")
        self.__label_show.setReadOnly(True)

        self.__btn_label = QPushButton("标注文件")
        self.__btn_label.setIcon(QIcon(resource_path("icons/choice.png")))
        self.__btn_label.setStyleSheet(pushbutton_css)
        self.__btn_label.setMinimumSize(150, 25)
        self.__btn_label.clicked.connect(self.__open_label_file)

        self.__label_layout.addStretch(1)
        self.__label_layout.addWidget(self.__label_info)
        self.__label_layout.setStretchFactor(self.__label_info, 1)
        self.__label_layout.addWidget(self.__label_show)
        self.__label_layout.setStretchFactor(self.__label_show, 3)
        self.__label_layout.addWidget(self.__btn_label)
        self.__label_layout.setStretchFactor(self.__btn_label, 1)
        self.__label_layout.addStretch(1)

        # ==============================================================
        self.__recog_layout = QHBoxLayout()

        self.__text_info = QLabel()
        self.__text_info.setText("检测结果文件路径：")
        self.__text_info.setStyleSheet(font_css)
        self.__text_info.setMinimumSize(120, 25)

        self.__text_show = QLineEdit()
        self.__text_show.setPlaceholderText("请选择检测结果文件")
        self.__text_show.setReadOnly(True)

        self.__btn_recog = QPushButton("检测结果文件")
        self.__btn_recog.setIcon(QIcon(resource_path("icons/choice.png")))
        self.__btn_recog.setStyleSheet(pushbutton_css)
        self.__btn_recog.setMinimumSize(150, 25)
        self.__btn_recog.clicked.connect(self.__open_test_file)

        self.__recog_layout.addStretch(1)
        self.__recog_layout.addWidget(self.__text_info)
        self.__recog_layout.setStretchFactor(self.__text_info, 1)
        self.__recog_layout.addWidget(self.__text_show)
        self.__recog_layout.setStretchFactor(self.__text_show, 3)
        self.__recog_layout.addWidget(self.__btn_recog)
        self.__recog_layout.setStretchFactor(self.__btn_recog, 1)
        self.__recog_layout.addStretch(1)

        # ==============================================================
        self.__run_layout = QHBoxLayout()

        self.__btn_run = QPushButton("运行")
        self.__btn_run.setIcon(QIcon(resource_path("icons/yes.png")))
        self.__btn_run.setStyleSheet(pushbutton_css)
        self.__btn_run.setMinimumSize(300, 40)
        self.__btn_run.clicked.connect(self.__eval_run)

        self.__run_layout.addStretch(1)
        self.__run_layout.addWidget(self.__btn_run)
        self.__run_layout.addStretch(1)

        # ==============================================================
        self.__show_info = QTextBrowser()
        self.__show_info.setLineWrapMode(0)  # 不换行设置
        self.__show_info.setText("评估结果展示")
        self.__show_info.setStyleSheet(border_css)

        # 加入布局中
        self.__info_layout.addLayout(self.__label_layout)
        self.__info_layout.setStretchFactor(self.__label_layout, 4)
        self.__info_layout.addStretch(1)
        self.__info_layout.addLayout(self.__recog_layout)
        self.__info_layout.setStretchFactor(self.__recog_layout, 4)
        self.__info_layout.addStretch(1)
        self.__info_layout.addLayout(self.__run_layout)
        self.__info_layout.setStretchFactor(self.__run_layout, 4)
        self.__info_layout.addStretch(1)
        self.__info_layout.addWidget(self.__show_info)
        self.__info_layout.setStretchFactor(self.__show_info, 20)

        """
        总布局设置
        """
        self.__main_widget.setLayout(self.__info_layout)
        self.setCentralWidget(self.__main_widget)

        # # 获取显示器分辨率大小
        # self.desktop = QApplication.desktop()
        # self.screenRect = self.desktop.screenGeometry()
        # self.height = self.screenRect.height()
        # self.width = self.screenRect.width()
        # # print(self.height, self.width)  # 1080 1920

        self.setWindowTitle("FastRun")
        self.resize(600, 500)
        self.__center()
        self.setWindowIcon(QIcon('icons/data.png'))

    def __open_label_file(self):
        """
        选择标注文件
        :return:
        """
        directory = QFileDialog.getExistingDirectory(self, "选择标注文件夹", "./")
        if directory:
            self.__file_sum = len(glob.glob(directory + '\*.json'))
            self.__label_path = directory
            self.__label_show.setText(self.__label_path)

    def __open_test_file(self):
        """
        选择测试文件
        :return:
        """
        directory = QFileDialog.getExistingDirectory(self, "选择测试文件夹", "./")
        if directory:
            self.__text_path = directory
            self.__text_show.setText(self.__text_path)

    def __center(self):
        """ 使当前对象居中显示
        """
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def __eval_run(self):
        """ 开始评估
        :return:
        """
        log_path = os.path.join(os.path.abspath(""), "log_file")
        try:
            # 设置进度条对象
            self.dialog = MyProgressDialog()
            self.dialog.set_max_length(self.__file_sum)

            # 执行算法，并设置线程类实现算法持续执行且其他功能阻塞
            run = MyAlgorithm(self.__label_path, self.__text_path, log_path)
            run.step_signal.connect(self.dialog.get_step)  # 记步信号改变时调用进度条步数进行同步
            run.result_signal.connect(self.__print_res)  # 算法结束时调用结束处理函数
            run.start()

            self.dialog.exec_()

        except Exception:
            QMessageBox.warning(self, "警告", "评估异常！\n（可能是文件选择有误）", QMessageBox.Ok)

    def __print_res(self, res):
        if res[0] is None:
            self.dialog.get_step(self.__file_sum)
            QMessageBox.warning(self, "警告", "评估异常！\n（可能是文件选择有误）", QMessageBox.Ok)
            return

        precision, recall, hmean, all_per_rate, all_full_rate, all_long_total, ignore_sum = res
        res = "检测评估结果：\nprecision: {:.2f}%\nrecall: {:.2f}%\nhmean: {:.2f}%\n\n" \
              "识别评估结果：\nall_per_rate：{:.2f}%\nall_full_rate：{:.2f}%\nall_long_total：{:}\n".format(
            precision * 100, recall * 100, hmean * 100, all_per_rate * 100, all_full_rate * 100, all_long_total
        )
        res += "\n共评估{:}个文件，有效文件为{:}个".format(self.__file_sum, self.__file_sum - ignore_sum)
        self.__show_info.setText(res)

