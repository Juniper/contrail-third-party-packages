#
# Regular cron jobs for the python-kafka package
#
0 4	* * *	root	[ -x /usr/bin/python-kafka_maintenance ] && /usr/bin/python-kafka_maintenance
