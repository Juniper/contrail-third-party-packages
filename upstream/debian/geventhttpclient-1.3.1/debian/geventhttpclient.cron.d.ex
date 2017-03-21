#
# Regular cron jobs for the geventhttpclient package
#
0 4	* * *	root	[ -x /usr/bin/geventhttpclient_maintenance ] && /usr/bin/geventhttpclient_maintenance
