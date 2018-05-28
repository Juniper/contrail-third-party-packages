# This is a sample spec file for wget

%define name		libipfix 
#%define release		1
%define version 	110209

#BuildRoot:	%{buildroot}
Summary: 		libipfix package
License: 		LGPLv3+
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}%{?dist}
Source: 		https://sourceforge.net/projects/libipfix/files/%{name}/%{name}_%{version}.tgz/download
#Prefix: 		/usr
Group: 			Development/Tools

BuildRequires: gcc

%description
The GNU wget program downloads files from the Internet using the command-line.

%prep
%setup -q -n %{name}_%{version}

%build
./configure prefix=$RPM_BUILD_ROOT/usr
make

%install
make install prefix=$RPM_BUILD_ROOT/usr

%files
%defattr(-,root,root)
/usr/*

