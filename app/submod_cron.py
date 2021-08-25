#!/usr/bin/env

import sys
from importlib import import_module

#sys.path.add('D:/GMG/submodule/SubModule/submod')
sys.path.insert(1, 'D:\\GMG\\submodule\\SubModule\\submod')
import os

file_name = 'test_cron.py'
path = os.path.abspath(file_name)

sys.path.insert(0, path)

from submod.test_cron import test_func


def execute_submod_cron():
    print("execute_submod_cron from submod_cron.py")
    #print(sys.path)
    print("path: ", path)


if __name__ == "__main__":
    execute_submod_cron()
