Summary:	Medusa - for quickly search files
Summary(pl):	Medusa - do szybkiego wyszukiwania plików
Name:		medusa
Version:	0.2
Release:	1
License:	GPL
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	ftp://ftp.gnome.org/pub/GNOME/unstable/sources/medusa/%{name}-%{version}.tar.gz
BuildRequires:	glib-devel
BuildRequires:	oaf-devel
BuildRequires:	GConf-devel
Requires:	gnome-vfs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

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
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Package contains header files.

%description -l pl devel
Pakiet zawiera pliki nag³ówkowe.

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
	--enable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install\
	DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/{lib*.so.*.*,vfs/modules/*.so}

gzip -9nf AUTHORS NEWS README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{_sysconfdir}/vfs
%attr(755,root,root) %{_bindir}/medusa-indexd
%attr(755,root,root) %{_bindir}/medusa-searchd
%attr(755,root,root) %{_bindir}/msearch
%attr(755,root,root) %{_libdir}/vfs/modules/*.so
%attr(755,root,root) %{_libdir}/vfs/modules/*.la
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_datadir}/medusa

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
