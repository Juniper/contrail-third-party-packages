MOCK_CONFIG_LOCATION = epel-6-x86_64-contrail
#MOCK_CONFIG_LOCATION = epel-7-x86_64
GIT_ROOT     := $(PWD)/../..
BUILD_BASE          := $(GIT_ROOT)/..
PREP = prep

$(PREP):
	if [ -d "/etc/mock" ]; then \
		sudo cp utils/epel-6-x86_64-contrail.cfg /etc/mock/; \
	fi; \
	mkdir -p $(BUILD_BASE)/BUILD

ifmap-server: $(PREP)
	@echo "About to make ifmap-server"
	#Fetch the source
	spectool -g -R specs/ifmap-server/ifmap-server.spec -C specs/ifmap-server/
	#mock instructions
	mock -r $(MOCK_CONFIG_LOCATION) --buildsrpm --sources specs/ifmap-server/ --spec specs/ifmap-server/ifmap-server.spec --resultdir=$(BUILD_BASE)/BUILD
	mock -r $(MOCK_CONFIG_LOCATION) $(BUILD_BASE)/BUILD/ifmap-server*.src.rpm --resultdir $(BUILD_BASE)/BUILD 
	rm -f specs/ifmap-server/irond-0.3.2-src.zip

iproute2: $(PREP)
	@echo "About to make iproute2 package"
	#Fetch the source
	spectool -g -R specs/iproute2/iproute2.spec -C specs/iproute2/
	#mock instructions
	mock -r $(MOCK_CONFIG_LOCATION) --buildsrpm --sources specs/iproute2/ --spec specs/iproute2/iproute2.spec --resultdir=$(BUILD_BASE)/BUILD
	mock -r $(MOCK_CONFIG_LOCATION) $(BUILD_BASE)/BUILD/iproute*.src.rpm --resultdir $(BUILD_BASE)/BUILD 
	rm -f specs/iproute2/iproute2-*.tar.gz

python-pycassa: $(PREP)
	@echo "About to make python-pycassa"
	#Fetch the source
	spectool -g -R specs/python-pycassa/python-pycassa.spec -C specs/python-pycassa/
	#mock instructions
	mock -r $(MOCK_CONFIG_LOCATION) --buildsrpm --sources specs/python-pycassa/ --spec specs/python-pycassa/python-pycassa.spec --resultdir=$(BUILD_BASE)/BUILD
	mock -r $(MOCK_CONFIG_LOCATION) $(BUILD_BASE)/BUILD/python-pycassa*.src.rpm --resultdir $(BUILD_BASE)/BUILD
	rm -f specs/python-pycassa/pycassa-1.10.0.tar.gz

python-kombu: $(PREP)
	@echo "About to make python-kombu"
	#Fetch the source
	spectool -g -R specs/python-kombu/python-kombu.spec -C specs/python-kombu/
	#mock instructions
	mock -r $(MOCK_CONFIG_LOCATION) --buildsrpm --sources specs/python-kombu/ --spec specs/python-kombu/python-kombu.spec --resultdir=$(BUILD_BASE)/BUILD
	mock -r $(MOCK_CONFIG_LOCATION) $(BUILD_BASE)/BUILD/python-kombu*.src.rpm --resultdir $(BUILD_BASE)/BUILD
	rm -f specs/python-kombu/python=kombu-1.4.1.tar.gz

python-zope-interface: $(PREP)
	@echo "About to make python-zope-interface"
	#Fetch the source
	spectool -g -R specs/python-zope-interface/python-zope-interface.spec -C specs/python-zope-interface/
	#mock instructions
	mock -r $(MOCK_CONFIG_LOCATION) --buildsrpm --sources specs/python-zope-interface/ --spec specs/python-zope-interface/python-zope-interface.spec --resultdir=$(BUILD_BASE)/BUILD
	mock -r $(MOCK_CONFIG_LOCATION) $(BUILD_BASE)/BUILD/python-zope*.src.rpm --resultdir $(BUILD_BASE)/BUILD
	rm -f specs/python-zope-interface/zope.interface*.tar.gz

