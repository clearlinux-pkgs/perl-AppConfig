#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-AppConfig
Version  : 1.71
Release  : 6
URL      : https://cpan.metacpan.org/authors/id/N/NE/NEILB/AppConfig-1.71.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/N/NE/NEILB/AppConfig-1.71.tar.gz
Summary  : 'AppConfig is a bundle of Perl5 modules for reading configuration files and parsing command line arguments.'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-2.0
Requires: perl-AppConfig-license = %{version}-%{release}
Requires: perl-AppConfig-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Test::Pod)

%description
A Perl 5 module for reading configuration files and parsing command line
arguments.

%package dev
Summary: dev components for the perl-AppConfig package.
Group: Development
Provides: perl-AppConfig-devel = %{version}-%{release}
Requires: perl-AppConfig = %{version}-%{release}

%description dev
dev components for the perl-AppConfig package.


%package license
Summary: license components for the perl-AppConfig package.
Group: Default

%description license
license components for the perl-AppConfig package.


%package perl
Summary: perl components for the perl-AppConfig package.
Group: Default
Requires: perl-AppConfig = %{version}-%{release}

%description perl
perl components for the perl-AppConfig package.


%prep
%setup -q -n AppConfig-1.71
cd %{_builddir}/AppConfig-1.71

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-AppConfig
cp %{_builddir}/AppConfig-1.71/LICENSE %{buildroot}/usr/share/package-licenses/perl-AppConfig/f11692fc652e231edd2a23a60c72d9be8a840e0c
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/AppConfig.3
/usr/share/man/man3/AppConfig::Args.3
/usr/share/man/man3/AppConfig::CGI.3
/usr/share/man/man3/AppConfig::File.3
/usr/share/man/man3/AppConfig::Getopt.3
/usr/share/man/man3/AppConfig::State.3
/usr/share/man/man3/AppConfig::Sys.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-AppConfig/f11692fc652e231edd2a23a60c72d9be8a840e0c

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/AppConfig.pm
/usr/lib/perl5/vendor_perl/5.34.0/AppConfig/Args.pm
/usr/lib/perl5/vendor_perl/5.34.0/AppConfig/CGI.pm
/usr/lib/perl5/vendor_perl/5.34.0/AppConfig/File.pm
/usr/lib/perl5/vendor_perl/5.34.0/AppConfig/Getopt.pm
/usr/lib/perl5/vendor_perl/5.34.0/AppConfig/State.pm
/usr/lib/perl5/vendor_perl/5.34.0/AppConfig/Sys.pm
