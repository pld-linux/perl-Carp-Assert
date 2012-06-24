%include	/usr/lib/rpm/macros.perl
Summary:	Carp-Assert perl module
Summary(pl):	Modu� perla Carp-Assert
Name:		perl-Carp-Assert
Version:	0.08
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Carp/Carp-Assert-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Carp-Assert perl module

%description -l pl
Modu� perla Carp-Assert

%prep
%setup -q -n Carp-Assert-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Carp/Assert
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%{perl_sitelib}/Carp/Assert.pm
%{perl_sitearch}/auto/Carp/Assert

%{_mandir}/man3/*
