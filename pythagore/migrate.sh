#!/bin/sh
# manage.sh

# Run migrations
python manage.py migrate
python manage.py collectstatic --noinput

# Then run the main container command (passed to us as arguments)
exec "$@"
