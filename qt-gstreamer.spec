Summary:	QtGStreamer - libraries integrating Qt with GStreamer
Summary(pl.UTF-8):	QtGStreamer - biblioteki integrujące Qt z GStreamerem
Name:		qt-gstreamer
Version:	0.10.0.2
Release:	1
License:	LGPL v2+
Group:		Libraries
#Source0:	http://gstreamer.freedesktop.org/src/qt-gstreamer/%{name}-%{version}.tar.bz2
Source0:	http://gstreamer.freedesktop.org/src/qt-gstreamer/pre/%{name}-%{version}.tar.bz2
# Source0-md5:	55bd3c5e076b71e13f5d5652a631639a
URL:		http://gstreamer.net/
BuildRequires:	QtCore-devel >= 4.5
BuildRequires:	QtGui-devel >= 4.5
BuildRequires:	QtTest-devel >= 4.5
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	bison
BuildRequires:	boost-devel >= 1.40
BuildRequires:	cmake >= 2.8
BuildRequires:	flex
BuildRequires:	gstreamer-devel >= 0.10.31
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.31
BuildRequires:	libstdc++-devel >= 6:4.5
BuildRequires:	pkgconfig
BuildRequires:	qt4-qmake >= 4.5
Requires:	QtCore >= 4.5
Requires:	QtGui >= 4.5
Requires:	gstreamer >= 0.10.31
Requires:	gstreamer-plugins-base >= 0.10.31
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

Ponadto pakiet udostępnia element GStreamera "qwidgetvideosink" -
element wyjściowy obrazu rysujący bezpośrednio na QWidgetach przy
użyciu QPaintera.

%description -l pl.UTF-8
GstRTSP to serwer RTSP zbudowany w oparciu o GStreamera.

%package devel
Summary:	Header files for QtGStreamer libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek QtGStreamer
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	QtCore-devel >= 4.5
Requires:	QtGui-devel >= 4.5
Requires:	gstreamer-devel >= 0.10.31
Requires:	gstreamer-plugins-base-devel >= 0.10.31

%description devel
Header files for QtGStreamer libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek QtGStreamer.

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
%doc README
%attr(755,root,root) %{_libdir}/libQtGLib-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQtGLib-2.0.so.0
%attr(755,root,root) %{_libdir}/libQtGStreamer-0.10.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQtGStreamer-0.10.so.0
%attr(755,root,root) %{_libdir}/libQtGStreamerUi-0.10.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQtGStreamerUi-0.10.so.0
%attr(755,root,root) %{_libdir}/gstreamer-0.10/libgstqwidgetvideosink.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQtGLib-2.0.so
%attr(755,root,root) %{_libdir}/libQtGStreamer-0.10.so
%attr(755,root,root) %{_libdir}/libQtGStreamerUi-0.10.so
%{_includedir}/QtGStreamer
%{_pkgconfigdir}/QtGLib-2.0.pc
%{_pkgconfigdir}/QtGStreamer-0.10.pc
%{_pkgconfigdir}/QtGStreamerUi-0.10.pc
%dir %{_libdir}/QtGStreamer
%{_libdir}/QtGStreamer/QtGStreamer*.cmake
