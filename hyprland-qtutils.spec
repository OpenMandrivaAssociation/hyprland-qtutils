Name:		hyprland-qtutils
Version:	0.1.3
Release:	3
Summary:	Hyprland QT/qml utility apps
Group:		System/Libraries
License:	BSD-3-Clause
URL:		https://github.com/hyprwm/hyprland-qtutils
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(Qt6WaylandClient)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	Name:		hyprsysteminfo
Version:	0.1.3
Release:	1
Summary:	A tiny qt6/wml application to display information about the running system
License:	BSD-3-Clause
Group:		Hyprland

URL:		https://github.com/hyprwm/%{name}
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildSystem:	cmake

BuildRequires: desktop-file-utils
BuildRequires: gcc-c++
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6WaylandClient)
BuildRequires: qt6-qtbase-tools
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: wayland-devel
BuildRequires: pkgconfig(hyprutils)

Requires: /usr/bin/lscpu
Requires: /usr/bin/lspci
Requires: /usr/bin/free
Requires: hyprland-qt-support

%description
%{summary}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop

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
