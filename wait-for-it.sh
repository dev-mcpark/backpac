#!/bin/bash

dockerize -wait tcp://db:3306 -timeout 20s

echo "Ready db"