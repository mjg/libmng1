Name: libmng
Version: 1.0.1
Release: 2
URL: http://www.libmng.com/
Summary: Library for supporting MNG (Animated PNG) graphics
License: BSD-like
Source: http://www.libmng.com/download/%{name}-%{version}.tar.bz2
Group: System Environment/Libraries
BuildRoot: %{_tmppath}/%{name}-root
Prefix: %{_prefix}
Requires: zlib, libjpeg
BuildPrereq: gcc glibc-devel zlib-devel libjpeg-devel

%package devel
Summary: Development files for the MNG (Animated PNG) library
Group: Development/Libraries
Requires: %{name} = %{version}

%package static
Summary: MNG (Animated PNG) library for static linking
Group: Development/Libraries

%description
LibMNG is a library for accessing graphics in the MNG (Multi-image
Network Graphics, basically animated PNG) and JNG (JPEG Network Graphics,
basically JPEG streams integrated in a PNG chunk) formats.

%description devel
Development (Header) files for the LibMNG library.

LibMNG is a library for accessing graphics in the MNG (Multi-image
Network Graphics, basically animated PNG) and JNG (JPEG Network Graphics,
basically JPEG streams integrated in a PNG chunk) formats.

Install %{name}-devel if you wish to develop or compile applications
using MNG graphics.

%description static
A version of the LibMNG library for linking statically.

LibMNG is a library for accessing graphics in the MNG (Multi-image
Network Graphics, basically animated PNG) and JNG (JPEG Network Graphics,
basically JPEG streams integrated in a PNG chunk) formats.

Install %{name}-devel if you wish to develop or compile applications
using MNG graphics without depending on libmng being installed on the
user's system.


%prep
%setup

%build
[ ! -x ./configure ] && ./autogen.sh --help # generate, but don't run
%configure --enable-shared --enable-static --with-zlib --with-jpeg \
	--with-gnu-ld
make

%install
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{prefix}/lib/*.so.*

%files devel
%defattr(-,root,root)
%{prefix}/lib/*.la
%{prefix}/lib/*.so
%{prefix}/include/*

%files static
%defattr(-,root,root)
%{prefix}/lib/*.a

%changelog
* Wed Jun 20 2001 Than Ngo <rtthan@redhat.com> 1.0.1-2
- requires %%{name} = %%{version}

* Thu May  3 2001 Bernhard Rosenkraenzer <bero@redhat.com> 1.0.1-1
- 1.0.1

* Wed Feb 28 2001 Trond Eivind Glomsrød <teg@redhat.com>
- remove bogus symlink trick

* Mon Feb 26 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Update to 1.0.0 to make Qt 2.3.0 happy

* Sat Jan 19 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- 0.9.4, fixes MNG 1.0 spec compliance

* Tue Dec 19 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 0.9.3
- Add ldconfig calls in %%post and %%postun

* Tue Dec 05 2000 Florian La Roche <Florian.LaRoche@redhat.de>
- added a clean section to the spec file

* Tue Sep 19 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- initial rpm

