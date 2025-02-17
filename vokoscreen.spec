%define _legacy_common_support 1
%global prerel beta

Name:           vokoscreen
Version:        2.5.8
Release:        15.beta%{?dist}
Summary:        Screencast creator
License:        GPLv2+ and BSD
Group:          Applications/Multimedia
Url:            https://github.com/vkohaupt/vokoscreen
Source:         https://github.com/vkohaupt/vokoscreen/archive/%{version}%{?prerel:-%{prerel}}/%{name}-%{version}%{?prerel:-%{prerel}}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  alsa-lib-devel
BuildRequires:  ffmpeg-devel
BuildRequires:  libv4l-devel
BuildRequires:  libXrandr-devel
BuildRequires:  opencv-devel
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  qt5-qtmultimedia-devel
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
%autosetup -n %{name}-%{version}%{?prerel:-%{prerel}}

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
* Wed Jan 29 2025 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 2.5.8-15.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Aug 02 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 2.5.8-14.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 04 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 2.5.8-13.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 02 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 2.5.8-12.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Aug 08 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 2.5.8-11.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 2.5.8-10.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.5.8-9.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.5.8-8.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 19 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.5.8-7.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.5.8-6.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.5.8-5.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.5.8-4.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 Leigh Scott <leigh123linux@googlemail.com> - 2.5.8-3.beta
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.5.8-2.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 30 2018 Sérgio Basto <sergio@serjux.com> - 2.5.8-1
- Update to 2.5.8 (Beta)

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
