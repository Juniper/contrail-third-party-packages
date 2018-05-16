%define name python-jsonpickle
%define version 0.9.2
%define release 1
%define _relstr 0contrail

Summary: Python library for serializing any arbitrary object graph into JSON
Name:%{name}
Version: %{version}
Release: %{release}.%{_relstr}
Source0: https://pypi.python.org/packages/source/j/jsonpickle/jsonpickle-0.9.2.tar.gz
License: BSD License
Group: Development/Libraries
Prefix: %{_prefix}
Url: http://jsonpickle.github.io/

Provides: jsonpickle

%description
jsonpickle converts complex Python objects to and from JSON.

%prep
%setup -n jsonpickle-%{version}

%build
env CFLAGS="$RPM_OPT_FLAGS" python setup.py build

%install
python setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
