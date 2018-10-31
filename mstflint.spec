Summary:	Firmware burning and diagnostic tools for Mellanox HCA/NIC cards
Summary(pl.UTF-8):	Narzędzia modyfikujące firmware i diagnostyczne dla kart HCA/NIC Mellanox
Name:		mstflint
Version:	4.10.0
%define	upstream_ver	%{version}-3
Release:	1
License:	BSD or GPL v2
Group:		Networking/Utilities
Source0:	https://github.com/Mellanox/mstflint/releases/download/v%{upstream_ver}/%{name}-%{upstream_ver}.tar.gz
# Source0-md5:	0fd75b78de3fc46d2cf951eead225a5b
Patch0:		openssl-1.1.patch
URL:		https://github.com/Mellanox/mstflint
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
	--enable-cs \
	--enable-fw-mgr \
	--enable-xml2 \
	--enable-openssl
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
%{_sysconfdir}/mstflint/ca-bundle.crt
%attr(755,root,root) %{_bindir}/mstconfig
%attr(755,root,root) %{_bindir}/mstflint
%attr(755,root,root) %{_bindir}/mstmcra
%attr(755,root,root) %{_bindir}/mstmread
%attr(755,root,root) %{_bindir}/mstmtserver
%attr(755,root,root) %{_bindir}/mstmwrite
%attr(755,root,root) %{_bindir}/mstregdump
%attr(755,root,root) %{_bindir}/mstvpd
%attr(755,root,root) %{_bindir}/mstcongestion
%attr(755,root,root) %{_bindir}/mstfwmanager
%attr(755,root,root) %{_bindir}/mstfwreset
%dir %{_libdir}/mstflint
%dir %{_libdir}/mstflint/python_tools
%attr(755,root,root) %{_libdir}/mstflint/python_tools/c_dev_mgt.so
%attr(755,root,root) %{_libdir}/mstflint/python_tools/ccmdif.so
%{_libdir}/mstflint/python_tools/cmdif.py
%attr(755,root,root) %{_libdir}/mstflint/python_tools/cmtcr.so
%{_libdir}/mstflint/python_tools/dev_mgt.py
%dir %{_libdir}/mstflint/python_tools/mstfwreset
%dir %{_libdir}/mstflint/python_tools/mstfwreset/mlxfwresetlib
%{_libdir}/mstflint/python_tools/mstfwreset/mlxfwresetlib/__init__.py
%{_libdir}/mstflint/python_tools/mstfwreset/mlxfwresetlib/logger.py
%{_libdir}/mstflint/python_tools/mstfwreset/mlxfwresetlib/mcra.py
%{_libdir}/mstflint/python_tools/mstfwreset/mlxfwresetlib/mlnx_peripheral_components.py
%{_libdir}/mstflint/python_tools/mstfwreset/mlxfwresetlib/mlxfwreset_mlnxdriver.py
%{_libdir}/mstflint/python_tools/mstfwreset/mlxfwresetlib/mlxfwreset_status_checker.py
%{_libdir}/mstflint/python_tools/mstfwreset/mlxfwresetlib/mlxfwreset_utils.py
%{_libdir}/mstflint/python_tools/mstfwreset/mlxfwresetlib/pci_device.py
%{_libdir}/mstflint/python_tools/mstfwreset/mstfwreset.py
%{_libdir}/mstflint/python_tools/mtcr.py
%{_libdir}/mstflint/python_tools/regaccess.py
%attr(755,root,root) %{_libdir}/mstflint/python_tools/rreg_access.so
%{_libdir}/mstflint/python_tools/tools_version.py
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
%{_libdir}/mstflint/libmtcr_ul.a
%{_includedir}/mstflint
