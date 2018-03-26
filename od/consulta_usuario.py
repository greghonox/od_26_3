# -*- coding: utf-8 -*-
import sql
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_consulta_usuario(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(382, 320)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/img/configure_database_16704.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(320, 0, 61, 61))
        self.label.setStyleSheet("image: url(:/img/img/icons8-administrator-male.svg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 221, 21))
        font = QtGui.QFont()
        font.setFamily("FreeMono")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 658, 41))
        self.label_6.setStyleSheet("background-color:  rgba(255, 207, 183, 200);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 120, 361, 192))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setTabKeyNavigation(False)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 80, 90, 31))
        self.pushButton_2.setStyleSheet("background-color:   rgb(200,200,200);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/img/icons8-cancelar.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(170, 80, 97, 31))
        self.pushButton.setStyleSheet("image: url(:/img/img/icons8-ok-filled.svg);\n"
"background-color:   rgb(200,200,200);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/img/icons8-ok-filled.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setObjectName("pushButton")
        self.label_6.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.tableWidget.raise_()
        self.pushButton_2.raise_()
        self.pushButton.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.eventos()
        self.Consulta()

    def eventos(self):
        self.pushButton.clicked.connect(self.Cadastrar)
        self.pushButton_2.clicked.connect(self.Cancelar)

    def Consulta(self):        
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(10)
        self.tableWidget.setHorizontalHeaderLabels(["codigo","nome","senha"])
        
        resultado = sql.pegar_usuario()
        for linha_n ,dados_linha  in enumerate(resultado):
            for coluna , data in enumerate(dados_linha):
                self.tableWidget.setItem(linha_n,coluna,QTableWidgetItem(str(data)))
                print(linha_n, coluna)                    

    def Cadastrar(self):        
        from cadastrar_usuario import Ui_cadastrar_usuario
        print("Cadsatrar")
        self.janela = QtWidgets.QMainWindow()
        self.ui = Ui_cadastrar_usuario()
        self.ui.setupUi(self.janela)
        self.janela.show()         

    def Cancelar(self):
        sys.exit(0)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Consulta Usuários"))
        self.label_3.setText(_translate("Form", "Usuários"))
        self.pushButton_2.setText(_translate("Form", "Cancelar"))
        self.pushButton.setText(_translate("Form", "Cadastrar"))

import recursos

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_consulta_usuario()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

