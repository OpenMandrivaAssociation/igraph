# The LTO configure workaround rewrites this ancient libtool script into a
# command that starts with -e, so the shared library is never produced.
%global _disable_lto 1
# clang rejects the bundled gengraph headers' register variables as C++17.
# qsort.c is still K&R, which C23 rejects. -std=gnu17 is not valid for C++.
%global optflags %{optflags} -Wno-register

%define major   0
%define libname %mklibname %{name} %{major}
%define devname %mklibname -d %{name}

Name:		igraph
Version:	0.7.1
Release:	5
Summary:	Library for creating and manipulating graphs
Group:		Development/C
License:	GPLv2+
URL:		https://igraph.sourceforge.net/
Source0:    http://igraph.org/nightly/get/c/%{name}-%{version}.tar.gz
Source1:    http://igraph.org/c/doc/igraph.info

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool-base
BuildRequires:	slibtool
BuildRequires:	make
BuildRequires:	libxml2-devel
BuildRequires:	gmp-devel
Requires(post): /sbin/install-info
Requires(postun): /sbin/install-info

%description
igraph wants to be an efficient platform for 
1) complex network analysis and 
2) developing and implementing graph algorithms. 
It provides flexible and efficient data structures for graphs and related
tasks. It also provides implementation to many classic and new graph
algorithms like: maximum flows, graph isomorphism, scale-free
networks, community structure finding, etc.

%package -n %devname
Requires:	%libname = %{EVRD}
Requires:	pkgconfig
Provides:	igraph-devel

Summary:	Development files for igraph

%description -n %devname
The %{name}-devel package contains the header files and some
documentation needed to develop application with %{name}.

# The two-argument library helper names this package without the soname
# major and obsoletes the published lib64igraph0 name. Declare it directly.
%package -n %libname
Summary:	The igraph library
Group:		System/Libraries

%description -n %libname
The igraph library, a part of igraph.

%prep
%setup -q
# configure is regenerated from configure.ac. On success the libxml
# probe copies CFLAGS into CPPFLAGS, so -std=gnu17 reaches c++.
# Do not mention the configure macro here: rpm would expand it.
sed -i 's/CPPFLAGS="${OLDCFLAGS} ${XML2_CFLAGS}"/CPPFLAGS="${OLDCPPFLAGS} ${XML2_CFLAGS}"/' configure.ac configure

%build
# qsort.c is K&R. f2c calls feenableexcept, which needs _GNU_SOURCE.
# -std=gnu17 must stay off CXXFLAGS.
# Empty means "none needed". The words "none needed" are appended to CC.
export ac_cv_prog_cc_c23=
export CFLAGS="%{optflags} -std=gnu17 -D_GNU_SOURCE"
export CXXFLAGS="%{optflags}"
%configure
make %{?_smp_mflags} LIBTOOL=slibtool-shared


%install
%make_install LIBTOOL=slibtool-shared
install -Dm0644 doc/igraph.3 %{buildroot}/%{_mandir}/man3/igraph.3
install -Dm0644 %{SOURCE1} %{buildroot}/%{_infodir}/igraph.info
find . -name '.arch-ids' | xargs rm -rf

%check
make check || :

%files -n %libname
%{_libdir}/libigraph.so.%{major}*

%files -n %devname
%doc COPYING AUTHORS NEWS README
%doc examples
%{_includedir}/igraph
%{_libdir}/libigraph.so
%{_libdir}/pkgconfig/igraph.pc
%doc %{_mandir}/man3/igraph.3*
%doc %{_infodir}/igraph.info*
