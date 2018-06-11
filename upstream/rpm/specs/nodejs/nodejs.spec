%global with_debug 1

# We don't have pkgdocdir on EPEL6 (yet?)
%global _pkgdocdir %{_docdir}/%{name}-%{version}

# ARM builds currently break on the Debug builds, so we'll just
# build the standard runtime until that gets sorted out.
%ifarch %{arm} aarch64 %{power64}
%global with_debug 0
%endif

# == Node.js Version ==
%global nodejs_major 0
%global nodejs_minor 10
%global nodejs_patch 35
%global nodejs_abi %{nodejs_major}.%{nodejs_minor}
%global nodejs_version %{nodejs_major}.%{nodejs_minor}.%{nodejs_patch}

# == Bundled Dependency Versions ==
# v8 - from deps/v8/src/version.cc
%global v8_major 3
%global v8_minor 14
%global v8_build 5
%global v8_patch 11
# V8 presently breaks ABI at least every x.y release while never bumping SONAME
%global v8_abi %{v8_major}.%{v8_minor}
%global v8_version %{v8_major}.%{v8_minor}.%{v8_build}.%{v8_patch}

# c-ares - from deps/cares/include/ares_version.h
%global c_ares_major 1
%global c_ares_minor 9
%global c_ares_patch 0
%global c_ares_version %{c_ares_major}.%{c_ares_minor}.%{c_ares_patch}

# http-parser - from deps/http-parser/http_parser.h
%global http_parser_major 1
%global http_parser_minor 2
%global http_parser_version %{http_parser_major}.%{http_parser_minor}

# punycode - from lib/punycode.js
# Note: this was merged into the mainline since 0.6.x
%global punycode_major 1
%global punycode_minor 2
%global punycode_patch 0
%global punycode_version %{punycode_major}.%{punycode_minor}.%{punycode_patch}

Name: nodejs
Version: %{nodejs_version}
Release: 3%{?dist}
Summary: JavaScript runtime
License: MIT and ASL 2.0 and ISC and BSD
Group: Development/Languages
URL: http://nodejs.org/

# Exclusive archs must match v8
# In Fedora, this would be specified with %{nodejs_arches}
# keep it in sync.
ExclusiveArch: %{ix86} x86_64 %{arm}

# nodejs bundles openssl, but we use the system version in Fedora
# because openssl contains prohibited code, we remove openssl completely from
# the tarball, using the script in Source100
Source0: node-v%{version}-stripped.tar.gz
Source100: %{name}-tarball.sh

# The native module Requires generator remains in the nodejs SRPM, so it knows
# the nodejs and v8 versions.  The remainder has migrated to the
# nodejs-packaging SRPM.
Source7: nodejs_native.attr

# Disable running gyp on bundled deps we don't use
Patch1: nodejs-disable-gyp-deps.patch

# use system certificates instead of the bundled ones
# modified version of Debian patch:
# http://patch-tracker.debian.org/patch/series/view/nodejs/0.10.26~dfsg1-1/2014_donotinclude_root_certs.patch
Patch2: nodejs-use-system-certs.patch

BuildRequires: python-devel
BuildRequires: libuv-devel
BuildRequires: zlib-devel
# Node.js requires some features from openssl 1.0.1 for SPDY support
# but we'll try out best
BuildRequires: openssl-devel

# we need the system certificate store when Patch2 is applied
Requires: ca-certificates

#we need ABI virtual provides where SONAMEs aren't enough/not present so deps
#break when binary compatibility is broken
%global nodejs_abi 0.10
Provides: nodejs(abi) = %{nodejs_abi}
Provides: nodejs(v8-abi) = %{v8_abi}

#this corresponds to the "engine" requirement in package.json
Provides: nodejs(engine) = %{version}

# Node.js currently has a conflict with the 'node' package in Fedora
# The ham-radio group has agreed to rename their binary for us, but
# in the meantime, we're setting an explicit Conflicts: here
Conflicts: node <= 0.3.2-11

