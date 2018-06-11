Name:           userspace-rcu
Version:        0.10.0
Release:        1%{?dist}
Summary:        RCU (read-copy-update) implementation in user space

Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://liburcu.org/
Source0:        http://lttng.org/files/urcu/%{name}-%{version}.tar.bz2
BuildRequires:  autoconf automake libtool
BuildRequires:  pkgconfig
Obsoletes:      liburcu
Provides:       liburcu

%description
This data synchronization library provides read-side access which scales
linearly with the number of cores. It does so by allowing multiples copies
of a given data structure to live at the same time, and by monitoring
the data structure accesses to detect grace periods after which memory
reclamation is possible.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      liburcu-devel
Provides:       liburcu-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
%configure

make %{?_smp_mflags} V=1


%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -vf $RPM_BUILD_ROOT%{_libdir}/*.la


%check
make check
#make regtest

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%doc ChangeLog gpl-2.0.txt lgpl-relicensing.txt lgpl-2.1.txt
%{_docdir}/%{name}/README.md
%{_docdir}/%{name}/LICENSE
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/pkgconfig/liburcu*.pc
%{_docdir}/%{name}/README.md
%{_docdir}/%{name}/*.md
%{_docdir}/%{name}/examples/*


%changelog
* Thu Aug 03 2017 Michael Jeanson <mjeanson@efficios.com> - 0.10.0-1
- Updated to 0.10.0

* Tue Jun 20 2017 Michael Jeanson <mjeanson@efficios.com> - 0.9.4-1
- Updated to 0.9.4

* Wed Dec 07 2016 Michael Jeanson <mjeanson@efficios.com> - 0.9.3-1
- Updated to 0.9.3

* Wed Jun 08 2016 Michael Jeanson <mjeanson@efficios.com> - 0.9.2-1
- Updated to 0.9.2

* Tue Nov 10 2015 Michael Jeanson <mjeanson@efficios.com> - 0.9.1-1
- Sync packaging code with Fedora
- Updated to 0.9.1
