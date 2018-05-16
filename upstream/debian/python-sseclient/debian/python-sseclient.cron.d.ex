#
# Regular cron jobs for the python-sseclient package
#
0 4	* * *	root	[ -x /usr/bin/python-sseclient_maintenance ] && /usr/bin/python-sseclient_maintenance
