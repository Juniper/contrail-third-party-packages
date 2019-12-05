%define name xmltodict
%define version 0.7.0
%define unmangled_version 0.7.0
%define release 1
%define _relstr 0contrail
Summary: Makes working with XML feel like you are working with JSON
Name: %{name}
Version: %{version}
Release: %{release}.%{_relstr}
Source0: https://pypi.python.org/packages/source/x/xmltodict/xmltodict-0.7.0.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Martin Blech <martinblech@gmail.com>
Url: https://github.com/martinblech/xmltodict

%description
UNKNOWN

%prep
%setup -n %{name}-%{unmangled_version}

%build
python setup.py build

%install
python setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
