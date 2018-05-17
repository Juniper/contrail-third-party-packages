
%define name		kafka
%define version 	2.10
%define upstr_release 0.9.0.0
%define _relstr 0contrail0
%define _prefix /usr/share/kafka

#BuildRoot:	%{buildroot}
Summary: 		kafka package
License: 		GPL
Name: 			%{name}
Version: 		%{version}
Release: 		%{upstr_release}.%{_relstr}%{?dist}
Source:    https://archive.apache.org/dist/%{name}/%{upstr_release}/%{name}_%{version}-%{upstr_release}.tgz
Prefix: 		/usr/share/%{name}
Group: 			Development/Tools

%description
The GNU wget program downloads files from the Internet using the command-line.

%prep
%setup -q -n %{name}_%{version}-%{upstr_release}

%install
pushd %{_builddir}/kafka*/
for file in $(find . -type d); do
    install -d ${file} %{buildroot}/usr/share/%{name}/${file}
done
for file in $(find . -type f); do
    install -D ${file} %{buildroot}/usr/share/%{name}/${file}
done

popd

%files
%defattr(-,contrail,contrail)
/usr/share/kafka/*