python-simplejson: $(PREP)
	@echo "About to make python-simplejson"
	#Fetch the source
	spectool -g -R specs/python-simplejson/python-simplejson.spec -C specs/python-simplejson/
	#mock instructions
	mock -r $(MOCK_CONFIG_LOCATION) --buildsrpm --sources specs/python-simplejson/ --spec specs/python-simplejson/python-simplejson.spec --resultdir=$(BUILD_BASE)/BUILD
	mock -r $(MOCK_CONFIG_LOCATION) $(BUILD_BASE)/BUILD/python-simplejson*.src.rpm --resultdir $(BUILD_BASE)/BUILD
	rm -f specs/python-simplejson/simplejson*.tar.gz

python-lxml: $(PREP)
	@echo "About to make python-lxml"
	#Fetch the source
	spectool -g -R specs/python-lxml/python-lxml.spec -C specs/python-lxml/
	#mock instructions
	mock -r $(MOCK_CONFIG_LOCATION) --buildsrpm --sources specs/python-lxml/ --spec specs/python-lxml/python-lxml.spec --resultdir=$(BUILD_BASE)/BUILD
	mock -r $(MOCK_CONFIG_LOCATION) $(BUILD_BASE)/BUILD/python-lxml*.src.rpm --resultdir $(BUILD_BASE)/BUILD
	rm -f specs/python-lxml/lxml*.tar.gz

python-bottle: $(PREP)
	@echo "About to make python-bottle"
	#Fetch the source
	spectool -g -R specs/python-bottle/python-bottle.spec -C specs/python-bottle/
	#mock instructions
	mock -r $(MOCK_CONFIG_LOCATION) --buildsrpm --sources specs/python-bottle/ --spec specs/python-bottle/python-bottle.spec --resultdir=$(BUILD_BASE)/BUILD
	mock -r $(MOCK_CONFIG_LOCATION) $(BUILD_BASE)/BUILD/python-bottle*.src.rpm --resultdir $(BUILD_BASE)/BUILD
	rm -f specs/python-bottle/bottle*.tar.gz

python-geventhttpclient: $(PREP)
	@echo "About to make python-geventhttpclient"
	#Fetch the source
	spectool -g -R specs/python-geventhttpclient/python-geventhttpclient.spec -C specs/python-geventhttpclient/
	#mock instructions
	mock -r $(MOCK_CONFIG_LOCATION) --buildsrpm --sources specs/python-geventhttpclient/ --spec specs/python-geventhttpclient/python-geventhttpclient.spec --resultdir=$(BUILD_BASE)/BUILD
	mock -r $(MOCK_CONFIG_LOCATION) $(BUILD_BASE)/BUILD/python-geventhttpclient*.src.rpm --resultdir $(BUILD_BASE)/BUILD
	rm -f specs/python-geventhttpclient/geventhttpclient*.tar.gz

python-boto: $(PREP)
	@echo "About to make python-boto"
	#Fetch the source
	spectool -g -R specs/python-boto/python-boto.spec -C specs/python-boto/
	#mock instructions
	mock -r $(MOCK_CONFIG_LOCATION) --buildsrpm --sources specs/python-boto/ --spec specs/python-boto/python-boto.spec --resultdir=$(BUILD_BASE)/BUILD
	mock -r $(MOCK_CONFIG_LOCATION) $(BUILD_BASE)/BUILD/python-boto*.src.rpm --resultdir $(BUILD_BASE)/BUILD
	rm -f specs/python-boto/boto*.tar.gz

python-bitarray: $(PREP)
	@echo "About to make python-bitarray"
	#Fetch the source
	spectool -g -R specs/python-bitarray/python-bitarray.spec -C specs/python-bitarray/
	#mock instructions
	mock -r $(MOCK_CONFIG_LOCATION) --buildsrpm --sources specs/python-bitarray/ --spec specs/python-bitarray/python-bitarray.spec --resultdir=$(BUILD_BASE)/BUILD
	mock -r $(MOCK_CONFIG_LOCATION) $(BUILD_BASE)/BUILD/python-bitarray*.src.rpm --resultdir $(BUILD_BASE)/BUILD
	rm -f specs/python-bitarray/bitarray*.tar.gz

