# -*- coding: utf-8 -*-
import sql
import os
from main import main
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(282, 150)
        Dialog.setMaximumSize(QtCore.QSize(282, 150))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/img/configure_database_16704.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.entrar = QtWidgets.QPushButton(Dialog)
        self.entrar.setGeometry(QtCore.QRect(10, 120, 83, 25))
        self.entrar.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/img/icons8-ok-filled.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.entrar.setIcon(icon1)
        self.entrar.setObjectName("entrar")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 181, 17))
        font = QtGui.QFont()
        font.setFamily("FreeMono")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(112, 120, 91, 25))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/img/icons8-cancelar.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(11, 51, 195, 58))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.usuario = QtWidgets.QLineEdit(self.layoutWidget)
        self.usuario.setObjectName("usuario")
        self.gridLayout.addWidget(self.usuario, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.senha = QtWidgets.QLineEdit(self.layoutWidget)
        self.senha.setObjectName("senha")
        self.senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.gridLayout.addWidget(self.senha, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(220, 40, 61, 71))
        self.label_4.setStyleSheet("image: url(:/img/img/locked-padlock-gross-symbol_icon-icons.com_74141.svg);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        self.entrar.clicked.connect(self.entra)
        self.pushButton_2.clicked.connect(self.senha.clear)
        self.pushButton_2.clicked.connect(self.usuario.clear)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.usuario, self.senha)
        Dialog.setTabOrder(self.senha, self.entrar)
        Dialog.setTabOrder(self.entrar, self.pushButton_2)    
    
    def entra(self):
        print("Entrando...")
        
        ############### PRECISA ENCONTRAR O BANCO DE DADOS
        if(not os.path.exists(sql.banco)):
            print("Banco de Dados Encontrado!")

            if(not self.usuario.text() and not self.senha.text()):
                print("preencha a senha")
            elif(self.autenticar(self.usuario.text(),self.senha.text())):
                print("Entrou!")
                self.janela = QtWidgets.QMainWindow()
                self.ui = main()
                self.ui.setupUi(self.janela)
                self.janela.show()                        
                self.close()

        else:
            print("Banco nao foi encontrado!")            
            sql.criar_tabelas()            
            sql.inserir_usuario("greg","123")
            print("Criado banco de dados {} com sucesso!".format(sql.caminho+sql.banco))
    
    def autenticar(self,usuario,senha):
        for resultado in sql.pegar_usuario():
            if(resultado[1] == usuario and resultado[2] == senha):
                return True
                        


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "ARPROTECT"))
        self.entrar.setText(_translate("Dialog", "ENTRAR"))
        self.label_3.setText(_translate("Dialog", "SISTEMA ESTOQUE"))
        self.pushButton_2.setText(_translate("Dialog", "CANCELAR"))
        self.label.setText(_translate("Dialog", "NOME"))
        self.label_2.setText(_translate("Dialog", "SENHA"))

    def confirmar(self):
        print("confirmado")

import recursos

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

