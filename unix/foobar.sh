#!/bin/bash

echo -n Hola > dummy.txt
./foo &
cat dummy.txt
./bar
