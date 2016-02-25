# Example watch control file for uscan
# Rename this file to "watch" and then you can run the "uscan" command
# to check for upstream updates and more.
# See uscan(1) for format

# Compulsory line, this is a version 3 file
version=3

# Uncomment to examine a Webpage
# <Webpage URL> <string match>
#http://www.example.com/downloads.php kafka-(.*)\.tar\.gz
http://download.nextag.com/apache/kafka/0.8.1.1/kafka_2.9.2-0.8.1.1.tgz
# Uncomment to examine a Webserver directory
#http://www.example.com/pub/kafka-(.*)\.tar\.gz

# Uncommment to examine a FTP server
#ftp://ftp.example.com/pub/kafka-(.*)\.tar\.gz debian uupdate

# Uncomment to find new files on sourceforge, for devscripts >= 2.9
# http://sf.net/kafka/kafka-(.*)\.tar\.gz

# Uncomment to find new files on GooglePages
# http://example.googlepages.com/foo.html kafka-(.*)\.tar\.gz
