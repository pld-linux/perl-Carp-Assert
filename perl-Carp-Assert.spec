%include	/usr/lib/rpm/macros.perl
Summary:	Carp-Assert perl module
Summary(pl):	Modu³ perla Carp-Assert
Name:		perl-Carp-Assert
Version:	0.16
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Carp/Carp-Assert-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Carp-Assert perl module.

%description -l pl
Modu³ perla Carp-Assert.

%prep
%setup -q -n Carp-Assert-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Carp/Assert.pm
%{_mandir}/man3/*
