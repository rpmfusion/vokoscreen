Name:           vokoscreen
Version:        2.5.0
Release:        4%{?dist}
Summary:        Screencast creator
License:        GPLv2+ and BSD
Group:          Applications/Multimedia
Url:            https://github.com/vkohaupt/vokoscreen
Source:         https://github.com/vkohaupt/vokoscreen/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  alsa-lib-devel
BuildRequires:  ffmpeg-devel
BuildRequires:  libv4l-devel
BuildRequires:  libXrandr-devel
BuildRequires:  opencv-devel
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  qtsingleapplication-qt5-devel 
Requires:       alsa-utils
Requires:       ffmpeg
Requires:       lame
Requires:       mkvtoolnix
Requires:       pulseaudio-utils
Requires:       v4l-utils-devel-tools

%description
vokoscreen is an easy to use screencast creator to record educational
videos, live recordings of browser, installation, videoconferences, etc.

%prep
%autosetup -p0

# remove bundled QtSingleApplication libraries
rm -rf QtSingleApplicationQt5

%build
%{qmake_qt5} \
      QMAKE_CXXFLAGS+=" -I%{_includedir}/qt5/QtSolutions" \
      QMAKE_LIBS+=" -lQt5Solutions_SingleApplication-2.6"
make %{?_smp_mflags} all


%install
make INSTALL_ROOT=%{buildroot} install
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%post
/usr/bin/update-desktop-database &> /dev/null || :

%postun
/usr/bin/update-desktop-database &> /dev/null || :


%files
%doc AUTHORS COPYING CHANGE CREDITS
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/%{name}.1.*

%changelog
* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 2.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 2.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 20 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Aug 17 2016 Leigh Scott <leigh123linux@googlemail.com> - 2.5.0-1
- Update to 2.5.0
- Switch build to qt5
- Use bundled libqtx5

* Wed Aug 17 2016 Leigh Scott <leigh123linux@googlemail.com> - 2.4.0-3
- Harden build
- Use qmake macro for build
- Fix source tag

* Tue Aug 16 2016 Martin Gansser <martinkg@fedoraproject.org> - 2.4.0-2
- Added Requirment ffmpeg, lame, rfbz #4188
- Added %%{name}-lrelease-qt4.patch

* Mon Jul 20 2015 Martin Gansser <martinkg@fedoraproject.org> - 2.4.0-1
- Update to 2.4.0

* Tue May 19 2015 Martin Gansser <martinkg@fedoraproject.org> - 2.3.0-1
- Update to 2.3.0

* Sat Nov 22 2014 Martin Gansser <martinkg@fedoraproject.org> - 2.1.0-3
- added BR libv4l-devel
- delete BR libv4l

* Sat Nov 22 2014 Martin Gansser <martinkg@fedoraproject.org> - 2.1.0-2
- added BR libv4l

* Fri Nov 21 2014 Martin Gansser <martinkg@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0

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
