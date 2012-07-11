Name:		rekonq
License:	GPLv3+
Version:	0.9.90
Release:	1
Group:		Graphical desktop/KDE
Summary:	A lightweight, WebKit based web browser for KDE
URL:		http://rekonq.sourceforge.net/
#Source0:	http://downloads.sourceforge.net/project/rekonq/%(echo %{version} | cut -d. -f1-2)/%{name}-%{version}.tar.bz2
Source0:	http://downloads.sourceforge.net/project/rekonq/1.0/%{name}-%{version}.tar.bz2
Source100:	rekonq.rpmlintrc
# Patch 0 provides default mandriva bookmark 
Patch0:		rekonq-0.6.80-add-mandriva-www-in-bookmark.patch
# Patch 1 provides some mandriva sites in default rekonq preview
# Patch 1 also fix the default website to point to /usr/share/doc/HTML/index.html
Patch1:		rekonq-0.9.0-add-mandriva-www-in-preview.patch
BuildRequires:	kdelibs4-devel >= 2:4.6.0
# Package konqueror is currently required because it's providing cookies,proxie & web shortcut support in rekonq
Requires:	konqueror

%description
rekonq is a KDE browser based on Webkit. Its code is based on Nokia
QtDemoBrowser, just like Arora. Anyway its implementation is going to embrace
KDE technologies to have a full-featured KDE web browser.

#------------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p0 -b .bookmark~
%patch1 -p1 -b .preview~

%build
%cmake_kde4
%make

%install
%__rm -rf %buildroot
%makeinstall_std -C build

%find_lang %{name} --with-html
%find_lang kwebapp

%files -f %{name}.lang,kwebapp.lang
%defattr(-,root,root)
%{_kde_bindir}/%{name}
%{_kde_bindir}/kwebapp
%{_kde_libdir}/libkdeinit4_%{name}.so
%{_kde_appsdir}/%{name}/
%{_kde_datadir}/config.kcfg/%{name}.kcfg
%{_kde_iconsdir}/hicolor/*/apps/%{name}.png
%{_kde_applicationsdir}/%{name}.desktop
