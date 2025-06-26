Name:		hyprland-qtutils
Version:	0.1.4
Release:	3
Summary:	Hyprland QT/qml utility apps
Group:		System/Libraries
License:	BSD-3-Clause
URL:		https://github.com/hyprwm/hyprland-qtutils
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:hyprsysteminfo
BuildRequires: desktop-file-utils
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6WaylandClient)
BuildRequires: qt6-qtbase-tools
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(hyprutils)

Requires: util-linux %dnl for /usr/bin/lscpu
Requires: pciutils %dnl for /usr/bin/lspci
Requires: procps-ng %dnl for /usr/bin/free
Requires: hyprland-qt-support

BuildSystem: cmake
BuildOption: -DCMAKE_BUILD_TYPE:STRING=Release -DCMAKE_INSTALL_PREFIX:PATH=/usr

%description
%{summary}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%description
%{summary}

%files
%license LICENSE
%doc README.md
%{_bindir}/hyprland-dialog
%{_bindir}/hyprland-donate-screen
%{_bindir}/hyprland-update-screen
