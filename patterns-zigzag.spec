Name:           patterns-zigzag
Version:        0
Release:        0
Summary:        Patterns for Zigzag Linux
License:        GPL-3.0
Group:          Metapackages
Url:            https://github.com/zigzag/zigzag-patterns
BuildRequires:  patterns-rpm-macros

%description
This package is used to build all patterns of Zigzag Linux

################################################################################

%package firmware
%pattern_basetechnologies
Summary:        Zigzag Firmware
Group:          Metapackages
Provides:       pattern() = zigzag-firmware
Provides:       pattern-icon() = pattern-basis
Provides:       pattern-order() = 1100
Provides:       pattern-visible()

Requires:       kernel-firmware
Requires:       ucode-intel
Requires:       ucode-amd
Requires:       atmel-firmware
Requires:       bcm20702a1-firmware
Requires:       ipw-firmware
Requires:       zd1211-firmware

%description firmware
Firmware packages needed for hardware enablement in certain environments

%files firmware
%dir %{_docdir}/patterns
%{_docdir}/patterns/zigzag-firmware.txt

################################################################################

%package xfirmware
%pattern_basetechnologies
Summary:        Zigzag Graphical Firmware
Group:          Metapackages
Provides:       pattern() = zigzag-xfirmware
Provides:       pattern-icon() = pattern-basis
Provides:       pattern-order() = 1100
Provides:       pattern-visible()

# Radeon
Requires: xf86-video-amdgpu
Requires: xf86-video-ati
Requires: libvdpau_radeonsi
Requires: libvdpau_r600

# nVidia
Requires: xf86-video-nouveau
Requires: Mesa-dri-nouveau
Requires: libvdpau_nouveau

# Intel
Requires: Mesa-libva
Requires: intel-vaapi-driver
Requires: libva-vdpau-driver
Requires: libvdpau_va_gl

%description xfirmware
Firmware packages needed for hardware enablement in certain graphical environments

%files xfirmware
%dir %{_docdir}/patterns
%{_docdir}/patterns/zigzag-xfirmware.txt

################################################################################

%package yast
%pattern_basetechnologies
Summary:        Zigzag YaST
Group:          Metapackages
Provides:       pattern() = zigzag-yast
Provides:       pattern-icon() = pattern-basis
Provides:       pattern-order() = 1100
Provides:       pattern-visible()

Requires:       yast2-control-center-qt
Requires:       libyui-qt
Requires:       libyui-qt-pkg
Requires:       yast2-firewall
Requires:       yast2-fonts
Requires:       yast2-country
Requires:       yast2-users
Requires:       yast2-sudo
Requires:       yast2-bootloader
Requires:       yast2-update
Requires:       yast2-online-update-frontend
Requires:       yast2-ntp-client
Requires:       yast2-sound
Requires:       yast2-apparmor
Requires:       yast2-sysconfig
Requires:       yast2-snapper

%description yast
Minimal useful distribution of YaST control panel

%files yast
%dir %{_docdir}/patterns
%{_docdir}/patterns/zigzag-yast.txt

################################################################################

%prep

%build

%install
mkdir -p %{buildroot}%{_docdir}/patterns
for i in zigzag-{firmware,xfirmware,yast}; do
    echo "This file marks the pattern $i to be installed." \
    >"%{buildroot}%{_docdir}/patterns/$i.txt"
done

%changelog
