%define name docker-py
%define version 0.7.2
%define unmangled_version 0.7.2
%define release 1
%define contrail_release 1contrail1
%define _prefix python

Summary: Python client for Docker.
Name: python-%{name}
Version: %{version}
Release: %{release}.%{contrail_release}%{?dist}
Source0: https://pypi.python.org/packages/source/d/docker-py/%{name}-%{unmangled_version}.tar.gz
License: Apache-2.0
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL: http://www.docker.com
Prefix: %{_prefix}
BuildArch: noarch
Vendor:  OpenContrail

BuildRequires:python-devel
BuildRequires:python-setuptools

%description
Python client for Docker rebuilt by OpenContrail from source

%prep
%setup -n %{name}-%{unmangled_version} -n docker-py-%{unmangled_version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)

%changelog
* Thu Mar 26 2015 Nagendra Maynattamai <npchandran@juniper.net> - 0.7.2-1.1contrail1
- Rebuilt from https://pypi.python.org/packages/source/d/docker-py/docker-py-0.7.2.tar.gz
