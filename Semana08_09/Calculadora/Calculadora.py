import sys
from PySide2 import QtCore,QtGui,QtWidgets 
from GuiCal import Ui_MainWindow 

class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)
    
        def calc(arg):
            self.lineEdit.setText(self.lineEdit.text()+arg)
            
        def resul():
            if self.lineEdit.text() !='':
                resp = eval(self.lineEdit.text())
            else:
                resp = 0
            self.lineEdit.setText('{}'.format(resp))
    
        self.Button0.clicked.connect(lambda: calc(self.Button0.text()))
        self.Button1.clicked.connect(lambda: calc(self.Button1.text()))
        self.Button2.clicked.connect(lambda: calc(self.Button2.text()))
        self.Button3.clicked.connect(lambda: calc(self.Button3.text()))
        self.Button4.clicked.connect(lambda: calc(self.Button4.text()))
        self.Button5.clicked.connect(lambda: calc(self.Button5.text()))
        self.Button6.clicked.connect(lambda: calc(self.Button6.text()))
        self.Button7.clicked.connect(lambda: calc(self.Button7.text()))
        self.Button8.clicked.connect(lambda: calc(self.Button8.text()))
        self.Button9.clicked.connect(lambda: calc(self.Button9.text()))
        self.Buttonmas.clicked.connect(lambda: calc(self.Buttonmas.text()))
        self.Buttonmen.clicked.connect(lambda: calc(self.Buttonmen.text()))
        self.Buttondiv.clicked.connect(lambda: calc(self.Buttondiv.text()))
        self.Buttonmul.clicked.connect(lambda: calc('*')) 
        self.Buttonigu.clicked.connect(lambda: resul())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Window = MainWindow()
    Window.show()
    sys.exit(app.exec_())