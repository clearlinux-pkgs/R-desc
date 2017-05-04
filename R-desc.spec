#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-desc
Version  : 1.1.0
Release  : 2
URL      : https://cran.r-project.org/src/contrib/desc_1.1.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/desc_1.1.0.tar.gz
Summary  : Manipulate DESCRIPTION Files
Group    : Development/Tools
License  : MIT
Requires: R-assertthat
Requires: R-rprojroot
BuildRequires : R-assertthat
BuildRequires : R-rprojroot
BuildRequires : clr-R-helpers

%description
# desc
> Parse DESCRIPTION files
[![Linux Build Status](https://travis-ci.org/r-pkgs/desc.svg?branch=master)](https://travis-ci.org/r-pkgs/desc)
[![Windows Build status](https://ci.appveyor.com/api/projects/status/github/r-pkgs/desc?svg=true)](https://ci.appveyor.com/project/gaborcsardi/desc)
[![](http://www.r-pkg.org/badges/version/desc)](http://www.r-pkg.org/pkg/desc)
[![CRAN RStudio mirror downloads](http://cranlogs.r-pkg.org/badges/desc)](http://www.r-pkg.org/pkg/desc)
[![Coverage Status](https://img.shields.io/codecov/c/github/r-pkgs/desc/master.svg)](https://codecov.io/github/r-pkgs/desc?branch=master)

%prep
%setup -q -c -n desc

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1493918025

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1493918025
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library desc
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library desc || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/desc/DESCRIPTION
/usr/lib64/R/library/desc/DESCRIPTION2
/usr/lib64/R/library/desc/INDEX
/usr/lib64/R/library/desc/LICENSE
/usr/lib64/R/library/desc/Meta/Rd.rds
/usr/lib64/R/library/desc/Meta/features.rds
/usr/lib64/R/library/desc/Meta/hsearch.rds
/usr/lib64/R/library/desc/Meta/links.rds
/usr/lib64/R/library/desc/Meta/nsInfo.rds
/usr/lib64/R/library/desc/Meta/package.rds
/usr/lib64/R/library/desc/NAMESPACE
/usr/lib64/R/library/desc/NEWS.md
/usr/lib64/R/library/desc/R/desc
/usr/lib64/R/library/desc/R/desc.rdb
/usr/lib64/R/library/desc/R/desc.rdx
/usr/lib64/R/library/desc/README.Rmd
/usr/lib64/R/library/desc/README.md
/usr/lib64/R/library/desc/help/AnIndex
/usr/lib64/R/library/desc/help/aliases.rds
/usr/lib64/R/library/desc/help/desc.rdb
/usr/lib64/R/library/desc/help/desc.rdx
/usr/lib64/R/library/desc/help/paths.rds
/usr/lib64/R/library/desc/html/00Index.html
/usr/lib64/R/library/desc/html/R.css
