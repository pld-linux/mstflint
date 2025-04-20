Summary:	Firmware burning and diagnostic tools for Mellanox HCA/NIC cards
Summary(pl.UTF-8):	Narzędzia modyfikujące firmware i diagnostyczne dla kart HCA/NIC Mellanox
Name:		mstflint
Version:	4.31.0
%define	upstream_ver	%{version}-1
Release:	1
License:	BSD or GPL v2
Group:		Networking/Utilities
Source0:	https://github.com/Mellanox/mstflint/releases/download/v%{upstream_ver}/%{name}-%{upstream_ver}.tar.gz
# Source0-md5:	19b8dd432ba7dbec66873190ec197fc7
Patch1:		x32.patch
URL:		https://github.com/Mellanox/mstflint
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	expat-devel
BuildRequires:	libibmad-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	muparser-devel
BuildRequires:	openssl-devel >= 1.0.2k
BuildRequires:	xz-devel
BuildRequires:	zlib-devel
# see common/compatibility.h
ExclusiveArch:	%{ix86} %{x8664} x32 %{arm} aarch64 e2k ia64 m68k hppa mips64 ppc ppc64 riscv
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Firmware burning and diagnostic tools for Mellanox HCA/NIC cards.

%description -l pl.UTF-8
Narzędzia modyfikujące firmware i diagnostyczne dla kart HCA/NIC
Mellanox.

%package devel
Summary:	Header files for Mellanox HCA/NIC cards access
Summary(pl.UTF-8):	Pliki nagłówkowe do dostępu do kart HCA/NIC Mellanox
Group:		Development/Libraries
# doesn't require base

%description devel
Header files for Mellanox HCA/NIC cards access.

%description devel -l pl.UTF-8
Pliki nagłówkowe do dostępu do kart HCA/NIC Mellanox.

%prep
%setup -q
%patch -P1 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__automake}
%{__autoheader}
%{__autoconf}
%configure \
	--enable-adb-generic-tools \
	--enable-cs \
	--enable-fw-mgr \
	--enable-xml2 \
	--enable-openssl
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README
%dir %{_sysconfdir}/mstflint
%{_sysconfdir}/mstflint/ca-bundle.crt
%attr(755,root,root) %{_bindir}/mstarchive
%attr(755,root,root) %{_bindir}/mstconfig
%attr(755,root,root) %{_bindir}/mstdevices_info
%attr(755,root,root) %{_bindir}/mstflint
%attr(755,root,root) %{_bindir}/mstfwctrl
%attr(755,root,root) %{_bindir}/mstfwtrace
%attr(755,root,root) %{_bindir}/mstlink
%attr(755,root,root) %{_bindir}/mstmcra
%attr(755,root,root) %{_bindir}/mstmget_temp
%attr(755,root,root) %{_bindir}/mstmread
%attr(755,root,root) %{_bindir}/mstmtserver
%attr(755,root,root) %{_bindir}/mstmwrite
%attr(755,root,root) %{_bindir}/mstprivhost
%attr(755,root,root) %{_bindir}/mstreg
%attr(755,root,root) %{_bindir}/mstregdump
%attr(755,root,root) %{_bindir}/mstresourcedump
%attr(755,root,root) %{_bindir}/mstresourceparse
%attr(755,root,root) %{_bindir}/mstvpd
%attr(755,root,root) %{_bindir}/mstcongestion
%attr(755,root,root) %{_bindir}/mstfwmanager
%attr(755,root,root) %{_bindir}/mstfwreset
%dir %{_libdir}/mstflint
%dir %{_libdir}/mstflint/python_tools
%attr(755,root,root) %{_libdir}/mstflint/python_tools/c_dev_mgt.so
%attr(755,root,root) %{_libdir}/mstflint/python_tools/ccmdif.so
%attr(755,root,root) %{_libdir}/mstflint/python_tools/cmtcr.so
%attr(755,root,root) %{_libdir}/mstflint/python_tools/rreg_access.so
%{_libdir}/mstflint/python_tools/*.py
%{_libdir}/mstflint/python_tools/mlxpci
%{_libdir}/mstflint/python_tools/mstfwreset
%{_libdir}/mstflint/python_tools/mstfwtrace
%{_libdir}/mstflint/python_tools/mstprivhost
%{_libdir}/mstflint/python_tools/resourcetools
%dir %{_libdir}/mstflint/sdk
%attr(755,root,root) %{_libdir}/mstflint/sdk/libresource_dump_sdk.so
%{_datadir}/mstflint
%{_mandir}/man1/mstarchive.1*
%{_mandir}/man1/mstconfig.1*
%{_mandir}/man1/mstcongestion.1*
%{_mandir}/man1/mstflint.1*
%{_mandir}/man1/mstfwmanager.1*
%{_mandir}/man1/mstfwreset.1*
%{_mandir}/man1/mstfwtrace.1*
%{_mandir}/man1/mstlink.1*
%{_mandir}/man1/mstmcra.1*
%{_mandir}/man1/mstmread.1*
%{_mandir}/man1/mstmtserver.1*
%{_mandir}/man1/mstmwrite.1*
%{_mandir}/man1/mstprivhost.1*
%{_mandir}/man1/mstreg.1*
%{_mandir}/man1/mstregdump.1*
%{_mandir}/man1/mstresourcedump.1*
%{_mandir}/man1/mstvpd.1*

%files devel
%defattr(644,root,root,755)
%{_libdir}/libmtcr_ul.a
%dir %{_libdir}/mstflint
%{_libdir}/mstflint/libmtcr_ul.a
%{_includedir}/mstflint
