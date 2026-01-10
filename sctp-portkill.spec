Name:           sctp-portkill
Version:        1.0
Release:        1%{?dist}
Summary:        Specialized utility to kill SCTP processes by port
License:        GPL
BuildArch:      noarch
# Requires iproute for the 'ss' command
Requires:       iproute, gawk, bash

%description
A targeted networking utility for RHEL/Fedora systems. It identifies 
and terminates processes specifically using the SCTP protocol on a 
given port. Useful for clearing stuck SIGTRAN, M3UA, or Diameter 
over SCTP associations.

%install
mkdir -p %{buildroot}/usr/bin/
install -m 755 %{_sourcedir}/sctp-portkill %{buildroot}/usr/bin/sctp-portkill

%files
/usr/bin/sctp-portkill
