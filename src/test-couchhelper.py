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


class URITest(unittest.TestCase):
    """
    Test Case for couchhelper
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

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

if __name__ == "__main__":
    unittest.main()

