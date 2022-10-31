# -*- coding: UTF-8 -*-

import sys

from PyQt5.QtWidgets import QApplication
from registration import LogWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    log = LogWindow()
    log.show()
    sys.exit(app.exec_())
