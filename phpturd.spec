Name:		phpturd
Version:	0.0.2
Release:	1%{?dist}
Summary:	PHP turd interception library
License:	GPLv2+
URL:		https://github.com/unipartdigital/phpturd
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	gcc
BuildRequires:	libselinux-devel
Provides:	libphpturd = %{version}-%{release}

%description
An LD_PRELOAD library that allows for incompetently written PHP code
(such as SuiteCRM) to be forcibly divided into two top-level "turd"
directories: a distribution tree (where permissions should be set as
read-only) and a writable scratch area.

%prep
%autosetup

%build
./autogen.sh
%configure
%make_build

%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la

%files
%doc README.md
%license COPYING
%{_libdir}/libphpturd.so
%{_libdir}/libphpturd.so.*

%changelog
* Fri May 15 2020 Michael Brown <mbrown@fensystems.co.uk> 0.0.2-1
- build: Add missing RPM BuildRequires

* Fri May 15 2020 Michael Brown <mbrown@fensystems.co.uk> 0.0.1-1
- First packaged version
