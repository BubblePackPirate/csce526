#!/bin/bash
set -e

# Apache gets grumpy about PID files pre-existing
rm -f /www/apache2/logs/httpd.pid

/www/bin/apachectl start &

echo "Something bad happened, I shouldnt be here!"
echo "Now enjoy this lovely black hole"
tail -f /dev/null
