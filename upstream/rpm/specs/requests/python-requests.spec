%define name requests
%define version 2.6.0
%define contrail_version 1contrail1
%define unmangled_version 2.6.0
%define unmangled_version 2.6.0
%define release 1

Summary: Python HTTP for Humans.
Name: python-%{name}
Version: %{version}
Release: %{release}.%{contrail_version}%{?dist}
Source0: https://pypi.python.org/packages/source/r/requests/%{name}-%{unmangled_version}.tar.gz
License: Apache 2.0
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Kenneth Reitz <me@kennethreitz.com>
Url: http://python-requests.org

BuildRequires:python-devel
BuildRequires:python-setuptools

%description
python-request package rebuilt by OpenContrail from sources

Requests: HTTP for Humans
=========================

.. image:: https://img.shields.io/pypi/v/requests.svg
    :target: https://pypi.python.org/pypi/requests

.. image:: https://img.shields.io/pypi/dm/requests.svg
        :target: https://pypi.python.org/pypi/requests


Requests is an Apache2 Licensed HTTP library, written in Python, for human
beings.

Most existing Python modules for sending HTTP requests are extremely
verbose and cumbersome. Python's builtin urllib2 module provides most of
the HTTP capabilities you should need, but the api is thoroughly broken.
It requires an enormous amount of work (even method overrides) to
perform the simplest of tasks.

Things shouldn't be this way. Not in Python.

.. code-block:: python

    >>> r = requests.get('https://api.github.com', auth=('user', 'pass'))
    >>> r.status_code
    204
    >>> r.headers['content-type']
    'application/json'
    >>> r.text
    ...

See `the same code, without Requests <https://gist.github.com/973705>`_.

Requests allow you to send HTTP/1.1 requests. You can add headers, form data,
multipart files, and parameters with simple Python dictionaries, and access the
response data in the same way. It's powered by httplib and `urllib3
<https://github.com/shazow/urllib3>`_, but it does all the hard work and crazy
hacks for you.


Features
--------

- International Domains and URLs
- Keep-Alive & Connection Pooling
- Sessions with Cookie Persistence
- Browser-style SSL Verification
- Basic/Digest Authentication
- Elegant Key/Value Cookies
- Automatic Decompression
- Unicode Response Bodies
- Multipart File Uploads
- Connection Timeouts
- Thread-safety
- HTTP(S) proxy support


Installation
------------

To install Requests, simply:

.. code-block:: bash

    $ pip install requests


Documentation
-------------

Documentation is available at http://docs.python-requests.org/.


Contribute
----------

#. Check for open issues or open a fresh issue to start a discussion around a feature idea or a bug. There is a `Contributor Friendly`_ tag for issues that should be ideal for people who are not very familiar with the codebase yet.
#. If you feel uncomfortable or uncertain about an issue or your changes, feel free to email @sigmavirus24 and he will happily help you via email, Skype, remote pairing or whatever you are comfortable with.
#. Fork `the repository`_ on GitHub to start making your changes to the **master** branch (or branch off of it).
#. Write a test which shows that the bug was fixed or that the feature works as expected.
#. Send a pull request and bug the maintainer until it gets merged and published. :) Make sure to add yourself to AUTHORS_.

.. _`the repository`: http://github.com/kennethreitz/requests
.. _AUTHORS: https://github.com/kennethreitz/requests/blob/master/AUTHORS.rst
.. _Contributor Friendly: https://github.com/kennethreitz/requests/issues?direction=desc&labels=Contributor+Friendly&page=1&sort=updated&state=open


.. :changelog:

Release History
---------------

2.6.0 (2015-03-14)
++++++++++++++++++

**Bugfixes**

- Fix handling of cookies on redirect. Previously a cookie without a host
  value set would use the hostname for the redirected URL exposing requests
  users to session fixation attacks and potentially cookie stealing. This was
  disclosed privately by Matthew Daley of `BugFuzz <https://bugfuzz.com>`_.
  An CVE identifier has not yet been assigned for this. This affects all
  versions of requests from v2.1.0 to v2.5.3 (inclusive on both ends).

- Fix error when requests is an ``install_requires`` dependency and ``python
  setup.py test`` is run. (#2462)

- Fix error when urllib3 is unbundled and requests continues to use the
  vendored import location.

- Include fixes to ``urllib3``'s header handling.

- Requests' handling of unvendored dependencies is now more restrictive.

**Features and Improvements**

- Support bytearrays when passed as parameters in the ``files`` argument.
  (#2468)

- Avoid data duplication when creating a request with ``str``, ``bytes``, or
  ``bytearray`` input to the ``files`` argument.

%prep
%setup -n %{name}-%{unmangled_version} -n requests-%{unmangled_version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)

%changelog
* Fri Mar 27 2015 Nagendra Maynattamai <npchandran@juniper.net> - 2.6.0.1.1contrail1
- Rebuilt by OpenContrail from sources https://pypi.python.org/packages/source/r/requests/requests-2.6.0.tar.gz
