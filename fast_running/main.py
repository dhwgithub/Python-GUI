import sys
from PyQt5.QtWidgets import QApplication

from main_window import MainWindow

if __name__ == '__main__':
    """
    启动程序
    """
    app = QApplication(sys.argv)

    main_window = MainWindow()  # 加载自定义界面
    main_window.show()

    sys.exit(app.exec_())
