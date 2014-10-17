INTRO:
This document describes how third party packages are maintained by contrail.

Distro:
We are maintaining the third party packages for debian and centos  separately. The set of packages maintained in this repo for the different distributions may be different.

Overview:
The third party packages that are being built fall under 2 categories. packages which had to be modified(eg., ifmap-server) and packages for which rpms were not available (eg., pycassa)

	When performing updates, decision to update a package or not is made based on the version information mentioned in the spec/rules file.
This is the convention we follow when creating versions:

   1) If we dont modify the third party package in any way, then append the string "0contrail" to the tag "Release" in the spec file
   2) If we are modifying the third party packages then , append the string "<software-release-no>contrail" to the tag "Release" in the spec file. [eg., if we added new patches to a third party package for the current release 3.0 then append string "3contrail" to  the version tag in spec file].

[Try issuing rpm upgrade with the new package to make sure that the new package is recognised as the higher version]

Packages:

Currently the following packages are maintained in this repo:
    ifmap-server
    python-bitarray
    python-bottle
    python-geventhttpclient
    python-lxml
    python-pycassa
    python-simplejson
    python-thrift
    python-zope-interface
    redis-py
    xmltodict
 
Repo Information:
This repo contains patches and specs for all the third party packages we are building. Along with that a Makefile is provided by which can build individual packages.

The files have been arranged such that when we choose to upstream a new package eg., ifmap-server, we can go to the upstream/rpm/ and copy the ifmap-folder contents to the cloned git@github.com:Juniper/rpms.git and raise a pull request.

Debian packaging:

Debian related packages are available in debian/<pkg-name> directory. Making debian packages differ for a first time package creation and modifying an existing package.

Adding a new package:

	1) Get the original source tar.gz file 
	2) Uncompress it
	3) Make sure the DEBEMAIL and DEBFULLNAME environment variables are set
	   in the shell
	4) Debianize the package by going inside the source dir and issuing
	   dh_make -f ../<pkg-name>.tar.gz
	   The above command creates a debian folder inside the source and also 
	   a orig.tar.gz file
	5) To make the changes install a tool called quilt and follow setup 
	   instructions:
		alias dquilt="quilt --quiltrc=${HOME}/.quiltrc-dpkg"
		complete -F _quilt_completion $_quilt_complete_opt dquilt

	   Create ~/.quiltrc-dpkg file with following instructions:
		d=. ; while [ ! -d $d/debian -a `readlink -e $d` != / ]; do d=$d/..; done
		if [ -d $d/debian ] && [ -z $QUILT_PATCHES ]; then
		    # if in Debian packaging tree with unset $QUILT_PATCHES
		    QUILT_PATCHES="debian/patches"
		    QUILT_PATCH_OPTS="--reject-format=unified"
		    QUILT_DIFF_ARGS="-p ab --no-timestamps --no-index --color=auto"
		    QUILT_REFRESH_ARGS="-p ab --no-timestamps --no-index"
		    QUILT_COLORS="diff_hdr=1;32:diff_add=1;34:diff_rem=1;31:diff_hunk=1;33:diff_ctx=35:diff_cctx=33"
		    if ! [ -d $d/debian/patches ]; then mkdir $d/debian/patches; fi
		fi
	6) Making changes to the package using quilt at a high level involves,
		1) creating debian/patches folder (if it does not exist)
		2) create a new patch file using "dquilt new <patch-name>.patch
		3) Add the file names that have to be modified using dquilt,
		   "dquilt add debian/rules"
		4) Issue "dquilt refresh" to capture all the changes in the patch
		   file
		5) describe the patch using "dquilt header -e"
	7) After making the changes include the revision number 1contrail1
           by issuing "dch -v <version-revision>"
	8) Issue "dpkg-buildpackage -us -uc" to make sure the package 
           builds with your changes
	   If successful this generates the following:
		 <pkg-name>_<version>-<revision>.dsc (called the src pkg)
		 <pkg-name>_<version>-<revision>.debian.tar.gz (just the debian folder)
		 <pkg-name>_<version>-<revision>_<arch>.deb (binary)
         	 <pkg-name>_<version>-<revision>_<arch>.changes

	9) commit the orig.tar.gz, .dsc and .debian.tar.gz file to github
	10)To push the package to ppa please refer to the packaging section

