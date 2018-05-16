#
# Regular cron jobs for the python-pyangbind package
#
0 4	* * *	root	[ -x /usr/bin/python-pyangbind_maintenance ] && /usr/bin/python-pyangbind_maintenance
