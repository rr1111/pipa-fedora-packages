Name: pipa-sensor-restart
Version: 0.1
Release: 1
Summary: Sytemd wakeup script that restart iio-sensor-proxy and exagonrpcd-sdsp
Source1: pipa-sensor-restart
License: Unknown
BuildArch: noarch

%description
Systemd wakeup script that restart iio-sensor-proxy and exagonrpcd-sdsp

%install
install -Dm0755 "%{SOURCE1}" "%{buildroot}/usr/lib/systemd/system-sleep/pipa-sensor-restart"

%files
/usr/lib/systemd/system-sleep/pipa-sensor-restart
