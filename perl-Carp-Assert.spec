#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Carp
%define		pnam	Assert
Summary:	Carp::Assert - executable comments
Summary(pl):	Carp::Assert - wykonywalne komentarze
Name:		perl-Carp-Assert
Version:	0.17
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6.1
%{!?_without_tests:BuildRequires:	perl-Test-Simple >= 0.18}
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Carp::Assert is intended for a purpose like the ANSI C library
assert.h. An assertion is used to prevent the impossible from being
asked of your code, or at least tell you when it does.

%description -l pl
Modu³ Carp::Assert s³u¿y do tego, co assert.h z ANSI C. U¿ywa siê
zapewnieñ (assertion), aby wykluczyæ wystêpowanie rzeczy niemo¿liwych,
albo przynajmniej wiedzieæ, gdzie siê zdarzaj±.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Carp
%{_mandir}/man3/*
