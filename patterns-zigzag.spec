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
Summary:        Zigzag firmware
Group:          Metapackages
Provides:       pattern() = zigzag-firmware
Provides:       pattern-icon() = pattern-basis
Provides:       pattern-order() = 1100
Provides:       pattern-visible()


Requires:       kernel-firmware-all
Requires:       ucode-intel
Requires:       ucode-amd
Requires:       atmel-firmware
Requires:       bcm20702a1-firmware
Requires:       ipw-firmware
Requires:       zd1211-firmware


%description firmware
Zigzag firmware

%files firmware
%dir %{_docdir}/patterns
%{_docdir}/patterns/zigzag-firmware.txt

################################################################################

%package xfirmware-intel
%pattern_basetechnologies
Summary:        Zigzag graphical firmware - Intel
Group:          Metapackages
Provides:       pattern() = zigzag-xfirmware-intel
Provides:       pattern-icon() = pattern-basis
Provides:       pattern-order() = 1100
Provides:       pattern-visible()
Obsoletes: patterns-zigzag-xfirmware

Requires:       Mesa-dri
Requires:       Mesa-libva
Requires:       libvulkan1
Requires:       libvulkan_intel
Requires:       intel-vaapi-driver
Requires:       intel-hybrid-driver
Requires:       intel-media-driver
Requires:       libva-vdpau-driver
Requires:       libvdpau_va_gl


%description xfirmware-intel
Zigzag graphical firmware - Intel

%files xfirmware-intel
%dir %{_docdir}/patterns
%{_docdir}/patterns/zigzag-xfirmware-intel.txt

################################################################################

%package xfirmware-nouveau
%pattern_basetechnologies
Summary:        Zigzag graphical firmware - Radeon
Group:          Metapackages
Provides:       pattern() = zigzag-xfirmware-nouveau
Provides:       pattern-icon() = pattern-basis
Provides:       pattern-order() = 1100
Provides:       pattern-visible()
Obsoletes: patterns-zigzag-xfirmware
Conflicts: kmod(nvidia)

Requires:       Mesa-dri
Requires:       Mesa-dri-nouveau
Requires:       xf86-video-nouveau
Requires:       libvdpau_nouveau


%description xfirmware-nouveau
Zigzag graphical firmware - Radeon

%files xfirmware-nouveau
%dir %{_docdir}/patterns
%{_docdir}/patterns/zigzag-xfirmware-nouveau.txt

################################################################################

%package xfirmware-radeon
%pattern_basetechnologies
Summary:        Zigzag graphical firmware - Nouveau
Group:          Metapackages
Provides:       pattern() = zigzag-xfirmware-radeon
Provides:       pattern-icon() = pattern-basis
Provides:       pattern-order() = 1100
Provides:       pattern-visible()
Obsoletes: patterns-zigzag-xfirmware

Requires:       Mesa-dri
Requires:       libvulkan1
Requires:       libvulkan_radeon
Requires:       xf86-video-amdgpu
Requires:       xf86-video-ati
Requires:       libvdpau_radeonsi
Requires:       libvdpau_r600
Requires:       libvdpau_r300


%description xfirmware-radeon
Zigzag graphical firmware - Nouveau

%files xfirmware-radeon
%dir %{_docdir}/patterns
%{_docdir}/patterns/zigzag-xfirmware-radeon.txt

################################################################################

%package printer
%pattern_basetechnologies
Summary:        Zigzag printing support
Group:          Metapackages
Provides:       pattern() = zigzag-printer
Provides:       pattern-icon() = pattern-basis
Provides:       pattern-order() = 1100
Provides:       pattern-visible()


Requires:       OpenPrintingPPDs
Requires:       bluez-cups
Requires:       cups
Requires:       cups-filters
Requires:       ghostscript
Requires:       udev-configure-printer
Requires:       cups-pk-helper


%description printer
Zigzag printing support

%files printer
%dir %{_docdir}/patterns
%{_docdir}/patterns/zigzag-printer.txt

################################################################################

%package immutable
%pattern_basetechnologies
Summary:        Zigzag immutable
Group:          Metapackages
Provides:       pattern() = zigzag-immutable
Provides:       pattern-icon() = pattern-basis
Provides:       pattern-order() = 1100
Provides:       pattern-visible()


Requires:       microos-tools
Requires:       health-checker-plugins-MicroOS
Requires:       libdnf-plugin-txnupd
Requires:       PackageKit-backend-dnf
Requires:       podman
Requires:       toolbox


%description immutable
Zigzag immutable

%files immutable
%dir %{_docdir}/patterns
%{_docdir}/patterns/zigzag-immutable.txt

################################################################################

