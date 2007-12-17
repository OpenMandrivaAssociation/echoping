Summary:	TCP "echo" performance test
Name:		echoping
Version:	5.2.0
Release:	%mkrel 2
License:	GPL
Group:		System/Base
URL:		http://echoping.sourceforge.net/
Source0:	ftp://ftp.internatif.org/pub/unix/echoping/echoping-%{version}.tar.bz2
BuildRequires:	openssl-devel
BuildRequires:	libidn-devel
BuildRequires:	libtool
BuildRequires:	autoconf2.5

%description
"echoping" is a small program to test (approximatively) performances of a
remote host by sending it TCP "echo" (or other protocol, such as HTTP)
packets.

%prep

%setup -q

%build

%configure2_5x \
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

%check

# only do this if we have a working network
if ping -c4 www.debian.org >/dev/null 2>&1; then
    make test
else
    echo "Network is not working, no tests will be executed."
fi

%install
rm -rf %{buildroot}

%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog README TODO DETAILS
%{_bindir}/echoping
%{_mandir}/man1/echoping.1*


