version=$(shell lsb_release -r | cut -f2 -d":" | cut -f1 -d".")
print-%  : ; @echo $* = $($*)
ifeq ($(strip $(version)), 6)
   MOCK_CONFIG = epel-6-x86_64-contrail
else
   MOCK_CONFIG = epel-7-x86_64-contrail
endif

RPM_DIR   := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
GIT_ROOT     := $(RPM_DIR:/upstream/rpm/=)
BUILD_BASE   := $(GIT_ROOT)/..

SPEC_DIR     := $(RPM_DIR)/specs
SPEC_TARGETS := $(notdir $(wildcard $(SPEC_DIR)/*))
UTILS_DIR    := $(RPM_DIR)/utils

PKG_NAME = $(shell sed -n 's/Name: \(.*\)/\1/p' $(SPEC_DIR)/$@/$@.spec)

all: $(SPEC_TARGETS)

list:
	@echo $(sort $(SPEC_TARGETS))

prep:
	if [ -d "/etc/mock" ] && [ ! -f "/etc/mock/$(MOCK_CONFIG).cfg" ]; then \
		sudo cp $(UTILS_DIR)/$(MOCK_CONFIG).cfg /etc/mock/; \
	fi; \
	mkdir -p $(BUILD_BASE)/BUILD

srpm-%: prep
	@echo "contrail-third-party-packages: About to make $@ src.rpm"
	spectool -g -R $(SPEC_DIR)/$@/$@.spec -C $(SPEC_DIR)/$@/
	mock -r $(MOCK_CONFIG) --buildsrpm --sources specs/$@/ --spec specs/$@/$@.spec --resultdir=$(BUILD_BASE)/BUILD


$(SPEC_TARGETS): srpm-$@
	@echo "contrail-third-party-packages: About to make $@ rpm"
	mock -r $(MOCK_CONFIG) $(BUILD_BASE)/BUILD/$(PKG_NAME)*.src.rpm --resultdir $(BUILD_BASE)/BUILD
	rm $(BUILD_BASE)/BUILD/$(PKG_NAME)*.src.rpm

