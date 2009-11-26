Name:		rekonq
License:	GPLv3+
Version:	0.3.0
Release:	%mkrel 1
Group:		Graphical desktop/KDE
Summary:	A lightweight, WebKit based web browser for KDE
URL:		http://rekonq.sourceforge.net/
Source:		http://downloads.sourceforge.net/rekonq/%{name}-%{version}.tar.bz2
BuildRequires:	kdelibs4-devel
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

%build
%cmake_kde4
%make

%install
%__rm -rf %buildroot
%makeinstall_std -C build

%find_lang %{name} --with-html

%clean
%__rm -rf %{buildroot}




