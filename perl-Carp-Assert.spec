%include	/usr/lib/rpm/macros.perl
%define		pdir	Carp
%define		pnam	Assert
Summary:	Carp::Assert Perl module
Summary(cs):	Modul Carp::Assert pro Perl
Summary(da):	Perlmodul Carp::Assert
Summary(de):	Carp::Assert Perl Modul
Summary(es):	Módulo de Perl Carp::Assert
Summary(fr):	Module Perl Carp::Assert
Summary(it):	Modulo di Perl Carp::Assert
Summary(ja):	Carp::Assert Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Carp::Assert ÆŞ ¸ğÁÙ
Summary(no):	Perlmodul Carp::Assert
Summary(pl):	Modu³ Perla Carp::Assert
Summary(pt):	Módulo de Perl Carp::Assert
Summary(pt_BR):	Módulo Perl Carp::Assert
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Carp::Assert
Summary(sv):	Carp::Assert Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Carp::Assert
Summary(zh_CN):	Carp::Assert Perl Ä£¿é
Name:		perl-Carp-Assert
Version:	0.17
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Carp::Assert perl module.

%description -l cs
Modul Carp::Assert pro Perl.

%description -l da
Perlmodul Carp::Assert.

%description -l de
Carp::Assert Perl Modul.

%description -l es
Módulo de Perl Carp::Assert.

%description -l fr
Module Perl Carp::Assert.

%description -l it
Modulo di Perl Carp::Assert.

%description -l ja
Carp::Assert Perl ¥â¥¸¥å¡¼¥ë

%description -l ko
Carp::Assert ÆŞ ¸ğÁÙ.

%description -l no
Perlmodul Carp::Assert.

%description -l pl
Modu³ perla Carp::Assert.

%description -l pt
Módulo de Perl Carp::Assert.

%description -l pt_BR
Módulo Perl Carp::Assert.

%description -l ru
íÏÄÕÌØ ÄÌÑ Perl Carp::Assert.

%description -l sv
Carp::Assert Perlmodul.

%description -l uk
íÏÄÕÌØ ÄÌÑ Perl Carp::Assert.

%description -l zh_CN
Carp::Assert Perl Ä£¿é

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/Carp
%{_mandir}/man3/*
