# -*- coding: utf-8 -*-
import os
import subprocess


def runSIM(mode, exePath, argv):
    nowPath = exePath
    nowPath = os.path.join(nowPath, 'SIM')
    fileName = 'sim_' + mode + '.exe'
    nowPath = os.path.join(nowPath, fileName)
    # print(nowPath)
    argv = nowPath + ' ' + argv
    # res = os.popen(argv)
    # res.close()
    p = subprocess.Popen(argv, stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    p.wait()
    return
