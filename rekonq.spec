Name:		rekonq
License:	GPLv3+
Version:	0.2.0
Release:	%mkrel 0.1
Group:		Graphical desktop/KDE
Summary:	A lightweight, WebKit based web browser for KDE
URL:		http://rekonq.sourceforge.net/
Source:		http://downloads.sourceforge.net/rekonq/%{name}-%{version}.tar.bz2
BuildRequires: kde4-macros
BuildRequires: kdelibs4-devel
BuildRequires: cmake
BuildRequires: make
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
rekonq is a KDE browser based on Webkit. Its code is based on Nokia
QtDemoBrowser, just like Arora. Anyway its implementation is going to embrace
KDE technologies to have a full-featured KDE web browser.

%prep
%setup -q

%build
%cmake_kde4
%make

%install
rm -rf %buildroot
%makeinstall_std -C build

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_kde_bindir}/%{name}
%{_kde_applicationsdir}/%{name}.desktop
%{_kde_appsdir}/%{name}/defaultbookmarks.xbel
%{_kde_appsdir}/%{name}/htmls/notfound.html
%{_kde_appsdir}/%{name}/pics/hi64-actions-download.png
%{_kde_appsdir}/%{name}/pics/loading.mng
%{_kde_appsdir}/%{name}/pics/webkit-icon.png
%{_kde_appsdir}/%{name}/%{name}ui.rc
%{_kde_datadir}/config.kcfg/%{name}.kcfg
%{_kde_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_kde_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_kde_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_kde_datadir}/locale/da/LC_MESSAGES/%{name}.mo
%{_kde_datadir}/locale/de/LC_MESSAGES/%{name}.mo
%{_kde_datadir}/locale/et/LC_MESSAGES/%{name}.mo
%{_kde_datadir}/locale/hu/LC_MESSAGES/%{name}.mo
%{_kde_datadir}/locale/is/LC_MESSAGES/%{name}.mo
%{_kde_datadir}/locale/it/LC_MESSAGES/%{name}.mo
%{_kde_datadir}/locale/nds/LC_MESSAGES/%{name}.mo
%{_kde_datadir}/locale/pl/LC_MESSAGES/%{name}.mo
%{_kde_datadir}/locale/pt/LC_MESSAGES/%{name}.mo
%{_kde_datadir}/locale/pt_BR/LC_MESSAGES/%{name}.mo
%{_kde_datadir}/locale/ru/LC_MESSAGES/%{name}.mo
%{_kde_datadir}/locale/sv/LC_MESSAGES/%{name}.mo
%{_kde_datadir}/locale/tr/LC_MESSAGES/%{name}.mo
%{_kde_datadir}/locale/uk/LC_MESSAGES/%{name}.mo
