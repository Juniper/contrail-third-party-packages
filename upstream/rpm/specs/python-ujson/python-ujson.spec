%define name python-ujson
%define version 1.35
%define unmangled_version 1.35
%define release 1
%define _relstr 0contrail

Summary: Ultra fast JSON encoder and decoder for Python
Name: %{name}
Version: %{version}
Release: %{release}.%{_relstr}
Source0: https://pypi.python.org/packages/16/c4/79f3409bc710559015464e5f49b9879430d8f87498ecdc335899732e5377/ujson-1.35.tar.gz
License: BSD License
Group: Development/Libraries
Prefix: %{_prefix}
Vendor: Jonas Tarnstrom <jonas.tarnstrom@esn.me>
Url: http://github.com/esnme/ultrajson

BuildRequires: python-devel

%description
UltraJSON is an ultra fast JSON encoder and decoder written in pure C with
bindings for Python 2.5+ and 3.

For a more painless day to day C/C++ JSON decoder experience please checkout
ujson4c, based on UltraJSON.

Please checkout the rest of the projects in the Ultra series:
http://github.com/esnme/ultramemcache
http://github.com/esnme/ultramysql



%prep
%setup -n ujson-1.35

%build
env CFLAGS="$RPM_OPT_FLAGS" python setup.py build

%install
python setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