%package apparmor
%pattern_basetechnologies
Summary:        Zigzag AppArmor support
Group:          Metapackages
Provides:       pattern() = zigzag-apparmor
Provides:       pattern-icon() = pattern-basis
Provides:       pattern-order() = 1100
Provides:       pattern-visible()


Requires:       apparmor-profiles
Requires:       apparmor-parser


%description apparmor
Zigzag AppArmor support

%files apparmor
%dir %{_docdir}/patterns
%{_docdir}/patterns/zigzag-apparmor.txt

################################################################################

%package base
%pattern_basetechnologies
Summary:        Zigzag barebone base
Group:          Metapackages
Provides:       pattern() = zigzag-base
Provides:       pattern-icon() = pattern-basis
Provides:       pattern-order() = 1100
Provides:       pattern-visible()


Requires:       patterns-base-minimal_base
Requires:       mozilla-nss-certs
Requires:       openSUSE-signkey-cert
Requires:       kernel-default-optional
Requires:       grub2-branding-openSUSE
Requires:       grub2-snapper-plugin
Requires:       grub2-i386-pc
Requires:       grub2-x86_64-efi
Requires:       syslinux


%description base
Zigzag barebone base

%files base
%dir %{_docdir}/patterns
%{_docdir}/patterns/zigzag-base.txt

################################################################################

%package utils
%pattern_basetechnologies
Summary:        Zigzag system utilities
Group:          Metapackages
Provides:       pattern() = zigzag-utils
Provides:       pattern-icon() = pattern-basis
Provides:       pattern-order() = 1100
Provides:       pattern-visible()


Requires:       sudo
Requires:       shim
Requires:       system-group-wheel
Requires:       finger
Requires:       time
Requires:       timezone
Requires:       man
Requires:       psmisc
Requires:       lsof
Requires:       curl
Requires:       less
Requires:       openssh
Requires:       iproute2
Requires:       iputils
Requires:       iw
Requires:       crda
Requires:       audit
Requires:       avahi
Requires:       zigzag-languages
Requires:       bash-completion
Requires:       vim-small
Requires:       rpmconf
Requires:       deltarpm
Requires:       sensors
Requires:       dmidecode
Requires:       hdparm
Requires:       sysfsutils
Requires:       pciutils
Requires:       usbutils
Requires:       fwupd
Requires:       smartmontools
Requires:       cryptsetup
Requires:       tar
Requires:       unar
Requires:       p7zip
Requires:       xfsprogs
Requires:       btrfsprogs
Requires:       btrfsmaintenance
Requires:       e2fsprogs
Requires:       ntfsprogs
Requires:       dosfstools
Requires:       f2fs-tools
Requires:       polkit-default-privs


%description utils
Zigzag system utilities

%files utils
%dir %{_docdir}/patterns
%{_docdir}/patterns/zigzag-utils.txt

################################################################################

%package desktop
%pattern_basetechnologies
Summary:        Zigzag base desktop
Group:          Metapackages
Provides:       pattern() = zigzag-desktop
Provides:       pattern-icon() = pattern-basis
Provides:       pattern-order() = 1100
Provides:       pattern-visible()


Requires:       flatpak
Requires:       zigzag-wallpapers
Requires:       xdg-user-dirs
Requires:       xdg-utils
Requires:       gsettings-backend-dconf
Requires:       bluez-firmware
Requires:       udisks2
Requires:       fonts-config
Requires:       iosevka-fonts-mini
Requires:       noto-sans-fonts
Requires:       noto-sans-sc-fonts
Requires:       noto-sans-jp-fonts
Requires:       noto-coloremoji-fonts
Requires:       zram-generator
Requires:       earlyoom
Requires:       samba
Requires:       samba-client
Requires:       cifs-utils


%description desktop
Zigzag base desktop

%files desktop
%dir %{_docdir}/patterns
%{_docdir}/patterns/zigzag-desktop.txt

################################################################################

%package network
%pattern_basetechnologies
Summary:        Zigzag network stack
Group:          Metapackages
Provides:       pattern() = zigzag-network
Provides:       pattern-icon() = pattern-basis
Provides:       pattern-order() = 1100
Provides:       pattern-visible()


Requires:       systemd-network
Requires:       NetworkManager
Requires:       NetworkManager-openvpn


%description network
Zigzag network stack

%files network
%dir %{_docdir}/patterns
%{_docdir}/patterns/zigzag-network.txt

################################################################################

%package laptop
%pattern_basetechnologies
Summary:        Zigzag laptop utils
Group:          Metapackages
Provides:       pattern() = zigzag-laptop
Provides:       pattern-icon() = pattern-basis
Provides:       pattern-order() = 1100
Provides:       pattern-visible()


Requires:       powertop
Requires:       thermald
Requires:       tlp
Requires:       tlp-rdw


%description laptop
Zigzag laptop utils

%files laptop
%dir %{_docdir}/patterns
%{_docdir}/patterns/zigzag-laptop.txt

