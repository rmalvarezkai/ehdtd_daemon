#!/bin/bash

cp db-create.sql /tmp/db-create.sql

cd /tmp

chown 0664 /tmp/db-create.sql

su postgres -c "psql -f db-create.sql"

#psql -h 127.0.0.1 -p 5432 -U ehdtd -w -d ehdtd -f ehdtd.sql

rm -f /tmp/db-create.sql






