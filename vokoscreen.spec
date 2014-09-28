Name:           vokoscreen
Version:        2.0.0
Release:        4%{?dist}
Summary:        Screencast creator
License:        GPLv2+ and BSD
Group:          Applications/Multimedia
Url:            https://github.com/vkohaupt/vokoscreen
Source:         https://github.com/vkohaupt/vokoscreen/archive/%{version}.tar.gz
# patch to link directly against the system libs
Patch0: %{name}-main.patch

BuildRequires:  desktop-file-utils
BuildRequires:  alsa-lib-devel
BuildRequires:  ffmpeg-devel
BuildRequires:  libqxt-devel
BuildRequires:  opencv-devel
BuildRequires:  qt4-devel
BuildRequires:  qtsingleapplication-devel
Requires:       alsa-utils
Requires:       mkvtoolnix
Requires:       pulseaudio-utils
Requires:       v4l-utils-devel-tools

%description
vokoscreen is an easy to use screencast creator to record educational
videos, live recordings of browser, installation, videoconferences, etc.

%prep
%setup -q
%patch0 -p0

# remove bundled libqxt + QtSingleApplication libraries
rm -f libqxt/*.h
rm -f QtSingleApplication/qtsingleapplication.h

%build
qmake-qt4 \
      QMAKE_STRIP="" \
      QMAKE_LRELEASE=%{_libdir}/qt4/bin/lrelease \
      QMAKE_CFLAGS+="%{optflags} -I%{_includedir}/QxtCore -I%{_includedir}/QxtGui -I%{_includedir}/QtSolutions -I%{_includedir}/QtNetwork" \
      QMAKE_CXXFLAGS+="%{optflags} -I%{_includedir}/QxtCore -I%{_includedir}/QxtGui -I%{_includedir}/QtSolutions -I%{_includedir}/QtNetwork" \
      QMAKE_LIBS+="%{optflags} -L%{_libdir} -lQxtCore -lQxtGui -lQtNetwork -lQtSolutions_SingleApplication-2.6"
make %{?_smp_mflags} all


%install
make INSTALL_ROOT=%{buildroot} install
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%post
/usr/bin/update-desktop-database &> /dev/null || :

%postun
/usr/bin/update-desktop-database &> /dev/null || :


%files
%doc AUTHORS COPYING CHANGE CREDITS SPECIAL-FEATURE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1.gz
%{_datadir}/pixmaps/%{name}.png

%changelog
* Sun Sep 21 2014 Martin Gansser <martinkg@fedoraproject.org> - 2.0.0-4
- fixed typos
- changed QMAKE_LRELEASE option

- added BSD to license tag
* Sun Sep 21 2014 Martin Gansser <martinkg@fedoraproject.org> - 2.0.0-3
- added BSD to license tag
- leaved comment what patch do

* Fri Sep 19 2014 Martin Gansser <martinkg@fedoraproject.org> - 2.0.0-2
- added patch to use system libraries
- added QMAKE flags to compile against system libraries
- added BR libqxt-devel
- added BR qtsingleapplication-devel
- added BR desktop-file-utils
- added %%desktop-file-validate
- added %%post and %%postun section

* Fri Sep 19 2014 Martin Gansser <martinkg@fedoraproject.org> - 2.0.0-1
- initial build for Fedora
