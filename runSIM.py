# -*- coding: utf-8 -*-
import os
import win32api


def runSIM(mode, argv):
    nowPath = os.getcwd()
    nowPath = os.path.join(nowPath, 'SIM')
    fileName = 'sim_' + mode + '.exe'
    nowPath = os.path.join(nowPath, fileName)
    # print(nowPath)
    # argv = nowPath + ' ' + argv
    res = win32api.ShellExecute(0, 'open', nowPath, argv, '', 0)

    return res


if __name__ == '__main__':
    runSIM('C++', '123')
