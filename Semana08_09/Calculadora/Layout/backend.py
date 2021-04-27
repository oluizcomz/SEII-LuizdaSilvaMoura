import sys
from PySide2 import QtCore,QtGui,QtWidgets 
from GuiCal import Ui_MainWindow 

class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Window = MainWindow()
    Window.show()
    sys.exit(app.exec_())