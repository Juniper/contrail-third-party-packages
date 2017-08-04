# Created by pyp2rpm-3.2.2
# Modified by Sanju <sanjua@juniper.net>
%global pypi_name pyang

Name:           python-%{pypi_name}
Version:        1.7.3
Release:        1%{?dist}
Summary:        A YANG (RFC 6020) validator and converter

License:        BSD
URL:            https://github.com/mbj4668/pyang
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      x86_64

Requires: python >= 2.7
BuildRequires:  python-devel
BuildRequires:  python-setuptools

%description
An extensible YANG (RFC 6020) validator. Provides a framwork for plugins that
can convert YANG modules to other formats.

Summary:        %{summary}
%{?python_provide:%python_provide python-%{pypi_name}}

%description -n python-%{pypi_name}
An extensible YANG (RFC 6020) validator. Provides a framwork for plugins that
can convert YANG modules to other formats.

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
%doc
%{_bindir}/yang2html
%{_bindir}/pyang
%{_bindir}/json2xml
%{_bindir}/yang2dsdl
%{python_sitelib}/%{pypi_name}
%{python_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Thu Aug 02 2017 root - 1.7.3
- Release package - 1.7.3
