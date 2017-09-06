#
# Regular cron jobs for the python-bottle-cork package
#
0 4	* * *	root	[ -x /usr/bin/python-bottle-cork_maintenance ] && /usr/bin/python-bottle-cork_maintenance
