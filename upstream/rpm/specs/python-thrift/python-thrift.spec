%define name thrift
%define version 0.9.1
%define unmangled_version 0.9.1
%define unmangled_version 0.9.1
%define release 1
%define _relstr 0contrail
Summary: Python bindings for the Apache Thrift RPC system
Name: python-%{name}
Version: %{version}
Release: %{release}.%{_relstr}
Source0: https://pypi.python.org/packages/source/t/thrift/thrift-0.9.1.tar.gz
License: Apache License 2.0
Group: Development/Libraries
Prefix: %{_prefix}
Vendor: ['Thrift Developers'] <['dev@thrift.apache.org']>
Url: http://thrift.apache.org

%description
UNKNOWN

%prep
%setup -n thrift-0.9.1


%build
env CFLAGS="$RPM_OPT_FLAGS" python setup.py build

%install
python setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
