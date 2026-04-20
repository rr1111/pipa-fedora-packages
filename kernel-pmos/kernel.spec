Name: kernel
ExclusiveArch: aarch64
Version: 6.19.12
Release: 1.dev.pipa
Summary: AIO package for linux kernel, modules and headers for Xiaomi Pad 6 (pipa)
URL: https://kernel.org
License: GPL
Source1: https://cdn.kernel.org/pub/linux/kernel/v6.x/linux-%{version}.tar.xz
Source2: pipa.config

Patch0001: 0001-arm64-dts-qcom-sm8250-xiaomi-pipa-Add-device-tree-fo.patch
Patch0002: 0002-power-supply-Add-driver-for-Qualcomm-PMIC-fuel-gauge.patch
Patch0003: 0003-Input-Add-nt36523-touchscreen-driver.patch
Patch0004: 0004-drm-Add-drm-notifier-support.patch
Patch0005: 0005-drm-dsi-emit-panel-turn-on-off-signal-to-touchscreen.patch
Patch0006: 0006-drm-msm-dsi-change-sync-mode-to-sync-on-DSI0-rather-.patch
Patch0007: 0007-drm-msm-dsi-support-DSC-configurations-with-slice_pe.patch
Patch0008: 0008-drm-panel-Add-support-for-Novatek-NT36532-panel.patch
Patch0009: 0009-drivers-media-i2c-ov13b10-add-device-tree-support-an.patch
Patch0010: 0010-ASoC-codecs-aw88261-add-hacks-for-xiaomi-pipa.patch
Patch0011: 0011-ASoC-qcom-sm8250-Add-tdm-support.patch

Provides: kernel = %{version}-%{release}
Provides: kernel-core = %{version}-%{release}
Provides: kernel-modules = %{version}-%{release}

BuildRequires: kmod, bash, coreutils, tar, git-core, which
BuildRequires: bzip2, xz, findutils, m4, perl-interpreter, perl-Carp, perl-devel, perl-generators, make, diffutils, gawk
BuildRequires: zstd
BuildRequires: gcc, binutils, redhat-rpm-config, hmaccalc, bison, flex, gcc-c++
BuildRequires: rust, rust-src, bindgen, rustfmt, clippy
BuildRequires: net-tools, hostname, bc, elfutils-devel
BuildRequires: dwarves
BuildRequires: python3
BuildRequires: python3-devel
BuildRequires: python3-pyyaml
BuildRequires: glibc-static
BuildRequires: rsync
BuildRequires: opencsd-devel >= 1.0.0
BuildRequires: openssl-devel

Requires: dracut >= 027
Requires: bash
Requires: coreutils
Requires: systemd

%description
Mainline kernel for Xiaomi Pad 6 (pipa).

%prep
tar -xf %{SOURCE1}
cd linux-%{version}
cp %{SOURCE2} .config
%patch0001 -p1
%patch0002 -p1
%patch0003 -p1
%patch0004 -p1
%patch0005 -p1
%patch0006 -p1
%patch0007 -p1
%patch0008 -p1
%patch0009 -p1
%patch0010 -p1
%patch0011 -p1


%build
cd linux-%{version}
make olddefconfig .config -j`nproc`
make EXTRAVERSION="-%{release}" -j`nproc`

%install
cd linux-%{version}
kernel_version=$(make EXTRAVERSION="-%{release}" kernelrelease)

mkdir -p %{buildroot}/boot/
cp arch/arm64/boot/Image.gz %{buildroot}/boot/vmlinuz-$kernel_version
cp System.map %{buildroot}/boot/System.map-$kernel_version
cp .config %{buildroot}/boot/config-$kernel_version

make EXTRAVERSION="-%{release}" modules_install INSTALL_MOD_PATH=%{buildroot}/usr
cp arch/arm64/boot/dts/qcom/sm8250-xiaomi-pipa.dtb %{buildroot}/usr/lib/modules/$kernel_version/devicetree
ln -s ./devicetree %{buildroot}/usr/lib/modules/$kernel_version/dtb
cp arch/arm64/boot/Image.gz %{buildroot}/usr/lib/modules/$kernel_version/vmlinuz
make EXTRAVERSION="-%{release}" headers_install INSTALL_HDR_PATH=%{buildroot}/usr
rm %{buildroot}/usr/lib/modules/%{version}*/build

%files
/boot/System.map-%{version}*
/boot/config-%{version}*
/boot/vmlinuz-%{version}*
/usr/lib/modules/%{version}*

%posttrans
dracut -f --kver %{version}-%{release} /usr/lib/modules/%{version}-%{release}/initramfs.img
kernel-install add %{version}-%{release} /usr/lib/modules/%{version}-%{release}/vmlinuz /usr/lib/modules/%{version}-%{release}/initramfs.img

%postun
kernel-install remove %{version}-%{release} /usr/lib/modules/%{version}-%{release}/vmlinuz


%package core
License: GPL
Summary: AIO package for linux kernel, modules and headers for Xiaomi Pad 6 (pipa).
Requires: kernel

%description core
Mainline kernel for Xiaomi Pad 6 (pipa).

%files core


%package modules
License: GPL
Summary: AIO package for linux kernel, modules and headers for Xiaomi Pad 6 (pipa).
Requires: kernel

%description modules
Mainline kernel for Xiaomi Pad 6 (pipa).

%files modules


%package devel
License: GPL
Summary: AIO package for linux kernel, modules and headers for Xiaomi Pad 6 (pipa).
Requires: kernel-headers

%description devel
Mainline kernel header for Xiaomi Pad 6 (pipa).

%files devel


%package headers
License: GPL
Summary: AIO package for linux kernel, modules and headers for Xiaomi Pad 6 (pipa).
Provides: kernel-devel = %{version}-%{release}

%description headers
Mainline kernel headers for Xiaomi Pad 6 (pipa).

%files headers
/usr/include


%package devel-matched
License: GPL
Summary: AIO package for linux kernel, modules and headers for Xiaomi Pad 6 (pipa).
Requires: kernel-devel
Requires: kernel-core

%description devel-matched
Mainline kernel headers for Xiaomi Pad 6 (pipa).

%files devel-matched

