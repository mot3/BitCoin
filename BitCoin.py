from PyQt5 import QtCore, QtGui, QtWidgets
import urllib.request, json, requests

class Ui_BitCoin(object):
    def setupUi(self, BitCoin):
        app.processEvents()
        BitCoin.setObjectName("BitCoin")
        BitCoin.setEnabled(True)
        BitCoin.resize(228, 135)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(BitCoin.sizePolicy().hasHeightForWidth())
        BitCoin.setSizePolicy(sizePolicy)
        BitCoin.setMinimumSize(QtCore.QSize(228, 135))
        BitCoin.setMaximumSize(QtCore.QSize(228, 135))
        BitCoin.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        BitCoin.setWindowFilePath("")
        self.centralwidget = QtWidgets.QWidget(BitCoin)
        self.centralwidget.setObjectName("centralwidget")
        self.bitcoin_price = QtWidgets.QLabel(self.centralwidget)
        self.bitcoin_price.setGeometry(QtCore.QRect(130, 90, 101, 21))
        self.bitcoin_price.setObjectName("bitcoin_price")
        self.get_price = QtWidgets.QPushButton(self.centralwidget)
        self.get_price.setGeometry(QtCore.QRect(150, 77, 70, 31))
        self.get_price.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.get_price.setObjectName("get_price")
        self.choose_price = QtWidgets.QComboBox(self.centralwidget)
        self.choose_price.setGeometry(QtCore.QRect(150, 10, 70, 22))
        self.choose_price.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.choose_price.setObjectName("choose_price")
        self.choose_price.addItem("")
        self.choose_price.addItem("")
        self.choose_price.addItem("")        
        self.choose_price.addItem("")
        self.choose_price.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(17, 10, 101, 20))
        self.label.setObjectName("label")
        self.show_price = QtWidgets.QLabel(self.centralwidget)
        self.show_price.setGeometry(QtCore.QRect(11, 84, 70, 13))
        self.show_price.setObjectName("show_price")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 80, 61, 20))
        self.label_3.setObjectName("label_3")
        BitCoin.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(BitCoin)
        self.statusbar.setObjectName("statusbar")
        BitCoin.setStatusBar(self.statusbar)

        app.processEvents()

        self.retranslateUi(BitCoin)
        self.get_price.clicked.connect(self.call_price)
        app.processEvents()
        QtCore.QMetaObject.connectSlotsByName(BitCoin)

        app.processEvents()

    def retranslateUi(self, BitCoin):
        _translate = QtCore.QCoreApplication.translate
        BitCoin.setWindowTitle(_translate("BitCoin", "BitCoin"))
        self.get_price.setText(_translate("BitCoin", "تبدیل"))
        self.choose_price.setItemText(0, _translate("BitCoin", "USD ($)"))
        self.choose_price.setItemText(1, _translate("BitCoin", 'IRI'))
        self.choose_price.setItemText(2, _translate("BitCoin", "EUR (€)"))
        self.choose_price.setItemText(3, _translate("BitCoin", "GBP (£)"))
        self.choose_price.setItemText(4, _translate("BitCoin", 'AUD (A$)'))
                
        self.label.setText(_translate("BitCoin", "تبدیل کننده بیت کوین"))
        self.label_3.setText(_translate("BitCoin", "1 بیت کوین:"))

        app.processEvents()

    def call_price(self):
        app.processEvents()
        currency = self.choose_price.currentText()[0:3]        

        if currency == 'IRI':
            key = 'JFGN2c6leJDktgSkIbrXezvEOa0ZxrS2'
            url = f'http://api.navasan.tech/latest/?api_key={key}'
            response = requests.get(url)
            data = response.json()
            price = data["usd_sell"]["value"]
            url = f'https://api.coinbase.com/v2/prices/BTC-USD/sell'
            app.processEvents()
            response = urllib.request.urlopen(url)
            app.processEvents()
            data = response.read()
            app.processEvents()
            USD = json.loads(data)['data']['amount']
            price = str(int(int(price) * float(USD)))
        else:
            url = f'https://api.coinbase.com/v2/prices/BTC-{currency}/sell'
            app.processEvents()
            response = urllib.request.urlopen(url)
            app.processEvents()
            data = response.read()
            app.processEvents()
            price = json.loads(data)['data']['amount']

        self.show_price.setText(f'{price} {currency}')
        app.processEvents()
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BitCoin = QtWidgets.QMainWindow()
    ui = Ui_BitCoin()
    ui.setupUi(BitCoin)
    BitCoin.show()
    sys.exit(app.exec_())