python-thrift: $(PREP)
	@echo "About to make python-thrift"
	#Fetch the source
	spectool -g -R specs/python-thrift/python-thrift.spec -C specs/python-thrift/
	#mock instructions
	mock -r $(MOCK_CONFIG_LOCATION) --buildsrpm --sources specs/python-thrift/ --spec specs/python-thrift/python-thrift.spec --resultdir=$(BUILD_BASE)/BUILD
	mock -r $(MOCK_CONFIG_LOCATION) $(BUILD_BASE)/BUILD/python-thrift*.src.rpm --resultdir $(BUILD_BASE)/BUILD
	rm -f specs/python-thrift/thrift*.tar.gz

redis-py: $(PREP)
	@echo "About to make redis-py"
	#Fetch the source
	spectool -g -R specs/redis-py/redis-py.spec -C specs/redis-py/
	#mock instructions
	mock -r $(MOCK_CONFIG_LOCATION) --buildsrpm --sources specs/redis-py/ --spec specs/redis-py/redis-py.spec --resultdir=$(BUILD_BASE)/BUILD
	mock -r $(MOCK_CONFIG_LOCATION) $(BUILD_BASE)/BUILD/redis-py*.src.rpm --resultdir $(BUILD_BASE)/BUILD
	rm -f specs/redis-py/redis*.tar.gz

docker-py: $(PREP)
	@echo "About to make docker-py"
	#Fetch the source
	spectool -g -R specs/python-docker-py/docker-py.spec -C specs/python-docker-py/
	#mock instructions
	mock -r $(MOCK_CONFIG_LOCATION) --buildsrpm --sources specs/python-docker-py/ --spec specs/python-docker-py/docker-py.spec --resultdir=$(BUILD_BASE)/BUILD
	mock -r $(MOCK_CONFIG_LOCATION) $(BUILD_BASE)/BUILD/docker-py*.src.rpm --resultdir $(BUILD_BASE)/BUILD
	rm -f specs/python-docker-py/docker*.tar.gz

xmltodict: $(PREP)
	@echo "About to make xmltodict"
	#Fetch the source
	spectool -g -R specs/xmltodict/xmltodict.spec -C specs/xmltodict/
	#mock instructions
	mock -r $(MOCK_CONFIG_LOCATION) --buildsrpm --sources specs/xmltodict/ --spec specs/xmltodict/xmltodict.spec --resultdir=$(BUILD_BASE)/BUILD
	mock -r $(MOCK_CONFIG_LOCATION) $(BUILD_BASE)/BUILD/xmltodict*.src.rpm --resultdir $(BUILD_BASE)/BUILD
	rm -f specs/xmltodict/xmltodict*.tar.gz

libvirt: $(PREP)
	@echo "About to make libvirt"
	#Fetch the source
	spectool -g -R specs/libvirt/libvirt.spec -C specs/libvirt/
	#mock instructions
	mock -r $(MOCK_CONFIG_LOCATION) --buildsrpm --sources specs/libvirt/ --spec specs/libvirt/libvirt.spec --resultdir=$(BUILD_BASE)/BUILD
	mock -r $(MOCK_CONFIG_LOCATION) $(BUILD_BASE)/BUILD/libvirt*.src.rpm --resultdir $(BUILD_BASE)/BUILD
	rm -f specs/libvirt/libvirt*.tar.gz

libipfix: $(PREP)
	@echo "About to make libipfix"
	#Fetch the source
	wget http://ie.archive.ubuntu.com/disk1/disk1/download.sourceforge.net/pub/sourceforge/l/li/libipfix/libipfix/libipfix_110209.tgz --directory-prefix=./specs/libipfix/
	#mock instructions
	mock -r $(MOCK_CONFIG_LOCATION) --buildsrpm --sources specs/libipfix/ --spec specs/libipfix/libipfix.spec --resultdir=$(BUILD_BASE)/BUILD
	mock -r $(MOCK_CONFIG_LOCATION) $(BUILD_BASE)/BUILD/libipfix*.src.rpm --resultdir $(BUILD_BASE)/BUILD
	rm -f specs/libipfix/libipfix*.tar.gz

