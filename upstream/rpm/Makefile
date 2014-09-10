MOCK_CONFIG_LOCATION = epel-6-x86_64-contrail
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

python-pycassa: $(PREP)
	@echo "About to make python-pycassa"
	#Fetch the source
	spectool -g -R specs/python-pycassa/python-pycassa.spec -C specs/python-pycassa/
	#mock instructions
	mock -r $(MOCK_CONFIG_LOCATION) --buildsrpm --sources specs/python-pycassa/ --spec specs/python-pycassa/python-pycassa.spec --resultdir=$(BUILD_BASE)/BUILD
	mock -r $(MOCK_CONFIG_LOCATION) $(BUILD_BASE)/BUILD/python-pycassa*.src.rpm --resultdir $(BUILD_BASE)/BUILD
	rm -f specs/ifmap-server/pycassa-1.10.0.tar.gz

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
	rm -f specs/python-kombu/zope.interface*.tar.gz

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
	rm -f specs/python-bottle/geventhttpclient*.tar.gz

all:$(PREP) \
	ifmap-server python-pycassa python-zope-interface \
	python-simplejson python-lxml python-bottle \
	python-geventhttpclient
