# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from cadastrar_produto import Ui_cadastrar_produto
from consulta_produto import Ui_consulta_produto

from cadastrar_fornecedor import Ui_Form_fornecedor
from consulta_fornecedor import Ui_consulta_fornecedor

from consulta_usuario import Ui_consulta_usuario


class main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(1182, 632)
        Main.setMinimumSize(QtCore.QSize(1182, 632))
        Main.setMaximumSize(QtCore.QSize(1182, 632))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/img/configure_database_16704.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Main.setWindowIcon(icon)
        self.centralWidget = QtWidgets.QWidget(Main)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1171, 591))
        self.label.setStyleSheet("image: url(:/img/img/logo.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        Main.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(Main)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1182, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuEstoque = QtWidgets.QMenu(self.menuBar)
        self.menuEstoque.setObjectName("menuEstoque")
        self.menuRelat_rio = QtWidgets.QMenu(self.menuBar)
        self.menuRelat_rio.setObjectName("menuRelat_rio")
        self.menuUsuarios = QtWidgets.QMenu(self.menuBar)
        self.menuUsuarios.setObjectName("menuUsuarios")
        self.menuConfigura_es = QtWidgets.QMenu(self.menuBar)
        self.menuConfigura_es.setObjectName("menuConfigura_es")
        self.menuForncedor = QtWidgets.QMenu(self.menuBar)
        self.menuForncedor.setObjectName("menuForncedor")
        Main.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(Main)
        self.statusBar.setObjectName("statusBar")
        Main.setStatusBar(self.statusBar)
        self.cadastrar_produto = QtWidgets.QAction(Main)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/img/icons8-plus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cadastrar_produto.setIcon(icon1)
        self.cadastrar_produto.setObjectName("cadastrar_produto")
        self.consultar_produto = QtWidgets.QAction(Main)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/img/statistics-report-for-business_icon-icons.com_70370.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.consultar_produto.setIcon(icon2)
        self.consultar_produto.setObjectName("consultar_produto")
        self.relatorio_produtos = QtWidgets.QAction(Main)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/img/img/print-printer-tool-with-printed-paper-outlined-symbol_icon-icons.com_57772.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.relatorio_produtos.setIcon(icon3)
        self.relatorio_produtos.setObjectName("relatorio_produtos")
        self.gerenciar_usuario = QtWidgets.QAction(Main)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/img/img/icons8-administrator-male.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.gerenciar_usuario.setIcon(icon4)
        self.gerenciar_usuario.setObjectName("gerenciar_usuario")
        self.actionConsultar_2 = QtWidgets.QAction(Main)
        self.actionConsultar_2.setObjectName("actionConsultar_2")
        self.bancodados = QtWidgets.QAction(Main)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/img/img/settings.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bancodados.setIcon(icon5)
        self.bancodados.setObjectName("bancodados")
        self.backup = QtWidgets.QAction(Main)
        self.backup.setIcon(icon5)
        self.backup.setObjectName("backup")
        self.actionFornecedor_CTRL_F = QtWidgets.QAction(Main)
        self.actionFornecedor_CTRL_F.setObjectName("actionFornecedor_CTRL_F")
        self.cadastrar_fornecedor = QtWidgets.QAction(Main)
        self.cadastrar_fornecedor.setIcon(icon1)
        self.cadastrar_fornecedor.setObjectName("cadastrar_fornecedor")
        self.consultar_fornecedor = QtWidgets.QAction(Main)
        self.consultar_fornecedor.setIcon(icon2)
        self.consultar_fornecedor.setObjectName("consultar_fornecedor")
        self.relatorio_usuarios = QtWidgets.QAction(Main)
        self.relatorio_usuarios.setIcon(icon3)
        self.relatorio_usuarios.setObjectName("relatorio_usuarios")
        self.relatorio_fornecedores = QtWidgets.QAction(Main)
        self.relatorio_fornecedores.setIcon(icon3)
        self.relatorio_fornecedores.setObjectName("relatorio_fornecedores")
        self.menuEstoque.addAction(self.cadastrar_produto)
        self.menuEstoque.addAction(self.consultar_produto)
        self.menuRelat_rio.addAction(self.relatorio_produtos)
        self.menuRelat_rio.addAction(self.relatorio_usuarios)
        self.menuRelat_rio.addAction(self.relatorio_fornecedores)
        self.menuUsuarios.addAction(self.gerenciar_usuario)
        self.menuConfigura_es.addAction(self.bancodados)
        self.menuConfigura_es.addAction(self.backup)
        self.menuForncedor.addAction(self.cadastrar_fornecedor)
        self.menuForncedor.addAction(self.consultar_fornecedor)
        self.menuBar.addAction(self.menuEstoque.menuAction())
        self.menuBar.addAction(self.menuForncedor.menuAction())
        self.menuBar.addAction(self.menuRelat_rio.menuAction())
        self.menuBar.addAction(self.menuUsuarios.menuAction())
        self.menuBar.addAction(self.menuConfigura_es.menuAction())

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)


        self.eventos()

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)
    
    def eventos(self):
        self.cadastrar_produto.triggered.connect(self.cadastrar_p)
        self.consultar_produto.triggered.connect(self.consulta_p)
        self.cadastrar_fornecedor.triggered.connect(self.cadastrar_f)
        self.consultar_fornecedor.triggered.connect(self.consultar_f)
        self.relatorio_produtos.triggered.connect(self.relat)
        self.gerenciar_usuario.triggered.connect(self.gerenciar_u)
        self.bancodados.triggered.connect(self.bancod)
        self.backup.triggered.connect(self.backupp)
        self.relatorio_usuarios.triggered.connect(self.relatorio_usuario)
        self.relatorio_fornecedores.triggered.connect(self.relatorio_fornecedore)

    def cadastrar_p(self):
        print("cadastrar produto")
        self.janela = QtWidgets.QMainWindow()
        self.ui = Ui_cadastrar_produto()
        self.ui.setupUi(self.janela)
        self.janela.show()

    def consulta_p(self):
        print("consulta produto")
        self.janela = QtWidgets.QMainWindow()
        self.ui = Ui_consulta_produto()
        self.ui.setupUi(self.janela)
        self.janela.show()


    def cadastrar_f(self):
        print("cdastrar fornecedor")
        self.janela = QtWidgets.QMainWindow()
        self.ui = Ui_Form_fornecedor()
        self.ui.setupUi(self.janela)
        self.janela.show()

    def consultar_f(self):
        print("consulta fornecedor")
        self.janela = QtWidgets.QMainWindow()
        self.ui = Ui_consulta_fornecedor()
        self.ui.setupUi(self.janela)
        self.janela.show()

    def relat(self):
        print("relatorio")

    def relatorio_usuario(self):
        print("relatorio_usuarios")

    def relatorio_fornecedore(self):
        print("relatorio_fonecedores")

    def gerenciar_u(self):
        print("gerenciar usuario")
        self.janela = QtWidgets.QMainWindow()
        self.ui = Ui_consulta_usuario()
        self.ui.setupUi(self.janela)
        self.janela.show()
        
    def bancod(self):
        print("banco de dados")
    def backupp(self):
        print("backup")

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "SISTEMA ESTOQUE-ARPROTECT"))
        self.menuEstoque.setTitle(_translate("Main", "Esto&que"))
        self.menuRelat_rio.setTitle(_translate("Main", "Re&latório"))
        self.menuUsuarios.setTitle(_translate("Main", "&Usuarios"))
        self.menuConfigura_es.setTitle(_translate("Main", "&Configurações"))
        self.menuForncedor.setTitle(_translate("Main", "Fornecedor"))
        self.cadastrar_produto.setText(_translate("Main", "Cadastrar(CTRL+C)"))
        self.cadastrar_produto.setToolTip(_translate("Main", "<html><head/><body><p><span style=\" color:#c9dc19;\">Cadastrar Produtos no sistema</span></p></body></html>"))
        self.cadastrar_produto.setShortcut(_translate("Main", "Ctrl+C"))
        self.consultar_produto.setText(_translate("Main", "Consultar(CTRL+L)"))
        self.consultar_produto.setToolTip(_translate("Main", "Consulta Produto no Sistema"))
        self.consultar_produto.setShortcut(_translate("Main", "Ctrl+L"))
        self.relatorio_produtos.setText(_translate("Main", "Produtos(CTRL+I)"))
        self.relatorio_produtos.setToolTip(_translate("Main", "Relátorio dos Produtos)"))
        self.relatorio_produtos.setShortcut(_translate("Main", "Ctrl+I"))
        self.gerenciar_usuario.setText(_translate("Main", "Gerenciar(CTRL+U)"))
        self.gerenciar_usuario.setToolTip(_translate("Main", "Gerencie os usuarios do sistema"))
        self.gerenciar_usuario.setShortcut(_translate("Main", "Ctrl+U"))
        self.actionConsultar_2.setText(_translate("Main", "Consultar"))
        self.bancodados.setText(_translate("Main", "Banco de Dados"))
        self.backup.setText(_translate("Main", "Backup"))
        self.actionFornecedor_CTRL_F.setText(_translate("Main", "&Fornecedor(CTRL+F)"))
        self.cadastrar_fornecedor.setText(_translate("Main", "Cadastrar(CTRL+F)"))
        self.cadastrar_fornecedor.setToolTip(_translate("Main", "<html><head/><body><p><span style=\" color:#ffff05;\">Cadastrar Fornecedor</span></p></body></html>"))
        self.cadastrar_fornecedor.setShortcut(_translate("Main", "Ctrl+F"))
        self.consultar_fornecedor.setText(_translate("Main", "Consultar"))
        self.consultar_fornecedor.setToolTip(_translate("Main", "Faça consulta dos fornecedores"))
        self.relatorio_usuarios.setText(_translate("Main", "Usuários"))
        self.relatorio_usuarios.setToolTip(_translate("Main", "Relatório dos usuarios "))
        self.relatorio_fornecedores.setText(_translate("Main", "Forncedores"))
        self.relatorio_fornecedores.setToolTip(_translate("Main", "Relátorio dos Fornecedores"))

import recursos
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    ui = main()
    ui.setupUi(Main)
    Main.show()
    sys.exit(app.exec_())

