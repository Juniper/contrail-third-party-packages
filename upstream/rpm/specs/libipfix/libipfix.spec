# This is a sample spec file for wget

%define name    libipfix 
%define version   110209

Summary:     libipfix package
License:     LGPLv3+
Name:        %{name}
Version:     %{version}
Release:     %{release}%{?dist}
Source:      https://sourceforge.net/projects/libipfix/files/%{name}/%{name}_%{version}.tgz/download
Group:       Development/Tools

BuildRequires: gcc

%description
The GNU wget program downloads files from the Internet using the command-line.

%prep
%setup -q -n %{name}_%{version}

%build
./configure --prefix=%{buildroot}/usr
make

%install
make install --prefix=%{buildroot}/usr

%files
%defattr(-,root,root)
/usr/*

