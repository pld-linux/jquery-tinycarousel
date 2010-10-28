%define		plugin	tinycarousel
Summary:	Tiny Carousel is a lightweight jQuery based carousel for sliding HTML based content
Name:		jquery-%{plugin}
Version:	1.77
Release:	1
License:	MIT / GPL
Group:		Applications/WWW
Source0:	http://www.baijs.nl/tinycarousel/js/jquery.tinycarousel.min.js
# Source0-md5:	82d69f50b1e9b653a41592e31550c5f3
URL:		http://baijs.nl/tinycarousel/
BuildRequires:	rpmbuild(macros) > 1.268
Requires:	jquery >= 1.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/%{plugin}

%description
Tiny Carousel is a lightweight carousel for sliding html based
content. It was built using the javascript jQuery library. Tiny
Carousel was designed to be a dynamic lightweight utility that gives
webdesigners a powerfull way of enhancing a websites user interface.

%prep
%setup -qcT

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -a %{SOURCE0} $RPM_BUILD_ROOT%{_appdir}/%{plugin}.js

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_appdir}
