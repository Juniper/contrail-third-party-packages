%global srcname kazoo

Name:           python-%{srcname}
Version:        2.5.0
Release:        1%{?dist}
Summary:        Higher Level Zookeeper Client
License:        Apache 2.0
URL:            https://pypi.python.org/pypi/kazoo
Source0:        https://pypi.python.org/packages/source/k/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

Requires:       python-eventlet >= 0.17.1
# 2.5.0 wants (but not requires) gevent>=1.2 but only 1.1.2 only available for build. for 2.4.0 it's >=1.1
# TODO: if gevent is critical than kazoo version should be down in contrail-thirdparty to 2.4.0
#Requires:       gevent >= 1.2

%description
Higher Level Zookeeper Client


%package -n python2-%{srcname}
Summary:        %{summary}
BuildRequires:  python2-devel
BuildRequires:  python%{?fedora:2}-setuptools
%{?python_provide:%python_provide python2-%{srcname}}


%description -n python2-%{srcname}
Higher Level Zookeeper Client


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}


%description -n python%{python3_pkgversion}-%{srcname}
Higher Level Zookeeper Client


%prep
%setup -q -n %{name}-%{version}


%build
%py2_build
%py3_build


%install
%py2_install
%py3_install


%files -n python2-%{srcname}
%license LICENSE
%doc README.md
%{python2_sitelib}/*


%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/*

