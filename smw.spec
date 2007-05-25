#
# TODO: 
# - icon in games menu
# - polish desc.
#
Summary:	Super Mario War is a Super Mario multiplayer game.
Name:		smw
Version:	1.7
Release:	0.1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://starowa.one.pl/~uzi/%{name}-%{version}.tar.gz
# Source0-md5:	84d1a4d76f6205aab32f83b8e25b7c20
#Source1:	%{name}.desktop
#Source2:	%{name}.png
#Source3:	%{name}-leveleditor.desktop
#Source4:	%{name}-leveleditor.png
URL:		http://smw.72dpiarmy.com/
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	SDL_image-devel >= 1.2.0
BuildRequires:	SDL_mixer-devel >= 1.2.0
BuildRequires:	libpng-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Super Mario War is a Super Mario multiplayer game.

#% description -l pl.UTF-8

%prep
%setup -q -n %{name}

%build
chmod +x ./configure
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}
#install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
#install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
#install %{SOURCE3} $RPM_BUILD_ROOT%{_desktopdir}
#install %{SOURCE4} $RPM_BUILD_ROOT%{_pixmapsdir}

export DESTDIR=$RPM_BUILD_ROOT
make install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc todo.txt README.txt WHATSNEW.txt
%attr(755,root,root) %{_bindir}/%{name}*
%{_datadir}/%{name}
#%{_pixmapsdir}/%{name}.png
#%{_desktopdir}/%{name}.desktop
#%{_pixmapsdir}/%{name}-leveleditor.png
#%{_desktopdir}/%{name}-leveleditor.desktop
