import sys

from PyQt5.QtWidgets import QApplication , QMainWindow, QWidget

from login import Ui_Login

if __name__ == '__main__':

    app = QApplication(sys.argv)
    login = QWidget()
    login_ui = Ui_Login()
    login_ui.setupUi(login)
    login.show()
    sys.exit(app.exec_())

