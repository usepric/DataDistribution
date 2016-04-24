# -*- coding:utf-8 -*-

import os
import subprocess
import DataMessages


class DataExport(object):
    def __init__(self,dbName,tableList,exportPath):
        self.dbName         = dbName
        self.tableList      = tableList
        self.exportPath     = exportPath

    def FullExport(self):
        cmdstr = 'innobackupex --user=' + dbuser + ' --password='+ dbpass + ' --host=127.0.0.1' + ' --datebase=' + tableList + ''
        p = subprocess.Popen(cmdstr,
                             shell=True,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT)
        for line in p.stdout.readlines():
            print line,

        retval = p.wait()

    def DiffExport(self):
        os.system('')


