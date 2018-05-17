%define srcname ncclient
%define version 0.3.2
%define unmangled_version 0.3.2
%define release 1
%define _relstr 0contrail0

Summary: Python library for NETCONF clients
Name: python-%{srcname}
Version: %{version}
Release: %{release}.%{_relstr}%{?dist}
Source0: https://github.com/leopoul/%{srcname}/archive/v%{version}.tar.gz
License: Apache License 2.0
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{srcname}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Shikhar Bhushan, Leonidas Poulopoulos <shikhar@schmizz.net, leopoul@noc.grnet.gr>
Url: http://schmizz.net/ncclient/
BuildRequires:  python-devel

%description
UNKNOWN

%prep
%setup -q -n ncclient-0.3.2

%build
python setup.py build

%install
python setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
