Summary:	Firmware burning and diagnostic tools for Mellanox HCA/NIC cards
Summary(pl.UTF-8):	Narzędzia modyfikujące firmware i diagnostyczne dla kart HCA/NIC Mellanox
Name:		mstflint
Version:	3.5.0
Release:	1
License:	BSD or GPL v2
Group:		Networking/Utilities
Source0:	http://www.openfabrics.org/downloads/mstflint/%{name}-%{version}.tar.gz
# Source0-md5:	00c3ea4ea8c99f89a0733a72fcb14fb9
Patch0:		%{name}-format.patch
URL:		http://www.openfabrics.org/
BuildRequires:	libstdc++-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Firmware burning and diagnostic tools for Mellanox HCA/NIC cards

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
%configure
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
%attr(755,root,root) %{_bindir}/mstflint
%attr(755,root,root) %{_bindir}/mstmcra
%attr(755,root,root) %{_bindir}/mstmread
%attr(755,root,root) %{_bindir}/mstmtserver
%attr(755,root,root) %{_bindir}/mstmwrite
%attr(755,root,root) %{_bindir}/mstregdump
%attr(755,root,root) %{_bindir}/mstvpd
%{_datadir}/mstflint
%{_mandir}/man1/mstflint.1*

%files devel
%defattr(644,root,root,755)
%{_libdir}/libmtcr_ul.a
%{_includedir}/mtcr_ul
