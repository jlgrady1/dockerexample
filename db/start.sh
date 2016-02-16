#!/bin/bash

ID=`docker run --name docker-example-db --hostname docker-example-db -d -P postgres:9.2`
DB_PORT=`dhelper port $ID`
sleep 5
psql -U postgres -h $DIP -p $DB_PORT -c "CREATE DATABASE dockerexample WITH ENCODING 'UTF8'"
