%define name lxml
%define version 2.3.3
%define unmangled_version 2.3.3
%define unmangled_version 2.3.3
%define release 1
%define _relstr 0contrail

Summary: Powerful and Pythonic XML processing library combining libxml2/libxslt with the ElementTree API.
Name: python-%{name}
Version: %{version}
Release: %{release}.%{_relstr}
Source0: https://pypi.python.org/packages/source/l/lxml/lxml-2.3.3.tar.gz 
License: UNKNOWN
Group: Development/Libraries
Prefix: %{_prefix}
Vendor: lxml dev team <lxml-dev@lxml.de>
Url: http://lxml.de/

BuildRequires:python-devel
BuildRequires:libxslt-devel

%description
lxml is a Pythonic, mature binding for the libxml2 and libxslt libraries.  It
provides safe and convenient access to these libraries using the ElementTree
API.

It extends the ElementTree API significantly to offer support for XPath,
RelaxNG, XML Schema, XSLT, C14N and much more.

To contact the project, go to the `project home page
<http://lxml.de/>`_ or see our bug tracker at
https://launchpad.net/lxml

In case you want to use the current in-development version of lxml,
you can get it from the github repository at
https://github.com/lxml/lxml .  Note that this requires Cython to
build the sources, see the build instructions on the project home
page.  To the same end, running ``easy_install lxml==dev`` will
install lxml from
https://github.com/lxml/lxml/tarball/master#egg=lxml-dev if you have
an appropriate version of Cython installed.


After an official release of a new stable series, bug fixes may become
available at
https://github.com/lxml/lxml/tree/lxml-2.3 .
Running ``easy_install lxml==2.3bugfix`` will install
the unreleased branch state from
https://github.com/lxml/lxml/tarball/lxml-2.3#egg=lxml-2.3bugfix
as soon as a maintenance branch has been established.  Note that this
requires Cython to be installed at an appropriate version for the build.

2.3.3 (2012-01-04)
==================

Features added
--------------

* ``lxml.html.tostring()`` gained new serialisation options
  ``with_tail`` and ``doctype``.

Bugs fixed
----------

* Fixed a crash when using ``iterparse()`` for HTML parsing and
  requesting start events.

* Fixed parsing of more selectors in cssselect.  Whitespace before
  pseudo-elements and pseudo-classes is significant as it is a
  descendant combinator.
  "E :pseudo" should parse the same as "E \*:pseudo", not "E:pseudo".
  Patch by Simon Sapin.

* lxml.html.diff no longer raises an exception when hitting
  'img' tags without 'src' attribute.

Other changes
--------------




%prep
%setup -n lxml-2.3.3 

%build
env CFLAGS="$RPM_OPT_FLAGS" python setup.py build

%install
python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
/usr/lib64/python2.6/site-packages/lxml*
%defattr(-,root,root)
