#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : functools32
Version  : 3.2.3
Release  : 4
URL      : https://pypi.python.org/packages/source/f/functools32/functools32-3.2.3-1.tar.gz
Source0  : https://pypi.python.org/packages/source/f/functools32/functools32-3.2.3-1.tar.gz
Summary  : Backport of the functools module from Python 3.2.3 for use on 2.7 and PyPy.
Group    : Development/Tools
License  : Python-2.0
Requires: functools32-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : setuptools

%description
No detailed description available

%package python
Summary: python components for the functools32 package.
Group: Default

%description python
python components for the functools32 package.


%prep
%setup -q -n functools32-3.2.3-1

%build
python2 setup.py build -b py2

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=intel.com,localhost
py.test-2.7
%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
