#
# WARNING: needed test on Zope 2.7.x and Plone 2.x
#
%define		zope_subname	ZPhotoSlides
Summary:	Product is a web photo gallery for the dynamic wev-based server Zope
Summary(pl.UTF-8):	Produkt umożliwiający tworzenie dynamicznych galerii zdjęć dla Zope
Name:		Zope-%{zope_subname}
Version:	2.0
Release:	3
License:	GPL v2+
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/zphotoslides/%{zope_subname}-%{version}.tar.gz
# Source0-md5:	9dd96e47716ba4950d6b222cdd82edb3
URL:		http://www.zphotoslides.org/
BuildRequires:	python
BuildRequires:	rpmbuild(macros) >= 1.268
%pyrequires_eq	python-modules
Requires(post,postun):	/usr/sbin/installzopeproduct
Requires:	Zope
Requires:	python-Imaging
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ZPhotoSlides is a web photo gallery for the dynamic wev-based server
Zope.

%description -l pl.UTF-8
ZPhotoSlides umożliwia tworzenie dynamicznych galerii zdjęć dla
serwera Zope.

%prep
%setup -q -n %{zope_subname}
find . -type d -name CVS | xargs rm -rf

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -af {Extensions,dtml,help,i18n,photo_edition,skins,www,zpt,country*,*.py,version.txt,refresh.txt} \
	$RPM_BUILD_ROOT%{_datadir}/%{name}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/installzopeproduct %{_datadir}/%{name} %{zope_subname}
%service -q zope restart

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname}
	%service -q zope restart
fi

%files
%defattr(644,root,root,755)
%doc CHANGES README TODO UPGRADE
%{_datadir}/%{name}
