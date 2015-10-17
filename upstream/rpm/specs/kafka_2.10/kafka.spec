
%define name		kafka 
%define version 	2.10
%define upstr_release 0.9.0.0_SNAPSHOT 
%define _relstr 0contrail0
%define _prefix /usr/share/kafka

#BuildRoot:	%{buildroot}
Summary: 		kafka package
License: 		GPL
Name: 			%{name}
Version: 		%{version}
Release: 		%{upstr_release}.%{_relstr}%{?dist}
Source: 		https://github.com/Juniper/contrail-third-party-cache/blob/master/kafka/kafka_2.10-0.9.0.0-SNAPSHOT.tgz		
Prefix: 		/usr/share/kafka
Group: 			Development/Tools

%description
The GNU wget program downloads files from the Internet using the command-line.

%prep
%setup -q -n %{name}_%{version}-0.9.0.0-SNAPSHOT

%install
pushd %{_builddir}/kafka*/
for file in $(find . -type d); do
    install -d ${file} %{buildroot}/usr/share/kafka/${file}
done
for file in $(find . -type f); do
    install -D ${file} %{buildroot}/usr/share/kafka/${file}
done

popd

%files
%defattr(-,contrail,contrail)
/usr/share/kafka/*
