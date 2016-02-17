#!/bin/bash
NAME=`dhelper name dockerexample`
docker run -d -P --name $NAME --hostname $NAME --link docker-example-db:db dockerexample

