# sitelib for noarch packages, sitearch for others (remove the unneeded one)
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}

%global pkg     pyhash

Name:           python-pyhash
Version:        0.6.2
Release:        1%{?dist}
Summary:        Python Non-cryptographic Hash Library.

License:        Apache Software License.
URL:            https://github.com/flier/pyfasthash
Source0:        https://pypi.python.org/packages/source/p/%{pkg}/%{pkg}-0.6.2.tar.gz

BuildRequires:  python-devel boost-devel

%description
pyhash is a python non-cryptographic hash library, including FNV1,
MurmurHash1/2/3, lookup3, SuperFastHash, CityHash, SpookyHash etc

%prep
%setup -q -n %{pkg}-%{version}


%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README.md
%{python_sitearch}/*


%changelog
* Tue Oct 28 2014 Eugene Zamriy <eugene@zamriy.info> - 0.6.2-1
- Initial release: 0.6.2 version
