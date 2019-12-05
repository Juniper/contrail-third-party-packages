%define src_name bitstring
%define version 3.1.5
%define unmangled_version 3.1.5
%define release 1
%define _relstr 0contrail0
Summary: Simple construction, analysis and modification of binary data.
Name: python-%{src_name}
Version: %{version}
Release: %{release}.%{_relstr}
Source0: https://pypi.python.org/packages/f3/e5/dfe4c49c93d174a5fd807ed307d3a3f38c6b3e140972945f81a5f5578ca7/bitstring-3.1.5.zip
License: MIT
Group: Development/Libraries
Prefix: %{_prefix}
Vendor: Scott Griffiths <dr.scottgriffiths@gmail.com>
Url: https://github.com/scott-griffiths/bitstring
BuildRequires: python-devel

%description
==================
Bitstring Module
==================

bitstring is a pure Python module designed to help make the creation and analysis of binary data as simple and natural as possible.

Bitstrings can be constructed from integers (big and little endian), hex, octal, binary, strings or files. They can be sliced, joined, reversed, inserted into, overwritten, etc.
with simple functions or slice notation. They can also be read from, searched and replaced, and navigated in, similar to a file or stream.

bitstring is open source software, and has been released under the MIT licence.

This module works in both Python 2.7 and Python 3.

Documentation

The manual for the bitstring module is available here <http://packages.python.org/bitstring>. It contains a walk-through of all the features and a complete reference section.

It is also available as a PDF as part of the source download.

Installation

If you have downloaded and unzipped the package then you need to run the setup.py script with the 'install' argument:

python setup.py install
You may need to run this with root privileges on Unix-like systems.

If you haven't yet downloaded the package then you can just try:

easy_install bitstring
or

pip install bitstring
Simple Examples

Creation:

>>> a = BitArray(bin='00101')
>>> b = Bits(a_file_object)
>>> c = BitArray('0xff, 0b101, 0o65, uint:6=22')
>>> d = pack('intle:16, hex=a, 0b1', 100, a='0x34f')
>>> e = pack('<16h', *range(16))
Different interpretations, slicing and concatenation:

>>> a = BitArray('0x1af')
>>> a.hex, a.bin, a.uint
('1af', '000110101111', 431)
>>> a[10:3:-1].bin
'1110101'
>>> 3*a + '0b100'
BitArray('0o0657056705674')
Reading data sequentially:

>>> b = BitStream('0x160120f')
>>> b.read(12).hex
'160'
>>> b.pos = 0
>>> b.read('uint:12')
352
>>> b.readlist('uint:12, bin:3')
[288, '111']
Searching, inserting and deleting:

>>> c = BitArray('0b00010010010010001111')   # c.hex == '0x1248f'
>>> c.find('0x48')
(8,)
>>> c.replace('0b001', '0xabc')
>>> c.insert('0b0000')
>>> del c[12:16]
Unit Tests

The 400+ unit tests should all pass for Python 2.6 and later.

The bitstring module has been released as open source under the MIT License. Copyright (c) 2016 Scott Griffiths

For more information see the project's homepage on GitHub: <https://github.com/scott-griffiths/bitstring>

%prep
%setup -n %{src_name}-%{unmangled_version}

%build
env CFLAGS="$RPM_OPT_FLAGS" python setup.py build

%install
python setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
