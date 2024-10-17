%define major   0
%define libname %mklibname %{name} %{major}
%define devname %mklibname -d %{name}

Name:		igraph
Version:	0.7.1
Release:	3
Summary:	Library for creating and manipulating graphs
Group:		Development/C
License:	GPLv2+
URL:		https://igraph.sourceforge.net/
Source0:    http://igraph.org/nightly/get/c/%{name}-%{version}.tar.gz
Source1:    http://igraph.org/c/doc/igraph.info

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
Requires:  %libname = %{version}-%{release}
Requires:  pkgconfig
Provides: igraph-devel

Summary:   Development files for igraph

%description -n %devname
The %{name}-devel package contains the header files and some
documentation needed to develop application with %{name}.

%libpackage %name %major

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}


%install
%make_install
install -Dm0644 doc/igraph.3 %{buildroot}/%{_mandir}/man3/igraph.3
install -Dm0644 %{SOURCE1} %{buildroot}/%{_infodir}/igraph.info
find . -name '.arch-ids' | xargs rm -rf

%check
make check || :

%files -n %devname
%doc COPYING AUTHORS NEWS README
%doc examples
%{_includedir}/igraph
%{_libdir}/libigraph.so
%{_libdir}/pkgconfig/igraph.pc
%doc %{_mandir}/man3/igraph.3*
%doc %{_infodir}/igraph.info*

%changelog
* Thu Jul 28 2016 Than Ngo <than@redhat.com> - 0.7.1-3
- %%check: make non-fatal as temporary workaround for scipy build on secondary arch

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Sep 30 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.7.1-1
- Update to 0.7.1
- Install info page from upstream

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.6.5-4
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Dec 09 2013 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.6.5-1
- Update to 0.6.5
- Update Source0 and URL
- Remove no longer-used patches
- Little spec clean up

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-8.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-7.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-6.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-5.2
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-4.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Oct 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.5.4-3.2
- rebuild with new gmp without compat lib

* Wed Oct 12 2011 Peter Schiffer <pschiffe@redhat.com> - 0.5.4-3.1
- rebuild with new gmp

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 29 2010 jkeating - 0.5.4-2
- Rebuilt for gcc bug 634757

* Thu Sep 16 2010 Neal Becker <ndbecker2@gmail.com> - 0.5.4-1
- Update to 0.5.4

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun May  3 2009 Neal Becker <ndbecker2@gmail.com> - 0.5.2-4
- Try removing Provides

* Sat May  2 2009 Neal Becker <ndbecker2@gmail.com> - 0.5.2-3
- Put back Provides for devel

* Tue Apr 28 2009 Neal Becker <ndbecker2@gmail.com> - 0.5.2-2
- Try enable gmp, graphml

* Mon Apr 27 2009 Neal Becker <ndbecker2@gmail.com> - 0.5.2-1
- Update to 0.5.2
- Try not applying patch #3

* Thu Feb 26 2009 Neal Becker <ndbecker2@gmail.com> - 0.5.1-6
- Make that 0.5.1-6

* Thu Feb 26 2009 Neal Becker <ndbecker2@gmail.com> - 0.5.1-5
- Patch3 for gcc-4.4 (cstdio)

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 22 2008 Neal Becker <ndbecker2@gmail.com> - 0.5.1-4
- Bump tag

* Sun Nov 16 2008 Neal Becker <ndbecker2@gmail.com> - 0.5.1-2
- Remove igraph-cstdlib.patch
- Remove igraph-test.patch

* Sun Nov 16 2008 Neal Becker <ndbecker2@gmail.com> - 0.5.1-1
- Update to 0.5.1

* Thu Sep 18 2008 Neal Becker <ndbecker2@gmail.com> - 0.5-14
- Add BR libxml2-devel to get graphml support.

* Tue Feb 26 2008 Neal Becker <ndbecker2@gmail.com> - 0.5-13
- More test fixes

* Tue Feb 26 2008 Neal Becker <ndbecker2@gmail.com> - 0.5-12
- Fix to ignore 1 bad test

* Tue Feb 26 2008 Neal Becker <ndbecker2@gmail.com> - 0.5-11
- Add patch for tests for gcc-4.3

* Mon Feb 25 2008 Neal Becker <ndbecker2@gmail.com> - 0.5-10
- Run check

* Sun Feb 17 2008 Neal Becker <ndbecker2@gmail.com> - 0.5-9
- Don't need provides

* Sun Feb 17 2008 Neal Becker <ndbecker2@gmail.com> - 0.5-8
- Add provides to main package

* Sun Feb 17 2008 Neal Becker <ndbecker2@gmail.com> - 0.5-7
- Add provides to devel package

* Sat Feb 16 2008 Neal Becker <ndbecker2@gmail.com> - 0.5-6
- fix patch

* Sat Feb 16 2008 Neal Becker <ndbecker2@gmail.com> - 0.5-5
- More patches

* Sat Feb 16 2008 Neal Becker <ndbecker2@gmail.com> - 0.5-4
- Try again to fix patch

* Sat Feb 16 2008 Neal Becker <ndbecker2@gmail.com> - 0.5-3
- fix patch

* Sat Feb 16 2008 Neal Becker <ndbecker2@gmail.com> - 0.5-2
- Still need patch1

* Fri Feb 15 2008 Neal Becker <ndbecker2@gmail.com> - 0.5-1
- update to 0.5

* Wed Feb 13 2008 Neal Becker <ndbecker2@gmail.com> - 0.4.5-7
- Try again with that patch

* Wed Feb 13 2008 Neal Becker <ndbecker2@gmail.com> - 0.4.5-6
- Updated igraph-cstdlib.patch

* Wed Feb 13 2008 Neal Becker <ndbecker2@gmail.com> - 0.4.5-5
- Add cstdlib patch for std::exit

* Wed Jan 30 2008 Neal Becker <ndbecker2@gmail.com> - 0.4.5-4
- Install examples instead of examples/simple

* Tue Jan 29 2008 Neal Becker <ndbecker2@gmail.com> - 0.4.5-3
- Include examples/simple in devel doc
- Fix devel description

* Tue Jan 29 2008 Neal Becker <ndbecker2@gmail.com> - 0.4.5-2
- Updates per panemade@gmail.com

* Wed Jan 23 2008 Neal Becker <ndbecker2@gmail.com> - 0.4.5-1
- Initial package

