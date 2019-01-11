Name:           python-thrift
Version:        0.9.2
Release:        0
Summary:        Python bindings for the Apache Thrift RPC system
License:        Apache-2.0
Group:          Development/Languages/Python
Url:            https://thrift.apache.org
Source:         https://pypi.python.org/packages/source/t/thrift/thrift-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version} && 0%{?suse_version} <= 1110
%{!?python_sitearch: %global python_sitearch %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%endif

%description
Thrift Python Software Library

Thrift is provided as a set of Python packages. The top level package is
thrift, and there are subpackages for the protocol, transport, and server
code. Each package contains modules using standard Thrift naming conventions
(i.e. TProtocol, TTransport) and implementations in corresponding modules
(i.e. TSocket).  There is also a subpackage reflection, which contains
the generated code for the reflection structures.

%prep
%setup -q -n thrift-%{version}

%build
CFLAGS="%{optflags} -fno-strict-aliasing" python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}
%fdupes %{buildroot}%{python_sitearch}

%files
%defattr(-,root,root,-)
%{python_sitearch}/thrift-%{version}-py%{py_ver}.egg-info
%{python_sitearch}/thrift

%changelog