#!/usr/bin/env bash

echo Removing weird characters...
node fixsql.js

echo Converting XML to SQL...
python xmldumpimport.py xml_parts_nohash.xml > parts.sql

echo Generated parts.sql



