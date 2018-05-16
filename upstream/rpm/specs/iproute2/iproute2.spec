##%define date_version 20091009
%define cbq_version v0.7.3
%define up_version 3.1.0

Summary: Advanced IP routing and network device configuration tools
Name: iproute
Version: 3.1.0
Release: contrail%{?dist}
Group: Applications/System
Source: https://www.kernel.org/pub/linux/utils/net/iproute2/iproute2-3.1.0.tar.gz
URL:    http://linux-net.osdl.org/index.php/Iproute2

License: GPLv2+ and Public Domain
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: tex(latex) tex(dvips) linuxdoc-tools
BuildRequires: flex psutils db4-devel bison
# introduction new iptables (xtables) which broke ipt
BuildRequires: iptables >= 1.4.5
BuildRequires: iptables-devel >= 1.4.5
Requires:      iptables >= 1.4.5

%description
The iproute package contains networking utilities (ip and rtmon, for
example) which are designed to use the advanced networking
capabilities of the Linux 2.4.x and 2.6.x kernel.

%package devel
Summary: iproute development files
Group: Development/Libraries
License: GPLv2+
Provides: iproute-static = %{version}-%{release}

%description devel
The libnetlink static library.

%package doc
Summary: ip and tc documentation with examples
Group:  Applications/System
License: GPLv2+

%description doc
The iproute documentation contains howtos and examples of settings.

%prep
%setup -q -n iproute2-%{up_version}
sed -i "s/_VERSION_/%{version}/" man/man8/ss.8
# rhbz#974694
sed -i 's/iproute-doc/%{name}-%{version}/' man/man8/lnstat.8

%build
export LIBDIR=/%{_libdir}
export IPT_LIB_DIR=/%{_lib}/xtables
./configure
make %{?_smp_mflags}
make -C doc

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/sbin \
     $RPM_BUILD_ROOT%{_sbindir} \
     $RPM_BUILD_ROOT%{_includedir} \
     $RPM_BUILD_ROOT%{_mandir}/man3 \
     $RPM_BUILD_ROOT%{_mandir}/man8 \
     $RPM_BUILD_ROOT/%{_sysconfdir}/iproute2 \
     $RPM_BUILD_ROOT%{_datadir}/tc \
     $RPM_BUILD_ROOT%{_libdir}/tc

