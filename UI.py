# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(600, 500)
        MainWindow.setMinimumSize(QtCore.QSize(600, 500))
        MainWindow.setMaximumSize(QtCore.QSize(600, 500))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.filePathEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.filePathEdit.setMinimumSize(QtCore.QSize(350, 40))
        self.filePathEdit.setMaximumSize(QtCore.QSize(350, 40))
        self.filePathEdit.setReadOnly(True)
        self.filePathEdit.setObjectName("filePathEdit")
        self.horizontalLayout_3.addWidget(self.filePathEdit)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.chooseFileButton = QtWidgets.QToolButton(self.centralwidget)
        self.chooseFileButton.setMinimumSize(QtCore.QSize(20, 40))
        self.chooseFileButton.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.chooseFileButton.setAutoRaise(False)
        self.chooseFileButton.setObjectName("chooseFileButton")
        self.horizontalLayout_3.addWidget(self.chooseFileButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(4, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.resultText = QtWidgets.QTextBrowser(self.centralwidget)
        self.resultText.setObjectName("resultText")
        self.horizontalLayout.addWidget(self.resultText)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.languageLabel = QtWidgets.QLabel(self.centralwidget)
        self.languageLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.languageLabel.setAutoFillBackground(False)
        self.languageLabel.setTextFormat(QtCore.Qt.AutoText)
        self.languageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.languageLabel.setObjectName("languageLabel")
        self.verticalLayout.addWidget(self.languageLabel)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setMinimumSize(QtCore.QSize(100, 30))
        self.comboBox.setMaximumSize(QtCore.QSize(100, 30))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.changeNameButton = QtWidgets.QPushButton(self.centralwidget)
        self.changeNameButton.setEnabled(False)
        self.changeNameButton.setMinimumSize(QtCore.QSize(150, 40))
        self.changeNameButton.setMaximumSize(QtCore.QSize(150, 40))
        self.changeNameButton.setObjectName("changeNameButton")
        self.verticalLayout.addWidget(self.changeNameButton)
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setEnabled(False)
        self.startButton.setMinimumSize(QtCore.QSize(150, 40))
        self.startButton.setMaximumSize(QtCore.QSize(150, 40))
        self.startButton.setObjectName("startButton")
        self.verticalLayout.addWidget(self.startButton)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.setStretch(0, 10)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 2)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 20)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "代码查重软件"))
        self.filePathEdit.setText(_translate("MainWindow", "请选择文件路径"))
        self.chooseFileButton.setText(_translate("MainWindow", "打开文件夹"))
        self.resultText.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">本软件为SIM的GUI</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://dickgrune.com/Programs/similarity_tester/\"><span style=\" font-family:\'-apple-system\'; font-size:16px; text-decoration: underline; color:#0366d6; background-color:#ffffff;\">SIM</span></a><span style=\" font-family:\'-apple-system\'; font-size:16px; color:#24292e; background-color:#ffffff;\">是Dick Grune开发的一款代码查重软件</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'-apple-system\'; font-size:16px; color:#24292e; background-color:#ffffff;\">软件使用说明如下：</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'-apple-system\'; font-size:16px; color:#24292e; background-color:#ffffff;\">1.把需要查重的代码放到同一个文件夹目录下。(只包含需要查重的代码文件，文件夹目录不包含中文)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'-apple-system\'; font-size:16px; color:#24292e; background-color:#ffffff;\">注：</span><a href=\"https://dickgrune.com/Programs/similarity_tester/\"><span style=\" font-family:\'-apple-system\'; text-decoration: underline; color:#0366d6; background-color:#ffffff;\">SIM</span></a><span style=\" font-family:\'-apple-system\'; font-size:16px; color:#24292e; background-color:#ffffff;\">只支持单语言，单文件查重。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'-apple-system\'; font-size:16px; color:#24292e; background-color:#ffffff;\">2.选择文件夹路径。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'-apple-system\'; font-size:16px; color:#24292e; background-color:#ffffff;\">3.软件不支持中文文件名，点击按钮即可自动把文件中的中文更改成对应拼音。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'-apple-system\'; font-size:16px; color:#24292e; background-color:#ffffff;\">4.点击进行查重</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'-apple-system\'; font-size:16px; color:#24292e;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'-apple-system\'; font-size:16px; color:#24292e;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'-apple-system\'; font-size:16px; color:#24292e;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'-apple-system\'; font-size:16px; color:#24292e;\">                                   Made by ZXF</span></p></body></html>"))
        self.languageLabel.setText(_translate("MainWindow", "选择待查重程序语言："))
        self.comboBox.setItemText(0, _translate("MainWindow", "C"))
        self.comboBox.setItemText(1, _translate("MainWindow", "C++"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Java"))
        self.comboBox.setItemText(3, _translate("MainWindow", "lisp"))
        self.comboBox.setItemText(4, _translate("MainWindow", "m2"))
        self.comboBox.setItemText(5, _translate("MainWindow", "mira"))
        self.comboBox.setItemText(6, _translate("MainWindow", "pasc"))
        self.comboBox.setItemText(7, _translate("MainWindow", "8086"))
        self.comboBox.setItemText(8, _translate("MainWindow", "Text"))
        self.changeNameButton.setText(_translate("MainWindow", "点击更改文件名"))
        self.startButton.setText(_translate("MainWindow", "点击查重"))
