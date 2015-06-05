#
# spec file for package python-kazoo
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           python-kazoo
Version:        1.3.1
Release:        1.1
Summary:        Higher Level Zookeeper Client
License:        Apache-2.0
Group:          Development/Languages/Python
Url:            https://github.com/yahoo/Zake
Source:         https://pypi.python.org/packages/source/k/kazoo/kazoo-%{version}.zip
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  unzip
# Test requirements:
#BuildRequires:  python-gevent
#BuildRequires:  python-mock
#BuildRequires:  python-coverage
#BuildRequires:  python-nose
#BuildRequires:  python-zope.interface >= 3.8.0
#BuildRequires:  python-nose
Requires:       python-zope.interface >= 3.8.0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version} && 0%{?suse_version} <= 1110
%{!?python_sitelib: %global python_sitelib %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%else
BuildArch:      noarch
%endif

%description
Implements a higher level API to Apache Zookeeper for Python clients.

%prep
%setup -q -n kazoo-%{version}

%build
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

#NOTE(saschpe): Currently require a running Zookeeper instance:
#%%check
#python setup.py test

%files
%defattr(-,root,root,-)
%doc LICENSE README.rst
%{python_sitelib}/*

%changelog
* Wed Apr  2 2014 speilicke@suse.com
- Initial version
