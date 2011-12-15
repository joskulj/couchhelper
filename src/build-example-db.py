#!/usr/bin/python

import couchhelper

data = [
    { 
        "artist":"Iron Maiden", 
        "album":"Iron Maiden", 
        "year":1980 
    },
    { 
        "artist":"Iron Maiden", 
        "album":"Killers", 
        "year":1981 
    },
    { 
        "artist":"Iron Maiden", 
        "album":"The Number Of The Beast", 
        "year":1982 
    },
    { 
        "artist":"Iron Maiden", 
        "album":"Piece Of Mind", 
        "year":1983 
    },
    { 
        "artist":"Metallica", 
        "album":"Kill 'Em All", 
        "year":1983 
    },
    { 
        "artist":"Metallica", 
        "album":"Ride The Lightning", 
        "year":1984 
    },
    { 
        "artist":"Metallica", 
        "album":"Master Of Puppets", 
        "year":1985 
    },
    { 
        "artist":"Anthrax", 
        "album":"Spreading The Desease", 
        "year":1985
    },
    { 
        "artist":"Anthrax", 
        "album":"Among The Living", 
        "year":1987
    },
    { 
        "artist":"Anthrax", 
        "album":"State Of Euphoria", 
        "year":1988
    },
    { 
        "artist":"Helloween", 
        "album":"Walls Of Jericho", 
        "year":1985
    },
    { 
        "artist":"Helloween", 
        "album":"Keeper Of The Seven Keys, Part 1", 
        "year":1987
    },
    { 
        "artist":"Helloween", 
        "album":"Keeper Of The Seven Keys, Part 2", 
        "year":1988
    }
]

if __name__ == "__main__":
    print "Building example database ..."
    database = couchhelper.CouchDatabase("metal-examples")
    i = 1
    for entry in data:
        doc_id = "".join(["key-", str(i)])
        i = i + 1
        doc = couchhelper.CouchDocument(doc_id)
        for key in entry.keys():
            value = entry[key]
            doc.set_value(key, value)
        database.save_document(doc)
    print "Finished."

