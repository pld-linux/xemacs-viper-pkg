Summary:	VI emulation support
Summary(pl):	VI emulation support
Name:		xemacs-viper-pkg
%define 	srcname	viper
Version:	1.18
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Source0:	ftp://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
Patch0:		xemacs-viper-pkg-info.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl 

%prep
%setup -q -c
%patch0 -p1

%build
(cd man/viper; awk '/^\\input texinfo/ {print FILENAME}' * | xargs makeinfo)

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages
cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages
install -d $RPM_BUILD_ROOT%{_infodir}
mv -f  $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/info/*.info* $RPM_BUILD_ROOT%{_infodir}
rm -fr $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/info

gzip -9nf $RPM_BUILD_ROOT%{_infodir}/*.info* \
	lisp/viper/README lisp/viper/ChangeLog 

%clean
rm -fr $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%{_datadir}/xemacs-packages%{_sysconfdir}/*
%{_infodir}/*
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.elc
%doc lisp/viper/README.gz lisp/viper/ChangeLog.gz
