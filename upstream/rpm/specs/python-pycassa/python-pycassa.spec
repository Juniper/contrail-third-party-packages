%define         _relstr      0contrail
Name: python-pycassa
Summary: python-pycassa
Version: 1.10.0
Release: %{_relstr}%{?dist}
License: MIT
Group: Applications/System
URL: https://github.com/pycassa/pycassa
Source: https://pypi.python.org/packages/source/p/pycassa/pycassa-1.10.0.tar.gz
Patch0: ez_setup.py.patch

BuildArch: noarch

Requires: python-thrift
Requires: python-setuptools

#Requires:           contrail-analytics-venv
#Requires:           contrail-api-venv
%define             _venv_root    /opt/contrail/api-venv
%define             _venvtr       --prefix=%{_venv_root}
%define             _anl_venv_root    /opt/contrail/analytics-venv
%define             _anl_venvtr       --prefix=%{_anl_venv_root}

%define _pyver        %( %{__python} -c "import sys; print '%s.%s' % sys.version_info[0:2]" )
%define _pysitepkg    /lib/python%{_pyver}/site-packages
%description
spec file for pycassa package

%prep

%setup -n pycassa-1.10.0
%patch0 -p0

%build
env CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
install -d -m 755 %{buildroot}%{_bindir}
install -m 755 pycassaShell %{buildroot}%{_bindir}
%{__python} setup.py install -O1 --root=$RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{python_sitelib}/pycassa
%{python_sitelib}/ez_setup.py*
%{python_sitelib}/pycassa*egg-info
%{_bindir}/pycassaShell
%{python_sitelib}/pycassa
%{python_sitelib}/ez_setup.py*
%{python_sitelib}/pycassa*egg-info
/usr/bin/pycassaShell

%post

%changelog
* Mon Dec 17 2012 Pedro Marques <roque@build01> - config-1
- Initial build.
