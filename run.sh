#!/bin/sh
export FLASK_APP=main

if [ $1 = 'develop' ]
then
    export FLASK_ENV=development
    export FLASK_APP=main
    export FLASK_DEBUG=true
else
    export FLASK_ENV=production
    export FLASK_DEBUG=false
fi

flask run