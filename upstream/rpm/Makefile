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
	mock -r $(MOCK_CONFIG_LOCATION) $(BUILD_BASE)/SRPMS/ifmap-server*.src.rpm --resultdir $(BUILD_BASE)/BUILD 
	rm -f specs/ifmap-server/irond-0.3.2-src.zip

all:$(PREP) \
	ifmap-server
