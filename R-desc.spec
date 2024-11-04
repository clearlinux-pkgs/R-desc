#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v3
# autospec commit: c1050fe
#
Name     : R-desc
Version  : 1.4.3
Release  : 67
URL      : https://cran.r-project.org/src/contrib/desc_1.4.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/desc_1.4.3.tar.gz
Summary  : Manipulate DESCRIPTION Files
Group    : Development/Tools
License  : MIT
Requires: R-R6
Requires: R-cli
BuildRequires : R-R6
BuildRequires : R-cli
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
files.  It is intended for packages that create or manipulate other
    packages.

%prep
%setup -q -n desc
pushd ..
cp -a desc buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1702276614

%install
export SOURCE_DATE_EPOCH=1702276614
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/desc/DESCRIPTION
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
/usr/lib64/R/library/desc/WORDLIST
/usr/lib64/R/library/desc/help/AnIndex
/usr/lib64/R/library/desc/help/aliases.rds
/usr/lib64/R/library/desc/help/desc.rdb
/usr/lib64/R/library/desc/help/desc.rdx
/usr/lib64/R/library/desc/help/paths.rds
/usr/lib64/R/library/desc/html/00Index.html
/usr/lib64/R/library/desc/html/R.css
/usr/lib64/R/library/desc/tests/testthat.R
/usr/lib64/R/library/desc/tests/testthat/D1
/usr/lib64/R/library/desc/tests/testthat/D10
/usr/lib64/R/library/desc/tests/testthat/D11
/usr/lib64/R/library/desc/tests/testthat/D12
/usr/lib64/R/library/desc/tests/testthat/D13
/usr/lib64/R/library/desc/tests/testthat/D14
/usr/lib64/R/library/desc/tests/testthat/D15
/usr/lib64/R/library/desc/tests/testthat/D2
/usr/lib64/R/library/desc/tests/testthat/D3
/usr/lib64/R/library/desc/tests/testthat/D4
/usr/lib64/R/library/desc/tests/testthat/D5
/usr/lib64/R/library/desc/tests/testthat/D6
/usr/lib64/R/library/desc/tests/testthat/D7
/usr/lib64/R/library/desc/tests/testthat/D8
/usr/lib64/R/library/desc/tests/testthat/D9
/usr/lib64/R/library/desc/tests/testthat/_snaps/authors.md
/usr/lib64/R/library/desc/tests/testthat/_snaps/str.md
/usr/lib64/R/library/desc/tests/testthat/files/DESCRIPTION
/usr/lib64/R/library/desc/tests/testthat/fixtures/notpkg_1.0.tar.gz
/usr/lib64/R/library/desc/tests/testthat/fixtures/pkg_1.0.0.tar.gz
/usr/lib64/R/library/desc/tests/testthat/fixtures/pkg_1.0.0.tgz
/usr/lib64/R/library/desc/tests/testthat/fixtures/pkg_1.0.0.zip
/usr/lib64/R/library/desc/tests/testthat/fixtures/pkg_1.0.0_R_x86_64-pc-linux-gnu.tar.gz
/usr/lib64/R/library/desc/tests/testthat/fixtures/xxx.gz
/usr/lib64/R/library/desc/tests/testthat/fixtures/xxx.tar.gz
/usr/lib64/R/library/desc/tests/testthat/fixtures/xxx.zip
/usr/lib64/R/library/desc/tests/testthat/helper.R
/usr/lib64/R/library/desc/tests/testthat/output/to_latex.tex
/usr/lib64/R/library/desc/tests/testthat/test-archives.R
/usr/lib64/R/library/desc/tests/testthat/test-assertions.R
/usr/lib64/R/library/desc/tests/testthat/test-authors.R
/usr/lib64/R/library/desc/tests/testthat/test-built.R
/usr/lib64/R/library/desc/tests/testthat/test-checks.R
/usr/lib64/R/library/desc/tests/testthat/test-collate.R
/usr/lib64/R/library/desc/tests/testthat/test-create.R
/usr/lib64/R/library/desc/tests/testthat/test-deps.R
/usr/lib64/R/library/desc/tests/testthat/test-desc.R
/usr/lib64/R/library/desc/tests/testthat/test-encoding.R
/usr/lib64/R/library/desc/tests/testthat/test-find-package-root.R
/usr/lib64/R/library/desc/tests/testthat/test-idempotent.R
/usr/lib64/R/library/desc/tests/testthat/test-non-oo.R
/usr/lib64/R/library/desc/tests/testthat/test-queries.R
/usr/lib64/R/library/desc/tests/testthat/test-read.R
/usr/lib64/R/library/desc/tests/testthat/test-remotes.R
/usr/lib64/R/library/desc/tests/testthat/test-repair.R
/usr/lib64/R/library/desc/tests/testthat/test-spelling.R
/usr/lib64/R/library/desc/tests/testthat/test-str.R
/usr/lib64/R/library/desc/tests/testthat/test-to_latex.R
/usr/lib64/R/library/desc/tests/testthat/test-trailing-ws.R
/usr/lib64/R/library/desc/tests/testthat/test-urls.R
/usr/lib64/R/library/desc/tests/testthat/test-utils.R
/usr/lib64/R/library/desc/tests/testthat/test-validation.R
/usr/lib64/R/library/desc/tests/testthat/test-versions.R
/usr/lib64/R/library/desc/tests/testthat/test-write.R