# The punycode module was absorbed into the standard library in v0.6.
# It still exists as a seperate package for the benefit of users of older
# versions.  Since we've never shipped anything older than v0.10 in Fedora,
# we don't need the seperate nodejs-punycode package, so we Provide it here so
# dependent packages don't need to override the dependency generator.
# See also: RHBZ#11511811
Provides: nodejs-punycode = %{punycode_version}
Provides: npm(punycode) = %{punycode_version}

# Node.js has forked c-ares from upstream in an incompatible way, so we need
# to carry the bundled version internally.
# See https://github.com/nodejs/node/commit/766d063e0578c0f7758c3a965c971763f43fec85
# Keep this in sync with deps/cares/include/ares_version.h
Provides: bundled(c-ares) = %{c_ares_version}

# Node.js is closely tied to the version of v8 that is used with it. It makes
# sense to use the bundled version because upstream consistently breaks ABI
# even in point releases. Node.js upstream has now removed the ability to build
# against a shared system version entirely.
# See https://github.com/nodejs/node/commit/d726a177ed59c37cf5306983ed00ecd858cfbbef
Provides: bundled(v8) = %{v8_version}

# Node.js and http-parser share an upstream. The http-parser upstream does not
# do releases often and is almost always far behind the bundled version
Provides: bundled(http-parser) = %{http_parser_version}


%description
Node.js is a platform built on Chrome's JavaScript runtime
for easily building fast, scalable network applications.
Node.js uses an event-driven, non-blocking I/O model that
makes it lightweight and efficient, perfect for data-intensive
real-time applications that run across distributed devices.

%package devel
Summary: JavaScript runtime - development headers
Group: Development/Languages
Requires: %{name}%{?_isa} == %{version}-%{release}
Requires: libuv-devel%{?_isa}
Requires: v8-devel%{?_isa}
Requires: openssl-devel%{?_isa} zlib-devel%{?_isa}
Requires: nodejs-packaging

%description devel
Development headers for the Node.js JavaScript runtime.

%package docs
Summary: Node.js API documentation
Group: Documentation
BuildArch: noarch

%description docs
The API documentation for the Node.js JavaScript runtime.


%prep
%setup -q -n node-v%{version}

# remove bundled dependencies
%patch1 -p1
rm -rf deps/npm \
       deps/uv \
       deps/zlib

# remove bundled CA certificates
%patch2 -p1
rm -f src/node_root_certs.h


%build
# build with debugging symbols and add defines from libuv (#892601)
export CFLAGS='%{optflags} -g -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -fno-delete-null-pointer-checks'
export CXXFLAGS='%{optflags} -g -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -fno-delete-null-pointer-checks'

./configure --prefix=%{_prefix} \
           --shared-openssl \
           --shared-zlib \
           --shared-libuv \
           --without-npm \
           --without-dtrace

%if %{?with_debug} == 1
# Setting BUILDTYPE=Debug builds both release and debug binaries
make BUILDTYPE=Debug %{?_smp_mflags}
%else
make BUILDTYPE=Release %{?_smp_mflags}
%endif


%install
rm -rf %{buildroot}

./tools/install.py install %{buildroot}

# and remove dtrace file again
rm -rf %{buildroot}/%{_prefix}/lib/dtrace

# Set the binary permissions properly
chmod 0755 %{buildroot}/%{_bindir}/node

%if %{?with_debug} == 1
# Install the debug binary and set its permissions
install -Dpm0755 out/Debug/node %{buildroot}/%{_bindir}/node_g
%endif

# own the sitelib directory
mkdir -p %{buildroot}%{_prefix}/lib/node_modules

# ensure Requires are added to every native module that match the Provides from
# the nodejs build in the buildroot
install -Dpm0644 %{SOURCE7} %{buildroot}%{_rpmconfigdir}/fileattrs/nodejs_native.attr
cat << EOF > %{buildroot}%{_rpmconfigdir}/nodejs_native.req
#!/bin/sh
echo 'nodejs(abi) = %nodejs_abi'
echo 'nodejs(v8-abi) = %v8_abi'
EOF
chmod 0755 %{buildroot}%{_rpmconfigdir}/nodejs_native.req

