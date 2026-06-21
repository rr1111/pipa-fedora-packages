Name: pipa-sound-conf
Version: 2.0
Release: 1%{?dist}
Summary: Sound config for Xiaomi Mi Pad 6 (pipa)
Source1: xiaomi-pipa.conf
Source2: hifi.conf
Source3: wireplumber.conf
Source4: HDMI_pipa.conf
License: MIT
BuildArch: noarch

Obsoletes: alsa-ucm-conf-xiaomi-pipa < %{version}-%{release}
Obsoletes: alsa-ucm-conf-sm8250

Requires: wireplumber

%description
Sound configuration for Xiaomi Mi Pad 6 (pipa)

%changelog
* Sun Jun 21 2026 rey <renerinner114@pm.me> - 2.0-1
- Initial package, add configs for DP audio, etc.


%install
install -Dm644 "%{SOURCE1}" "%{buildroot}/usr/share/alsa/ucm2/conf.d/sm8250/Xiaomi Pad 6.conf"

install -Dm644 "%{SOURCE2}" "%{buildroot}/usr/share/alsa/ucm2/Qualcomm/sm8250/HiFi_pipa.conf"

install -Dm644 "%{SOURCE4}" "%{buildroot}/usr/share/alsa/ucm2/Qualcomm/sm8250/HDMI_pipa.conf"

ln -s "Xiaomi Pad 6.conf" "%{buildroot}/usr/share/alsa/ucm2/conf.d/sm8250/Xiaomi-Pad6-pipa-M82.conf"

install -Dm644 "%{SOURCE3}" "%{buildroot}/usr/share/wireplumber/wireplumber.conf.d/51-pipa.conf"

%files
/usr/share/alsa/ucm2/conf.d/sm8250/Xiaomi\ Pad\ 6.conf
/usr/share/alsa/ucm2/Qualcomm/sm8250/HiFi_pipa.conf
/usr/share/alsa/ucm2/Qualcomm/sm8250/HDMI_pipa.conf
/usr/share/alsa/ucm2/conf.d/sm8250/Xiaomi-Pad6-pipa-M82.conf
/usr/share/wireplumber/wireplumber.conf.d/51-pipa.conf
