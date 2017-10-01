#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : functools32
Version  : 3.2.3.1
Release  : 15
URL      : http://pypi.debian.net/functools32/functools32-3.2.3-1.tar.gz
Source0  : http://pypi.debian.net/functools32/functools32-3.2.3-1.tar.gz
Summary  : Backport of the functools module from Python 3.2.3 for use on 2.7 and PyPy.
Group    : Development/Tools
License  : Python-2.0
Requires: functools32-legacypython
Requires: functools32-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
This is a backport of the functools standard library module from
        Python 3.2.3 for use on Python 2.7 and PyPy. It includes
        new features `lru_cache` (Least-recently-used cache decorator).

%package legacypython
Summary: legacypython components for the functools32 package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the functools32 package.


%package python
Summary: python components for the functools32 package.
Group: Default
Requires: functools32-legacypython

%description python
python components for the functools32 package.


%prep
%setup -q -n functools32-3.2.3-1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1506877102
python2 setup.py build -b py2

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)