#install documentation
mkdir -p %{buildroot}%{_pkgdocdir}/html
cp -pr doc/* %{buildroot}%{_pkgdocdir}/html
rm -f %{buildroot}%{_pkgdocdir}/html/nodejs.1
cp -p LICENSE %{buildroot}%{_pkgdocdir}/html
cp -p ChangeLog LICENSE README.md AUTHORS %{buildroot}%{_pkgdocdir}

#node-gyp needs common.gypi too
mkdir -p %{buildroot}%{_datadir}/node
cp -p common.gypi %{buildroot}%{_datadir}/node


%check
# Fail the build if the versions don't match
%{buildroot}/%{_bindir}/node -e "require('assert').equal(process.versions.node, '%{nodejs_version}')"
%{buildroot}/%{_bindir}/node -e "require('assert').equal(process.versions.v8, '%{v8_version}')"
%{buildroot}/%{_bindir}/node -e "require('assert').equal(process.versions.ares.replace(/-DEV$/, ''), '%{c_ares_version}')"
%{buildroot}/%{_bindir}/node -e "require('assert').equal(process.versions.http_parser, '%{http_parser_version}')"

# Ensure we have punycode and that the version matches
%{buildroot}/%{_bindir}/node -e "require(\"assert\").equal(require(\"punycode\").version, '%{punycode_version}')"


%files
%{_bindir}/node
%{_mandir}/man1/node.*
%dir %{_prefix}/lib/node_modules
%dir %{_datadir}/node
%{_rpmconfigdir}/fileattrs/nodejs_native.attr
%{_rpmconfigdir}/nodejs_native.req
%dir %{_pkgdocdir}
%{_pkgdocdir}/ChangeLog
%{_pkgdocdir}/LICENSE
%{_pkgdocdir}/README.md
%{_pkgdocdir}/AUTHORS

%files devel
%if %{?with_debug} == 1
%{_bindir}/node_g
%endif
%{_includedir}/node
%{_datadir}/node/common.gypi

%files docs
%dir %{_pkgdocdir}
%{_pkgdocdir}/html

%changelog
* Mon Oct 24 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.10.48-3
- Update to 0.10.48 (security fix)
- https://nodejs.org/en/blog/release/v0.10.48
- fixes CVE-2016-5180

* Mon Oct 03 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.10.47-2
- Update to 0.10.47 (security fix)
- https://nodejs.org/en/blog/release/v0.10.47
- fixes CVE RHBZ#1346910 and RHBZ#1379921
- Bump v8 patch

* Fri Jun 24 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.10.46-1
- Update to 0.10.46 (security fix)
- https://github.com/nodejs/node/blob/v0.10.46/ChangeLog
- Bump http-parser version

* Wed Feb 10 2016 Stephen Gallagher <sgallagh@redhat.com> - 0.10.43-4
- Verify that the built node reports the expected versions
- Properly Provides: http-parser
- Fix Provides: for punycode
- Don't attempt to build on PowerPC

* Wed Feb 10 2016 Stephen Gallagher <sgallagh@redhat.com> - 0.10.42-3
- Remove duplicated content from spec file

* Wed Feb 10 2016 Stephen Gallagher <sgallagh@redhat.com> - 0.10.42-2
- Re-enable debug builds on supported arches

* Wed Feb 10 2016 Stephen Gallagher <sgallagh@redhat.com> - 0.10.42-1
- Update to Node.js 0.10.42
- https://github.com/nodejs/node/blob/v0.10.42/ChangeLog
- Bundle v8, c-ares and http-parser with Node.js
- Drop patches that revert v8 UTF8 change
- Resolves: RHBZ#1306203
- Resolves: RHBZ#1306200
- Resolves: RHBZ#1306207

* Tue Feb 24 2015 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.10.36-3
- bump v8 requires (RHBZ#1195457)

* Thu Feb 19 2015 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.10.36-1
- new upstream release 0.10.36
  http://blog.nodejs.org/2015/01/26/node-v0-10-36-stable/
- Please note that several upstream releases were skipped due to regressions
  reported in the upstream bug tracker.  Please also review the 0.10.34 and
  0.10.35 changelogs available at the above URL for a list of all changes.

* Wed Nov 19 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.10.33-1
- new upstream release 0.10.33
  http://blog.nodejs.org/2014/10/23/node-v0-10-33-stable/
- This release disables SSLv3 to secure Node.js services against the POODLE
  attack.  (CVE-2014-3566; RHBZ#1152789)  For more information or to learn how
  to re-enable SSLv3 in order to support legacy clients, please see the upstream
  release announcement linked above.

* Tue Oct 21 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.10.32-2
- add Provides nodejs-punycode (RHBZ#1151811)

* Thu Sep 18 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.10.32-1
- new upstream release 0.10.32
  http://blog.nodejs.org/2014/08/19/node-v0-10-31-stable/
  http://blog.nodejs.org/2014/09/16/node-v0-10-32-stable/

* Fri Aug 01 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.10.30-1
- new upstream release 0.10.30
  http://blog.nodejs.org/2014/07/31/node-v0-10-30-stable/

* Thu Jun 19 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.10.29-1
- new upstream release 0.10.29
  http://blog.nodejs.org/2014/06/16/node-v0-10-29-stable/
- The invalid UTF8 fix has been reverted since this breaks v8 API, which cannot
  be done in a stable distribution release.  This build of nodejs will behave as
  if NODE_INVALID_UTF8 was set.  For more information on the implications, see:
  http://blog.nodejs.org/2014/06/16/openssl-and-breaking-utf-8-change/

* Sat May 03 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.10.28-1
- new upstream release 0.10.28
  There is no dfference between 0.10.27 and 0.10.28 for Fedora, as the only
  thing updated was npm, which is shipped seperately.  The latest was only
  packaged to avoid confusion.  Please see the v0.10.27 changelog for relevant
  changes in this update:
  http://blog.nodejs.org/2014/05/01/node-v0-10-27-stable/

* Thu Feb 20 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.10.26-1
- new upstream release 0.10.26
  http://blog.nodejs.org/2014/02/18/node-v0-10-26-stable/

* Mon Jan 27 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.10.25-1
- new upstream release 0.10.25
  http://blog.nodejs.org/2014/01/23/node-v0-10-25-stable/

* Thu Dec 19 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.10.24-1
- new upstream release 0.10.24
  http://blog.nodejs.org/2013/12/19/node-v0-10-24-stable/
- upstream install script installs the headers now

* Thu Dec 12 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.10.23-1
- new upstream release 0.10.23
  http://blog.nodejs.org/2013/12/11/node-v0-10-23-stable/

* Tue Nov 12 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.10.22-1
- new upstream release 0.10.22
  http://blog.nodejs.org/2013/11/12/node-v0-10-22-stable/

* Fri Oct 18 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.10.21-1
- new upstream release 0.10.21
  http://blog.nodejs.org/2013/10/18/node-v0-10-21-stable/
- resolves an undisclosed security vulnerability in the http module

* Tue Oct 01 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.10.20-1
- new upstream release 0.10.20
  http://blog.nodejs.org/2013/09/30/node-v0-10-20-stable/

* Wed Sep 25 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.10.19-1
- new upstream release 0.10.19
  http://blog.nodejs.org/2013/09/24/node-v0-10-19-stable/

* Fri Sep 06 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.10.18-1
- new upstream release 0.10.18
  http://blog.nodejs.org/2013/09/04/node-v0-10-18-stable/

* Tue Aug 27 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.10.17-1
- new upstream release 0.10.17
  http://blog.nodejs.org/2013/08/21/node-v0-10-17-stable/

* Sat Aug 17 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.10.16-1
- new upstream release 0.10.16
  http://blog.nodejs.org/2013/08/16/node-v0-10-16-stable/
- add v8-devel to -devel Requires
- restrict -devel Requires to the same architecture

* Wed Aug 14 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.10.14-3
- fix typo in _isa macro in v8 Requires

* Thu Jul 25 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.10.14-1
- new upstream release 0.10.14
  http://blog.nodejs.org/2013/07/25/node-v0-10-14-stable/

* Wed Jul 10 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.10.13-1
- new upstream release 0.10.13
  http://blog.nodejs.org/2013/07/09/node-v0-10-13-stable/
- remove RPM macros, etc. now that they've migrated to nodejs-packaging

* Wed Jun 19 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.10.12-1
- new upstream release 0.10.12
  http://blog.nodejs.org/2013/06/18/node-v0-10-12-stable/
- split off a -packaging subpackage with RPM macros, etc.
- build -docs as noarch
- copy mutiple version logic from nodejs-packaging SRPM for now

* Fri May 31 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.10.9-1
- new upstream release 0.10.9
  http://blog.nodejs.org/2013/05/30/node-v0-10-9-stable/

* Wed May 29 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.10.8-1
- new upstream release 0.10.8
  http://blog.nodejs.org/2013/05/24/node-v0-10-8-stable/

* Wed May 29 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.10.7-1
- new upstream release 0.10.7
  http://blog.nodejs.org/2013/05/17/node-v0-10-7-stable/
- strip openssl from the tarball; it contains prohibited code (RHBZ#967736)
- patch Makefile so we can just remove all bundled deps completely

* Mon May 06 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.10.5-3
- nodejs-fixdep: work properly when a package has no dependencies

* Mon Apr 29 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.10.5-2
- nodejs-symlink-deps: make it work when --check is used and just
  devDependencies exist

* Wed Apr 24 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.10.5-1
- new upstream release 0.10.5
  http://blog.nodejs.org/2013/04/23/node-v0-10-5-stable/

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.10.4-1
- new upstream release 0.10.4
  http://blog.nodejs.org/2013/04/11/node-v0-10-4-stable/
- drop dependency generator files not supported on EL6
- port nodejs_default_filter to EL6
- add nodejs_find_provides_and_requires macro to invoke dependency generator
- invoke the standard RPM provides and requires generators from the Node.js ones
- write native module Requires from nodejs.req
- change the c-ares-devel Requires in -devel to match the BuildRequires

* Tue Apr 09 2013 Stephen Gallagher <sgallagh@redhat.com> - 0.10.3-2.1
- Build against c-ares 1.9

* Thu Apr 04 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.10.3-2
- nodejs-symlink-deps: symlink unconditionally in the buildroot

* Wed Apr 03 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.10.3-1
- new upstream release 0.10.3
  http://blog.nodejs.org/2013/04/03/node-v0-10-3-stable/
- nodejs-symlink-deps: only create symlink if target exists
- nodejs-symlink-deps: symlink devDependencies when --check is used

* Sun Mar 31 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.10.2-1
- new upstream release 0.10.2
  http://blog.nodejs.org/2013/03/28/node-v0-10-2-stable/
- remove %%nodejs_arches macro since it will only be useful if it is present in
  the redhat-rpm-config package
- add default filtering macro to remove unwanted Provides from native modules
- nodejs-symlink-deps now supports multiple modules in one SRPM properly
- nodejs-symlink-deps also now supports a --check argument that works in the
  current working directry instead of the buildroot

* Fri Mar 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.10.1-1
- new upstream release 0.10.1
  http://blog.nodejs.org/2013/03/21/node-v0-10-1-stable/

* Wed Mar 20 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.10.0-4
- fix escaping in dependency generator regular expressions (RHBZ#923941)

* Wed Mar 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.10.0-3
- add virtual ABI provides for node and v8 so binary module's deps break when
  binary compatibility is broken
- automatically add matching Requires to nodejs binary modules
- add %%nodejs_arches macro to future-proof ExcluseArch stanza in dependent
  packages

* Tue Mar 12 2013 Stephen Gallagher <sgallagh@redhat.com> - 0.10.0-2
- Fix up documentation subpackage

* Mon Mar 11 2013 Stephen Gallagher <sgallagh@redhat.com> - 0.10.0-1
- Update to stable 0.10.0 release
- https://raw.github.com/joyent/node/v0.10.0/ChangeLog

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.9.5-10
- minor bugfixes to RPM magic
  - nodejs-symlink-deps: don't create an empty node_modules dir when a module
    has no dependencies
  - nodes-fixdep: support adding deps when none exist
- Add the full set of headers usually bundled with node as deps to nodejs-devel.
  This way `npm install` for native modules that assume the stuff bundled with
  node exists will usually "just work".
-move RPM magic to nodejs-devel as requested by FPC

* Sat Jan 12 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.9.5-9
- fix brown paper bag bug in requires generation script

* Thu Jan 10 2013 Stephen Gallagher <sgallagh@redhat.com> - 0.9.5-8
- Build debug binary and install it in the nodejs-devel subpackage

* Thu Jan 10 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.9.5-7
- don't use make install since it rebuilds everything

* Thu Jan 10 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.9.5-6
- add %%{?isa}, epoch to v8 deps

* Wed Jan 09 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.9.5-5
- add defines to match libuv (#892601)
- make v8 dependency explicit (and thus more accurate)
- add -g to $C(XX)FLAGS instead of patching configure to add it
- don't write pointless 'npm(foo) > 0' deps

* Sat Jan 05 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.9.5-4
- install development headers
- add nodejs_sitearch macro

* Wed Jan 02 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.9.5-3
- make nodejs-symlink-deps actually work

* Tue Jan 01 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.9.5-2
- provide nodejs-devel so modules can BuildRequire it (and be consistent
  with other interpreted languages in the distro)

* Tue Jan 01 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.9.5-1
- new upstream release 0.9.5
- provide nodejs-devel for the moment
- fix minor bugs in RPM magic
- add nodejs_fixdep macro so packagers can easily adjust dependencies in
  package.json files

* Wed Dec 26 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.9.4-1
- new upstream release 0.9.4
- system library patches are now upstream
- respect optflags
- include documentation in subpackage
- add RPM dependency generation and related magic
- guard libuv depedency so it always gets bumped when nodejs does
- add -devel subpackage with enough to make node-gyp happy

* Thu Dec 20 2012 Stephen Gallagher <sgallagh@redhat.com> - 0.9.3-9
- Drop requirement on openssl 1.0.1

* Wed Dec 19 2012 Dan Horák <dan[at]danny.cz> - 0.9.3-8
- set exclusive arch list to match v8

* Tue Dec 18 2012 Stephen Gallagher <sgallagh@redhat.com> - 0.9.3-7
- Add remaining changes from code review
- Remove unnecessary BuildRequires on findutils
- Remove %%clean section

* Fri Dec 14 2012 Stephen Gallagher <sgallagh@redhat.com> - 0.9.3-6
- Fixes from code review
- Fix executable permissions
- Correct the License field
- Build debuginfo properly

* Thu Dec 13 2012 Stephen Gallagher <sgallagh@redhat.com> - 0.9.3-5
- Return back to using the standard binary name
- Temporarily adding a conflict against the ham radio node package until they
  complete an agreed rename of their binary.

* Wed Nov 28 2012 Stephen Gallagher <sgallagh@redhat.com> - 0.9.3-4
- Rename binary and manpage to nodejs

* Mon Nov 19 2012 Stephen Gallagher <sgallagh@redhat.com> - 0.9.3-3
- Update to latest upstream development release 0.9.3
- Include upstreamed patches to unbundle dependent libraries

* Tue Oct 23 2012 Adrian Alves <alvesadrian@fedoraproject.org>  0.8.12-1
- Fixes and Patches suggested by Matthias Runge

* Mon Apr 09 2012 Adrian Alves <alvesadrian@fedoraproject.org> 0.6.5
- First build.

