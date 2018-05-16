#
# Regular cron jobs for the python-kafka-python package
#
0 4	* * *	root	[ -x /usr/bin/python-kafka-python_maintenance ] && /usr/bin/python-kafka-python_maintenance
