#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : XStatic-mdi
Version  : 1.1.70.1
Release  : 3
URL      : https://pypi.python.org/packages/source/X/XStatic-mdi/XStatic-mdi-1.1.70.1.tar.gz
Source0  : https://pypi.python.org/packages/source/X/XStatic-mdi/XStatic-mdi-1.1.70.1.tar.gz
Summary  : mdi 1.1.70 (XStatic packaging standard)
Group    : Development/Tools
License  : OFL-1.1
Requires: XStatic-mdi-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : setuptools

%description
XStatic-mdi
-----------
mdi javascript library packaged for setuptools (easy_install) / pip.

%package python
Summary: python components for the XStatic-mdi package.
Group: Default
Provides: xstatic-mdi-python

%description python
python components for the XStatic-mdi package.


%prep
%setup -q -n XStatic-mdi-1.1.70.1

%build
python2 setup.py build -b py2

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
