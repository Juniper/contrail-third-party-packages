%define __jar_repack 0
%define _prefix /opt
%define debug_package %{nil}
%define src_name kafka
%define version 0.9.0.1
%define scala_version 2.11
%define build_number 1
%define tarball_name %{src_name}_%{scala_version}-%{version}
%define tarball %{tarball_name}.tgz
%define release 0contrail0


Summary: Apache Kafka is publish-subscribe messaging rethought as a distributed commit log.
Name: %{src_name}
Version: %{version}
Release: %{build_number}%{?dist}
License: Apache License, Version 2.0
Group: Applications
Source0: http://archive.apache.org/dist/kafka/%{version}/%{tarball}
URL: http://kafka.apache.org/
BuildRoot: %{_tmppath}/%{src_name}-%{version}-%{release}-buildroot
Prefix: /opt
Vendor: Apache Software Foundation
Provides: kafka

%description
Kafka is designed to allow a single cluster to serve as the central data backbone for a large organization. It can be elastically and transparently expanded without downtime. Data streams are partitioned and spread over a cluster of machines to allow data streams larger than the capability of any single machine and to allow clusters of co-ordinated consumers. Messages are persisted on disk and replicated within the cluster to prevent data loss.

%prep
%setup -n %{tarball_name}

%build
rm -f libs/{kafka_*-javadoc.jar,kafka_*-scaladoc.jar,kafka_*-sources.jar,*.asc}
rm config/zookeeper.properties

%install
mkdir -p $RPM_BUILD_ROOT%{_prefix}/kafka
mkdir $RPM_BUILD_ROOT%{_prefix}/kafka/bin
cp bin/kafka-*.sh $RPM_BUILD_ROOT%{_prefix}/kafka/bin/
cp -r libs $RPM_BUILD_ROOT%{_prefix}/kafka/
cp -r config $RPM_BUILD_ROOT%{_prefix}/kafka/
mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d
mkdir -p $RPM_BUILD_ROOT/var/log/kafka

%clean
rm -rf $RPM_BUILD_ROOT

%pre
/usr/bin/getent group kafka >/dev/null || /usr/sbin/groupadd -r kafka
if ! /usr/bin/getent passwd kafka >/dev/null ; then
    /usr/sbin/useradd -r -g kafka -m -d %{_prefix}/kafka -s /bin/bash -c "Kafka" kafka
fi

%post
if [ $1 = 1 ]; then
    /sbin/chkconfig --add kafka
fi

%preun
# When the last version of a package is erased, $1 is 0
if [ $1 = 0 ]; then
    /sbin/service kafka stop >/dev/null
    /sbin/chkconfig --del kafka
fi

%postun
# When the last version of a package is erased, $1 is 0
# Otherwise it's an upgrade and we need to restart the service
if [ $1 -ge 1 ]; then
    /sbin/service kafka stop >/dev/null 2>&1
    sleep 1
    /sbin/service kafka start >/dev/null 2>&1
fi

%files
%defattr(-,root,root)
%attr(0755,kafka,kafka) %dir /opt/kafka
%attr(0755,kafka,kafka) /opt/kafka/bin
%attr(0755,kafka,kafka) /opt/kafka/libs
%config(noreplace) %attr(755,kafka,kafka) /opt/kafka/config
%attr(0755,kafka,kafka) %dir /var/log/kafka

%doc NOTICE
%doc LICENSE

%changelog
* Mon Mar 11 2019 Michal Czuba (michal.czuba@codilime.com) - 1
- Initial release: 1 version
- removed custom init script and packager info
- changed Kafka sources URL
- added some define variables e.g. Kafka version
* Fri Mar 08 2019 Michal Czuba (michal.czuba@codilime.com)
- Initially forked from https://github.com/id/kafka-rpm (Ivan Dyachkov <ivan.dyachkov@klarna.com>)
