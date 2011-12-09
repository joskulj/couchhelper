#!/usr/bin/python

from couchhelper import *

def list_databases():
    database = CouchDatabase()
    l = database.get_databases()
    for entry in l:
        print entry

if __name__ == "__main__":
    list_databases()

