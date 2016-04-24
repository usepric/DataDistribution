# -*- coding:utf8 -*-

import ConfigParser

config = ConfigParser.ConfigParser()
config.read("config")
#source
SDBUSER = config.get("DBINFO", "sdbuser")
SDBPASS = config.get("DBINFO", "sdbpass")
SDBNAME = config.get("DBINFO", "sdbname")
SDBHOST = config.get("DBINFO", "sdbhost")
TABLIST  = config.get("DBINFO", "stablst").replace(',',' ')
#Target
TDBUSER = config.get("DBINFO", "tdbuser")
TDBPASS = config.get("DBINFO", "tdbpass")
TDBHOST = config.get("DBINFO", "tdbhost")
TDBNAME = config.get("DBINFO", "tdbname")

#Mail
MUSER = config.get("MAILINFO", "muser")
MPASS = config.get("MAILINFO", "mpass")
MLIST = config.get("MAILINFO", "receivelist")

print SDBUSER
print SDBPASS
print SDBNAME
print SDBHOST
print TABLIST




