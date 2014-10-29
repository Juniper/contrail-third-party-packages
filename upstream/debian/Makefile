PREP = prep
GIT_ROOT = $(shell git rev-parse --show-toplevel)

$(PREP): 
	#First time run requires update to install pkgs
	sudo apt-get update
	#Install pbuilder and copy the conf file
	if [ -d "/var/cache/pbuilder" ]; then \
		@echo "Folder found"; \
		cp utils/.pbuilderrc ~/; \
	else \
		@echo "Folder not found"; \
		sudo apt-get install pbuilder debootstrap devscripts; \
		sudo cp utils/.pbuilderrc ~/; \
		sudo pbuilder create; \
	fi; \
	sudo pbuilder update
	mkdir -p $(GIT_ROOT)/../BUILD

kazoo:$(PREP)
	#Copy the kazoo to build dir and prepare a .orig file
	cp -R kazoo/kazoo-1.3.1 $(GIT_ROOT)/../BUILD/
	(cd $(GIT_ROOT)/../BUILD ; rm -rf kazoo-1.3.1/debian/patches)
	(cd $(GIT_ROOT)/../BUILD; tar -zcvf kazoo_1.3.1.orig.tar.gz kazoo-1.3.1)
	
	#Build the kazoo from the BUILD dir	
	(cd $(GIT_ROOT)/../BUILD/kazoo-1.3.1; sudo pdebuild --use-pdebuild-internal --debbuildopts -tc)

all:$(PREP) \
	kazoo
