# -*- coding: utf-8 -*-
import os


def rumSIM(mode, argv):
    nowPath = os.getcwd()
    nowPath = os.path.join(nowPath, 'SIM')
    fileName = 'sim_' + mode + '.exe'
    nowPath = os.path.join(nowPath, fileName)
    # print(nowPath)
    argv = nowPath + ' ' + argv
    res = os.system(argv)


if __name__ == '__main__':
    rumSIM('C++', '123')
