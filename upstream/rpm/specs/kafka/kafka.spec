
%define name		kafka 
%define version 	2.9.2
%define upstr_release 0.8.1.1
%define _relstr 0contrail0
%define _prefix /usr/share/kafka

#BuildRoot:	%{buildroot}
Summary: 		kafka package
License: 		GPL
Name: 			%{name}
Version: 		%{version}
Release: 		%{upstr_release}.%{_relstr}%{?dist}
Source: 		http://mirror.olnevhost.net/pub/apache/kafka/0.8.1.1/kafka_2.9.2-0.8.1.1.tgz
Prefix: 		/usr/share/kafka
Group: 			Development/Tools

%description
The GNU wget program downloads files from the Internet using the command-line.

%prep
%setup -q -n %{name}_%{version}-%{upstr_release}

%install
pushd %{_builddir}/kafka*/
find . -print | sed 's;^.;'"%{buildroot}/usr/share/kafka/"';'| xargs install -d -m 755
popd

%files
%defattr(-,contrail,contrail)
/usr/share/kafka/*
