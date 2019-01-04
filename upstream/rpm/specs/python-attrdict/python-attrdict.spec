%define srcname attrdict

Name:     python-%srcname
Version:  2.0.0
Release:  0
Summary:  AttrDict is an MIT-licensed library that provides mapping objects that allow their elements to be accessed both as keys and as attributes
License:  MIT License
Url:      https://pypi.org/project/attrdict/
Source0:   https://pypi.python.org/packages/source/a/attrdict/attrdict-2.0.0.tar.gz
BuildArch: noarch

BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  unzip

Requires:       python-six

%description
AttrDict is an MIT-licensed library that provides mapping objects that allow their elements to be accessed both as keys and as attributes

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
