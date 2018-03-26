# -*- coding: utf-8 -*-
import sql
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_cadastrar_usuario(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(330, 347)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(33)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(330, 347))
        Form.setMaximumSize(QtCore.QSize(330, 347))
        Form.setFocusPolicy(QtCore.Qt.TabFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/img/configure_database_16704.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
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
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(170, 0, 161, 101))
        self.label.setStyleSheet("image: url(:/img/img/1455555019_users-9_icon-icons.com_53249.svg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(10, 70, 311, 221))
        self.tabWidget.setStyleSheet("background: rgb(200, 200,200);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 50, 201, 101))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(8, 8, 4, 8)
        self.formLayout.setHorizontalSpacing(8)
        self.formLayout.setVerticalSpacing(21)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.nome = QtWidgets.QLineEdit(self.layoutWidget)
        self.nome.setObjectName("nome")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nome)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.senha = QtWidgets.QLineEdit(self.layoutWidget)
        self.senha.setObjectName("senha")
        self.senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.senha)
        self.tabWidget.addTab(self.tab, "")
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setGeometry(QtCore.QRect(130, 300, 191, 31))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.pushButton = QtWidgets.QPushButton(self.splitter)
        self.pushButton.setStyleSheet("image: url(:/img/img/icons8-ok-filled.svg);\n"
"background-color:   rgb(200,200,200);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/img/icons8-ok-filled.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.splitter)
        self.pushButton_2.setStyleSheet("background-color:   rgb(200,200,200);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/img/icons8-cancelar.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 658, 41))
        self.label_6.setStyleSheet("background-color:  rgba(255, 207, 183, 200);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_6.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.tabWidget.raise_()
        self.splitter.raise_()

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.pushButton, self.pushButton_2)
        Form.setTabOrder(self.pushButton_2, self.tabWidget)
        self.eventos()

    def eventos(self):
        self.pushButton.clicked.connect(self.cadastrar)
        self.pushButton_2.clicked.connect(self.cancelar)

    def cadastrar(self):
        if(not self.nome.text()  or not self.senha.text()):
            print("preencha o usuario e senha!")
        else:
            sql.inserir_usuario(self.nome.text(),self.senha.text())
    def cancelar(self):
        import sys
        sys.exit()


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Cadastrar Usuário"))
        self.label_3.setText(_translate("Form", "Cadastrar Produto"))
        self.label_2.setText(_translate("Form", "Nome"))
        self.label_4.setText(_translate("Form", "Senha"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", ""))
        self.pushButton.setText(_translate("Form", "Cadastrar"))
        self.pushButton_2.setText(_translate("Form", "Cancelar"))

import recursos

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_cadastrar_usuario()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

