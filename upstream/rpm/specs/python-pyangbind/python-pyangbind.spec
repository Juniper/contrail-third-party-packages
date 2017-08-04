# Created by pyp2rpm-3.2.2
# Modified by Sanju <sanjua@juniper.net>
%global pypi_name pyangbind

Name:           python-%{pypi_name}
Version:        0.2.0
Release:        1%{?dist}
Summary:        PyangBind is a plugin for pyang which converts YANG datamodels into a Python class hierarchy, such that Python can be used to manipulate data that conforms with a YANG model

License:        Apache
URL:            https://github.com/robshakir/pyangbind
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      x86_64

Requires: python >= 2.7
BuildRequires:  python-devel
BuildRequires:  python-setuptools

%description
PyangBind PyangBind is a plugin for pyang which converts YANG data models into
a Python class hierarchy, such that Python can be used to manipulate data that
conforms with a YANG model.This module provides the supporting classes and
functions that PyangBind modules utilise, particularly:*
pyangbind.base.PybindBase which is the parent class inherited by all container
or module YANG objects.*...

Summary:        %{summary}
%{?python_provide:%python_provide python-%{pypi_name}}

Requires:       python-pyang
Requires:       python-bitarray
Requires:       python-lxml
%description -n python-%{pypi_name}
PyangBind PyangBind is a plugin for pyang which converts YANG data models into
a Python class hierarchy, such that Python can be used to manipulate data that
conforms with a YANG model.This module provides the supporting classes and
functions that PyangBind modules utilise, particularly:*
pyangbind.base.PybindBase which is the parent class inherited by all container
or module YANG objects.*...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py_build

%install
python setup.py install -O1 --root=$RPM_BUILD_ROOT

%define _unpackaged_files_terminate_build 0

%files -n python-%{pypi_name}
%doc README.rst README.md
%{python_sitelib}/%{pypi_name}
%{python_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Thu Aug 03 2017 root - 0.2.0
- Release package - 0.2.0
