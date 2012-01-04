couchhelper - Version 0.1.0

Copyright 2011, Jochen Skulj, jochen@jochenskulj.de
Published under GNU General Public License


Installation
============

To install the couchhelper library on a Linux system, execute
following command:

  sudo python setup.py install


Overview
========

couchhelper is a Python class library that helps to access
CouchDB databases. To use the library following classes can
be used:

 - CouchDatabase
 - CouchKey
 - CouchDocument

 All other classes in the library are needed for internal usage.


CouchDatabase
=============

CouchDatabase is used to access a CouchDB database. An instance
can created by passing the name of the database:

  >>> from couchhelper.couchhelper import *
  >>> db = CouchDatabase("example-database")

If the database with the given name doesn't exist, it will be
created. By default, CouchDatabase uses localhost and port
5984 to access CouchDB. If you want to access a CouchDB instance
on another server or at another port, you can pass this as
additional parameters:

  >>> db = CouchDatabase("example-database", "127.0.0.1", "5984")

CouchDatabase contains following functions:

  - get_databases
  - delete_database
  - save_document
  - load_document
  - delete_document
  - get_document_list
  - add_view
  - get_view_list
  - query_view


CouchKey
========

CouchKey is a helper class to generate document ids out of primary 
values. If a document should store one or more values that identify
the document unique you can create a CouchKey by passing a list of
values and generate a key that can be used as a document id:

  >>> key = CouchKey([ "Ulrich", "Lars", "12/26/1963" ])
  >>> key.get_key()
  '2cf1a0aa2fe6fc9d7be3ed30603f4950'


CouchDocument
=============

CouchDocument represents a document that can be stored in a CouchDB.
A instance of the CouchDocument class is primarily a dictionary that
is identified by a document id and has a revision id. To create an
instance the document id has to be passed as parameter of a
constructor. You can use CouchKey class to generate such a document id.
When creating an instance, the revision id should be kept empty. It
will be set when the document is saved or updated in the database.
Example usage:

  >>> doc = CouchDocument(key.get_key())
  >>> doc.set_value("firstname", "Lars")
  >>> doc.set_value("lastname", "Ulrich")
  >>> doc.set_value("birthdate", "12/26/1963")
  >>> db.save_document(doc)
  True
  >>> doc.get_rev_id()
  u'1-a418d081bff35df90fa8ac2fd8fcaaef'

