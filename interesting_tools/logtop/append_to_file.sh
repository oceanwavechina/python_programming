#!/bin/bash


while True
do
    date +%s | xargs md5 -s >> test.txt
    sleep 1
done
