# TODO: -devel and Qt*Declarative-* packages conflict with gstreamer0.10 equivalents
#
# Conditional build:
%bcond_without	qt4	# Qt 4 libraries
%bcond_without	qt5	# Qt 5 libraries
#
Summary:	QtGStreamer - libraries integrating Qt 4 with GStreamer
Summary(pl.UTF-8):	QtGStreamer - biblioteki integrujące Qt 4 z GStreamerem
Name:		qt-gstreamer
Version:	1.2.0
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://gstreamer.freedesktop.org/src/qt-gstreamer/%{name}-%{version}.tar.xz
# Source0-md5:	fd794045a828c184acc1794b08a463fd
Patch0:		boost-moc.patch
URL:		http://gstreamer.net/
BuildRequires:	OpenGL-devel
BuildRequires:	bison
BuildRequires:	boost-devel >= 1.39
BuildRequires:	cmake >= 2.8.9
BuildRequires:	doxygen
BuildRequires:	flex
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	gstreamer-devel >= 1.0.0
BuildRequires:	gstreamer-plugins-base-devel >= 1.0.0
BuildRequires:	libstdc++-devel >= 6:4.5
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
%if %{with qt4}
BuildRequires:	QtCore-devel >= 4.7
BuildRequires:	QtDeclarative-devel >= 4.7
BuildRequires:	QtGui-devel >= 4.7
BuildRequires:	QtOpenGL-devel >= 4.7
BuildRequires:	QtTest-devel >= 4.7
BuildRequires:	qt4-qmake >= 4.7
%endif
%if %{with qt5}
BuildRequires:	Qt5Core-devel >= 5.0.0
BuildRequires:	Qt5Declarative-devel >= 5.0.0
BuildRequires:	Qt5Gui-devel >= 5.0.0
BuildRequires:	Qt5OpenGL-devel >= 5.0.0
BuildRequires:	Qt5Qml-devel >= 5.0.0
BuildRequires:	Qt5Quick-devel >= 5.0.0
BuildRequires:	Qt5Widgets-devel >= 5.0.0
BuildRequires:	Qt5Test-devel >= 5.0.0
BuildRequires:	qt5-qmake >= 5.0.0
%endif
Requires:	QtCore >= 4.7
Requires:	QtGui >= 4.7
Requires:	QtOpenGL >= 4.7
Requires:	gstreamer >= 1.0.0
Requires:	gstreamer-plugins-base >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QtGStreamer is a set of libraries and plugins providing C++ bindings
for GStreamer with a Qt-style API plus some helper classes for
integrating GStreamer better in Qt 4 applications.

Currently, it consists of the following parts:
 * QtGLib - library providing C++/Qt 4 bindings for parts of the GLib
   and GObject APIs, a base on which QtGStreamer is built.
 * QtGStreamer - library providing C++/Qt 4 bindings for GStreamer
 * QtGStreamerUi - library providing integration with QtGui;
   currently, it only provides a video widget that embeds GStreamer's
   video sinks.
 * QtGStreamerUtils - library providing some high level utility
   classes.

In addition, it provides a "qwidgetvideosink" GStreamer element, an
video sink element that can draw directly on QWidgets using QPainter.

%description -l pl.UTF-8
QtGStreamer to zestaw bibliotek i wtyczek z wiązaniami C++ do
GStreamera o API w stylu Qt oraz klasami pomocniczymi dla lepszej
integracji GStreamera w aplikacjach Qt 4.

Obecnie zawiera następujące części:
 - QtGLib - biblioteka z wiązaniami C++/Qt 4 dla części API bibliotek
   GLib i GObject; w oparciu o nią zbudowany jest QtGStreamer
 - QtGStreamer - biblioteka z wiązaniami C++/Qt 4 do GStreamera
 - QtGStreamerUi - biblioteka integrująca z QtGui; obecnie zawiera
   tylko widget wideo osadzający wyjście obrazu (videosink) GStremera.
 - QtGStreamerUtils - biblioteka udostępniająca klasy narzędziowe
   wysokiego poziomu.

Ponadto pakiet udostępnia element GStreamera "qwidgetvideosink" -
element wyjściowy obrazu rysujący bezpośrednio na QWidgetach przy
użyciu QPaintera.

%package devel
Summary:	Header files for QtGStreamer libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek QtGStreamer
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	QtCore-devel >= 4.7
Requires:	QtGui-devel >= 4.7
Requires:	gstreamer-devel >= 1.0.0
Requires:	gstreamer-plugins-base-devel >= 1.0.0

%description devel
Header files for QtGStreamer libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek QtGStreamer.

%package -n QtDeclarative-plugin-gstreamer
Summary:	Qt GStreamer plugin for QtDeclarative
Summary(pl.UTF-8):	Wtyczka Qt GStreamer dla QtDeclarative
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	QtDeclarative >= 4.7

