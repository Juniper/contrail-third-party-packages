%define srcname configparser

Name:     python-%srcname
Version:  3.8.1
Release:  0
Summary:  ConfigParser module
License:  MIT
URL:      https://bitbucket.org/ambv/configparser
Source0:  https://files.pythonhosted.org/packages/b1/83/fa54eee6643ffb30ab5a5bebdb523c697363658e46b85729e3d587a3765e/configparser-3.8.1.tar.gz
BuildArch: noarch

# BuildRequires:  python-devel
# BuildRequires:  python-setuptools

BuildRequires:  python2-devel python2-setuptools
Requires:       python2-setuptools

%description
The ancient ConfigParser module available in the standard library 2.x
has seen a major update in Python 3.2. This package is a backport of
those changes so that they can be used directly in Python 2.6 - 3.5.

%prep
%setup -q -n %{srcname}-%{version}

%build
%py2_build

%install
# %py2_install

The files are not executable anyway, so just delete the shebangs
rmshebangs() {
  for fil in $(grep -Frl '/usr/bin/env' $1); do
    sed -i.orig "\%/usr/bin/env%d" $fil
    touch -r $fil.orig $fil
    rm $fil.orig
  done
}

# cp -p setup.cfg.py2 setup.cfg
%{__python2} setup.py install --skip-build --root %{buildroot}
rmshebangs %{buildroot}%{python2_sitelib}
rm %{buildroot}%{python2_sitelib}/backports/__init__.*
# %if 0%{?with_python3}
# cp -p setup.cfg.py3 setup.cfg
# %{__python3} setup.py install --skip-build --root %{buildroot}
# rmshebangs %{buildroot}%{python3_sitelib}
# %endif

%check
# cp -p setup.cfg.py2 setup.cfg
%{__python2} setup.py test

%files
%defattr(-,root,root,-)
%doc README
%{python_sitelib}/*
