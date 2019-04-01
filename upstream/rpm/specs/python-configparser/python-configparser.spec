%global pkgname configparser
%global sum Backport of Python 3 configparser module

%if 0%{?fedora} > 12
  %global with_python3 1
%endif

# Rename to python2-configparser after Fedora 23
%if 0%{?fedora} > 23
  %global with_p2subpkg 1
%endif

# __python2 macro doesn't exist for el6
%if 0%{?el6}
  %define __python2 %{__python}
  %define python2_sitelib %{python_sitelib}
%endif

Name:           python-%{pkgname}
Version:	    3.5.0b2
Release:        1%{?dist}
Summary:	    %{sum}
License:	    MIT
URL:		    https://pypi.python.org/pypi/configparser
Source0:	    https://pypi.python.org/packages/source/c/configparser/configparser-%{version}.tar.gz
BuildArch:	    noarch

# For Fedora > 23 builds (protection against rename of python-setuptools)
%if 0%{?with_p2subpkg}
BuildRequires:  python2-devel python2-setuptools
Requires:	    python2-setuptools
%else
BuildRequires:  python2-devel python-setuptools
Requires:	    python-setuptools
Provides:       python2-%{pkgname} = %{version}-%{release}
%endif

%if 0%{?with_python3}
BuildRequires:  python3-devel python3-setuptools
Requires:	    python3-setuptools
%endif

%description
The ancient ConfigParser module available in the standard library 2.x
has seen a major update in Python 3.2. This package is a backport of
those changes so that they can be used directly in Python 2.6 - 3.5.

# For Fedora > 23 builds
%if 0%{?with_p2subpkg}
%package -n python2-%{pkgname}
Summary:        %{sum}
%{?python_provide:%python_provide python2-%{pkgname}}

%description -n python2-%{pkgname}
The ancient ConfigParser module available in the standard library 2.x
has seen a major update in Python 3.2. This package is a backport of
those changes so that they can be used directly in Python 2.6 - 3.5.
%endif

%if 0%{?with_python3}
%package -n python3-%{pkgname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{pkgname}}

%description -n python3-%{pkgname}
The ancient ConfigParser module available in the standard library 2.x
has seen a major update in Python 3.2. This package is a backport of
those changes so that they can be used directly in Python 2.6 - 3.5.
%endif


%prep
%setup -q -n configparser-%{version}
rm -rf *.egg-info


%build
%{__python2} setup.py build
%if 0%{?with_python3}
%{__python3} setup.py build
%endif

%install
rm -rf %{buildroot}
%{__python2} setup.py install --skip-build --root %{buildroot}
%if 0%{?with_python3}
%{__python3} setup.py install --skip-build --root %{buildroot}
%endif

%check
%{__python2} setup.py test
%if 0%{?with_python3}
%{__python3} setup.py test
%endif

# For Fedora > 23 builds
%if 0%{?with_p2subpkg}
%files -n python2-%{pkgname}
%doc README.rst
%{python2_sitelib}/*
%else
%files
%doc README.rst
%{python2_sitelib}/*
%endif

%if 0%{?with_python3}
%files -n python3-%{pkgname}
%doc README.rst
%{python3_sitelib}/*
%endif


%changelog
* Mon Apr 1 2019 Sahana Chandrashekar <sahanas@juniper.net> - 3.5.0b2-1
- Used for contrail third party packages rpm

* Thu Dec 17 2015 Avram Lubkin <aviso@fedoraproject.org> - 3.5.0b2-1
- Updated to build for el6
- Updated to build Python3 packages
- Changed Python2 package name to python2-configparser for Fedora 24+
- Updated description
- Removed license comments

* Thu Jul 16 2015 José Matos <jamatos@fedoraproject.org> - 3.5.0b2-0.2
- Improve description to make it clear that this package in only needed for python 2.7
- Make the license tag information more explicit.

* Wed Jul 15 2015 José Matos <jamatos@fedoraproject.org> - 3.5.0b2-0.1
- First release for Fedora
