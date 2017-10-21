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

%package base
%pattern_basetechnologies
Summary:        Zigzag Base
Group:          Metapackages
Provides:       pattern() = zigzag-base
Provides:       pattern-icon() = pattern-basis
Provides:       pattern-order() = 1100
Provides:       pattern-visible()

Requires:       finger
Requires:       timezone
Requires:       man
Requires:       psmisc
Requires:       lsof
Requires:       curl
Requires:       less
Requires:       tree
Requires:       patch
Requires:       colordiff
Requires:       deltarpm
Requires:       rpmconf
Requires:       ca-certificates-mozilla
Requires:       mozilla-nss-certs
Requires:       crda

%description base
Basic system components that should be present on every system

%files base
%dir %{_docdir}/patterns
%{_docdir}/patterns/zigzag-base.txt

################################################################################

%package firmware
%pattern_basetechnologies
Summary:        Zigzag Firmware
Group:          Metapackages
Provides:       pattern() = zigzag-firmware
Provides:       pattern-icon() = pattern-basis
Provides:       pattern-order() = 1100
Provides:       pattern-visible()

Requires:       ucode-intel
Requires:       ucode-amd
Requires:       atmel-firmware
Requires:       bcm20702a1-firmware
Requires:       ipw-firmware
Requires:       zd1211-firmware
Requires:       fwupdate

%description firmware
Firmware packages needed for hardware enablement in certain environments

%files firmware
%dir %{_docdir}/patterns
%{_docdir}/patterns/zigzag-firmware.txt

################################################################################

%package laptop
%pattern_basetechnologies
Summary:        Zigzag Laptop
Group:          Metapackages
Provides:       pattern() = zigzag-laptop
Provides:       pattern-icon() = pattern-basis
Provides:       pattern-order() = 1100
Provides:       pattern-visible()

Requires:       thermald
Requires:       tlp
Requires:       tlp-rdw
Requires:       powertop

%description laptop
System components useful only on laptop computers

%files laptop
%dir %{_docdir}/patterns
%{_docdir}/patterns/zigzag-laptop.txt

################################################################################

%package graphical
%pattern_graphicalenvironments
Summary:        Zigzag Graphical Base
Group:          Metapackages
Provides:       pattern() = zigzag-graphical
Provides:       pattern-icon() = pattern-basis
Provides:       pattern-order() = 1100
Provides:       pattern-visible()

Requires:       xorg-x11-essentials
Requires:       xorg-x11-server
Requires:       xrandr
Requires:       xdpyinfo
Requires:       xhost
Requires:       xorg-x11-fonts
Requires:       xorg-x11-driver-video
Requires:       xf86-video-amdgpu
Requires:       xf86-video-nouveau
Requires:       xf86-input-libinput
Requires:       Mesa-demo-x
Requires:       Mesa-libva
Requires:       vaapi-tools
Requires:       libgstvdpau
Requires:       libvdpau_va_gl1
Requires:       libva-vdpau-driver
Requires:       libva-egl1
Requires:       libva-glx1
Requires:       vaapi-intel-driver

%description graphical
Baisc display server, tools and Mesa packages

%files graphical
%dir %{_docdir}/patterns
%{_docdir}/patterns/zigzag-graphical.txt

################################################################################

%package plasma
%pattern_graphicalenvironments
Summary:        Zigzag KDE Plasma
Group:          Metapackages
Provides:       pattern() = zigzag-plasma
Provides:       pattern-icon() = pattern-basis
Provides:       pattern-order() = 1100
Provides:       pattern-visible()

Requires:       sddm
Requires:       plasma5-session
Requires:       plasma5-pa
Requires:       ksshaskpass5
Requires:       pinentry-qt5
Requires:       kde-gtk-config5-gtk2
Requires:       kde-gtk-config5-gtk3
Requires:       gtk2-metatheme-breeze
Requires:       gtk3-metatheme-breeze
Requires:       kio_mtp
Requires:       kio_iso
Requires:       pam_kwallet
Requires:       xdg-desktop-portal-kde

%description plasma
Minimal plasma desktop environment installation

%files plasma
%dir %{_docdir}/patterns
%{_docdir}/patterns/zigzag-plasma.txt

################################################################################

%prep

%build

%install
mkdir -p %{buildroot}%{_docdir}/patterns
for i in zigzag-{base,firmware,laptop,graphical,plasma}; do
    echo "This file marks the pattern $i to be installed." \
    >"%{buildroot}%{_docdir}/patterns/$i.txt"
done

%changelog
