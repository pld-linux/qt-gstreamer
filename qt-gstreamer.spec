# NOTE: copy package to qt-gstreamer0.10 before updating to 1.0.x (when available)
# TODO: Qt5 packages
Summary:	QtGStreamer - libraries integrating Qt with GStreamer
Summary(pl.UTF-8):	QtGStreamer - biblioteki integrujące Qt z GStreamerem
Name:		qt-gstreamer
Version:	0.10.3
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://gstreamer.freedesktop.org/src/qt-gstreamer/%{name}-%{version}.tar.bz2
# Source0-md5:	1dfbca4ffa924b0896dadb42221600e2
URL:		http://gstreamer.net/
BuildRequires:	OpenGL-devel
BuildRequires:	QtCore-devel >= 4.7
BuildRequires:	QtDeclarative-devel >= 4.7
BuildRequires:	QtGui-devel >= 4.7
BuildRequires:	QtOpenGL-devel >= 4.7
BuildRequires:	QtTest-devel >= 4.7
BuildRequires:	bison
BuildRequires:	boost-devel >= 1.39
BuildRequires:	cmake >= 2.8.9
BuildRequires:	flex
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	gstreamer0.10-devel >= 0.10.33
BuildRequires:	gstreamer0.10-plugins-base-devel >= 0.10.33
BuildRequires:	libstdc++-devel >= 6:4.5
BuildRequires:	pkgconfig
BuildRequires:	qt4-qmake >= 4.7
Requires:	QtCore >= 4.7
Requires:	QtGui >= 4.7
Requires:	QtOpenGL >= 4.7
Requires:	gstreamer0.10 >= 0.10.33
Requires:	gstreamer0.10-plugins-base >= 0.10.33
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QtGStreamer is a set of libraries and plugins providing C++ bindings
for GStreamer with a Qt-style API plus some helper classes for
integrating GStreamer better in Qt applications.

Currently, it consists of the following parts:
 * QtGLib - library providing C++/Qt bindings for parts of the GLib
   and GObject APIs, a base on which QtGStreamer is built.
 * QtGStreamer - library providing C++/Qt bindings for GStreamer
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
integracji GStreamera w aplikacjach Qt.

Obecnie zawiera następujące części:
 - QtGLib - biblioteka z wiązaniami C++/Qt dla części API bibliotek
   GLib i GObject; w oparciu o nią zbudowany jest QtGStreamer
 - QtGStreamer - biblioteka z wiązaniami C++/Qt do GStreamera
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
Requires:	gstreamer0.10-devel >= 0.10.33
Requires:	gstreamer0.10-plugins-base-devel >= 0.10.33

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

%prep
%setup -q

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_CXX_FLAGS_RELEASE="-DNDEBUG" \
	-DQTGSTREAMER_EXAMPLES=OFF \
	-DQT_QMAKE_EXECUTABLE=/usr/bin/qmake-qt4

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_libdir}/libQtGLib-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQtGLib-2.0.so.0
%attr(755,root,root) %{_libdir}/libQtGStreamer-0.10.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQtGStreamer-0.10.so.0
%attr(755,root,root) %{_libdir}/libQtGStreamerUi-0.10.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQtGStreamerUi-0.10.so.0
%attr(755,root,root) %{_libdir}/libQtGStreamerUtils-0.10.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQtGStreamerUtils-0.10.so.0
%attr(755,root,root) %{_libdir}/gstreamer-0.10/libgstqtvideosink.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQtGLib-2.0.so
%attr(755,root,root) %{_libdir}/libQtGStreamer-0.10.so
%attr(755,root,root) %{_libdir}/libQtGStreamerUi-0.10.so
%attr(755,root,root) %{_libdir}/libQtGStreamerUtils-0.10.so
%{_includedir}/QtGStreamer
%{_pkgconfigdir}/QtGLib-2.0.pc
%{_pkgconfigdir}/QtGStreamer-0.10.pc
%{_pkgconfigdir}/QtGStreamerUi-0.10.pc
%{_pkgconfigdir}/QtGStreamerUtils-0.10.pc
%{_libdir}/cmake/QtGStreamer

%files -n QtDeclarative-plugin-gstreamer
%defattr(644,root,root,755)
%dir %{_libdir}/qt4/imports/QtGStreamer
%attr(755,root,root) %{_libdir}/qt4/imports/QtGStreamer/libQtGStreamerQuick1.so
%{_libdir}/qt4/imports/QtGStreamer/qmldir
