version=$(shell lsb_release -r | cut -f2 -d":" | cut -f1 -d".")
print-%  : ; @echo $* = $($*)
ifeq ($(strip $(version)), 6)
   MOCK_CONFIG = epel-6-x86_64-contrail
else
   MOCK_CONFIG = epel-7-x86_64-contrail
endif

RPM_DIR   := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
GIT_ROOT     := $(RPM_DIR:/upstream/rpm/=)
BUILD_BASE   ?= $(GIT_ROOT)/..

SPEC_DIR     := $(RPM_DIR)/specs
SPEC_TARGETS := $(notdir $(wildcard $(SPEC_DIR)/*))
UTILS_DIR    := $(RPM_DIR)/utils

PKG_NAME = $(shell rpmspec --query --queryformat='%{name}-%{version}-%{release}\n' $(SPEC_DIR)/$@/$@.spec | head -n1)

all: $(SPEC_TARGETS)

list:
	@echo $(sort $(SPEC_TARGETS))

prep:
	@echo "Build base is $(BUILD_BASE)"
	@if [ -d "/etc/mock" ] && [ ! -f "/etc/mock/$(MOCK_CONFIG).cfg" ]; then \
		sudo cp $(UTILS_DIR)/$(MOCK_CONFIG).cfg /etc/mock/; \
	fi; \
	mkdir -p $(BUILD_BASE)/BUILD; \
	mkdir -p $(BUILD_BASE)/SRPMS; \
	mkdir -p $(BUILD_BASE)/RPMS;

clean_srpms:
	@test -d $(BUILD_BASE)/SRPMS && rm $(BUILD_BASE)/SRPMS/*.src.rpm

clean_rpms:
	@test -d $(BUILD_BASE)/RPMS && rm $(BUILD_BASE)/RPMS/*.rpm

clean: clean_srpms clean_rpms
	::

touch_all:
	find . -exec touch {} +

$(SPEC_TARGETS): prep
	@echo "contrail-third-party-packages: prepare sources for $@"
	spectool -g -R $(SPEC_DIR)/$@/$@.spec -C $(SPEC_DIR)/$@/
	@if ! cat /proc/self/cgroup | grep -q docker ; then \
		echo "contrail-third-party-packages: About to make $@ src.rpm" ; \
		mock -r $(MOCK_CONFIG) --buildsrpm --sources specs/$@/ --spec specs/$@/$@.spec --resultdir=$(BUILD_BASE)/SRPMS ;\
		echo "contrail-third-party-packages: About to make $@ rpm" ; \
		mock -r $(MOCK_CONFIG) $(BUILD_BASE)/SRPMS/$(PKG_NAME).src.rpm --resultdir $(BUILD_BASE)/RPMS ;\
		echo "contrail-third-party-packages: About to clean up src.rpm" ; \
		rm $(BUILD_BASE)/SRPMS/$(PKG_NAME).src.rpm ; \
		rm $(BUILD_BASE)/RPMS/$(PKG_NAME).src.rpm ; \
	else \
		echo "docker env: contrail-third-party-packages: make $@" ; \
		yum-builddep -q -y specs/$@/$@.spec ; \
		rpmbuild -bb \
			--define "_buildrootdir $$(mktemp -d)" \
			--define "_topdir $(BUILD_BASE)" \
			--define "_sourcedir $(SPEC_DIR)/$@" \
			specs/$@/$@.spec ; \
	fi
