# -*-coding=utf8-*-
import sys
import renameChineseToEnglish
import runSIM
import UI
import time
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QFont


class MainWindow(QMainWindow, UI.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.exePath = os.getcwd()

    def getExistingDirectory(self):
        fileDirectory = QFileDialog.getExistingDirectory(self, "选则文件夹", "/")
        self.filePathEdit.setText(fileDirectory)
        self.changeNameButton.setEnabled(True)
        self.startButton.setEnabled(False)
        self.resultText.setText("请选择查重语言和阙值,选择完毕后请点击更改文件名")

    def changeFilesName(self):
        nowFilePath = self.filePathEdit.text()
        self.resultText.setText("开始更改文件名")

        startTime = time.time()
        cnt = renameChineseToEnglish.rename(nowFilePath)
        endTime = time.time()

        self.resultText.append("更改文件名完成")
        self.resultText.append("共更改%s个包含中文的文件名" % (str(cnt)))
        self.resultText.append("共耗时%.6fs" % (endTime - startTime))
        self.resultText.append("可开始进行查重")
        self.startButton.setEnabled(True)

    def startRunSIM(self):
        mode = self.languageComboBox.currentText()
        startTime = time.time()
        os.chdir(self.filePathEdit.text())

        argv = '-p -t ' + self.limitSpinBox.text()
        argv = argv + ' -o sim_res.txt *.*'
        # print(argv)
        runSIM.runSIM(mode, self.exePath, argv)

        argv = '-o sim_res_all.txt *.*'
        runSIM.runSIM(mode, self.exePath, argv)

        endTime = time.time()
        self.resultText.setText('查重完成\n结果见sim_res.txt和sim_res_all.txt')
        self.resultText.append("共耗时%.6fs" % (endTime - startTime))
        self.startButton.setEnabled(False)
        self.changeNameButton.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
