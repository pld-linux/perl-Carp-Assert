#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Carp
%define		pnam	Assert
Summary:	Carp::Assert - executable comments
Summary(pl.UTF-8):	Carp::Assert - wykonywalne komentarze
Name:		perl-Carp-Assert
Version:	0.20
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Carp/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9dafe361b9e5e93e8e3e70e015f6b191
URL:		http://search.cpan.org/dist/Carp-Assert/
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-Pod-Tests >= 0.18
BuildRequires:	perl-Test-Simple >= 0.40
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Carp::Assert is intended for a purpose like the ANSI C library
assert.h. An assertion is used to prevent the impossible from being
asked of your code, or at least tell you when it does.

%description -l pl.UTF-8
Moduł Carp::Assert służy do tego, co assert.h z ANSI C. Używa się
zapewnień (assertion), aby wykluczyć występowanie rzeczy niemożliwych,
albo przynajmniej wiedzieć, gdzie się zdarzają.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Carp/Assert.pm
%{_mandir}/man3/*
