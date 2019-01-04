%define srcname attrdict

Name:     python-%srcname
Version:  2.0.0
Release:  0
Summary:  AttrDict is an MIT-licensed library that provides mapping objects that allow their elements to be accessed both as keys and as attributes
License:  MIT License
Url:      https://pypi.org/project/attrdict/
Source0:   https://files.pythonhosted.org/packages/35/bb/bac3e42ae04bc082c28cd8186bfb5b50fb240a4f7419f876c683125ccc8b/%{srcname}-%{version}.tar.gz
BuildArch: noarch

BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  unzip

Requires:       python-six

%description
https://files.pythonhosted.org/packages/35/bb/bac3e42ae04bc082c28cd8186bfb5b50fb240a4f7419f876c683125ccc8b/attrdict-2.0.0.tar.gz

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
