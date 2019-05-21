#!/usr/bin/env bash
echo "cefFlask booting server"
python main.py &
echo "cefFlask booting embedded browser in 3"
sleep 1
echo 2
sleep 1
echo 1
sleep 1
pid=$!
python cef_boot.py
kill ${pid}