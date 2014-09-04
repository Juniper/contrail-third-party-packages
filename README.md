
This repo contains patches and specs for all the third party packages we are building. Along with that a Makefile is provided by which can build individual packages.

The files have been arranged such that when we choose to upstream a new package eg., ifmap-server, we can go to the upstream/rpm/ and copy the ifmap-folder contents to the cloned git@github.com:Juniper/rpms.git and raise a pull request.

1) How to rebuild a thirdparty package?
Have a build-VM ready. Additionally install git,spectool(to get the source targz given a spec file) and mock-1.1.41 ( to build the rpms given the source and spec file)in the VM. Checkout this repo.
Go to $(SB_TOP)/upstream/rpm. Issue make <target-name>. It should place the rpms(source and binary) in BUILD directory outisde the SB.

2) How to debug if the build fails?
The BUILD directory that gets created outside the sandbox should have a build.log file which contains the error messages.

3) How to add new patches and upstream to existing third party package?
Add the patch to the package folder located in $(SB_TOP)/upstream/rpm/specs/<package-name>/. Include the patch in spec file as well.then follow the steps in question 1.

4) How to add a new package?
If you have a spec file and/or  diffs that you apply to an exisiting upstream package put that inside the $(SB_TOP)/upstream/rpm/specs/<package-name>. Change the Make file in $(SB_TOP)/upstream/rpm and add a new target for the package added. The Make should have instructions to start the mock with the spec file and source file location. Use question 2 to debug the make failures.

5) How to upstream a package?
clone git@github.com:Juniper/rpms.git
Copy the folder $(SB_TOP)/upstream/rpm/specs/<package-name> to $(SB_TOP_newly_cloned)/specs/
Raise a pull request. 

6) Build fails because build dependency packages cannot be fetched
Identify the repo that hosts the build dependecy package. Add this repo to the config file, upstream/rpm/utils/ and issue rebuild.
