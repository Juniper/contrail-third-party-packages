#
# Regular cron jobs for the kafka package
#
0 4	* * *	root	[ -x /usr/bin/kafka_maintenance ] && /usr/bin/kafka_maintenance