%description -n QtDeclarative-plugin-gstreamer
Qt GStreamer plugin for QtDeclarative.

%description -n QtDeclarative-plugin-gstreamer -l pl.UTF-8
Wtyczka Qt GStreamer dla QtDeclarative.

%package -n qt5-gstreamer
Summary:	Qt5GStreamer - libraries integrating Qt 5 with GStreamer
Summary(pl.UTF-8):	Qt5GStreamer - biblioteki integrujące Qt 5 z GStreamerem
Group:		Libraries
Requires:	Qt5Core >= 5.0.0
Requires:	Qt5Gui >= 5.0.0
Requires:	Qt5OpenGL >= 5.0.0
Requires:	Qt5Quick >= 5.0.0
Requires:	Qt5Widgets >= 5.0.0
Requires:	gstreamer >= 1.0.0
Requires:	gstreamer-plugins-base >= 1.0.0

%description -n qt5-gstreamer
Qt5GStreamer is a set of libraries and plugins providing C++ bindings
for GStreamer with a Qt-style API plus some helper classes for
integrating GStreamer better in Qt 5 applications.

Currently, it consists of the following parts:
 * Qt5GLib - library providing C++/Qt 5 bindings for parts of the GLib
   and GObject APIs, a base on which Qt5GStreamer is built.
 * Qt5GStreamer - library providing C++/Qt 5 bindings for GStreamer
 * Qt5GStreamerUi - library providing integration with Qt5Gui;
   currently, it only provides a video widget that embeds GStreamer's
   video sinks.
 * Qt5GStreamerUtils - library providing some high level utility
   classes.

In addition, it provides a "qwidgetvideosink" GStreamer element, an
video sink element that can draw directly on QWidgets using QPainter.

%description -n qt5-gstreamer -l pl.UTF-8
Qt5GStreamer to zestaw bibliotek i wtyczek z wiązaniami C++ do
GStreamera o API w stylu Qt oraz klasami pomocniczymi dla lepszej
integracji GStreamera w aplikacjach Qt 5.

Obecnie zawiera następujące części:
 - Qt5GLib - biblioteka z wiązaniami C++/Qt 5 dla części API bibliotek
   GLib i GObject; w oparciu o nią zbudowany jest QtGStreamer
 - Qt5GStreamer - biblioteka z wiązaniami C++/Qt 5 do GStreamera
 - Qt5GStreamerUi - biblioteka integrująca z Qt5Gui; obecnie zawiera
   tylko widget wideo osadzający wyjście obrazu (videosink) GStremera.
 - QtGStreamerUtils - biblioteka udostępniająca klasy narzędziowe
   wysokiego poziomu.

Ponadto pakiet udostępnia element GStreamera "qwidgetvideosink" -
element wyjściowy obrazu rysujący bezpośrednio na QWidgetach przy
użyciu QPaintera.

%package -n qt5-gstreamer-devel
Summary:	Header files for Qt5GStreamer libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek QtGStreamer
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt5Core-devel >= 5.0.0
Requires:	Qt5Gui-devel >= 5.0.0
Requires:	Qt5Quick-devel >= 5.0.0
Requires:	Qt5Widgets-devel >= 5.0.0
Requires:	gstreamer-devel >= 1.0.0
Requires:	gstreamer-plugins-base-devel >= 1.0.0

%description -n qt5-gstreamer-devel
Header files for Qt5GStreamer libraries.

%description -n qt5-gstreamer-devel -l pl.UTF-8
Pliki nagłówkowe bibliotek Qt5GStreamer.

%package -n Qt5Declarative-plugin-gstreamer
Summary:	Qt GStreamer plugin for Qt5Declarative (Quick1)
Summary(pl.UTF-8):	Wtyczka Qt GStreamer dla Qt5Declarative (Quick1)
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt5Declarative >= 5.0.0

%description -n Qt5Declarative-plugin-gstreamer
Qt GStreamer plugin for Qt5Declarative (Quick1).

%description -n Qt5Declarative-plugin-gstreamer -l pl.UTF-8
Wtyczka Qt GStreamer dla Qt5Declarative (Quick1).

%package -n Qt5Qml-plugin-gstreamer
Summary:	Qt GStreamer plugin for Qt5Qml (Quick2)
Summary(pl.UTF-8):	Wtyczka Qt GStreamer dla Qt5Qml (Quick2)
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt5Qml >= 5.0.0
Requires:	Qt5Quick >= 5.0.0

%description -n Qt5Qml-plugin-gstreamer
Qt GStreamer plugin for Qt5Qml (Quick2).

%description -n Qt5Qml-plugin-gstreamer -l pl.UTF-8
Wtyczka Qt GStreamer dla Qt5Qml (Quick2).

%prep
%setup -q
%patch0 -p1