kafka: $(PREP)
	@echo "About to make kafka"
	#Fetch the source
	spectool -g -R specs/kafka/kafka.spec -C specs/kafka/
	#mock instructions
	/usr/bin/mock -r $(MOCK_CONFIG_LOCATION) --buildsrpm --sources specs/kafka/ --spec specs/kafka/kafka.spec --resultdir=$(BUILD_BASE)/BUILD
	/usr/bin/mock -r $(MOCK_CONFIG_LOCATION) $(BUILD_BASE)/BUILD/kafka*.src.rpm --resultdir $(BUILD_BASE)/BUILD
	rm -f specs/kafka/kafka*.tar.gz

librdkafka: $(PREP)
	@echo "Abt to make librdkafka"
	#Fetch the source
	(cd specs/librdkafka/; wget https://github.com/edenhill/librdkafka/archive/0.8.5.tar.gz)
	#Rename the source tgz
	mv specs/librdkafka/0.8.5.tar.gz specs/librdkafka/librdkafka-0.8.5.tar.gz
	#mock instructions
	/usr/bin/mock -r $(MOCK_CONFIG_LOCATION) --buildsrpm --sources specs/librdkafka/ --spec specs/librdkafka/librdkafka.spec --resultdir=$(BUILD_BASE)/BUILD
	/usr/bin/mock -r $(MOCK_CONFIG_LOCATION) $(BUILD_BASE)/BUILD/librdkafka*.src.rpm --resultdir $(BUILD_BASE)/BUILD
	rm -f specs/librdkafka/librdkafka*.tar.gz
	rm -rf specs/librdkafka/librdkafka-0.8.5-2

kafka-python: $(PREP)
	@echo "About to make kafka-python"
	#Fetch the source
	spectool -g -R specs/kafka-python/kafka-python.spec -C specs/kafka-python/
	#mock instructions
	/usr/bin/mock -r $(MOCK_CONFIG_LOCATION) --buildsrpm --sources specs/kafka-python/ --spec specs/kafka-python/kafka-python.spec --resultdir=$(BUILD_BASE)/BUILD
	/usr/bin/mock -r $(MOCK_CONFIG_LOCATION) $(BUILD_BASE)/BUILD/python-kafka-python*.src.rpm --resultdir $(BUILD_BASE)/BUILD
	rm -f specs/kafka-python/kafka-python*.tar.gz

python-docker-py: $(PREP)
	@echo "About to make python-docker-py"
	# Fetch the source
	(spectool -g -R specs/docker-py/python-docker-py.spec -C specs/docker-py/)
	(mv specs/docker-py/docker-py-0.7.2.tar.gz specs/docker-py/python-docker-py-0.7.2.tar.gz)
	# mock instructions
	/usr/bin/mock -r $(MOCK_CONFIG_LOCATION) --buildsrpm --sources specs/docker-py/ --spec specs/docker-py/python-docker-py.spec --resultdir=$(BUILD_BASE)/BUILD
	/usr/bin/mock -r $(MOCK_CONFIG_LOCATION) $(BUILD_BASE)/BUILD/python-docker-py*.src.rpm --resultdir $(BUILD_BASE)/BUILD
	rm -f specs/docker-py/python-docker-py*.tar.gz

python-requests: $(PREP)
	@echo "About to make python-requests"
	# Fetch the source
	(spectool -g -R specs/requests/python-requests.spec -C specs/requests/)
	(mv specs/requests/requests-2.6.0.tar.gz specs/requests/python-requests-2.6.0.tar.gz)
	# mock instructions
	/usr/bin/mock -r $(MOCK_CONFIG_LOCATION) --buildsrpm --sources specs/requests/ --spec specs/requests/python-requests.spec --resultdir=$(BUILD_BASE)/BUILD
	/usr/bin/mock -r $(MOCK_CONFIG_LOCATION) $(BUILD_BASE)/BUILD/python-requests*.src.rpm --resultdir $(BUILD_BASE)/BUILD
	rm -f specs/requests/python-requests*.tar.gz

all:$(PREP) \
	ifmap-server python-pycassa python-zope-interface \
	python-simplejson python-lxml python-bottle \
	python-geventhttpclient python-boto \
	python-bitarray python-thrift redis-py \
	xmltodict libvirt docker-py kafka librdkafka \
        kafka-python
