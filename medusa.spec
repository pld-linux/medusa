Summary:	Medusa - for quickly search files
Summary(pl):	Medusa - do szybkiego wyszukiwania plik�w
Name:		medusa
Version:	0.5.0
Release:	1
License:	GPL
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	ftp://ftp.gnome.org/pub/GNOME/unstable/sources/medusa/%{name}-%{version}.tar.gz
BuildRequires:	GConf-devel
BuildRequires:	glib-devel >= 1.2.0
BuildRequires:	gnome-vfs-devel >= 0.4
BuildRequires:	gnome-libs-devel >= 1.0.0
BuildRequires:	db1-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11/GNOME

%description
Medusa is software that allows you to quickly search your system for
particular types of files, using an index.

%description -l pl
Medusa jest oprogramowaniem pozwalaj�cym szybko znale�� odpowiednie
typy plik�w w twoim systemie u�ywaj�c indeksu.

%package devel
Summary:	medusa - header files
Summary(pl):	medusa - pliki nag��wkowe
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Package contains header files.

%description -l pl devel
Pakiet zawiera pliki nag��wkowe.

%package static
Summary:	Medusa staic libraries
Summary(pl):	Biblioteki statyczne medusy
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description static
Medusa staic libraries.

%description -l pl static
Biblioteki statyczne medusy.

%prep
%setup -q

%build
%configure \
	--with-proc-interrupts \
	--enable-static \
	--with-mit-ext \
	--with-xidle-ext \
	--with-sgivc-ext

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install\
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_sysconfdir}/cron.daily	$RPM_BUILD_ROOT/etc
mv $RPM_BUILD_ROOT%{_sysconfdir}/profile.d	$RPM_BUILD_ROOT/etc

gzip -9nf AUTHORS NEWS README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{_sysconfdir}/vfs/modules/*
%dir %{_sysconfdir}/medusa
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/medusa/*
%attr(755,root,root) %{_bindir}/medusa-e*
%attr(755,root,root) %{_bindir}/medusa-i*
%attr(755,root,root) %{_bindir}/medusa-s*
%attr(755,root,root) %{_bindir}/msearch
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_libdir}/vfs/modules/*.so
%attr(755,root,root) %{_libdir}/vfs/modules/*.la
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_prefix}/com/medusa
%dir %{_var}/medusa
%attr(755,root,root) /etc/profile.d/*
%attr(755,root,root) /etc/cron.daily/*
%{_mandir}/man*/*

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