%build
%if %{with qt4}
install -d build-qt4
cd build-qt4
%cmake .. \
	-DCMAKE_CXX_FLAGS_RELEASE="-DNDEBUG" \
	-DQTGSTREAMER_EXAMPLES=OFF \
	-DQT_QMAKE_EXECUTABLE=/usr/bin/qmake-qt4
%{__make}
cd ..
%endif

%if %{with qt5}
install -d build-qt5
cd build-qt5
%cmake .. \
	-DCMAKE_CXX_FLAGS_RELEASE="-DNDEBUG" \
	-DQTGSTREAMER_EXAMPLES=OFF \
	-DQT_QMAKE_EXECUTABLE=/usr/bin/qmake-qt5 \
	-DQT_VERSION=5
%{__make}
cd ..
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with qt4}
%{__make} -C build-qt4 install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%if %{with qt5}
%{__make} -C build-qt5 install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	-n qt5-gstreamer -p /sbin/ldconfig
%postun	-n qt5-gstreamer -p /sbin/ldconfig

%if %{with qt4}
%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_libdir}/libQtGLib-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQtGLib-2.0.so.0
%attr(755,root,root) %{_libdir}/libQtGStreamer-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQtGStreamer-1.0.so.0
%attr(755,root,root) %{_libdir}/libQtGStreamerUi-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQtGStreamerUi-1.0.so.0
%attr(755,root,root) %{_libdir}/libQtGStreamerUtils-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQtGStreamerUtils-1.0.so.0
%attr(755,root,root) %{_libdir}/gstreamer-1.0/libgstqtvideosink.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQtGLib-2.0.so
%attr(755,root,root) %{_libdir}/libQtGStreamer-1.0.so
%attr(755,root,root) %{_libdir}/libQtGStreamerUi-1.0.so
%attr(755,root,root) %{_libdir}/libQtGStreamerUtils-1.0.so
%{_includedir}/QtGStreamer
%{_pkgconfigdir}/QtGLib-2.0.pc
%{_pkgconfigdir}/QtGStreamer-1.0.pc
%{_pkgconfigdir}/QtGStreamerUi-1.0.pc
%{_pkgconfigdir}/QtGStreamerUtils-1.0.pc
%{_libdir}/cmake/QtGStreamer

%files -n QtDeclarative-plugin-gstreamer
%defattr(644,root,root,755)
%dir %{_libdir}/qt4/imports/QtGStreamer
%attr(755,root,root) %{_libdir}/qt4/imports/QtGStreamer/libQtGStreamerQuick1.so
%{_libdir}/qt4/imports/QtGStreamer/qmldir
%endif

%if %{with qt5}
%files -n qt5-gstreamer
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_libdir}/libQt5GLib-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5GLib-2.0.so.0
%attr(755,root,root) %{_libdir}/libQt5GStreamer-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5GStreamer-1.0.so.0
%attr(755,root,root) %{_libdir}/libQt5GStreamerQuick-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5GStreamerQuick-1.0.so.0
%attr(755,root,root) %{_libdir}/libQt5GStreamerUi-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5GStreamerUi-1.0.so.0
%attr(755,root,root) %{_libdir}/libQt5GStreamerUtils-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5GStreamerUtils-1.0.so.0
%attr(755,root,root) %{_libdir}/gstreamer-1.0/libgstqt5videosink.so

%files -n qt5-gstreamer-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5GLib-2.0.so
%attr(755,root,root) %{_libdir}/libQt5GStreamer-1.0.so
%attr(755,root,root) %{_libdir}/libQt5GStreamerQuick-1.0.so
%attr(755,root,root) %{_libdir}/libQt5GStreamerUi-1.0.so
%attr(755,root,root) %{_libdir}/libQt5GStreamerUtils-1.0.so
%{_includedir}/Qt5GStreamer
%{_pkgconfigdir}/Qt5GLib-2.0.pc
%{_pkgconfigdir}/Qt5GStreamer-1.0.pc
%{_pkgconfigdir}/Qt5GStreamerQuick-1.0.pc
%{_pkgconfigdir}/Qt5GStreamerUi-1.0.pc
%{_pkgconfigdir}/Qt5GStreamerUtils-1.0.pc
%{_libdir}/cmake/Qt5GStreamer

%files -n Qt5Declarative-plugin-gstreamer
%defattr(644,root,root,755)
%dir %{_libdir}/qt5/imports/QtGStreamer
%attr(755,root,root) %{_libdir}/qt5/imports/QtGStreamer/libQtGStreamerQuick1.so
%{_libdir}/qt5/imports/QtGStreamer/qmldir

%files -n Qt5Qml-plugin-gstreamer
%defattr(644,root,root,755)
%dir %{_libdir}/qt5/qml/QtGStreamer
%attr(755,root,root) %{_libdir}/qt5/qml/QtGStreamer/libQtGStreamerQuick2.so
%{_libdir}/qt5/qml/QtGStreamer/qmldir
%endif
