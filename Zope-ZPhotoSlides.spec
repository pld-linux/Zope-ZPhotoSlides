#
# WARNING: needed test on Zope 2.7.x and Plone 2.x
#
%define		zope_subname	ZPhotoSlides
Summary:	Product is a web photo gallery for the dynamic wev-based server Zope
Summary(pl):	Produkt umo¿liwiaj±cy tworzenie dynamicznych galerii zdjêæ dla Zope
Name:		Zope-%{zope_subname}
Version:	2.0
Release:	1
License:	GPL v2+
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/sourceforge/zphotoslides/%{zope_subname}-%{version}.tar.gz
# Source0-md5:	9dd96e47716ba4950d6b222cdd82edb3
URL:		http://www.zphotoslides.org/
%pyrequires_eq	python-modules
Requires:	python-Imaging
Requires:	Zope
Requires(post,postun):	/usr/sbin/installzopeproduct
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ZPhotoSlides is a web photo gallery for the dynamic wev-based server
Zope.

%description -l pl
ZPhotoSlides umo¿liwia tworzenie dynamicznych galerii zdjêæ dla
serwera Zope.

%prep
%setup -q -n %{zope_subname}
find . -type d -name CVS | xargs rm -rf

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -af {Extensions,dtml,help,i18n,photo_edition,www,zpt,country*,*.py,version.txt,refresh.txt} \
	$RPM_BUILD_ROOT%{_datadir}/%{name}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/installzopeproduct %{_datadir}/%{name} %{zope_subname}
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname}
	if [ -f /var/lock/subsys/zope ]; then
		/etc/rc.d/init.d/zope restart >&2
	fi
fi

%files
%defattr(644,root,root,755)
%doc CHANGES README TODO UPGRADE
%{_datadir}/%{name}
