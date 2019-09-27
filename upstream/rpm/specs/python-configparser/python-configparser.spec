%define srcname configparser

Name:     python-%srcname
Version:  3.5.3
Release:  0
Summary:  ConfigParser module
License:  MIT
URL:      https://bitbucket.org/ambv/configparser
Source0:  https://files.pythonhosted.org/packages/37/ab/4e606ca94d04050cfe393d7496da2a758f27e98e64fa46b49c5ab04e9f20/configparser-3.5.3.tar.gz
BuildArch: noarch

BuildRequires:  python2-devel python2-setuptools
Requires:       python2-setuptools

%description
The ancient ConfigParser module available in the standard library 2.x
has seen a major update in Python 3.2. This package is a backport of
those changes so that they can be used directly in Python 2.6 - 3.5.

%prep
%setup -q -n %{srcname}-%{version}
rm -rf *.egg-info

# Python 2 setuptools cannot handle non-ASCII characters in setup.cfg.
# See https://github.com/pypa/setuptools/issues/1062
sed -i 's/Ł/L/' setup.cfg

%build
%{__python2} setup.py build

%install
# The files are not executable anyway, so just delete the shebangs
rmshebangs() {
  for fil in $(grep -Frl '/usr/bin/env' $1); do
    sed -i.orig "\%/usr/bin/env%d" $fil
    touch -r $fil.orig $fil
    rm $fil.orig
  done
}

%{__python2} setup.py install --skip-build --root %{buildroot}
rmshebangs %{buildroot}%{python2_sitelib}
rm %{buildroot}%{python2_sitelib}/backports/__init__.*
rm -rf %{buildroot}%{python2_sitelib}/*.egg-info

%check
%{__python2} setup.py test

%files
%doc README.rst
%{python2_sitelib}/*
