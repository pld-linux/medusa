%define	snap	20040228
Summary:	Medusa - for quickly search files
Summary(pl):	Medusa - do szybkiego wyszukiwania plików
Summary(pt_BR):	Medusa: procura e indexação de pacotes para uso com o Nautilus
Name:		medusa
Version:	0.6.1
Release:	0.%{snap}.1
License:	GPL
Group:		Libraries
Source0:	%{name}-%{version}-%{snap}.tar.bz2
# Source0-md5:	6fd8cd94afd7e3343ae0198e1444de31
#Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/medusa/0.5/%{name}-%{version}.tar.bz2
Patch0:		%{name}-am_fix.patch
Patch1:		%{name}-locale-names.patch
BuildRequires:	GConf2-devel >= 2.0.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-common >= 2.8.0
BuildRequires:	gnome-vfs2-devel >= 2.0.0
BuildRequires:	intltool >= 0.28
BuildRequires:	libglade2-devel >= 2.0.1
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.2.8
Requires(post):	GConf2
Obsoletes:	libmedusa0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
Requires:	%{name} = %{version}-%{release}
Obsoletes:	libmedusa0-devel

%description devel
Package contains medusa header files.

%description devel -l pl
Pakiet zawiera pliki nag³ówkowe dla medusy.

%package static
Summary:	Medusa static libraries
Summary(pl):	Biblioteki statyczne medusy
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Medusa static libraries.

%description static -l pl
Biblioteki statyczne medusy.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

mv po/{no,nb}.po

%build
rm -f missing
cp /usr/share/automake/mkinstalldirs .
glib-gettextize --copy --force
%{__libtoolize}
intltoolize --copy --force
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--enable-static \
	--disable-schemas-install \
	--with-mit-ext \
	--with-xidle-ext \
	--with-sgivc-ext \
	--with-proc-interrupts

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

rm -f $RPM_BUILD_ROOT%{_libdir}/gnome-vfs-2.0/modules/*.{la,a}

%find_lang %{name}-2.0

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install

%files -f %{name}-2.0.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog DEBUGGING NEWS README THANKS TODO
%doc doc/{how_to_use_msearch,indexing_methodology,ui.txt}
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/gnome-vfs-2.0/modules/lib*.so
%{_sysconfdir}/gconf/schemas/*
%{_sysconfdir}/gnome-vfs-2.0/modules/*
%{_datadir}/%{name}-2.0
%{_mandir}/man*/*

%files devel
%defattr(644,root,root,755)
%doc doc/{arch.txt,flags,search*,state_of_queries,tokenizer}
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/libmedusa-2
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
