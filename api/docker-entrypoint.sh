#!/bin/sh

./wait-for-it.sh elasticsearch:9200 -t 60 -- true
python import_csv.py --filename /data/isrc_lookup.csv