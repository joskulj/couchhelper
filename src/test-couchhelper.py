#!/usr/bin/python

# test-couchhelper - test suite for couchhelper
#
# Copyright 2011 Jochen Skulj, jochen@jochenskulj.de
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.


import unittest

from couchhelper import *

data = [
    { "artist":"Iron Maiden", "album":"Iron Maiden", "year":1980 },
    { "artist":"Iron Maiden", "album":"Killers", "year":1981 },
    { "artist":"Iron Maiden", "album":"The Number Of The Beast", "year":1982 },
    { "artist":"Iron Maiden", "album":"Piece Of Mind","year":1983 },
    { "artist":"Metallica", "album":"Kill 'Em All", "year":1983 },
    { "artist":"Metallica", "album":"Ride The Lightning", "year":1984 },
    { "artist":"Metallica", "album":"Master Of Puppets", "year":1985 },
    { "artist":"Anthrax", "album":"Spreading The Desease", "year":1985 },
    { "artist":"Anthrax", "album":"Among The Living", "year":1987 },
    { "artist":"Anthrax", "album":"State Of Euphoria", "year":1988 },
    { "artist":"Helloween", "album":"Walls Of Jericho", "year":1985 },
    { "artist":"Helloween", "album":"Keeper Of The Seven Keys, Part 1", "year":1987 },
    { "artist":"Helloween", "album":"Keeper Of The Seven Keys, Part 2", "year":1988 }
]

view_source = \
    """
    function(doc) {
        if (doc.value.artist == "Iron Maiden") {
            emit(doc._id, doc._rev)
        }
    }
    """

class URITest(unittest.TestCase):
    """
    Test Case for couchhelper
    """

    def setUp(self):
        """
        creates a test database with test data
        """
        database = CouchDatabase("test-couchhelper-example")
        for entry in data:
            artist = entry["artist"]
            album = entry["album"]
            year = entry["year"]
            doc_id = CouchKey([artist, album])
            doc = CouchDocument(doc_id.get_key())
            doc.set_value("artist", artist)
            doc.set_value("album", album)
            doc.set_value("year", year)
            database.save_document(doc)

    def tearDown(self):
        """
        deletes the test database
        """
        database = CouchDatabase("test-couchhelper-example")
        database.delete_database()

    def test_couch_uri(self):
        """
        tests the class CouchURI
        """
        uri = CouchURI(True)
        uri.append("mydb")
        self.assertEquals(uri.get_uri_string(), "/mydb/")
        uri = CouchURI()
        uri.append("_all_dbs")
        self.assertEquals(uri.get_uri_string(), "/_all_dbs")
        uri = CouchURI()
        uri.append("mydb")
        uri.append("_all_docs")
        self.assertEquals(uri.get_uri_string(), "/mydb/_all_docs")

    def test_keys(self):
        """
        tests, if CouchKey generates unique keys
        """
        key_list = [ ]
        for entry in data:
            artist = entry["artist"]
            album = entry["album"]
            key = CouchKey([artist, album])
            self.assertFalse(key == None)
            key_string = key.get_key()
            self.assertFalse(key_string == None)
            self.assertFalse(key_string in key_list)
            key_list.append(key_string)

    def test_load_document(self):
        """
        tests loading existing documents
        """
        database = CouchDatabase("test-couchhelper-example")
        for entry in data:
            artist = entry["artist"]
            album = entry["album"]
            year = entry["year"]
            doc_id = CouchKey([artist, album])
            doc = database.load_document(doc_id.get_key())
            self.assertTrue(doc != None)
            self.assertEquals(doc.get_value("artist"), artist)
            self.assertEquals(doc.get_value("album"), album)
            self.assertEquals(doc.get_value("year"), year)

    def test_update_document(self):
        """
        tests updating a document
        """
        database = CouchDatabase("test-couchhelper-example")
        artist = "Iron Maiden"
        album = "Powerslave"
        year = "1900"
        doc_id = CouchKey([artist, album])
        doc1 = CouchDocument(doc_id.get_key())
        doc1.set_value("artist", artist)
        doc1.set_value("album", album)
        doc1.set_value("year", year)
        database.save_document(doc1)
        doc2 = database.load_document(doc_id.get_key())
        self.assertTrue(doc2 != None)
        rev_id2 = doc2.get_rev_id()
        self.assertTrue(rev_id2 != None)
        self.assertEquals(doc2.get_value("artist"), artist)
        self.assertEquals(doc2.get_value("album"), album)
        self.assertEquals(doc2.get_value("year"), year)
        doc2.set_value("year", 1984)
        database.save_document(doc2)
        doc3 = database.load_document(doc_id.get_key())
        self.assertTrue(doc3)
        rev_id3 = doc3.get_rev_id()
        self.assertTrue(rev_id3 != None)
        self.assertTrue(rev_id2 != rev_id3)
        self.assertEquals(doc3.get_value("artist"), artist)
        self.assertEquals(doc3.get_value("album"), album)
        self.assertEquals(doc3.get_value("year"), 1984)

    def test_delete_document(self):
        """
        tests deleting a document 
        """
        database = CouchDatabase("test-couchhelper-example")
        artist = "Iron Maiden"
        album = "Somewhere In Time"
        year = 1986
        doc_id = CouchKey([artist, album])
        doc1 = CouchDocument(doc_id.get_key())
        doc1.set_value("artist", artist)
        doc1.set_value("album", album)
        doc1.set_value("year", year)
        database.save_document(doc1)
        doc2 = database.load_document(doc_id.get_key())
        self.assertTrue(doc2 != None)
        database.delete_document(doc2)
        doc3 = database.load_document(doc_id.get_key())
        self.assertTrue(doc3 == None)

    def test_view(self):
        """
        tests usage of a view
        """
        database = CouchDatabase("test-couchhelper-example")
        database.add_view("maiden_view", view_source)
        view_result = database.query_view("maiden_view")
        for entry in view_result:
            doc_id = entry["id"]
            doc = database.load_document(doc_id)
            self.assertEquals(doc.get_value("artist"), "Iron Maiden")

if __name__ == "__main__":
    unittest.main()

