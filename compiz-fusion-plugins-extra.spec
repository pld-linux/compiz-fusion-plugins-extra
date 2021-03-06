%define	pkgname	compiz-plugins-extra
Summary:	Extra Compiz Fusion plugins
Summary(pl.UTF-8):	Dodatkowe wtyczki Compiz Fusion
Name:		compiz-fusion-plugins-extra
Version:	0.8.6
Release:	2
License:	GPL v2+
Group:		X11
Source0:	http://releases.compiz.org/%{version}/%{pkgname}-%{version}.tar.bz2
# Source0-md5:	fdeec3e437e70d7f68900c031f3165d5
Source1:	compizcap.png
# Source1-md5:	9e846f6c3bc6c7e4d02c252306ada136
Source2:	fusioncap.png
# Source2-md5:	73ba92ba4b139f6d68cdf4669868ff85
Source3:	splash_background.png
# Source3-md5:	d315d5d5e994e61543372ff54c60db62
Source4:	splash_logo.png
# Source4-md5:	224c6427e261a4b5497586d110ec1e93
Patch0:		%{name}-libnotify.patch
URL:		http://www.compiz.org/
BuildRequires:	GConf2-devel
BuildRequires:	OpenGL-devel
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.9
BuildRequires:	cairo-devel >= 1.0
# No current version, take last one:
#BuildRequires:	compiz-bcop >= %{version}
BuildRequires:	compiz-bcop >= 0.8.4
BuildRequires:	compiz-devel >= %{version}
BuildRequires:	compiz-fusion-plugins-main-devel >= %{version}
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libnotify-devel
BuildRequires:	libtool
BuildRequires:	pango-devel >= 1:1.10.0
BuildRequires:	pkgconfig
Requires:	compiz >= %{version}
Obsoletes:	beryl-plugins
Obsoletes:	beryl-plugins-unsupported
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Addhelper: Darkens unfocused windows so the user can concentrate on
    the focused window.
Bench: Displays the current frames per second as a simple benchmark.
Crashhandler: Creates a backtrace of a Compiz crash and is able to
    start an alternative window manager.
Cubecaps: Displays top and bottom caps on Compiz Cube.
Cubereflex: Adds a reflective ground to the Compiz Cube plugin.
ExtraWM: Adds additional window manager actions to Compiz.
Fadedesktop: Fades windows out to display the desktop background.
Firepaint: Draw with fire on the screen.
Gears: Renders the famous "glxgears" gears inside of the transparent
    cube.
Goto-Viewport: Switches to a given viewport by pressing a keybinding
    and the viewport number.
Group: Enables the grouping of windows to resize and move them, and
    the tabbing of several windows together.
Motion blur (mblur): Creates a motion blur for different screen
    animations.
Reflex: Draws a reflection behind transparent areas of a window.
Scalefilter: Provides a way to filter and select windows by title
    while using the Compiz Scale plugin.
Showdesktop: Slides all windows toward the edges of the screen to
    expose the desktop.
Splash: Displays a simple animated splash image.
Trailfocus: Gradually dims windows as other windows gain focus.
Widget: Features a widget layer similar to OS X Dashboard.

%description -l pl.UTF-8
Addhelper: Przyciemnia nieaktywne okna umożliwiając użytkownikowi
    skupienie się na aktywnym oknie.
Bench: Wyświetla liczbę klatek na sekundę.
Crashhandler: Tworzy backtrace po wysypaniu się Compiza i jest w
    stanie włączyć alternatywny menedżer okien.
Cubecaps: Wyświetla górną i dolną powierzchnię na kostce.
Cubereflex: Dodaje odbijającą światło powierzchnię pod kostką.
ExtraWM: Dodaje dodatkowe akcje menedżera okien do Compiza.
Fadedesktop: Okna zanikają, by pokazać pulpit.
Firepaint: Rysowanie oknem na ekranie.
Gears: Renderuje zębatki z "glxgears" wewnątrz przezroczystej kostki.
Goto-Viewport: Przełącza na dany viewport po naciśnięciu skrótu
    klawiszowego.
Group: Umożliwia grupowanie okien w celu zmiany rozmiaru i
    przesuwania, jak również zgrupowanie okien za pomocą zakładek.
Motion blur (mblur): Umożliwia rozmycie ekranu w czasie animacji
    ekranowych.
Reflex: Rysuje odbicie pod przezroczystymi obszarami okna.
Scalefilter: Umożliwia filtrowanie i wybór okien po nazwie podczas
    używania wtyczki Scale.
Showdesktop: Usuwa okna w kąty ekranu by odsłonić pulpit.
Splash: Wyświetla prosty animowany ekran powitalny.
Trailfocus: Powili przyciemnia nieaktywne okna.
Widget: Tworzy warstwę z widgetami, podobną do Dashboarda w OS X.

%package devel
Summary:	Header file for animation addon plugin
Summary(pl.UTF-8):	Plik nagłówkowy wtyczki animation addon
Group:		X11/Development/Libraries

%description devel
Header file for animation addon plugin.

%description devel -l pl.UTF-8
Plik nagłówkowy wtyczki animation addon.

%prep
%setup -q -n %{pkgname}-%{version}
%patch0 -p1

%build
%{__glib_gettextize}
%{__intltoolize} --automake
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/compiz/*.la

install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/compiz
install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/compiz
install %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/compiz
install %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/compiz

%find_lang %{pkgname}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{pkgname}.lang
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_libdir}/compiz/*.so
%{_datadir}/compiz/*.xml
%{_datadir}/compiz/*.png

%files devel
%defattr(644,root,root,755)
%{_includedir}/compiz/compiz-animationaddon.h
%{_pkgconfigdir}/compiz-animationaddon.pc
