Name:		hyprland-qtutils
Version:	0.1.5
Release:	1
Summary:	Hyprland QT/qml utility apps
Group:		System/Libraries
License:	BSD-3-Clause
URL:		https://github.com/hyprwm/hyprland-qtutils
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:		WaylandClientPrivate.patch

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
BuildRequires: pkgconfig(Qt6QmlNetwork)
BuildRequires: cmake(Qt6QmlAssetDownloader)
BuildRequires: pkgconfig(Qt6LabsSynchronizer)
BuildRequires: pkgconfig(Qt6QmlCore)
BuildRequires: qt6-qtbase-theme-gtk3
BuildRequires: pkgconfig(Qt6WaylandClient)

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
%{_bindir}/hyprland-dialog
%{_bindir}/hyprland-donate-screen
%{_bindir}/hyprland-update-screen
