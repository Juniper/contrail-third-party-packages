# Created by pyp2rpm-0.4.2
%global pypi_name jsonschema

%global with_python3 1

Name:           python-%{pypi_name}
Version:        2.5.1
Release:        3.contrail1%{?dist}
Summary:        An implementation of JSON Schema validation for Python

License:        MIT
URL:            http://pypi.python.org/pypi/jsonschema
Source0:        http://pypi.python.org/packages/source/j/jsonschema/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%if %{?rhel}%{!?rhel:0} == 6
BuildRequires:  python-unittest2
BuildRequires:  python-argparse
%endif
BuildRequires:  python2-devel
BuildRequires:  python-nose
BuildRequires:  python-mock
# Avoid unpackaged deps:
#BuildRequires:  python-vcversioner
#BuildRequires:  python-functools32
# Alternative for functools32.lru_cache
BuildRequires:  python-repoze-lru
%if 0%{?with_python3}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-nose
BuildRequires:  python%{python3_pkgversion}-mock
%endif

# avoid functools32, vcversioner
Patch0: avoid-unpackaged.patch

%description
jsonschema is JSON Schema validator currently based on
http://tools.ietf.org/html/draft-zyp-json-schema-03

%package -n python2-%{pypi_name}
Summary:        An implementation of JSON Schema validation for Python 2
#Requires: python-functools32
Requires: python-repoze-lru
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
jsonschema is JSON Schema validator currently based on
http://tools.ietf.org/html/draft-zyp-json-schema-03

%if 0%{?with_python3}
%package -n python%{python3_pkgversion}-%{pypi_name}
Summary:        An implementation of JSON Schema validation for Python %{python3_version}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
jsonschema is JSON Schema validator currently based on
http://tools.ietf.org/html/draft-zyp-json-schema-03
%endif

%prep
%setup -q -n %{pypi_name}-%{version}
%patch0 -p1

%build
%if 0%{?with_python3}
%py3_build
%endif
%py2_build


%install
%if 0%{?with_python3}
%py3_install
%endif
%py2_install

%check
%if 0%{?with_python3}
%{_bindir}/nosetests-%{python3_version} -v
%endif
%{_bindir}/nosetests-%{python2_version} -v

%files -n python2-%{pypi_name}
%license COPYING
%doc README.rst
%{_bindir}/jsonschema
%{python2_sitelib}/%{pypi_name}/
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%if 0%{?with_python3}
%files -n python%{python3_pkgversion}-%{pypi_name}
%license COPYING
%doc README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%endif


%changelog
* Thu Apr 12 2018 Krzysztof Klimonda <krzysztof.klimonda@codilime.com> - 2.5.1-3.contrail1
- Release package for Contrail

* Mon Nov 21 2016 Orion Poplawski <orion@cora.nwra.com> - 2.5.1-3
- Enable python3 builds for EPEL (bug #1395653)
- Ship python2-jsonschema
- Modernize spec
- Use %%license

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Feb 26 2016 Lon Hohberger <lhh@redhat.com> 2.5.1-1
- Update to 2.5.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild


* Tue Oct 13 2015 Robert Kuska <rkuska@redhat.com> - 2.4.0-3
- Rebuilt for Python3.5 rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Sep 06 2014 Alan Pevec <apevec@redhat.com> - 2.4.0-1
- Latest upstream

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon Mar 10 2014 Pádraig Brady <pbrady@redhat.com> - 2.3.0-1
- Latest upstream

* Tue Feb 04 2014 Matthias Runge <mrunge@redhat.com> - 2.0.0-3
- fix %%{? issues in spec

* Thu Oct 17 2013 Thomas Spura <tomspur@fedoraproject.org> - 2.0.0-2
- add python3 subpackage (#1016207)
- add %%check

* Fri Aug 16 2013 Alan Pevec <apevec@redhat.com> 2.0.0-1
- Update to 2.0.0 release

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 13 2013 Pádraig Brady <P@draigBrady.com> - 1.3.0-1
- Update to 1.3.0 release

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May 23 2012 Pádraig Brady <P@draigBrady.com> - 0.2-1
- Initial package.
