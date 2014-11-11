#
# Regular cron jobs for the libipfix package
#
0 4	* * *	root	[ -x /usr/bin/libipfix_maintenance ] && /usr/bin/libipfix_maintenance