install -m 755 ip/ip ip/ifcfg ip/rtmon tc/tc  $RPM_BUILD_ROOT/sbin
install -m 755 misc/ss misc/nstat misc/rtacct misc/lnstat misc/arpd $RPM_BUILD_ROOT%{_sbindir}
# linux-atm not available in RHEL
#install -m 755 tc/q_atm.so $RPM_BUILD_ROOT%{_libdir}/tc
install -m 755 tc/m_xt.so $RPM_BUILD_ROOT%{_libdir}/tc
install -m 644 netem/normal.dist netem/pareto.dist netem/paretonormal.dist $RPM_BUILD_ROOT%{_datadir}/tc
install -m 644 man/man8/*.8 $RPM_BUILD_ROOT/%{_mandir}/man8
rm -r $RPM_BUILD_ROOT/%{_mandir}/man8/ss.8
iconv -f latin1 -t utf8 < man/man8/ss.8 > $RPM_BUILD_ROOT/%{_mandir}/man8/ss.8
install -m 644 man/man3/*.3 $RPM_BUILD_ROOT/%{_mandir}/man3
install -m 755 examples/cbq.init-%{cbq_version} $RPM_BUILD_ROOT/sbin/cbq
install -d -m 755 $RPM_BUILD_ROOT/%{_sysconfdir}/sysconfig/cbq

# libnetlink
install -m644 include/libnetlink.h %{buildroot}%{_includedir}
install -m644 lib/libnetlink.a %{buildroot}%{_libdir}

cp -f etc/iproute2/* $RPM_BUILD_ROOT/%{_sysconfdir}/iproute2
rm -rf $RPM_BUILD_ROOT/%{_libdir}/debug/*

#create example avpkt file
cat <<EOF > $RPM_BUILD_ROOT/%{_sysconfdir}/sysconfig/cbq/cbq-0000.example
DEVICE=eth0,10Mbit,1Mbit
RATE=128Kbit
WEIGHT=10Kbit
PRIO=5
RULE=192.168.1.0/24
EOF

cat <<EOF > $RPM_BUILD_ROOT/%{_sysconfdir}/sysconfig/cbq/avpkt
AVPKT=3000
EOF

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%dir %{_sysconfdir}/iproute2
%doc README README.decnet README.iproute2+tc README.distribution README.lnstat COPYING
/sbin/*
%{_mandir}/man8/*
%attr(644,root,root) %config(noreplace) %{_sysconfdir}/iproute2/*
%{_sbindir}/*
%dir %{_datadir}/tc
%{_datadir}/tc/*
%dir %{_libdir}/tc
%{_libdir}/tc/*
%dir %{_sysconfdir}/sysconfig/cbq
%config(noreplace) %{_sysconfdir}/sysconfig/cbq/*

%files devel
%doc COPYING
%{_mandir}/man3/*
%{_libdir}/libnetlink.a
%{_includedir}/libnetlink.h

%files doc
%defattr(-,root,root,-)
%doc doc/*.ps
%doc examples
%doc RELNOTES

%changelog
* Mon Jan 05 2015 Anirban Chakraborty <abchak@juniper.net> - 3.1.0
- Build iproute2 package wth netns support for Centos 6.x

* Tue May 13 2014 Petr Šabata <contyk@redhat.com> - 2.6.32-32
- Fix a floating point exception regression introduced with the
  incorrect fix of #859145 (#1045200)

* Tue Oct 08 2013 Petr Šabata <contyk@redhat.com> - 2.6.32-31
- Removed the unsporrted features from the bridge(8) manpage and
  document bridge fdb replace (#929313)

* Tue Sep 24 2013 Petr Pisar <ppisar@redhat.com> - 2.6.32-30
- Recognize ip monitor neigh-miss event (#1011148)

* Mon Sep 23 2013 Petr Pisar <ppisar@redhat.com> - 2.6.32-29
- Document tc -OK option (#851371)
- Document "bridge mdb" and "bridge monitor mdb" (#885977)
- Document bridge unsupported features (#929313)

* Fri Sep 13 2013 Petr Šabata <contyk@redhat.com> - 2.6.32-28
- Correct the rto_min patch (#859145)
- Fix the libnetlink regression (#1002677)

* Thu Aug 29 2013 Petr Šabata <contyk@redhat.com> - 2.6.32-27
- Fix #977845 properly

* Mon Aug 26 2013 Petr Šabata <contyk@redhat.com> - 2.6.32-26
- Add the bridge(8) manual page

* Tue Aug 20 2013 Petr Šabata <contyk@redhat.com> - 2.6.32-25
- Backport the current bridge command completely (#929313, #908155, #885977)

* Wed Aug 14 2013 Petr Šabata <contyk@redhat.com> - 2.6.32-24
- Don't hang on rtnl_send() in a confined domain (#985526)
- Run lnstat indefinitely if -c was not specified (#977845)
- lnstat manpage SEE ALSO path fixes (#974694)
- Document tc's force and batch options (#950122)
- Fix include/linux/if_link.h to get in line with upstream again (#903228)
- Add support for the IPv6 tokenized interface (#950400)
- Handle ip-route rto_min parameters correctly (#859145)
- Add VXLAN support (#929313, #908155)
- Add mdb subcommand to bridge (#885977)
- tc now supports the -OK option (#851371)

* Wed Oct 17 2012 Petr Šabata <contyk@redhat.com> - 2.6.32-23
- Include support for initrwnd (#867286)

* Mon Oct 15 2012 Petr Šabata <contyk@redhat.com> - 2.6.32-22
- Add nl attribute to filter dump requests (#864167),
  thanks to Andy Gospodarek

* Tue Aug 28 2012 Petr Šabata <contyk@redhat.com> - 2.6.32-21
- Package the libnetlink static library (#821106)
- Display UDP sockets with 'ss -l[u|a]' (#811219)

* Mon Apr 16 2012 Petr Šabata <contyk@redhat.com> - 2.6.32-20
- Add support for multicast rules, IPv4 only due to kernel limitations;
  see #631984, comment 14 for details (#812779)

* Wed Feb 15 2012 Petr Šabata <contyk@redhat.com> - 2.6.32-19
- Adding mqprio qdisc support (#748767)
- Adding QFQ discipline support (#788120)
- A required update of include/linux/pkt_sched.h

* Wed Jan 04 2012 Petr Šabata <contyk@redhat.com> - 2.6.32-18
- Fix changing of ip6ip6 tunnel hoplimit
- Resolves: rhbz#730627
- lnstat -d should dump to stdout
- Resolves: rhbz#736106

* Thu Aug 11 2011 Petr Sabata <contyk@redhat.com> - 2.6.32-17
- Fix GRED options clearing
- Resolves: rhbz#709652
- Add macvlan/macvtap passtru support
- Resolves: rhbz#692867
- Resolves: rhbz#693878

* Tue Feb 22 2011 Petr Sabata <psabata@redhat.com> - 2.6.32-16
- Link and install m_xt.so properly
- Related: rhbz#670295
- Related: rhbz#636943 
- Related: rhbz#641918 
- Related: rhbz#678986
- Related: rhbz#678986

* Tue Feb 22 2011 Petr Sabata <psabata@redhat.com> - 2.6.32-15
- secondary-flush.patch
- Resolves: rhbz#678986

* Tue Feb 22 2011 Petr Sabata <psabata@redhat.com> - 2.6.32-14
- Fix'd to properly build against xtables interface
- Related: rhbz#670295
- Related: rhbz#636943 
- Related: rhbz#641918 
- Related: rhbz#678986

* Fri Feb  4 2011 Petr Sabata <psabata@redhat.com> - 2.6.32-13
- Do not segfault when creating veth with peer option without any name provided
- link_veth_segv.patch
- Resolves: rhbz#636943

* Thu Feb  3 2011 Petr Sabata <psabata@redhat.com> - 2.6.32-12
- ip xfrm security context patches
- Resolves: rhbz#670295

* Wed Jan 26 2011 Petr Sabata <psabata@redhat.com> - 2.6.32-11
- man-pages.patch update
- Resolves: rhbz#641918

* Thu Jul 22 2010 Petr Sabata <psabata@redhat.com> - 2.6.32-10
- tc IPv6 priority patch
- Resolves: rhbz#586112

* Mon Jun 28 2010 Petr Sabata <psabata@redhat.com> - 2.6.32-9
- SR-IOV patch update to include manpage changes
- Resolves: rhbz#606680

* Thu Jun 24 2010 Petr Sabata <psabata@redhat.com> - 2.6.32-8
- Add support for setting and showing SR-IOV virtual function link params
- Patch from Petr Lautrbach
- Resolves: rhbz#606680

* Thu Jun 17 2010 Marcela Mašláňová <mmaslano@redhat.com> - 2.6.32-7
- fix cbq man page, which linked non-existing page
- Related: rhbz#592201

* Wed Jun 16 2010 Marcela Mašláňová <mmaslano@redhat.com> - 2.6.32-6
- apply patch from Petr Lautrbach to fix rpmdiff issues -> merge all 
  Makefile patches into one iproute-Makefile-RHEL-setting.patch
- fix man page by plautrba
- fix typo in lnstat by plautrba
- add missing options for ss by plautrba
- fix usage and man of arpd by plautrba
- Resolves: rhbz#596172, rhbz#592201, rhbz#592230, rhbz#592226, rhbz#592266

* Mon Apr 12 2010 Marcela Mašláňová <mmaslano@redhat.com> - 2.6.32-5
- change BR to tex(*) according to guidelines, remove commented parts
- Related: rhbz#543948

* Tue Mar 30 2010 Marcela Mašláňová <mmaslano@redhat.com> - 2.6.32-4
- fix testsuite to be executable at least locally under root
- Related: rhbz#543948

* Mon Mar  1 2010 Marcela Mašláňová <mmaslano@redhat.com> - 2.6.32-3
- remove BR on linux-atm because we want drop it from RHEL-6
- Related: bz#566364

* Tue Jan 26 2010 Marcela Mašláňová <mmaslano@redhat.com> - 2.6.32-2
- add macvlan aka VESA support d63a9b2b1e4e3eab0d0577d0a0f412d50be1e0a7
- kernel headers 2.6.33 ab322673298bd0b8927cdd9d11f3d36af5941b93
  are needed for macvlan features and probably for other added later.
- fix number of release which contains 2.6.32 kernel headers and features
  but it was released as 2.6.31
- Resolves: rhbz#553344

* Mon Jan  4 2010 Marcela Mašláňová <mmaslano@redhat.com> - 2.6.31-1
- update to 2.6.31
- 539232 patch cbq initscript
- Related: rhbz#552238

* Mon Oct 12 2009 Marcela Mašláňová <mmaslano@redhat.com> - 2.6.29-5.0.20091009gitdaf49fd6
ersion isn't available but it's needed -> switch to git snapshots

* Thu Sep 24 2009 Marcela Mašláňová <mmaslano@redhat.com> - 2.6.29-5
- create missing man pages

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.29-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Apr 23 2009 Marcela Mašláňová <mmaslano@redhat.com> - 2.6.29-3
- new iptables (xtables) bring problems to tc, when ipt is used. 
  rhbz#497344 still broken. tc_modules.patch brings correct paths to
  xtables, but that doesn't fix whole issue.
- 497355 ip should allow creation of an IPsec SA with 'proto any' 
  and specified sport and dport as selectors

* Tue Apr 14 2009 Marcela Mašláňová <mmaslano@redhat.com> - 2.6.29-2
- c3651bf4763d7247e3edd4e20526a85de459041b ip6tunnel: Fix no default 
 display of ip4ip6 tunnels
- e48f73d6a5e90d2f883e15ccedf4f53d26bb6e74 missing arpd directory

* Wed Mar 25 2009 Marcela Mašláňová <mmaslano@redhat.com> - 2.6.29-1
- update to 2.6.29
- remove DDR patch which became part of sourc
- add patch with correct headers 1957a322c9932e1a1d2ca1fd37ce4b335ceb7113

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb  4 2009 Marcela Mašláňová <mmaslano@redhat.com> - 2.6.28-2
- 483484 install distribution files into /usr/share and also fixed
 install paths in spec
- add the latest change from git which add DRR support
 c86f34942a0ce9f8203c0c38f9fe9604f96be706

* Mon Jan 19 2009 Marcela Mašláňová <mmaslano@redhat.com> - 2.6.28-1
- previous two patches were included into 2.6.28 release.
- update

* Mon Jan 12 2009 Marcela Mašláňová <mmaslano@redhat.com> - 2.6.27-2
- 475130 - Negative preferred lifetimes of IPv6 prefixes/addresses
  displayed incorrectly
- 472878 - “ip maddr show” in IB interface causes a stack corruption
- both patches will be probably in iproute v2.6.28

* Thu Dec 4 2008 Marcela Maslanova <mmaslano@redhat.com> - 2.6.27-1
- aead support was included into upstream version
- patch for moving libs is now deprecated
- update to 2.6.27

* Tue Aug 12 2008 Marcela Maslanova <mmaslano@redhat.com> - 2.6.26-1
- update to 2.6.26
- clean patches

* Tue Jul 22 2008 Marcela Maslanova <mmaslano@redhat.com> - 2.6.25-5
- fix iproute2-2.6.25-segfault.patch

* Thu Jul 10 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.6.25-4
- rebuild for new db4-4.7

* Thu Jul  3 2008 Marcela Maslanova <mmaslano@redhat.com> - 2.6.25-3
- 449933 instead of failing strncpy use copying byte after byte

* Wed May 14 2008 Marcela Maslanova <mmaslano@redhat.com> - 2.6.25-2
- allow replay setting, solve also 444724

* Mon Apr 21 2008 Marcela Maslanova <mmaslano@redhat.com> - 2.6.25-1
- update
- remove patch for backward compatibility
- add patch for AEAD compatibility

* Thu Feb 21 2008 Marcela Maslanova <mmaslano@redhat.com> - 2.6.23-4
- add creating ps file again. Fix was done in texlive

* Wed Feb  6 2008 Marcela Maslanova <mmaslano@redhat.com> - 2.6.23-3
- rebuild without tetex files. It isn't working in rawhide yet. Added
	new source for ps files. 
- #431179 backward compatibility for previous iproute versions

* Mon Jan 21 2008 Marcela Maslanova <mmaslano@redhat.com> - 2.6.23-2
- rebuild with fix tetex and linuxdoc-tools -> manual pdf
- clean unnecessary patches
- add into spec *.so objects, new BR linux-atm-libs-devel

* Wed Oct 31 2007 Marcela Maslanova <mmaslano@redhat.com> - 2.6.23-1
- new version from upstrem 2.3.23

* Tue Oct 23 2007 Marcela Maslanova <mmaslano@redhat.com> - 2.6.22-5
- move files from /usr/lib/tc to /usr/share/tc
- remove listing files twice

* Thu Aug 30 2007 Marcela Maslanova <mmaslano@redhat.com> - 2.6.22-3
- package review #225903

* Mon Aug 27 2007 Jeremy Katz <katzj@redhat.com> - 2.6.22-2
- rebuild for new db4

* Wed Jul 11 2007 Radek Vokál <rvokal@redhat.com> - 2.6.22-1
- upgrade to 2.6.22

* Mon Mar 19 2007 Radek Vokál <rvokal@redhat.com> - 2.6.20-2
- fix broken tc-pfifo man page (#232891)

* Thu Mar 15 2007 Radek Vokál <rvokal@redhat.com> - 2.6.20-1
- upgrade to 2.6.20

* Fri Dec 15 2006 Radek Vokál <rvokal@redhat.com> - 2.6.19-1
- upgrade to 2.6.19

* Mon Dec 11 2006 Radek Vokál <rvokal@redhat.com> - 2.6.18-5
- fix snapshot version

* Fri Dec  1 2006 Radek Vokál <rvokal@redhat.com> - 2.6.18-4
- spec file cleanup
- one more rebuilt against db4

* Thu Nov 16 2006 Radek Vokál <rvokal@redhat.com> - 2.6.18-3
- fix defective manpage for tc-pfifo (#215399)

* Mon Nov 13 2006 Radek Vokál <rvokal@redhat.com> - 2.6.18-2
- rebuilt against new db4

* Tue Oct  3 2006 Radek Vokal <rvokal@redhat.com> - 2.6.18-1
- upgrade to upstream 2.6.18
- initcwnd patch merged
- bug fix for xfrm monitor
- alignment fixes for cris
- documentation corrections
        
* Mon Oct  2 2006 Radek Vokal <rvokal@redhat.com> - 2.6.16-7
- fix ip.8 man page, add initcwnd option

* Sun Oct 01 2006 Jesse Keating <jkeating@redhat.com> - 2.6.16-6
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Tue Sep 19 2006 Radek Vokal <rvokal@redhat.com> - 2.6.16-5
- fix crash when resolving ip address

* Mon Aug 21 2006 Radek Vokál <rvokal@redhat.com> - 2.6.16-4
- add LOWER_UP and DORMANT flags (#202199)
- use dist tag

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.6.16-3.1
- rebuild

* Mon Jun 26 2006 Radek Vokál <rvokal@redhat.com> - 2.6.16-3
- improve handling of initcwnd value (#179719)

* Sun May 28 2006 Radek Vokál <rvokal@redhat.com> - 2.6.16-2
- fix BuildRequires: flex (#193403)

* Sun Mar 26 2006 Radek Vokál <rvokal@redhat.com> - 2.6.16-1
- upgrade to 2.6.16-060323
- don't hardcode /usr/lib in tc (#186607)

* Wed Feb 22 2006 Radek Vokál <rvokal@redhat.com> - 2.6.15-2
- own /usr/lib/tc (#181953)
- obsoletes shapecfg (#182284)

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.6.15-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.6.15-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Tue Jan 17 2006 Radek Vokal <rvokal@redhat.com> 2.6.15-1
- upgrade to 2.6.15-060110

* Mon Dec 12 2005 Radek Vokal <rvokal@redhat.com> 2.6.14-11
- rebuilt

* Fri Dec 09 2005 Radek Vokal <rvokal@redhat.com> 2.6.14-10
- remove backup of config files (#175302)

* Fri Nov 11 2005 Radek Vokal <rvokal@redhat.com> 2.6.14-9
- use tc manpages and cbq.init from source tarball (#172851)

* Thu Nov 10 2005 Radek Vokal <rvokal@redhat.com> 2.6.14-8
- new upstream source 

* Mon Oct 31 2005 Radek Vokal <rvokal@redhat.com> 2.6.14-7
- add warning to ip tunnel add command (#128107)

* Fri Oct 07 2005 Bill Nottingham <notting@redhat.com> 2.6.14-6
- update from upstream (appears to fix #170111)

* Fri Oct 07 2005 Radek Vokal <rvokal@redhat.com> 2.6.14-5
- update from upstream
- fixed host_len size for memcpy (#168903) <Matt_Domsch@dell.com>

* Fri Sep 23 2005 Radek Vokal <rvokal@redhat.com> 2.6.14-4
- add RPM_OPT_FLAGS

* Mon Sep 19 2005 Radek Vokal <rvokal@redhat.com> 2.6.14-3
- forget to apply the patch :( 

* Mon Sep 19 2005 Radek Vokal <rvokal@redhat.com> 2.6.14-2
- make ip help work again (#168449)

* Wed Sep 14 2005 Radek Vokal <rvokal@redhat.com> 2.6.14-1
- upgrade to ss050901 for 2.6.14 kernel headers

* Fri Aug 26 2005 Radek Vokal <rvokal@redhat.com> 2.6.13-3
- added /sbin/cbq script and sample configuration files (#166301)

* Fri Aug 19 2005 Radek Vokal <rvokal@redhat.com> 2.6.13-2
- upgrade to iproute2-050816

* Thu Aug 11 2005 Radek Vokal <rvokal@redhat.com> 2.6.13-1
- update to snapshot for 2.6.13+ kernel

* Tue May 24 2005 Radek Vokal <rvokal@redhat.com> 2.6.11-2
- removed useless initvar patch (#150798)
- new upstream source 

* Tue Mar 15 2005 Radek Vokal <rvokal@redhat.com> 2.6.11-1
- update to iproute-2.6.11

* Fri Mar 04 2005 Radek Vokal <rvokal@redhat.com> 2.6.10-2
- gcc4 rebuilt

* Wed Feb 16 2005 Radek Vokal <rvokal@redhat.com> 2.6.10-1
- update to iproute-2.6.10

* Thu Dec 23 2004 Radek Vokal <rvokal@redhat.com> 2.6.9-6
- added arpd into sbin

* Mon Nov 29 2004 Radek Vokal <rvokal@redhat.com> 2.6.9-5
- debug info removed from makefile and from spec (#140891)

* Tue Nov 16 2004 Radek Vokal <rvokal@redhat.com> 2.6.9-4
- source file updated from snapshot version
- endian patch adding <endian.h> 

* Sat Sep 18 2004 Joshua Blanton <jblanton@cs.ohiou.edu> 2.6.9-3
- added installation of netem module for tc

* Mon Sep 06 2004 Radek Vokal <rvokal@redhat.com> 2.6.9-2
- fixed possible buffer owerflow, path by Steve Grubb <linux_4ever@yahoo.com>

* Wed Sep 01 2004 Radek Vokal <rvokal@redhat.com> 2.6.9-1
- updated to iproute-2.6.9, spec file change, patches cleared

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed May 26 2004 Phil Knirsch <pknirsch@redhat.com> 2.4.7-16
- Took tons of manpages from debian, much more complete (#123952).

* Thu May 06 2004 Phil Knirsch <pknirsch@redhat.com> 2.4.7-15
- rebuilt

* Thu May 06 2004 Phil Knirsch <pknirsch@redhat.com> 2.4.7-13.2
- Built security errata version for FC1.

* Wed Apr 21 2004 Phil Knirsch <pknirsch@redhat.com> 2.4.7-14
- Fixed -f option for ss (#118355).
- Small description fix (#110997).
- Added initialization of some vars (#74961). 
- Added patch to initialize "default" rule as well (#60693).

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Nov 05 2003 Phil Knirsch <pknirsch@redhat.com> 2.4.7-12
- Security errata for netlink (CAN-2003-0856).

* Thu Oct 23 2003 Phil Knirsch <pknirsch@redhat.com>
- Updated to latest version. Used by other distros, so seems stable. ;-)
- Quite a few patches needed updating in that turn.
- Added ss (#107363) and several other new nifty tools.

* Tue Jun 17 2003 Phil Knirsch <pknirsch@redhat.com>
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Thu Jan 16 2003 Phil Knirsch <pknirsch@redhat.com> 2.4.7-7
- Added htb3-tc patch from http://luxik.cdi.cz/~devik/qos/htb/ (#75486).

* Fri Oct 11 2002 Bill Nottingham <notting@redhat.com> 2.4.7-6
- remove flags patch at author's request

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jun 19 2002 Phil Knirsch <pknirsch@redhat.com> 2.4.7-4
- Don't forcibly strip binaries

* Mon May 27 2002 Phil Knirsch <pknirsch@redhat.com> 2.4.7-3
- Fixed missing diffserv and atm support in config (#57278).
- Fixed inconsistent numeric base problem for command line (#65473).

* Tue May 14 2002 Phil Knirsch <pknirsch@redhat.com> 2.4.7-2
- Added patch to fix crosscompiling by Adrian Linkins.

* Fri Mar 15 2002 Phil Knirsch <pknirsch@redhat.com> 2.4.7-1
- Update to latest stable release 2.4.7-now-ss010824.
- Added simple man page for ip.

* Wed Aug  8 2001 Bill Nottingham <notting@redhat.com>
- allow setting of allmulti & promisc flags (#48669)

* Mon Jul 02 2001 Than Ngo <than@redhat.com>
- fix build problem in beehive if kernel-sources is not installed

* Fri May 25 2001 Helge Deller <hdeller@redhat.de>
- updated to iproute2-2.2.4-now-ss001007.tar.gz 
- bzip2 source tar file
- "License" replaces "Copyright"
- added "BuildPrereq: tetex-latex tetex-dvips psutils"
- rebuilt for 7.2

* Tue May  1 2001 Bill Nottingham <notting@redhat.com>
- use the system headers - the included ones are broken
- ETH_P_ECHO went away

* Sat Jan  6 2001 Jeff Johnson <jbj@redhat.com>
- test for specific KERNEL_INCLUDE directories.

* Thu Oct 12 2000 Than Ngo <than@redhat.com>
- rebuild for 7.1

* Thu Oct 12 2000 Than Ngo <than@redhat.com>
- add default configuration files for iproute (Bug #10549, #18887)

* Tue Jul 25 2000 Jakub Jelinek <jakub@redhat.com>
- fix include-glibc/ to cope with glibc 2.2 new resolver headers

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sun Jun 18 2000 Than Ngo <than@redhat.de>
- rebuilt in the new build environment
- use RPM macros
- handle RPM_OPT_FLAGS

* Sat Jun 03 2000 Than Ngo <than@redhat.de>
- fix iproute to build with new glibc

* Fri May 26 2000 Ngo Than <than@redhat.de>
- update to 2.2.4-now-ss000305
- add configuration files

* Mon Sep 13 1999 Bill Nottingham <notting@redhat.com>
- strip binaries

* Mon Aug 16 1999 Cristian Gafton <gafton@redhat.com>
- first build
