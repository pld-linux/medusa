Summary:	Medusa - for quickly search files
Summary(pl):	Medusa - do szybkiego wyszukiwania plików
Summary(pt_BR):	Medusa: procura e indexação de pacotes para uso com o Nautilus
Name:		medusa
Version:	0.5.1
Release:	8
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/medusa/0.5/%{name}-%{version}.tar.bz2
# Source0-md5:	5f0b6ca0db367eda482760c922051e62
Patch0:		%{name}-includes.patch
Patch1:		%{name}-missing_AM_PATH_GNOME.patch
Patch2:		%{name}-no_db1_ac_fix.patch
Patch3:		%{name}-am_fix.patch
BuildRequires:	GConf-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	db3-devel
BuildRequires:	glib-devel >= 1.2.0
BuildRequires:	gnome-libs-devel >= 1.0.0
BuildRequires:	gnome-vfs-devel >= 1.0.0
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libmedusa0

%define		_sysconfdir	/etc/X11/GNOME
%define		_localstatedir	/var/lib

%description
Medusa is software that allows you to quickly search your system for
particular types of files, using an index.

%description -l pl
Medusa jest oprogramowaniem pozwalaj±cym szybko znale¼æ odpowiednie
typy plików w twoim systemie u¿ywaj±c indeksu.

%package devel
Summary:	medusa - header files
Summary(pl):	medusa - pliki nag³ówkowe
Group:		Development/Libraries
Requires:	%{name} = %{version}
Obsoletes:	libmedusa0-devel

%description devel
Package contains medusa header files.

%description devel -l pl
Pakiet zawiera pliki nag³ówkowe dla medusy.

%package static
Summary:	Medusa static libraries
Summary(pl):	Biblioteki statyczne medusy
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Medusa static libraries.

%description static -l pl
Biblioteki statyczne medusy.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
rm -f missing
libtoolize -c -f
%{__aclocal} -I %{_aclocaldir}/gnome
%{__autoconf}
%{__automake}
%configure \
	--with-proc-interrupts \
	--enable-static \
	--disable-prefer-db1 \
	--with-mit-ext \
	--with-xidle-ext \
	--with-sgivc-ext

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	medusacronconfdir=/etc/cron.daily \
	medusaidledconfdir=/etc/profile.d

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README index-configuration/medusa-init
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/medusa/*
%attr(755,root,root) /etc/profile.d/*
%attr(755,root,root) /etc/cron.daily/*
%dir %{_sysconfdir}/medusa
%{_sysconfdir}/vfs/modules/*
#%attr(755,root,root) %{_bindir}/medusa-e*
%attr(755,root,root) %{_bindir}/medusa-i*
%attr(755,root,root) %{_bindir}/medusa-s*
%attr(755,root,root) %{_bindir}/msearch
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_libdir}/vfs/modules/*.so
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_localstatedir}/medusa
%{_mandir}/man*/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/medusa-config
%{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/libmedusa

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%{_libdir}/vfs/modules/*.a
