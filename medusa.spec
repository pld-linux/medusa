Summary:	Medusa - for quickly search files
Summary(pl):	Medusa - do szybkiego wyszukiwania plików
Name:		medusa
Version:	0.2
Release:	1
License:	GPL
Group:		Libraries
Group(pl):	Biblioteki
Source0:	http://download.eazel.com/source/%{name}-%{version}.tar.gz
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
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Package contains header files.

%description devel -l pl
Pakiet zawiera pliki nag³ówkowe.

%prep
%setup -q

%build
LDFLAGS="-s"; export LDFLAGS
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} \
	DESTDIR=$RPM_BUILD_ROOT \
	install

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
%attr(755,root,root) %{_libdir}/vfs/modules/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_datadir}/medusa

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/medusa-config
%{_includedir}/libmedusa
%attr(755,root,root) %{_libdir}/*.la
%{_libdir}/*.so
