Name: pipa-sensor-restart
Version: 0.1
Release: 5
Summary: Sytemd wakeup script that restart iio-sensor-proxy and exagonrpcd-sdsp
Source1: pipa-sensor-restart
License: Unknown
BuildArch: noarch

%description
Systemd wakeup script that restarts iio-sensor-proxy and hexagonrpcd-sdsp to hack around sensor suspend issues on pipa

%install
install -Dm0755 "%{SOURCE1}" "%{buildroot}/usr/lib/systemd/system-sleep/pipa-sensor-restart"
install -Dm0755 "%{SOURCE1}" "%{buildroot}/usr/local/bin/pipa-sensor-restart"

%files
/usr/lib/systemd/system-sleep/pipa-sensor-restart
/usr/local/bin/pipa-sensor-restart
