%define srcname kazoo

Name:     python-%srcname
Version:  2.7.0
Release:  0
Summary:  Higher Level Zookeeper Client
License:  Apache 2.0
Url:      https://pypi.python.org/pypi/kazoo/
Source0:   https://pypi.python.org/packages/source/k/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch: noarch

BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  unzip

Requires:       python-six
Requires:       python-eventlet >= 0.17.1

%description
Implements a higher level API to Apache Zookeeper for Python clients.

%prep
%setup -q -n %{srcname}-%{version}

%build
%py2_build

%install
%py2_install

%files
%defattr(-,root,root,-)
%doc LICENSE README.md
%{python_sitelib}/*
