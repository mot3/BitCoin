from PyQt5 import QtCore, QtGui, QtWidgets
import urllib.request, json


class Ui_BitCoin(object):  
    def setupUi(self, BitCoin):            
        BitCoin.setObjectName("BitCoin")
        BitCoin.setEnabled(True)
        BitCoin.resize(378, 330)
        BitCoin.setWindowFilePath("")
        self.centralwidget = QtWidgets.QWidget(BitCoin)
        self.centralwidget.setObjectName("centralwidget")
        self.bitcoin_price = QtWidgets.QLabel(self.centralwidget)
        self.bitcoin_price.setGeometry(QtCore.QRect(130, 90, 101, 21))
        self.bitcoin_price.setObjectName("bitcoin_price")
        self.push_B = QtWidgets.QPushButton(self.centralwidget)
        self.push_B.setGeometry(QtCore.QRect(140, 130, 81, 41))
        self.push_B.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.push_B.setObjectName("push_B")
        BitCoin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(BitCoin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 378, 23))
        self.menubar.setObjectName("menubar")
        BitCoin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(BitCoin)
        self.statusbar.setObjectName("statusbar")
        BitCoin.setStatusBar(self.statusbar)

        self.retranslateUi(BitCoin)
        self.push_B.clicked.connect(self.get_btc)
        QtCore.QMetaObject.connectSlotsByName(BitCoin)

    def retranslateUi(self, BitCoin):
        _translate = QtCore.QCoreApplication.translate
        BitCoin.setWindowTitle(_translate("BitCoin", "BitCoin"))
        self.push_B.setText(_translate("BitCoin", "Enter"))
    
    def get_btc(self):
        url = 'https://api.coinbase.com/v2/prices/BTC-USD/buy'
        response = urllib.request.urlopen(url)
        data = response.read()
        price = float(json.loads(data)['data']['amount'])        
        self.bitcoin_price.setText("%s" %price)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BitCoin = QtWidgets.QMainWindow()
    ui = Ui_BitCoin()
    ui.setupUi(BitCoin)
    BitCoin.show()
    sys.exit(app.exec_())