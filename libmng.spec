Name: libmng
Version: 0.9.2
Release: 1tc1
URL: http://www.libmng.com/
Summary: Library for supporting MNG (Animated PNG) graphics
License: BSD-like
Distribution: BlueSky
Packager: RedHat
Source: http://www.libmng.com/%{name}-%{version}.tar.bz2
Group: System Environment/Libraries
BuildRoot: %{_tmppath}/%{name}-root
Prefix: %{_prefix}
Requires: zlib, libjpeg
BuildPrereq: glibc-devel zlib-devel libjpeg-devel

%package devel
Summary: Development files for the MNG (Animated PNG) library
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

%prep
%setup -n libmng-devel
rm -rf makefile # Stupid name for a directory...

%build
[ ! -x ./configure ] && ./autogen.sh --help # generate, but don't run
%configure --enable-shared --with-zlib --with-jpeg
make

%install
%makeinstall

%post
/sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{prefix}/lib/*.so.*

%files devel
%defattr(-,root,root)
%{prefix}/lib/*.la
%{prefix}/lib/*.so
%{prefix}/include/*

%changelog
* Thu Oct 19 2000 Chih-Wei Huang <cwhuang@linux.org.tw>
- remove static

* Tue Sep 19 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- initial rpm

%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT
