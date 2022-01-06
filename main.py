from sympy.utilities.decorator import public
import rsa
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

qtCreatorFile = "RSAGUI.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class GUICKO(QMainWindow, Ui_MainWindow): 

    error = "error"
    def default(self):
        self.vstupnyText.setText('Ahoj')

    def generateKeys(self):
        try:
            kluce = rsa.generateKey()
    
            self.klucE.setText(str(kluce['e']))
            self.kluc_D.setText(str(kluce['d']))
            self.klucN.setText(str(kluce['n']))
            self.klucn.setText(str(kluce['n']))
        except:
            self.sifrovanyText.setText(self.error)

    def encryption(self):
        try:
            self.sifrovanyText.setText(str(rsa.sifruj(int(self.klucE.toPlainText()),int(self.klucN.toPlainText()),self.vstupnyText.toPlainText())))
        except:
              self.sifrovanyText.setText(self.error)
    def decryption(self):
        try:
            self.desifrovany.setText(str(rsa.desifruj(int(self.kluc_D.toPlainText()),int(self.klucn.toPlainText()),self.sifrovanyText.toPlainText())))
        except:
            self.desifrovany.setText(self.error)
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.sifruj.clicked.connect(self.encryption)
        self.desifruj.clicked.connect(self.decryption)
        self.generujkluce.clicked.connect(self.generateKeys)
        self.default()
     
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GUICKO()
    window.show()
    sys.exit(app.exec_())