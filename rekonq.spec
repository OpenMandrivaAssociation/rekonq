Name:		rekonq
License:	GPLv3+
Version:	0.6.80
Release:	%mkrel 1
Group:		Graphical desktop/KDE
Summary:	A lightweight, WebKit based web browser for KDE
URL:		http://rekonq.sourceforge.net/
Source:		http://downloads.sourceforge.net/rekonq/%{name}-%{version}.tar.bz2
# Patch 0 provides default mandriva bookmark 
Patch0:		rekonq-0.6.80-add-mandriva-www-in-bookmark.patch
# Patch 1 provides some mandriva sites in default rekonq preview
# Patch 1 also fix the default website to point to /usr/share/doc/HTML/index.html
Patch1:		rekonq-0.6.80-add-mandriva-www-in-preview.patch
BuildRequires:	kdelibs4-devel >= 2:4.6.0
# Package konqueror is currently required because it's providing cookies,proxie & web shortcut support in rekonq
Requires:	konqueror
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
rekonq is a KDE browser based on Webkit. Its code is based on Nokia
QtDemoBrowser, just like Arora. Anyway its implementation is going to embrace
KDE technologies to have a full-featured KDE web browser.


%files -f %name.lang
%defattr(-,root,root)
%{_kde_bindir}/%{name}
%{_kde_libdir}/libkdeinit4_%{name}.so
%{_kde_appsdir}/%{name}/
%{_kde_datadir}/config.kcfg/%{name}.kcfg
%{_kde_iconsdir}/hicolor/*/apps/%{name}.png
%{_kde_applicationsdir}/%{name}.desktop

#----------------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p0
%patch1 -p0

%build
%cmake_kde4
%make

%install
%__rm -rf %buildroot
%makeinstall_std -C build

%find_lang %{name} --with-html

%clean
%__rm -rf %{buildroot}




