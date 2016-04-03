#!/bin/bash
# Starts the Goal Sentry API Server

HOME=/home/goalsentry
VENVDIR=$HOME/.goalsentry_env
APPDIR=/home/goalsentry/api

cd $APPDIR
source $VENVDIR/bin/activate
$VENVDIR/bin/uwsgi --ini $HOME/api/goalsentry.ini