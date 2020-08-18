import test
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def fun():
    print('ok')


# 使用designer软件（一般位于python组件包里）设计界面
# 然后（用如下命令）生成py文件进行功能编辑
# pyuic5 -o test.py untitled.ui
# 功能编辑可使用本main模板文件进行修改
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = test.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    # 实现自己添加的功能，实现的按钮在def retranslateUi(self, MainWindow)找
    ui.pushButton.setText('点击')
    ui.pushButton.clicked.connect(fun)

    ui.label.setText("这是我的UI程序")
    ui.toolButton.clicked.connect(fun)

    sys.exit(app.exec())
