# -*- coding: utf-8 -*-
import os


def runSIM(mode, exePath, argv):
    nowPath = exePath
    nowPath = os.path.join(nowPath, 'SIM')
    fileName = 'sim_' + mode + '.exe'
    nowPath = os.path.join(nowPath, fileName)
    # print(nowPath)
    argv = nowPath + ' ' + argv
    res = os.popen(argv)
    res.close()
