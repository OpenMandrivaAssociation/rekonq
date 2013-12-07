Summary:	A lightweight, WebKit based web browser for KDE
Name:		rekonq
Version:	2.3.2
Release:	6
License:	GPLv3+
Group:		Graphical desktop/KDE
Url:		http://rekonq.sourceforge.net/
#Source0:	http://downloads.sourceforge.net/project/rekonq/%(echo %{version} | cut -d. -f1-2)/%{name}-%{version}.tar.bz2
Source0:	http://freefr.dl.sourceforge.net/project/rekonq/2.0/rekonq-%version.tar.bz2
# Russian translation done for 2.3.1
Source1:	rus.tgz
Source2:	rudoc.tgz
Source100:	rekonq.rpmlintrc
# Patch 0 provides default mandriva bookmark
Patch0:		rekonq-0.6.80-add-mandriva-www-in-bookmark.patch
# Patch 1 provides some mandriva sites in default rekonq preview
# Patch 1 also fix the default website to point to /usr/share/doc/HTML/index.html
Patch1:		rekonq-0.9.0-add-mandriva-www-in-preview.patch
BuildRequires:	kdelibs4-devel
# Needed to enable additional features
BuildRequires:	nepomuk-core-devel
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(libkactivities)
BuildRequires:	pkgconfig(soprano)
BuildRequires:	pkgconfig(qoauth)
BuildRequires:	qt4-designer-plugin-qt3support
BuildRequires:	qt4-devel
# Package konqueror is currently required because it's providing cookies,proxie & web shortcut support in rekonq
Requires:	konqueror

%description
rekonq is a KDE browser based on Webkit. Its code is based on Nokia
QtDemoBrowser, just like Arora. Anyway its implementation is going to embrace
KDE technologies to have a full-featured KDE web browser.

#------------------------------------------------------------------------------

%prep
%setup -q
%apply_patches

cd po
tar xf %{SOURCE1}
cd ../doc
tar xf %{SOURCE2}

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang %{name} --with-html

%files -f %{name}.lang
%{_kde_bindir}/%{name}
%{_kde_libdir}/libkdeinit4_%{name}.so
%{_kde_appsdir}/%{name}/
%{_kde_datadir}/config.kcfg/%{name}.kcfg
%{_kde_iconsdir}/hicolor/*/apps/%{name}.png
%{_kde_applicationsdir}/%{name}.desktop
