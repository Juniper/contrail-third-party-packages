%define name geventhttpclient
%define version 1.0a
%define unmangled_version 1.0a
%define unmangled_version 1.0a
%define release 1
%define _relstr 0contrail

Summary: http client library for gevent
Name: python-%{name}
Version: %{version}
Release: %{release}.%{_relstr}
Source0: https://pypi.python.org/packages/source/g/geventhttpclient/geventhttpclient-1.0a.tar.gz
License: UNKNOWN
Group: Development/Libraries
Prefix: %{_prefix}
Vendor: Antonin Amand <antonin.amand@gmail.com>

BuildRequires: python-setuptools
BuildRequires: gcc
BuildRequires: python-devel

%description
UNKNOWN

%prep
%setup -q -n geventhttpclient-1.0a

%build
env CFLAGS="$RPM_OPT_FLAGS" python setup.py build

%install
python setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
