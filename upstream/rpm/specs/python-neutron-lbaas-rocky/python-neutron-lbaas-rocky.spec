%global modulename neutron_lbaas
%global servicename neutron-lbaas
%global type LBaaS
%define upstream_version 13.0.0
%define release 1
%define _relstr 0contrail
%define rel_version rocky

Name:           python-%{servicename}-%{rel_version}
Version:        %{upstream_version}
Release:        1%{?dist}
Epoch:          1
Summary:        Openstack Networking %{type} plugin

License:        ASL 2.0
URL:            http://launchpad.net/neutron/
Source0:        https://tarballs.openstack.org/%{servicename}/%{servicename}-%{upstream_version}.tar.gz

BuildArch:      noarch
BuildRequires:  python-pbr
BuildRequires:  python-setuptools
BuildRequires:  git
BuildRequires:  unzip

%description -n python-%{servicename}-%{rel_version}
This is a %{type} service plugin for Openstack Neutron (Networking) service.

This package contains the Neutron %{type} Python library.

%prep
%autosetup -n %{servicename}-%{upstream_version} -S git

# Let's handle dependencies ourselves
rm -f requirements.txt

# Kill egg-info in order to generate new SOURCES.txt
rm -rf neutron_lbaas.egg-info

%build
export PBR_VERSION=%{version}
export SKIP_PIP_INSTALL=1
%{__python2} setup.py build

%install
export PBR_VERSION=%{version}
export SKIP_PIP_INSTALL=1
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}

%files
%license LICENSE
%doc AUTHORS CONTRIBUTING.rst README.rst
%{python2_sitelib}/%{modulename}
%{python2_sitelib}/%{modulename}-%{version}-py%{python2_version}.egg-info
%exclude %{python2_sitelib}/%{modulename}/tests
/usr/bin/*
/usr/etc/neutron/*
