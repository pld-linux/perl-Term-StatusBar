#
# Conditional build:
%bcond_without	tests	# do perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Term
%define		pnam	StatusBar
Summary:	Term::StatusBar - dynamic progress bar
Summary(pl.UTF-8):   Term::StatusBar - dynamiczny pasek postępu
Name:		perl-Term-StatusBar
Version:	1.18
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9203efb3f76e6c4ac986a393b9df657e
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Term::StatusBar provides an easy way to create a terminal status bar,
much like those found in a graphical environment. Term::Size is used
to ensure the bar does not extend beyond the terminal's width. All
output is sent to STDOUT by default.

%description -l pl.UTF-8
Term::StatusBar udostępnia łatwy sposób tworzenia na terminalu paska
stanu podobnego do tych, które można zobaczyć w graficznym środowisku.
Używa Term::Size do zapewnienia, żeby pasek nie przekroczył szerokości
terminala. Całe wyjście domyślnie jest kierowane na STDOUT.

%prep
%setup -q -n %{pdir}-%{pnam}

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
%{perl_vendorlib}/Term/StatusBar.pm
%{_mandir}/man3/*
