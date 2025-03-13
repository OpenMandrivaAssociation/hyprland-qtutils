Name:		hyprland-qtutils
Version:	0.1.3
Release:	1
Summary:	Hyprland QT/qml utility apps
Group:		Hyprland
License:	BSD-3-Clause
URL:		https://github.com/hyprwm/hyprland-qtutils
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(Qt6WaylandClient)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	lib64xkbcommon-devel
BuildRequires:	qt6-qtbase-tools

BuildRequires:	pkgconfig(hyprutils)
BuildRequires:	wayland-devel

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
