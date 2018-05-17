%define src_name cassandra-driver
%define version 3.0.0
%define unmangled_version 3.0.0
%define unmangled_version 3.0.0
%define release 0contrail2 

Summary: Python driver for Cassandra
Name: python-%{src_name}
Version: %{version}
Release: %{release}%{?dist}
Source0: https://pypi.python.org/packages/source/c/cassandra-driver/%{src_name}-%{unmangled_version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
Prefix: %{_prefix}
Vendor: Tyler Hobbs <tyler@datastax.com>
Url: http://github.com/datastax/python-driver

BuildRequires:  python-devel
BuildRequires:  python-setuptools
Requires:  python-futures

%description
DataStax Python Driver for Apache Cassandra
===========================================

A modern, `feature-rich <https://github.com/datastax/python-driver#features>`_ and highly-tunable Python client library for Apache Cassandra (1.2+) and DataStax Enterprise (3.1+) using exclusively Cassandra's binary protocol and Cassandra Query Language v3.

The driver supports Python 2.6, 2.7, 3.3, and 3.4.

Feedback Requested
------------------
**Help us focus our efforts!** Provide your input on the `Platform and Runtime Survey <https://docs.google.com/a/datastax.com/forms/d/10wkbKLqmqs91gvhFW5u43y60pg_geZDolVNrxfO5_48/viewform>`_ (we kept it short).

Features
--------
* `Synchronous <http://datastax.github.io/python-driver/api/cassandra/cluster.html#cassandra.cluster.Session.execute>`_ and `Asynchronous <http://datastax.github.io/python-driver/api/cassandra/cluster.html#cassandra.cluster.Session.execute_async>`_ APIs
* `Simple, Prepared, and Batch statements <http://datastax.github.io/python-driver/api/cassandra/query.html#cassandra.query.Statement>`_
* Asynchronous IO, parallel execution, request pipelining
* `Connection pooling <http://datastax.github.io/python-driver/api/cassandra/cluster.html#cassandra.cluster.Cluster.get_core_connections_per_host>`_
* Automatic node discovery
* `Automatic reconnection <http://datastax.github.io/python-driver/api/cassandra/policies.html#reconnecting-to-dead-hosts>`_
* Configurable `load balancing <http://datastax.github.io/python-driver/api/cassandra/policies.html#load-balancing>`_ and `retry policies <http://datastax.github.io/python-driver/api/cassandra/policies.html#retrying-failed-operations>`_
* `Concurrent execution utilities <http://datastax.github.io/python-driver/api/cassandra/concurrent.html>`_
* `Object mapper <http://datastax.github.io/python-driver/object_mapper.html>`_

Installation
------------
Installation through pip is recommended::

    $ pip install cassandra-driver

For more complete installation instructions, see the
`installation guide <http://datastax.github.io/python-driver/installation.html>`_.

Documentation
-------------
The documentation can be found online `here <http://datastax.github.io/python-driver/index.html>`_.

A couple of links for getting up to speed:

* `Installation <http://datastax.github.io/python-driver/installation.html>`_
* `Getting started guide <http://datastax.github.io/python-driver/getting_started.html>`_
* `API docs <http://datastax.github.io/python-driver/api/index.html>`_
* `Performance tips <http://datastax.github.io/python-driver/performance.html>`_

Object Mapper
-------------
cqlengine (originally developed by Blake Eggleston and Jon Haddad, with contributions from the
community) is now maintained as an integral part of this package. Refer to
`documentation here <http://datastax.github.io/python-driver/object_mapper.html>`_.

Reporting Problems
------------------
Please report any bugs and make any feature requests on the
`JIRA <https://datastax-oss.atlassian.net/browse/PYTHON>`_ issue tracker.

If you would like to contribute, please feel free to open a pull request.

Getting Help
------------
Your two best options for getting help with the driver are the
`mailing list <https://groups.google.com/a/lists.datastax.com/forum/#!forum/python-driver-user>`_
and the IRC channel.

For IRC, use the #datastax-drivers channel on irc.freenode.net.  If you don't have an IRC client,
you can use `freenode's web-based client <http://webchat.freenode.net/?channels=#datastax-drivers>`_.

Features to be Added
--------------------
* C extension for encoding/decoding messages

License
-------
Copyright 2013-2015 DataStax

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.


%prep
%setup -n %{src_name}-%{unmangled_version} -n %{src_name}-%{unmangled_version}

%build
env CFLAGS="$RPM_OPT_FLAGS" python setup.py build --no-libev --no-cython

%install
python setup.py install --no-cython --no-libev --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
