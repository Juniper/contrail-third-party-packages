%global pkgname configparser
%global sum Backport of Python 3 configparser module

%define version 3.8.1

%if 0%{?fedora} || 0%{?rhel} > 7
  %global with_python3 1
  # Rename to python2-configparser after Fedora 23
  %global with_p2subpkg 1
%endif

# __python2 macro doesn't exist for el6
%if 0%{?el6}
  %define __python2 %{__python}
  %define python2_sitelib %{python_sitelib}
%endif

Name:           python-%{pkgname}
Version:        3.8.1
Release:        2%{?dist}
Summary:        %{sum}
License:        MIT
URL:            https://bitbucket.org/ambv/configparser
#Source0:        %pypi_source %pkgname
#Source0:        https://files.pythonhosted.org/packages/b6/a6/eceea7c5a5dbcf56815bed411c38cabd8a879386be10717b160e7362b5a2/configparser-3.7.1.tar.gz
Source0:        https://files.pythonhosted.org/packages/b1/83/fa54eee6643ffb30ab5a5bebdb523c697363658e46b85729e3d587a3765e/configparser-3.8.1.tar.gz
BuildArch:      noarch

# # For Fedora > 23 builds (protection against rename of python-setuptools)
# %if 0%{?with_p2subpkg}
# BuildRequires:  python2-devel python2-setuptools
# Requires:       python2-setuptools
# %else
# BuildRequires:  python2-devel python-setuptools
# Requires:       python-setuptools
# Requires:       python2-backports
# Provides:       python2-%{pkgname} = %{version}-%{release}
# %endif

# %if 0%{?with_python3}
# BuildRequires:  python3-devel python3-setuptools
# Requires:       python3-setuptools
# %endif

%description
The ancient ConfigParser module available in the standard library 2.x
has seen a major update in Python 3.2. This package is a backport of
those changes so that they can be used directly in Python 2.6 - 3.5.

# # For Fedora > 23 builds
# %if 0%{?with_p2subpkg}
# %package -n python2-%{pkgname}
# Summary:        %{sum}
# Requires:       python2-backports
# %{?python_provide:%python_provide python2-%{pkgname}}

%description -n python2-%{pkgname}
The ancient ConfigParser module available in the standard library 2.x
has seen a major update in Python 3.2. This package is a backport of
those changes so that they can be used directly in Python 2.6 - 3.5.
%endif

# %if 0%{?with_python3}
# %package -n python3-%{pkgname}
# Summary:        %{sum}
# %{?python_provide:%python_provide python3-%{pkgname}}

# %description -n python3-%{pkgname}
# The ancient ConfigParser module available in the standard library 2.x
# has seen a major update in Python 3.2. This package is a backport of
# those changes so that they can be used directly in Python 2.6 - 3.5.
# %endif


%prep
%setup -q -n configparser-%{version}
rm -rf *.egg-info

# Python 2 setuptools cannot handle non-ASCII characters in setup.cfg.
# See https://github.com/pypa/setuptools/issues/1062
sed 's/Ł/L/' setup.cfg > setup.cfg.py2
cp -p setup.cfg setup.cfg.py3

%build
cp -p setup.cfg.py2 setup.cfg
%{__python2} setup.py build
# %if 0%{?with_python3}
# cp -p setup.cfg.py3 setup.cfg
# %{__python3} setup.py build
# %endif

%install
# The files are not executable anyway, so just delete the shebangs
rmshebangs() {
  for fil in $(grep -Frl '/usr/bin/env' $1); do
    sed -i.orig "\%/usr/bin/env%d" $fil
    touch -r $fil.orig $fil
    rm $fil.orig
  done
}

cp -p setup.cfg.py2 setup.cfg
%{__python2} setup.py install --skip-build --root %{buildroot}
rmshebangs %{buildroot}%{python2_sitelib}
rm %{buildroot}%{python2_sitelib}/backports/__init__.*
# %if 0%{?with_python3}
# cp -p setup.cfg.py3 setup.cfg
# %{__python3} setup.py install --skip-build --root %{buildroot}
# rmshebangs %{buildroot}%{python3_sitelib}
# %endif

%check
cp -p setup.cfg.py2 setup.cfg
%{__python2} setup.py test
# %if 0%{?with_python3}
# cp -p setup.cfg.py3 setup.cfg
# %{__python3} setup.py test
# %endif

# # For Fedora > 23 builds
# %if 0%{?with_p2subpkg}
# %files -n python2-%{pkgname}
# %doc README.rst
# %{python2_sitelib}/backports/configparser/
# %{python2_sitelib}/configparser*
# %else
# %files
# %doc README.rst
# %{python2_sitelib}/backports/*
# %{python2_sitelib}/configparser*
# %endif

# %if 0%{?with_python3}
# %files -n python3-%{pkgname}
# %doc README.rst
# %{python3_sitelib}/*
# %endif
