#
# Regular cron jobs for the python-pyang package
#
0 4	* * *	root	[ -x /usr/bin/python-pyang_maintenance ] && /usr/bin/python-pyang_maintenance
