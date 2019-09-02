%if 0%{?rhel} && 0%{?rhel} < 7
%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%global python2_version 2.6
%global with_python3 0
%global with_python2 1
%endif

%if 0%{?rhel} && 0%{?rhel} >= 7
%global with_python3 1
%global with_python2 1
%endif

%global commit bee0f3bcb8ba9e7bd131d64e3bf631f5bd06c5b4
%global date 20181019
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name: future
Summary: Easy, clean, reliable Python 2/3 compatibility
Version: 0.16.0
Release: 15.%{date}git%{shortcommit}%{?dist}
License: MIT
URL: http://python-future.org/
Source0: https://github.com/PythonCharmers/python-future/archive/%{commit}/python-%{name}-%{commit}.tar.gz
BuildArch: noarch


%package -n python2-%{name}
Summary: Easy, clean, reliable Python 2/3 compatibility
%{?python_provide:%python_provide python2-%{name}}
%if 0%{?rhel} && 0%{?rhel} <= 6
BuildRequires: python-argparse, python-unittest2, python-importlib 
Requires:      python-importlib
Requires:      python-argparse
%endif
BuildRequires: python2-devel
BuildRequires: python2-setuptools
BuildRequires: numpy
BuildRequires: python-requests
BuildRequires: python2-pytest
Provides:      future = 0:%{version}-%{release}
%description -n python2-%{name}
Python2 %{name} is the missing compatibility layer between Python 2 and
Python 3. It allows you to use a single, clean Python 3.x-compatible
codebase to support both Python 2 and Python 3 with minimal overhead.

It provides ``future`` and ``past`` packages with backports and forward
ports of features from Python 3 and 2. It also comes with ``futurize`` and
``pasteurize``, customized 2to3-based scripts that helps you to convert
either Py2 or Py3 code easily to support both Python 2 and 3 in a single
clean Py3-style codebase, module by module.
%endif

%prep
%setup -qc

pushd python-future-%{commit}
popd

%if 0%{?with_python2}
cp -a python-future-%{commit} python2
find python2 -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python2}|'
%endif

%build
%if 0%{?with_python2}
pushd python2
%py2_build
popd
%endif

%install

%if 0%{?with_python2}
pushd python2
%py2_install
cp -p $RPM_BUILD_ROOT%{_bindir}/futurize $RPM_BUILD_ROOT%{_bindir}/python%{python2_version}-futurize
cp -p $RPM_BUILD_ROOT%{_bindir}/pasteurize $RPM_BUILD_ROOT%{_bindir}/python%{python2_version}-pasteurize

for i in futurize futurize-2 futurize-%{python2_version}; do
  touch $i
  install -p $i $RPM_BUILD_ROOT%{_bindir}
  ln -sf %{_bindir}/python%{python2_version}-futurize $RPM_BUILD_ROOT%{_bindir}/$i
done
for i in pasteurize pasteurize-2 pasteurize-%{python2_version}; do
  touch $i
  install -p $i $RPM_BUILD_ROOT%{_bindir}
  ln -sf %{_bindir}/python%{python2_version}-pasteurize $RPM_BUILD_ROOT%{_bindir}/$i
done
sed -i -e '/^#!\//, 1d' $RPM_BUILD_ROOT%{python2_sitelib}/future/backports/test/pystone.py
popd
%endif

##This packages ships PEM certificates in future/backports/test directory
##It's for testing purpose, i guess. Ignore them.
%check
%if 0%{?with_python2}
pushd python2
PYTHONPATH=$PWD/build/lib py.test -v
popd
%endif

%if 0%{?with_python2}
%files -n python2-%{name}
%doc python2/README.rst
%license python2/LICENSE.txt
%{_bindir}/futurize
%{_bindir}/futurize-2*
%{_bindir}/pasteurize
%{_bindir}/pasteurize-2*
%{_bindir}/python%{python2_version}-futurize
%{_bindir}/python%{python2_version}-pasteurize
%{python2_sitelib}/future/
%{python2_sitelib}/past/
%{python2_sitelib}/libfuturize/
%{python2_sitelib}/libpasteurize/
%{python2_sitelib}/tkinter/
%{python2_sitelib}/_dummy_thread/
%{python2_sitelib}/_markupbase/
%{python2_sitelib}/_thread/
%{python2_sitelib}/builtins/
%{python2_sitelib}/copyreg/
%{python2_sitelib}/html/
%{python2_sitelib}/http/
%{python2_sitelib}/queue/
%{python2_sitelib}/reprlib/
%{python2_sitelib}/socketserver/
%{python2_sitelib}/winreg/
%{python2_sitelib}/xmlrpc/
%{python2_sitelib}/*.egg-info
%endif