################################################################################

%package plasma
%pattern_basetechnologies
Summary:        Zigzag Plasma Desktop
Group:          Metapackages
Provides:       pattern() = zigzag-plasma
Provides:       pattern-icon() = pattern-basis
Provides:       pattern-order() = 1100
Provides:       pattern-visible()


Requires:       bluedevil5
Requires:       colord-kde
Requires:       ffmpegthumbs
Requires:       gtk3-metatheme-breeze
Requires:       kcm_tablet
Requires:       kde-gtk-config5-gtk3
Requires:       kdegraphics-thumbnailers
Requires:       kdenetwork-filesharing
Requires:       kgamma5
Requires:       kio-extras5
Requires:       ksshaskpass5
Requires:       plasma5-thunderbolt
Requires:       plasma5-systemmonitor
Requires:       plasma5-disks
Requires:       pam_kwallet
Requires:       phonon4qt5-backend-gstreamer
Requires:       pinentry-qt5
Requires:       plasma-nm5-openvpn
Requires:       plasma5-defaults-zigzag
Requires:       plasma5-pa
Requires:       plasma5-session
Requires:       plasma5-session-wayland
Requires:       sddm
Requires:       xdg-desktop-portal-kde
Requires:       xdg-desktop-portal-gtk


%description plasma
Zigzag Plasma Desktop

%files plasma
%dir %{_docdir}/patterns
%{_docdir}/patterns/zigzag-plasma.txt

################################################################################

%package plasma-apps
%pattern_basetechnologies
Summary:        Zigzag Plasma Desktop applications
Group:          Metapackages
Provides:       pattern() = zigzag-plasma-apps
Provides:       pattern-icon() = pattern-basis
Provides:       pattern-order() = 1100
Provides:       pattern-visible()


Requires:       dolphin
Requires:       konsole
Requires:       ark
Requires:       kcolorchooser
Requires:       discover
Requires:       discover-notifier
Requires:       discover-backend-flatpak
Requires:       discover-backend-packagekit
Requires:       discover-backend-fwupd
Requires:       kwalletmanager5
Requires:       spectacle


%description plasma-apps
Zigzag Plasma Desktop applications

%files plasma-apps
%dir %{_docdir}/patterns
%{_docdir}/patterns/zigzag-plasma-apps.txt

################################################################################

%package gfx
%pattern_basetechnologies
Summary:        Zigzag graphics stack
Group:          Metapackages
Provides:       pattern() = zigzag-gfx
Provides:       pattern-icon() = pattern-basis
Provides:       pattern-order() = 1100
Provides:       pattern-visible()


Requires:       Mesa-demo-x
Requires:       vulkan-tools
Requires:       libva-utils
Requires:       libva-glx2
Requires:       xf86-input-libinput
Requires:       xf86-video-vmware


%description gfx
Zigzag graphics stack

%files gfx
%dir %{_docdir}/patterns
%{_docdir}/patterns/zigzag-gfx.txt

################################################################################

%package audio
%pattern_basetechnologies
Summary:        Zigzag audio stack
Group:          Metapackages
Provides:       pattern() = zigzag-audio
Provides:       pattern-icon() = pattern-basis
Provides:       pattern-order() = 1100
Provides:       pattern-visible()


Requires:       alsa-firmware
Requires:       alsa-utils
Requires:       pipewire
Requires:       pipewire-modules
Requires:       pipewire-alsa
Requires:       pipewire-pulseaudio
Requires:       gstreamer-plugin-pipewire


%description audio
Zigzag audio stack

%files audio
%dir %{_docdir}/patterns
%{_docdir}/patterns/zigzag-audio.txt

################################################################################

%package xorg
%pattern_basetechnologies
Summary:        Zigzag X.org
Group:          Metapackages
Provides:       pattern() = zigzag-xorg
Provides:       pattern-icon() = pattern-basis
Provides:       pattern-order() = 1100
Provides:       pattern-visible()


Requires:       xorg-x11-essentials
Requires:       xorg-x11-server
Requires:       xorg-x11-fonts
Requires:       xorg-x11-driver-video
Requires:       xrandr
Requires:       xclip


%description xorg
Zigzag X.org

%files xorg
%dir %{_docdir}/patterns
%{_docdir}/patterns/zigzag-xorg.txt



%prep

%build

%install
mkdir -p %{buildroot}%{_docdir}/patterns
for i in zigzag-{firmware,xfirmware-intel,xfirmware-nouveau,xfirmware-radeon,printer,immutable,apparmor,base,utils,desktop,network,laptop,plasma,plasma-apps,gfx,audio,xorg}; do
    echo "This file marks the pattern $i to be installed." \
    >"%{buildroot}%{_docdir}/patterns/$i.txt"
done

%changelog
