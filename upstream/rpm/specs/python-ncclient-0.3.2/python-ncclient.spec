#
# spec file for package python-ncclient
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           python-ncclient
Version:        0.3.2
Release:        2.1.4
Url:            https://github.com/CiscoSystems/ncclient
Summary:        Python NETCONF protocol library
License:        Apache-2.0
Group:          Development/Languages/Python
Source:         ncclient-%{version}.tar.gz
# Forward ported from https://github.com/CiscoSystems/ncclient required for the
# quantum nexus plugin to work with nexus switches
Patch0:         nexus-support.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  python-base
# Documentation requirements:
BuildRequires:  python-Sphinx
Requires:       python-paramiko >= 1.7.7.1
%if 0%{?suse_version} && 0%{?suse_version} <= 1110
%{!?python_sitelib: %global python_sitelib %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%else
BuildArch:      noarch
%endif

%description
ncclient is a Python library that facilitates client-side scripting
and application development around the NETCONF protocol.

%prep
%setup -q -n leopoul-ncclient-3304dc4
%patch0 -p1

%build
python setup.py build
cd docs && make html && rm build/html/.buildinfo

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE README examples docs/build/html
%{python_sitelib}/*

%changelog
* Mon Aug 26 2013 rhafer@suse.com
- added nexus-support.patch: this is required to make make ncclient
  capable of accessing cisco nexus switches (for quantum's nexus
  plugin)
* Thu Aug  8 2013 dmueller@suse.com
- (rpm-wise) downgrade to a released version 0.3.2:
  * http://ncclient.grnet.gr/0.3.2/
* Mon Jul 29 2013 speilicke@suse.com
- Require python-paramiko (for ssh transport)
- Build HTML documentation
