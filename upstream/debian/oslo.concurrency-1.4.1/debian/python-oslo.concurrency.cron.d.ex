#
# Regular cron jobs for the python-oslo.concurrency package
#
0 4	* * *	root	[ -x /usr/bin/python-oslo.concurrency_maintenance ] && /usr/bin/python-oslo.concurrency_maintenance
