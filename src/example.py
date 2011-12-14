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
    database = CouchDatabase("example-database")
    if database.delete_database():
        print "database deleted."

def create_document():
    database = CouchDatabase("example-database")
    doc = CouchDocument("The-Number-Of-The-Beast")
    doc.set_value("title", "The Number of the Beast")
    doc.set_value("artist", "Iron Maiden")
    doc.set_value("year", "1982")
    if database.save_document(doc):
        print doc.get_rev_id()
        print "document saved."
    else:
        print "failed to save document."

def list_documents():
    print "Documents:"
    database = CouchDatabase("example-database")
    doc_list = database.get_document_list()
    for entry in doc_list:
        print entry

def load_document():
    database = CouchDatabase("example-database")
    doc = database.load_document("The-Number-Of-The-Beast")
    print doc.get_doc_id()
    print doc.get_rev_id()
    print doc.get_value("title")
    print doc.get_value("artist")
    print doc.get_value("year")

def update_document():
    database = CouchDatabase("example-database")
    doc = database.load_document("The-Number-Of-The-Beast")
    doc.set_value("vocals", "Bruce Dickinson")
    database.save_document(doc)
    print doc.get_rev_id()

def delete_document():
    print "Delete ..."
    database = CouchDatabase("example-database")
    doc = database.load_document("The-Number-Of-The-Beast")
    database.delete_document(doc)
    doc2 =  database.load_document("The-Number-Of-The-Beast")
    if doc2 == None:
        print "document deleted."

if __name__ == "__main__":
    list_databases()
    create_database()
    list_databases()
    create_document()
    list_documents()
    load_document()
    update_document()
    delete_document()
    # 2nd attempt should fail
    # create_document()
    # delete_database()
    # list_databases()

