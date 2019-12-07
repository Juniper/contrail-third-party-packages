%define srcname fysom

Name:     python-%srcname
Version:  1.0.8
Release:  0
Summary:  pYthOn Finite State Machine
License:  MIT
Url:      https://pypi.org/project/%{srcname}/
Source0:  https://pypi.python.org/packages/source/f/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch: noarch

BuildRequires:  python-devel
BuildRequires:  python-setuptools

%description
Python Finite State Machine

%prep
%setup -q -n %{srcname}-%{version}

%build
%py2_build

%install
%py2_install

%files
%defattr(-,root,root,-)
%doc README
%{python_sitelib}/*
