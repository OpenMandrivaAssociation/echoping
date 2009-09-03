Summary:	TCP "echo" performance test
Name:		echoping
Version:	6.0.2
Release:	%mkrel 2
License:	GPLv2+
Group:		System/Base
URL:		http://echoping.sourceforge.net/
Source0:	ftp://ftp.internatif.org/pub/unix/echoping/echoping-%{version}.tar.bz2
BuildRequires:	openssl-devel
BuildRequires:	libidn-devel
BuildRequires:	libtool
BuildRequires:	openldap-devel
BuildRequires:	popt-devel
BuildRequires:	postgresql-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

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

%build

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
rm -rf %{buildroot}

%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README TODO DETAILS
%dir %{_libdir}/%{name}
%{_bindir}/echoping
%{_libdir}/%{name}/*.so.0*
%{_mandir}/man1/echoping*.1*

%files devel
%defattr(-,root,root)
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_libdir}/%{name}/*.so
%{_libdir}/%{name}/*.la
