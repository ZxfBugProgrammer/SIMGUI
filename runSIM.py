# -*- coding: utf-8 -*-
import os
import subprocess

import win32api


def runSIM(mode, argv):
    nowPath = os.getcwd()
    nowPath = os.path.join(nowPath, 'SIM')
    fileName = 'sim_' + mode + '.exe'
    nowPath = os.path.join(nowPath, fileName)
    # print(nowPath)
    argv = nowPath + ' ' + argv
    res = os.popen(argv)
    res.close()
