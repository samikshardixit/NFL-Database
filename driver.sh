#! /bin/bash

[ -z "$PGDB" ]              && export PGDB="postgres"
[ -z "$PGUSERNAME" ]        && export PGUSERNAME="postgres"
[ -z "$PGPASSWORD" ]        && export PGPASSWORD="Sidh@1509"
[ -z "$PGHOST" ]            && export PGHOST="localhost"
[ -z "$PGPORT" ]            && export PGPORT="5432"
[ -z "$NFLDBSTARTYEAR" ]    && export NFLDBSTARTYEAR=2018
[ -z "$NFLDBENDYEAR" ]      && export NFLDBENDYEAR=2024
[ -z "$NFLSUBDB" ]          && export NFLSUBDB="nflDb"

echo 'Make a choice:'
echo '    1. Intial DB setup (WARNING THIS TAKES A LONG TIME ONLY RUN ONCE!)'
echo '    2. Run front end'
read USERCHOICE

if [ "$USERCHOICE" -eq 1 ]; then
    pip install -r requirements.txt
    cd setup
    python db_init.py
    cd ..
elif [ "$USERCHOICE" -eq 2 ]; then
    [ -z "$FLASK_APP" ]         && export FLASK_APP="app.py"
    python -m flask run
else
    echo "Invalid Choice"
fi