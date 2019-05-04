# RHEL 6 didn't have a __python2 macro.
# Amazon Linux 2015.9 is based on RHEL6, with /usr/bin/python2 -> python2.6, while
# /usr/bin/python -> python2.7.  Explicitly use python2.6.
%if 0%{?rhel} == 6 || 0%{?rhel} == 5
%global __python2 /usr/bin/python2.6
%endif

%if 0%{?rhel} <= 5
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
%endif

%if 0%{?fedora} || 0%{?rhel} >= 8
%global with_docs 1
%else
%global with_docs 0
%endif

%if 0%{?fedora}
%global with_python3 1
%bcond_without tests
%else
%global with_python3 0
%bcond_with tests
%endif

%{!?python_sitelib: %global python_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name: ansible
Summary: SSH-based configuration management, deployment, and task execution system
Version: 2.4.3.0
Release: 1.contrail1%{?dist}

Group: Development/Libraries
License: GPLv3+
Source0: http://releases.ansible.com/ansible/%{name}-%{version}.tar.gz

# Provides default search paths, among them /usr/share/ansible/roles,
# which will be used in other packages
Patch0:  ansible-rolepath.patch

# Patch to utilize a newer jinja2 package on epel6
# Non-upstreamable as it creates a dependency on a specific version of jinja.
# This is desirable for us as we have packages for that version but not for
# upstream as they don't know what their customers are running.
Patch100: ansible-newer-jinja.patch

Url: http://ansible.com
BuildArch: noarch

%if 0%{?rhel} && 0%{?rhel} <= 5
# On RHEL6 use the python26 stack
BuildRequires: python26-devel
Requires: python26-PyYAML
Requires: python26-paramiko
Requires: python26-jinja2
%endif

BuildRequires: python2-devel
BuildRequires: python-setuptools

# For building docs
BuildRequires: python-sphinx

# For tests
# We don't run tests on epel6, so don't bother pulling these in there.
%if %{with tests}
%if (0%{?fedora} ||  0%{?rhel} > 6)
BuildRequires: PyYAML
BuildRequires: python-cryptography
BuildRequires: python-paramiko
# accelerate is the only thing that makes keyczar mandatory.  Since accelerate
# is deprecated, ignore keyczar
#Requires: python-keyczar
BuildRequires: python-six
BuildRequires: python-nose
BuildRequires: python-coverage
BuildRequires: python-mock
#BuildRequires: python-boto3
#BuildRequires: python-botocore
BuildRequires: python-passlib
# rhel7 does not have python-pytest but has pytest
%if 0%{?rhel} > 6
BuildRequires: pytest
#BuildRequires: python-pytest-xdist
#BuildRequires: python-pytest-mock
%else
BuildRequires: python-pytest
BuildRequires: python-pytest-xdist
BuildRequires: python-pytest-mock
%endif
%endif
%endif

%if (0%{?rhel} && 0%{?rhel} <= 6)
# Ansible will work with the jinja2 shipped with RHEL6 but users can gain
# additional jinja features by using the newer version
Requires: python-jinja2-26
BuildRequires: python-jinja2-26

# Distros with python < 2.7.0
BuildRequires: python-unittest2

%else
Requires: python-jinja2
BuildRequires: python-jinja2
%endif

Requires: PyYAML
Requires: python-cryptography
Requires: python-passlib
Requires: python-paramiko
# accelerate is the only thing that makes keyczar mandatory.  Since accelerate
# is deprecated, just ignore it
#Requires: python-keyczar
Requires: python-httplib2
Requires: python-setuptools
Requires: python-six
Requires: sshpass

%if (0%{?fedora} ||  0%{?rhel} > 6)
# needed for json_query filter
# but avoid on rhel6 due to amazon linux conflicts
Requires: python2-jmespath
%endif

# 
# This is needed to update the old ansible-firewall package that is no 
# longer needed. Note that you should also remove ansible-node-firewall manually
# Where you still have it installed. 
#
Provides: ansible-fireball = %{version}-%{release}
Obsoletes: ansible-fireball < 1.2.4

%description

Ansible is a radically simple model-driven configuration management,
multi-node deployment, and remote task execution system. Ansible works
over SSH and does not require any software or daemons to be installed
on remote nodes. Extension modules can be written in any language and
are transferred to managed machines automatically.


%if 0%{?with_python3}
# Note, ansible is not intended to be used as a library so avoiding the
# python3-ansible and python2-ansible package names so we don't confuse users.

# Also note, similarly to dnf in its transition period, the python2 and python3
# versions of ansible should behave identically but python3-only bugs may be present.
# So upstream would like us to ship both py2 and py3 ansible (at least in
# rawhide) for people to beat on and find bugs.
%package -n ansible-python3
Summary: SSH-based configuration management, deployment, and task execution system
BuildRequires: python3-devel
BuildRequires: python3-setuptools

# For tests
BuildRequires: python3-PyYAML
BuildRequires: python3-paramiko
BuildRequires: python3-cryptography
# accelerate is the only thing that makes keyczar mandatory.  Since accelerate
# is deprecated, just ignore it
#BuildRequires: python-keyczar
BuildRequires: python3-six
BuildRequires: python3-nose
BuildRequires: python3-pytest
BuildRequires: python3-pytest-xdist
BuildRequires: python3-pytest-mock
BuildRequires: python3-coverage
BuildRequires: python3-mock
#BuildRequires: python3-boto3
#BuildRequires: python3-botocore
BuildRequires: python3-passlib
BuildRequires: python3-jinja2

Requires: python3-PyYAML
Requires: python3-paramiko
Requires: python3-cryptography
Requires: python3-passlib
# accelerate is the only thing that makes keyczar mandatory.  Since accelerate
# is deprecated, just ignore it
#Requires: python3-keyczar
Requires: python3-setuptools
Requires: python3-six
Requires: python3-jinja2
Requires: sshpass
# needed for json_query filter
Requires: python3-jmespath
%endif


%if 0%{?with_python3}
%description -n ansible-python3

Ansible is a radically simple model-driven configuration management,
multi-node deployment, and remote task execution system. Ansible works
over SSH and does not require any software or daemons to be installed
on remote nodes. Extension modules can be written in any language and
are transferred to managed machines automatically.

This package installs versions of ansible that execute on Python3.
%endif  # with_python3

%package -n ansible-doc
Summary: Documentation for Ansible

%description -n ansible-doc

Ansible is a radically simple model-driven configuration management,
multi-node deployment, and remote task execution system. Ansible works
over SSH and does not require any software or daemons to be installed
on remote nodes. Extension modules can be written in any language and
are transferred to managed machines automatically.

This package installs extensive documentation for ansible

%prep
%setup -q
%patch0 -p1

%if 0%{?rhel} == 6
%patch100 -p1
%endif

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif # with_python3

%build
%{__python2} setup.py build
# Build docs
# EPEL6/7 don't have a recent enough sphinx to build the docs
%if %with_docs
  make webdocs
%endif

%if 0%{?with_python3}
%py3_build
%endif # with_python3


%install
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install --root=$RPM_BUILD_ROOT
popd

for i in $RPM_BUILD_ROOT/%{_bindir}/ansible* ; do
    if [ $(basename $i) = "ansible-connection" -o $(basename $i) = "ansible" ] ; then
        mv $i $i-%{python3_version}
        ln -s %{_bindir}/$(basename $i)-%{python3_version} $i-3
    else
        # The ansible commands are themselves symlinks to /usr/bin/ansible.
        # Need to change them to point to the python3 version
        ln -s %{_bindir}/ansible-3 $i-%{python3_version}
        ln -s %{_bindir}/$(basename $i)-%{python3_version} $i-3
    fi
done
%endif # with_python3

%{__python2} setup.py install --root=$RPM_BUILD_ROOT
for i in $RPM_BUILD_ROOT/%{_bindir}/{ansible,ansible-console,ansible-doc,ansible-galaxy,ansible-playbook,ansible-pull,ansible-vault}  ; do
    mv $i $i-%{python2_version}
    ln -s %{_bindir}/$(basename $i)-%{python2_version} $i
    ln -s %{_bindir}/$(basename $i)-%{python2_version} $i-2
done

mkdir -p $RPM_BUILD_ROOT/etc/ansible/
mkdir -p $RPM_BUILD_ROOT/etc/ansible/roles/
cp examples/hosts $RPM_BUILD_ROOT/etc/ansible/
cp examples/ansible.cfg $RPM_BUILD_ROOT/etc/ansible/
mkdir -p $RPM_BUILD_ROOT%{_datadir}/ansible/roles
mkdir -p $RPM_BUILD_ROOT%{_datadir}/ansible/plugins
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1
cp -v docs/man/man1/*.1 $RPM_BUILD_ROOT/%{_mandir}/man1/

cp -pr docs/docsite/rst .
%if %with_docs
  cp -pr docs/docsite/_build/html .
%endif


%check
# RHEL <= 6 doesn't have a new enough python-mock to run the tests
# Currently RHEL <= 7 doesn't have pytest-xdist or a new enough pytest
# Fedora 25 doesn't have a new enough pytest
%if (0%{?fedora} >= 26 || 0%{?rhel} >= 8) && %{with tests}
if test -z $(which pytest) ; then
  mkdir tests_bin
  pushd tests_bin
  ln -s `which py.test` pytest
  export PATH=$PATH:$(pwd)
  popd
fi
make tests

%if 0%{?with_python3}
pushd %{py3dir}
if test -z $(which pytest) ; then
  mkdir tests_bin
  pushd tests_bin
  ln -s `which py.test` pytest
  export PATH=$PATH:$(pwd)
  popd
fi
make tests
%endif  # python3

%endif  # New enough Fedora/RHEL


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{python_sitelib}/ansible*
%{_bindir}/ansible*
%if 0%{?with_python3}
%exclude %{_bindir}/ansible*-3*
%endif  # python3
%config(noreplace) %{_sysconfdir}/ansible/
%doc README.md PKG-INFO COPYING CHANGELOG.md
%doc %{_mandir}/man1/ansible*
%dir /usr/share/ansible
%dir /usr/share/ansible/roles
%dir /usr/share/ansible/plugins

%if 0%{?with_python3}
%files -n ansible-python3
%defattr(-,root,root,-)
%{python3_sitelib}/ansible*
%{_bindir}/ansible*-3*
%config(noreplace) %{_sysconfdir}/ansible/
%doc README.md PKG-INFO COPYING CHANGELOG.md
%doc %{_mandir}/man1/ansible*
%endif  # python3

%files -n ansible-doc
%doc rst
%if %with_docs
%doc html
%endif

%changelog
* Thu Apr 12 2018 Krzysztof Klimonda <krzysztof.klimonda@codilime.com> - 2.4.3.0-1.contrail1
- Update to Ansible 2.4.3.0, required by contrail ansible scripts (LP #1762621)

* Tue Jan 16 2018 Pavel Cahyna <pcahyna@redhat.com> - 2.4.2.0-2
- Bump Release to not conflict with EPEL

* Tue Dec 19 2017 Pavel Cahyna <pcahyna@redhat.com> - 2.4.2.0-1
- Update to Ansible 2.4.2.0, unbreaks ansible-pull (bz #1506781, issue 31449)
- Claim ownership of the /usr/share/ansible/plugins dir (bz #1499847)

* Tue Nov 7 2017 Pavel Cahyna <pcahyna@redhat.com> - 2.4.1.0-1
- Sync with Fedora version 2.4.1.0-2, brings Ansible 2.4.1.0.
- Drop upstream patches.

* Tue Oct 3 2017 Pavel Cahyna <pcahyna@redhat.com> - 2.4.0.0-5
- Backport a fix for the selinux module. Upstream github issue 30618

* Tue Oct 3 2017 Pavel Cahyna <pcahyna@redhat.com> - 2.4.0.0-4
- Backport patch for CVE-2017-7550 - PR#30875 rhbz#1473645

* Thu Sep 21 2017 Pavel Cahyna <pcahyna@redhat.com> - 2.4.0.0-3
- Require python-jmespath, needed for the json_query filter. bz #1484910

* Fri Sep 15 2017 Pavel Cahyna <pcahyna@redhat.com> - 2.4.0.0-1
- Rebase to the Ansible 2.4.0.0 release (bz #1492477).

* Thu Aug 24 2017 Pavel Cahyna <pcahyna@redhat.com> - 2.3.2.0-2
- Add a runtime dependency on python-passlib (bz #1484860).

* Tue Aug 08 2017 Ryan Brown <rybrown@redhat.com> - 2.3.2.0-1
- Rebase to Ansible 2.3.2 release
- Resolves bz #1478867

* Tue Aug 08 2017 Pavel Cahyna <pcahyna@redhat.com> - 2.3.2.0-0.1.rc5
- Update to the latest release candidate of 2.3.2.0 (rc5)
- Drop the patch for issue 25933 (bz #1463440), it is included upstream.

* Mon Jun 26 2017 Pavel Cahyna <pcahyna@redhat.com> - 2.3.1.0-3
- Claim ownership of the /usr/share/ansible and /usr/share/ansible/roles dirs.

* Thu Jun 22 2017 Pavel Cahyna <pcahyna@redhat.com> - 2.3.1.0-2
- Package for RHEL Extras (inspired by rybrown's work)
- Disable tests in order to reduce build requirements
- Disable Python 3 support
- Do not depend on python-keyczar, it is needed only for the deprecated accelereated mode
- Default role search path in ansible.cfg including /usr/share/ansible/roles
- Apply a patch to fix ansible-galaxy regression https://github.com/ansible/ansible/issues/25933 (will be in 2.3.2)

* Thu Jun 01 2017 Kevin Fenzi <kevin@scrye.com> - 2.3.1.0-1
- Update to 2.3.1.0.

* Wed Apr 19 2017 James Hogarth <james.hogarth@gmail.com> - 2.3.0.0-3
- Update backported patch to the one actually merged upstream

* Wed Apr 19 2017 James Hogarth <james.hogarth@gmail.com> - 2.3.0.0-2
- Backport hotfix to fix ansible-galaxy regression https://github.com/ansible/ansible/issues/22572

* Wed Apr 12 2017 Toshio Kuratomi <toshio@fedoraproject.org> - 2.3.0.0-1
- Update to 2.3.0
- Remove upstreamed patches
- Remove controlpersist socket path path as a custom solution was included
  upstream
- Run the unittests from the upstream tarball now instead of having to download
  separately
- Build a documentation subpackage

* Tue Mar 28 2017 Kevin Fenzi <kevin@scrye.com> - 2.2.2.0-3
- Deal with RHEL7 pytest vs python-pytest.
- Rebase epel6 newer jinja patch.
- Conditionalize exclude for RHEL6 rpm.

* Tue Mar 28 2017 Kevin Fenzi <kevin@scrye.com> - 2.2.2.0-2
- Conditionalize python3 files for epel builds.

* Tue Mar 28 2017 Toshio Kuratomi <toshio@fedoraproject.org> - - 2.2.2.0-1
- 2.2.2.0 final
- Add new patch to fix unittests

* Mon Mar 27 2017 Toshio Kuratomi <toshio@fedoraproject.org> - - 2.2.2.0-0.4.rc1
- Add python-crypto and python3-crypto as explicit requirements

* Mon Mar 27 2017 Toshio Kuratomi <toshio@fedoraproject.org> - - 2.2.2.0-0.3.rc1
- Add a symlink for ansible executables to be accessed via python major version
  (ie: ansible-3) in addition to python-major-minor (ansible-3.6)

* Wed Mar  8 2017 Toshio Kuratomi <toshio@fedoraproject.org> - - 2.2.2.0-0.2.rc1
- Add a python3 ansible package.  Note that upstream doesn't intend for the library
  to be used by third parties so this is really just for the executables.  It's not
  strictly required that the executables be built for both python2 and python3 but
  we do need to get testing of the python3 version to know if it's stable enough to
  go into the next Fedora.  We also want the python2 version available in case a user
  has to get something done and the python3 version is too buggy.
- Fix Ansible cli scripts to handle appended python version

* Wed Feb 22 2017 Kevin Fenzi <kevin@scrye.com> - 2.2.2.0-0.1.rc1
- Update to 2.2.2.0 rc1. Fixes bug #1421485

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 16 2017 Kevin Fenzi <kevin@scrye.com> - 2.2.1.0-1
- Update to 2.2.1.
- Fixes: CVE-2016-9587 CVE-2016-8647 CVE-2016-9587 CVE-2016-8647
- Fixes bug #1405110

* Wed Nov 09 2016 Kevin Fenzi <kevin@scrye.com> - 2.2.0.0-3
- Update unit tests that will skip docker related tests if docker isn't available.
- Drop docker BuildRequires. Fixes bug #1392918

* Fri Nov  4 2016 Toshio Kuratomi <toshio@fedoraproject.org> - - 2.2.0.0-3
- Fix for dnf group install

* Tue Nov 01 2016 Kevin Fenzi <kevin@scrye.com> - 2.2.0.0-2
- Fix some BuildRequires to work on all branches.

* Tue Nov 01 2016 Kevin Fenzi <kevin@scrye.com> - 2.2.0.0-1
- Update to 2.2.0. Fixes #1390564 #1388531 #1387621 #1381538 #1388113 #1390646 #1388038 #1390650
- Fixes for CVE-2016-8628 CVE-2016-8614 CVE-2016-8628 CVE-2016-8614

* Thu Sep 29 2016 Kevin Fenzi <kevin@scrye.com> - 2.1.2.0-1
- Update to 2.1.2

* Thu Jul 28 2016 Kevin Fenzi <kevin@scrye.com> - 2.1.1.0-1
- Update to 2.1.1

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0.0-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jun 15 2016 Matt Domsch <matt@domsch.com> - 2.1.0.0-2
- Force python 2.6 on EL6

* Wed May 25 2016 Kevin Fenzi <kevin@scrye.com> - 2.1.0.0-1
- Update to 2.1.0.0.
- Fixes: 1334097 1337474 1332233 1336266

* Tue Apr 19 2016 Kevin Fenzi <kevin@scrye.com> - 2.0.2.0-1
- Update to 2.0.2.0. https://github.com/ansible/ansible/blob/stable-2.0/CHANGELOG.md
- Fixes CVE-2016-3096
- Fix for failed to resolve remote temporary directory issue. bug #1328359

* Thu Feb 25 2016 Toshio Kuratomi <toshio@fedoraproject.org> - 2.0.1.0-2
- Patch control_path to be not hit path length limitations (RH BZ #1311729)
- Version the test tarball

* Thu Feb 25 2016 Toshio Kuratomi <toshio@fedoraproject.org> - 2.0.1.0-1
- Update to upstream bugfix for 2.0.x release series.

* Thu Feb  4 2016 Toshio Kuratomi <toshio@fedoraproject.org> - - 2.0.0.2-3
- Utilize the python-jinja26 package on EPEL6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Toshio Kuratomi <toshio@fedoraproject.org> - - 2.0.0.2-1
- Ansible 2.0.0.2 release from upstream.  (Minor bugfix to one callback plugin
  API).

* Tue Jan 12 2016 Toshio Kuratomi <toshio@fedoraproject.org> - 2.0.0.1-1
- Ansible 2.0.0.1 from upstream.  Rewrite with many bugfixes, rewritten code,
  and new features. See the upstream changelog for details:
  https://github.com/ansible/ansible/blob/devel/CHANGELOG.md

* Wed Oct 14 2015 Adam Williamson <awilliam@redhat.com> - 1.9.4-2
- backport upstream fix for GH #2043 (crash when pulling Docker images)

* Fri Oct 09 2015 Kevin Fenzi <kevin@scrye.com> 1.9.4-1
- Update to 1.9.4

* Sun Oct 04 2015 Kevin Fenzi <kevin@scrye.com> 1.9.3-3
- Backport dnf module from head. Fixes bug #1267018

* Tue Sep  8 2015 Toshio Kuratomi <toshio@fedoraproject.org> - 1.9.3-2
- Pull in patch for yum module that fixes state=latest issue

* Thu Sep 03 2015 Kevin Fenzi <kevin@scrye.com> 1.9.3-1
- Update to 1.9.3
- Patch dnf as package manager. Fixes bug #1258080
- Fixes bug #1251392 (in 1.9.3 release)
- Add requires for sshpass package. Fixes bug #1258799

* Thu Jun 25 2015 Kevin Fenzi <kevin@scrye.com> 1.9.2-1
- Update to 1.9.2

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 27 2015 Toshio Kuratomi <toshio@fedoraproject.org> - 1.9.1-2
- Fix for dnf

* Tue Apr 28 2015 Kevin Fenzi <kevin@scrye.com> 1.9.1-1
- Update to 1.9.1

* Wed Mar 25 2015 Kevin Fenzi <kevin@scrye.com> 1.9.0.1-2
- Drop upstreamed epel6 patches. 

* Wed Mar 25 2015 Kevin Fenzi <kevin@scrye.com> 1.9.0.1-1
- Update to 1.9.0.1

* Wed Mar 25 2015 Kevin Fenzi <kevin@scrye.com> 1.9.0-1
- Update to 1.9.0

* Thu Feb 19 2015 Kevin Fenzi <kevin@scrye.com> 1.8.4-1
- Update to 1.8.4

* Tue Feb 17 2015 Kevin Fenzi <kevin@scrye.com> 1.8.3-1
- Update to 1.8.3

* Sun Jan 11 2015 Toshio Kuratomi <toshio@fedoraproject.org> - 1.8.2-3
- Work around a bug in python2.6 by using simplejson (applies in EPEL6)

* Wed Dec 17 2014 Michael Scherer <misc@zarb.org> 1.8.2-2
- precreate /etc/ansible/roles and /usr/share/ansible_plugins

* Sun Dec 07 2014 Kevin Fenzi <kevin@scrye.com> 1.8.2-1
- Update to 1.8.2

* Thu Nov 27 2014 Kevin Fenzi <kevin@scrye.com> 1.8.1-1
- Update to 1.8.1

* Tue Nov 25 2014 Kevin Fenzi <kevin@scrye.com> 1.8-2
- Rebase el6 patch

* Tue Nov 25 2014 Kevin Fenzi <kevin@scrye.com> 1.8-1
- Update to 1.8

* Thu Oct  9 2014 Toshio Kuratomi <toshio@fedoraproject.org> - 1.7.2-2
- Add /usr/bin/ansible to the rhel6 newer pycrypto patch

* Wed Sep 24 2014 Kevin Fenzi <kevin@scrye.com> 1.7.2-1
- Update to 1.7.2

* Thu Aug 14 2014 Kevin Fenzi <kevin@scrye.com> 1.7.1-1
- Update to 1.7.1

* Wed Aug 06 2014 Kevin Fenzi <kevin@scrye.com> 1.7-1
- Update to 1.7

* Fri Jul 25 2014 Kevin Fenzi <kevin@scrye.com> 1.6.10-1
- Update to 1.6.10

* Thu Jul 24 2014 Kevin Fenzi <kevin@scrye.com> 1.6.9-1
- Update to 1.6.9 with more shell quoting fixes.

* Tue Jul 22 2014 Kevin Fenzi <kevin@scrye.com> 1.6.8-1
- Update to 1.6.8 with fixes for shell quoting from previous release. 
- Fixes bugs #1122060 #1122061 #1122062

* Mon Jul 21 2014 Kevin Fenzi <kevin@scrye.com> 1.6.7-1
- Update to 1.6.7
- Fixes CVE-2014-4966 and CVE-2014-4967

* Tue Jul 01 2014 Kevin Fenzi <kevin@scrye.com> 1.6.6-1
- Update to 1.6.6

* Wed Jun 25 2014 Kevin Fenzi <kevin@scrye.com> 1.6.5-1
- Update to 1.6.5

* Wed Jun 25 2014 Kevin Fenzi <kevin@scrye.com> 1.6.4-1
- Update to 1.6.4

* Mon Jun 09 2014 Kevin Fenzi <kevin@scrye.com> 1.6.3-1
- Update to 1.6.3

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Kevin Fenzi <kevin@scrye.com> 1.6.2-1
- Update to 1.6.2 release

* Wed May  7 2014 Toshio Kuratomi <toshio@fedoraproject.org> - 1.6.1-1
- Bugfix 1.6.1 release

* Mon May  5 2014 Toshio Kuratomi <toshio@fedoraproject.org> - 1.6-1
- Update to 1.6
- Drop accelerate fix, merged upstream
- Refresh RHEL6 pycrypto patch.  It was half-merged upstream.

* Fri Apr 18 2014 Kevin Fenzi <kevin@scrye.com> 1.5.5-1
- Update to 1.5.5

* Mon Apr  7 2014 Toshio Kuratomi <toshio@fedoraproject.org> - 1.5.4-2
- Fix setuptools requirement to apply to rhel=6, not rhel<6

* Wed Apr  2 2014 Toshio Kuratomi <toshio@fedoraproject.org> - 1.5.4-1
- Update to 1.5.4
- Add upstream patch to fix accelerator mode
- Merge fedora and el6 spec files

* Fri Mar 14 2014 Kevin Fenzi <kevin@scrye.com> 1.5.3-2
- Update to NEW 1.5.3 upstream release.
- Add missing dependency on python-setuptools (el6 build)

* Thu Mar 13 2014 Kevin Fenzi <kevin@scrye.com> 1.5.3-1
- Update to 1.5.3
- Fix ansible-vault for newer python-crypto dependency (el6 build)

* Tue Mar 11 2014 Kevin Fenzi <kevin@scrye.com> 1.5.2-2
- Update to redone 1.5.2 release

* Tue Mar 11 2014 Kevin Fenzi <kevin@scrye.com> 1.5.2-1
- Update to 1.5.2

* Mon Mar 10 2014 Kevin Fenzi <kevin@scrye.com> 1.5.1-1
- Update to 1.5.1

* Fri Feb 28 2014 Kevin Fenzi <kevin@scrye.com> 1.5-1
- Update to 1.5

* Wed Feb 12 2014 Kevin Fenzi <kevin@scrye.com> 1.4.5-1
- Update to 1.4.5

* Sat Dec 28 2013 Kevin Fenzi <kevin@scrye.com> 1.4.3-1
- Update to 1.4.3 with ansible galaxy commands.
- Adds python-httplib2 to requires

* Wed Nov 27 2013 Kevin Fenzi <kevin@scrye.com> 1.4.1-1
- Update to upstream 1.4.1 bugfix release

* Thu Nov 21 2013 Kevin Fenzi <kevin@scrye.com> 1.4-1
- Update to 1.4

* Tue Oct 29 2013 Kevin Fenzi <kevin@scrye.com> 1.3.4-1
- Update to 1.3.4

* Tue Oct 08 2013 Kevin Fenzi <kevin@scrye.com> 1.3.3-1
- Update to 1.3.3

* Thu Sep 19 2013 Kevin Fenzi <kevin@scrye.com> 1.3.2-1
- Update to 1.3.2 with minor upstream fixes

* Mon Sep 16 2013 Kevin Fenzi <kevin@scrye.com> 1.3.1-1
- Update to 1.3.1

* Sat Sep 14 2013 Kevin Fenzi <kevin@scrye.com> 1.3.0-2
- Merge upstream spec changes to support EPEL5
- (Still needs python26-keyczar and deps added to EPEL)

* Thu Sep 12 2013 Kevin Fenzi <kevin@scrye.com> 1.3.0-1
- Update to 1.3.0
- Drop node-fireball subpackage entirely.
- Obsolete/provide fireball subpackage. 
- Add Requires python-keyczar on main package for accelerated mode.

* Wed Aug 21 2013 Kevin Fenzi <kevin@scrye.com> 1.2.3-2
- Update to 1.2.3
- Fixes CVE-2013-4260 and CVE-2013-4259

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 06 2013 Kevin Fenzi <kevin@scrye.com> 1.2.2-1
- Update to 1.2.2 with minor fixes

* Fri Jul 05 2013 Kevin Fenzi <kevin@scrye.com> 1.2.1-2
- Update to newer upstream re-release to fix a syntax error

* Thu Jul 04 2013 Kevin Fenzi <kevin@scrye.com> 1.2.1-1
- Update to 1.2.1
- Fixes CVE-2013-2233

* Mon Jun 10 2013 Kevin Fenzi <kevin@scrye.com> 1.2-1
- Update to 1.2

* Tue Apr 02 2013 Kevin Fenzi <kevin@scrye.com> 1.1-1
- Update to 1.1

* Mon Mar 18 2013 Kevin Fenzi <kevin@scrye.com> 1.0-1
- Update to 1.0

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 30 2012 Michael DeHaan <michael.dehaan@gmail.com> - 0.9-0
- Release 0.9

* Fri Oct 19 2012 Michael DeHaan <michael.dehaan@gmail.com> - 0.8-0
- Release of 0.8

* Thu Aug 9 2012 Michael DeHaan <michael.dehaan@gmail.com> - 0.7-0
- Release of 0.7

* Mon Aug 6 2012 Michael DeHaan <michael.dehaan@gmail.com> - 0.6-0
- Release of 0.6

* Wed Jul 4 2012 Michael DeHaan <michael.dehaan@gmail.com> - 0.5-0
- Release of 0.5

* Wed May 23 2012 Michael DeHaan <michael.dehaan@gmail.com> - 0.4-0
- Release of 0.4

* Mon Apr 23 2012 Michael DeHaan <michael.dehaan@gmail.com> - 0.3-1
- Release of 0.3

* Tue Apr  3 2012 John Eckersberg <jeckersb@redhat.com> - 0.0.2-1
- Release of 0.0.2

* Sat Mar 10 2012  <tbielawa@redhat.com> - 0.0.1-1
- Release of 0.0.1
