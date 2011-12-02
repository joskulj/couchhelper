#!/usr/bin/python

import unittest

from couchhelper import *

class URITest(unittest.TestCase):

    def test_mydb(self):
        uri = CouchURI(True)
        uri.append("mydb")
        self.assertEquals(uri.get_uri_string(), "/mydb/")

    def test_all_dbs(self):
        uri = CouchURI()
        uri.append("_all_dbs")
        self.assertEquals(uri.get_uri_string(), "/_all_dbs")

    def test_all_docs(self):
        uri = CouchURI()
        uri.append("mydb")
        uri.append("_all_docs")
        self.assertEquals(uri.get_uri_string(), "/mydb/_all_docs")

if __name__ == "__main__":
    unittest.main()

