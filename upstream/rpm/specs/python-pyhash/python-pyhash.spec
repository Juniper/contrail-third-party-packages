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

BuildRequires:  python-devel
BuildRequires:  boost-devel
BuildRequires:  python2-pip

%description
pyhash is a python non-cryptographic hash library, including FNV1,
MurmurHash1/2/3, lookup3, SuperFastHash, CityHash, SpookyHash etc

# added BuildRequires: python2-pip and manual setuptools-5.4.1 installation because
# when python-pyhash was being built it tried to install setuptools-5.4.1 and failed
# on downloading the zip archive due to redirects
%prep
%setup -q -n %{pkg}-%{version}
pip install https://files.pythonhosted.org/packages/98/9c/079cd02e1511fa0bc155af16a333aef6a33d9753e7cb2ba201f4cbd79b0c/setuptools-5.4.1.zip

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
