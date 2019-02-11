%define srcname jsnapy

Name:     python-%srcname
Version:  1.3.2
Release:  0
Summary:  Junos Snapshot Administrator (jsnapy) enables you to capture and audit runtime environment snapshots of your networked devices running the Junos operating system (Junos OS).
License:  Apache 2.0
Url:      https://pypi.org/project/jsnapy/
Source0:  https://pypi.python.org/packages/source/j/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch: noarch

BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  unzip

Requires:       python-six

%description
Junos Snapshot Administrator (jsnapy) enables you to capture and audit runtime environment snapshots of your networked devices running the Junos operating system (Junos OS).

%prep
%setup -q -n %{srcname}-%{version}

%build
%py2_build

%install
%py2_install

%files
%defattr(-,root,root,-)
%doc LICENSE.txt README.rst
%{python_sitelib}/*
