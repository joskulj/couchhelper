#!/usr/bin/python

from couchhelper import *

def list_databases():
    database = CouchDatabase()
    l = database.get_databases()
    for entry in l:
        print entry

def create_database():
    database = CouchDatabase("example-database")
    if database.get_name() == "example-database":
        print "database created."

def delete_database():
    pass

if __name__ == "__main__":
    list_databases()
    create_database()
    list_databases()
    delete_database()

