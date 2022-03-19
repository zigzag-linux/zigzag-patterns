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


Requires:       kernel-firmware-all
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

%package xfirmware-intel
%pattern_basetechnologies
Summary:        Zigzag Graphical Firmware - Intel
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
Firmware packages needed for hardware enablement in certain graphical environments

%files xfirmware-intel
%dir %{_docdir}/patterns
%{_docdir}/patterns/zigzag-xfirmware-intel.txt

################################################################################

%package xfirmware-nouveau
%pattern_basetechnologies
Summary:        Zigzag Graphical Firmware - Radeon
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
Firmware packages needed for hardware enablement in certain graphical environments

%files xfirmware-nouveau
%dir %{_docdir}/patterns
%{_docdir}/patterns/zigzag-xfirmware-nouveau.txt

################################################################################

%package xfirmware-radeon
%pattern_basetechnologies
Summary:        Zigzag Graphical Firmware - Nouveau
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
Firmware packages needed for hardware enablement in certain graphical environments

%files xfirmware-radeon
%dir %{_docdir}/patterns
%{_docdir}/patterns/zigzag-xfirmware-radeon.txt

################################################################################

%package printer
%pattern_basetechnologies
Summary:        Zigzag Printing Support
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
Base packages needed for enabling printing support

%files printer
%dir %{_docdir}/patterns
%{_docdir}/patterns/zigzag-printer.txt

################################################################################

%package immutable
%pattern_basetechnologies
Summary:        Zigzag Immutable Support
Group:          Metapackages
Provides:       pattern() = zigzag-immutable
Provides:       pattern-icon() = pattern-basis
Provides:       pattern-order() = 1100
Provides:       pattern-visible()


Requires:       microos-tools
Requires:       health-checker-plugins-MicroOS
Requires:       libdnf-plugin-txnupd
Requires:       PackageKit-backend-dnf
Requires:       toolbox


%description immutable
Base packages for immutable Zigzag system - package management and tooling

%files immutable
%dir %{_docdir}/patterns
%{_docdir}/patterns/zigzag-immutable.txt



%prep

%build

%install
mkdir -p %{buildroot}%{_docdir}/patterns
for i in zigzag-{firmware,xfirmware-intel,xfirmware-nouveau,xfirmware-radeon,printer,immutable}; do
    echo "This file marks the pattern $i to be installed." \
    >"%{buildroot}%{_docdir}/patterns/$i.txt"
done

%changelog