Modifying an existing package:

	1) check out the third party repo, and go the the debian/<package-name>
	2) It should contain orig.tar.gz, .dsc and .debian.tar.gz files
	3) Issue "dpkg-source -x <pkg-name>_<version>-<revision>.dsc"  
	4) Follow step 6 in "Adding a new package section" to make the
           changes to the current package
	5) After testing out the package change the revision of the 
	   package by modifying the changelog file or by issuing 
	   "dch -v <version-revision>"
	   where version is the upstream version number
	   and revision is the new revision viz., 1contrail2
	6) Delete the older .dsc and .debian.tar.gz file
	7) Follow step 8 in "Adding a new package section" to create newi
           files and git add the new .dsc and .debian.tar.gz file
   
Uploading package to PPA:

When the newly created package is tested it has to be uploaded to
ppa. Before uploading files to PPA create GPG certificate.
Set the shell variable, DEBSIGN_KEYID=Your_GPG_keyID
Here are the steps to upload a package:
    1) Checkout the repo
    2) Issue "dpkg-source -x <pkg-name>_<version>-<revision>.dsc"
    3) If this is the first time you are uploading the package to ppa
       then .orig.tar.gz file also has to be uploaded.
       Issue "dpkg-buildpackage -sa" (signs the files)
    4) If this is modification to the existing package in ppa, then
       Issue "dpkg-buildpackage -sd" (signs the files)
    5) After the package gets built,
       Issue "dput ppa:https://launchpad.net/~opencontrail/+archive/ubuntu/ppa/ <pkg-name>_<version>-<revision>.changes"
 
          
FAQ:

1) How to rebuild a thirdparty package?

Have a build-VM ready. Additionally install git,spectool(to get the source targz given a spec file) and mock-1.1.41 ( to build the rpms given the source and spec file)in the VM. Checkout this repo.
Go to $(SB_TOP)/upstream/rpm. Issue make <target-name>. It should place the rpms(source and binary) in BUILD directory outisde the SandBox.

3)How to setup mock ?

Mock is provided by epel. For centos 6.4 it can be installed the following way:

# wget http://download.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
# rpm -ivh epel-release-6-8.noarch.rpm

After installing mock, create user and grant sudo access
useradd makerpm -G mock
su - makerpm
rpmdev-setuptree

3) How to debug if the build fails?

The BUILD directory that gets created outside the sandbox should have a build.log file which contains the error messages.

4) How to add a new package?

If you have a spec file and/or  diffs that you apply to an exisiting upstream package put that inside the $(SB_TOP)/upstream/rpm/specs/<package-name>. Change the Make file in $(SB_TOP)/upstream/rpm and add a new target for the package added. The Make should have instructions to start the mock with the spec file and source file location. Use question 2 to debug the make failures.

5) How to upstream a package?

clone git@github.com:Juniper/rpms.git
Copy the folder $(SB_TOP)/upstream/rpm/specs/<package-name> to $(SB_TOP_newly_cloned)/specs/
Raise a pull request. 

6) Build fails because build dependency packages cannot be fetched

Identify the repo that hosts the build dependecy package. Add this repo to the config file, upstream/rpm/utils/ and issue rebuild.

7) How to create a spec file for a python library

Inside the python package issue
python setup.py bdist_rpm --spec-only
to get the spec file

8) How to add new patches and upstream to existing third party package?

Add the patch to the package folder located in $(SB_TOP)/upstream/rpm/specs/<package-name>/. Include the patch in spec file as well.then follow the steps in question 1.
 
