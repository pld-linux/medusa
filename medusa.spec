Summary:	Medusa - for quickly search files
Summary(pl):	Medusa - do szybkiego wyszukiwania plikÛw
Summary(pt_BR):	Medusa: procura e indexaÁ„o de pacotes para uso com o Nautilus
Name:		medusa
Version:	0.5.1
Release:	5
License:	GPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	‚…¬Ã…œ‘≈À…
Group(uk):	‚¶¬Ã¶œ‘≈À…
Source0:	ftp://ftp.gnome.org/pub/GNOME/unstable/sources/medusa/%{name}-%{version}.tar.bz2
Patch0:		%{name}-includes.patch
Patch1:		%{name}-ac_am_fix.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	GConf-devel
BuildRequires:	glib-devel >= 1.2.0
BuildRequires:	gnome-vfs-devel >= 1.0.0
BuildRequires:	gnome-libs-devel >= 1.0.0
BuildRequires:	db1-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sysconfdir	/etc/X11/GNOME

%description
Medusa is software that allows you to quickly search your system for
particular types of files, using an index.

%description -l pl
Medusa jest oprogramowaniem pozwalaj±cym szybko znaleºÊ odpowiednie
typy plikÛw w twoim systemie uøywaj±c indeksu.

%package devel
Summary:	medusa - header files
Summary(pl):	medusa - pliki nag≥Ûwkowe
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}

%description devel
Package contains medusa header files.

%description -l pl devel
Pakiet zawiera pliki nag≥Ûwkowe dla medusy.

%package static
Summary:	Medusa static libraries
Summary(pl):	Biblioteki statyczne medusy
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name}-devel = %{version}

%description static
Medusa static libraries.

%description -l pl static
Biblioteki statyczne medusy.

%prep
%setup -q
%patch0 -p1
#%patch1 -p1

%build
#rm -f missing
cp -f /usr/share/automake/config.* .
#libtoolize -c -f
#aclocal
#autoconf
#automake -a -c
%configure2_13 \
	--with-proc-interrupts \
	--enable-static \
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

gzip -9nf AUTHORS NEWS README index-configuration/medusa-init

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
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
#%{_prefix}/com/medusa
%dir %{_var}/medusa
%{_mandir}/man*/*
%doc *.gz index-configuration/*.gz

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/medusa-config
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/libmedusa

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%{_libdir}/vfs/modules/*.a
