Summary:	Firmware burning and diagnostic tools for Mellanox HCA/NIC cards
Summary(pl.UTF-8):	Narzędzia modyfikujące firmware i diagnostyczne dla kart HCA/NIC Mellanox
Name:		mstflint
Version:	4.4.0
Release:	2
License:	BSD or GPL v2
Group:		Networking/Utilities
Source0:	http://www.openfabrics.org/downloads/mstflint/%{name}-%{version}.tar.gz
# Source0-md5:	8846152be0581c76396e60e94e953c59
Patch0:		%{name}-types.patch
URL:		http://www.openfabrics.org/
BuildRequires:	libibmad-devel
BuildRequires:	libstdc++-devel
BuildRequires:	openssl-devel
BuildRequires:	zlib-devel
# see common/compatibility.h
ExclusiveArch:	%{ix86} %{x8664} x32 aarch64 ia64 ppc ppc64
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
%patch0 -p1

%build
%configure \
	--enable-cs
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README
%attr(755,root,root) %{_bindir}/hca_self_test.ofed
%attr(755,root,root) %{_bindir}/mstconfig
%attr(755,root,root) %{_bindir}/mstflint
%attr(755,root,root) %{_bindir}/mstmcra
%attr(755,root,root) %{_bindir}/mstmread
%attr(755,root,root) %{_bindir}/mstmtserver
%attr(755,root,root) %{_bindir}/mstmwrite
%attr(755,root,root) %{_bindir}/mstregdump
%attr(755,root,root) %{_bindir}/mstvpd
%{_datadir}/mstflint
%{_mandir}/man1/mstconfig.1*
%{_mandir}/man1/mstflint.1*
%{_mandir}/man1/mstmcra.1*
%{_mandir}/man1/mstmread.1*
%{_mandir}/man1/mstmtserver.1*
%{_mandir}/man1/mstmwrite.1*
%{_mandir}/man1/mstregdump.1*
%{_mandir}/man1/mstvpd.1*

%files devel
%defattr(644,root,root,755)
%dir %{_libdir}/mstflint
%{_libdir}/mstflint/libmtcr_ul.a
%{_includedir}/mstflint
