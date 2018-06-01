%define name docker-py
%define version 0.6.0
%define unmangled_version 0.6.0
%define unmangled_version 0.6.0
%define release 1contrail1

Summary: Python client for Docker.
Name: %{name}
Version: %{version}
Release: %{release}
Source0: https://pypi.python.org/packages/source/d/docker-py/docker-py-0.6.0.tar.gz
License: Apache Licence v2.0
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Patch0: 0001-docker-py.patch

BuildRequires:python-devel
BuildRequires:python-setuptools

%description
An API client for docker written in Python

%prep
%setup -q -n %{name}-%{unmangled_version} -n %{name}-%{unmangled_version}
%patch0 -p0

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
