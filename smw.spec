#
# remember sources are here : svn://svn.72dpiarmy.com/smw
# remember to "touch" every file in sources before archive in file (year 1970)
#
Summary:	Super Mario War - a Super Mario multiplayer game
Summary(pl.UTF-8):	Super Mario War - gra Super Mario dla wielu graczy
Name:		smw
Version:	1.7
Release:	4
License:	GPL
Group:		X11/Applications/Games
Source0:	http://starowa.one.pl/~uzi/pld/%{name}-%{version}.tar.gz
# Source0-md5:	32d287c39ff190936b343f6a6f51fe14
Source1:	%{name}.desktop
Source2:	%{name}.png
Source3:	%{name}-leveleditor.desktop
Source4:	%{name}-leveleditor.png
Patch0:		%{name}-gcc44.patch
Patch1:		%{name}-libpng15.patch
URL:		http://smw.72dpiarmy.com/
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	SDL_image-devel >= 1.2.0
BuildRequires:	SDL_mixer-devel >= 1.2.0
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Super Mario War is a Super Mario multiplayer game.

%description -l pl.UTF-8
Super Mario War to gra Super Mario dla wielu graczy.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

%build
chmod +x ./configure
%configure
%{__make} \
	CC="%{__cc}" \
	CXX="%{__cxx}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE3} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE4} $RPM_BUILD_ROOT%{_pixmapsdir}

export DESTDIR=$RPM_BUILD_ROOT
%{__make} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc todo.txt README.txt WHATSNEW.txt
%attr(755,root,root) %{_bindir}/%{name}*
%{_datadir}/%{name}
%{_pixmapsdir}/%{name}.png
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}-leveleditor.png
%{_desktopdir}/%{name}-leveleditor.desktop
