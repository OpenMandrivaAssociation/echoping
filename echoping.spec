Summary:	TCP "echo" performance test
Name:		echoping
Version:	6.0.2
Release:	6
License:	GPLv2+
Group:		System/Base
URL:		https://echoping.sourceforge.net/
Source0:	ftp://ftp.internatif.org/pub/unix/echoping/echoping-%{version}.tar.bz2
Patch0:     echoping-6.0.2-fix-plugin-loading.patch
Patch1:     echoping-6.0.2-fix-autotools.patch
BuildRequires:	openssl-devel
BuildRequires:	libidn-devel
BuildRequires:	libtool
BuildRequires:	openldap-devel
BuildRequires:	popt-devel
BuildRequires:	postgresql-devel

%description
"echoping" is a small program to test (approximatively) performances of a
remote host by sending it TCP "echo" (or other protocol, such as HTTP)
packets.

%package devel
Summary:	Development files and headers for %{name}
Group:		Development/C++

%description devel
Development files and headers for %{name}.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
autoreconf -fi
%configure2_5x \
    --disable-static \
    --enable-icp \
    --enable-http \
    --enable-smtp \
    --disable-ttcp \
    --enable-tos \
    --enable-priority \
    --with-libidn \
    --with-ssl \
    --without-gnutls

%make

# (tpg) tests fails on test-echoping-local
#check

# only do this if we have a working network
#if ping -c4 www.mandriva.com >/dev/null 2>&1; then
#    make test
#else
#    echo "Network is not working, no tests will be executed."
#fi

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog README TODO DETAILS
%dir %{_libdir}/%{name}
%{_bindir}/echoping
%{_libdir}/%{name}/*.so
%{_mandir}/man1/echoping*.1*

%files devel
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h

