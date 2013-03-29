Name:		rekonq
License:	GPLv3+
Version:	2.2.1
Release:	1
Group:		Graphical desktop/KDE
Summary:	A lightweight, WebKit based web browser for KDE
URL:		http://rekonq.sourceforge.net/
#Source0:	http://downloads.sourceforge.net/project/rekonq/%(echo %{version} | cut -d. -f1-2)/%{name}-%{version}.tar.bz2
Source0:	http://freefr.dl.sourceforge.net/project/rekonq/2.0/rekonq-%version.tar.bz2
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
%apply_patches

%build
%cmake_kde4
%make

%install
%__rm -rf %buildroot
%makeinstall_std -C build

%find_lang %{name} --with-html

%files -f %{name}.lang
%defattr(-,root,root)
%{_kde_bindir}/%{name}
%{_kde_libdir}/libkdeinit4_%{name}.so
%{_kde_appsdir}/%{name}/
%{_kde_datadir}/config.kcfg/%{name}.kcfg
%{_kde_iconsdir}/hicolor/*/apps/%{name}.png
%{_kde_applicationsdir}/%{name}.desktop


%changelog
* Wed Jul 25 2012 Bernhard Rosenkraenzer <bero@bero.eu> 1.0-1
+ Revision: 810980
- Update to 1.0

* Wed Jul 11 2012 Bernhard Rosenkraenzer <bero@bero.eu> 0.9.90-1
+ Revision: 808905
- Update to 0.9.90 (1.0-beta1)

* Sun Jun 17 2012 Bernhard Rosenkraenzer <bero@bero.eu> 0.9.80-1
+ Revision: 806027
- Update to 1.0-TP

* Sat May 05 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.9.2-1
+ Revision: 796514
- update to 0.9.2

* Sun Apr 01 2012 Bernhard Rosenkraenzer <bero@bero.eu> 0.9.1-1
+ Revision: 788563
- 0.9.1
- Fix rpmlint errors

* Mon Mar 05 2012 Bernhard Rosenkraenzer <bero@bero.eu> 0.9.0-1
+ Revision: 782193
- Update to 0.9.0
- Clean up spec file

* Thu Jan 05 2012 Bernhard Rosenkraenzer <bero@bero.eu> 0.8.1-1
+ Revision: 757917
- Update to 0.8.1

* Sun Apr 03 2011 Funda Wang <fwang@mandriva.org> 0.7.0-1
+ Revision: 650027
- new version 0.7.0

* Mon Mar 21 2011 Funda Wang <fwang@mandriva.org> 0.6.95-1
+ Revision: 647212
- update to new version 0.6.95

* Sun Feb 27 2011 Funda Wang <fwang@mandriva.org> 0.6.85-1
+ Revision: 640415
- new version 0.6.85

* Wed Feb 09 2011 Funda Wang <fwang@mandriva.org> 0.6.80-1
+ Revision: 637049
- New version 0.6.80

  + John Balcaen <mikala@mandriva.org>
    - Fix BuildRequires

* Mon Oct 11 2010 John Balcaen <mikala@mandriva.org> 0.6.1-1mdv2011.0
+ Revision: 584922
- Update to 0.6.1

* Sat Oct 02 2010 John Balcaen <mikala@mandriva.org> 0.6.0-1mdv2011.0
+ Revision: 582413
- Update to 0.6.0

* Sun Aug 22 2010 Funda Wang <fwang@mandriva.org> 0.5.80-1mdv2011.0
+ Revision: 571788
- update to new version 0.5.80

* Fri Jul 09 2010 Funda Wang <fwang@mandriva.org> 0.5.0-1mdv2011.0
+ Revision: 549885
- New version 0.5.0

* Sat Mar 13 2010 Funda Wang <fwang@mandriva.org> 0.4.0-1mdv2010.1
+ Revision: 518643
- new version 0.4.0

* Thu Feb 11 2010 Funda Wang <fwang@mandriva.org> 0.3.90-1mdv2010.1
+ Revision: 504123
- New version 0.3.90 (based on kdewebkit)

  + John Balcaen <mikala@mandriva.org>
    - Update patch1 (now use /usr/share/doc/HTML/index.html as default homepage)

* Fri Nov 27 2009 John Balcaen <mikala@mandriva.org> 0.3.0-2mdv2010.1
+ Revision: 470526
- Add a Requires against konqueror (package is currently providing cookies,proxy & web shorcut support for rekonq)
- add patch0 to change default bookmarks
- add patch1 to change default preview

* Thu Nov 26 2009 John Balcaen <mikala@mandriva.org> 0.3.0-1mdv2010.1
+ Revision: 470312
- Update to 0.3.0
- use %%find_lang macro
- fix some buildrequires

* Tue Oct 20 2009 Raphaël Gertz <rapsys@mandriva.org> 0.2.0-0.1mdv2010.0
+ Revision: 458489
- First release and import rekonq files
- Created package structure for rekonq.

