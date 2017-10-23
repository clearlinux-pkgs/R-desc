#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-desc
Version  : 1.1.1
Release  : 6
URL      : https://cran.r-project.org/src/contrib/desc_1.1.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/desc_1.1.1.tar.gz
Summary  : Manipulate DESCRIPTION Files
Group    : Development/Tools
License  : MIT
Requires: R-assertthat
Requires: R-rprojroot
BuildRequires : R-assertthat
BuildRequires : R-rprojroot
BuildRequires : clr-R-helpers

%description
It is intended for packages that create or manipulate other packages.

%prep
%setup -q -c -n desc

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1505675015

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1505675015
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library desc
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library desc
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library desc|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || : || :


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
