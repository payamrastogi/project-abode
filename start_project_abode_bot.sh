#!/bin/bash

source ./venv/bin/activate
pip install -r requirements.txt
nohup python telegram_client.py &
echo $! >> project_abode_bot.pid