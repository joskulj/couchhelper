# Bash script to build Debian Packege

VERSION=0.1.0

rm -rf deb_dist

python setup.py sdist
cp dist/couchhelper-$VERSION.tar.gz .
py2dsc -m 'Jochen Skulj <jochen@jochenskulj.de>' couchhelper-$VERSION.tar.gz 
cd deb_dist/couchhelper-$VERSION
debuild

rm couchhelper-$VERSION.tar.gz 
