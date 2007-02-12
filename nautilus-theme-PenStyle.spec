Summary:	Pen Style theme
Summary(pl.UTF-8):   Motyw Pen Style
Name:		nautilus-theme-PenStyle
Version:	1.0
Release:	1
License:	Free
Group:		X11/Amusements
Source0:	http://www.lucidus.btinternet.co.uk/nautilus/PenStyle.tar.gz
# Source0-md5:	e1bebf44f2e0e3dafbbb197efd6442a4
URL:		http://sunshineinabag.co.uk/
Requires:	nautilus
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch


%description
Pen Style theme. CPU intensive (vector icons).

%description -l pl.UTF-8
Motyw Pen Style (rysowany długopisem). Zjada dużo czasu procesora z
powodu wektorowych ikonek.

%prep
%setup -q -n PenStyle

%build
rm -rf .thumbnails .xvpics backgrounds/.xvpics patterns/.xvpics throbber/.xvpics

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pixmapsdir}/nautilus/PenStyle

mv * $RPM_BUILD_ROOT%{_pixmapsdir}/nautilus/PenStyle

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_pixmapsdir}/nautilus/PenStyle
