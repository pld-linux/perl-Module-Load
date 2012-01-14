#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Module
%define		pnam	Load
Summary:	Module::Load - runtime require of both modules and files
Summary(pl.UTF-8):	Module::Load - wymaganie zarówno modułów jak i plików w czasie działania programu
Name:		perl-Module-Load
Version:	0.22
Release:	1
# "same as perl"
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e3e83a51a4b7e2fdc6794b5a9e348a94
URL:		http://search.cpan.org/dist/Module-Load/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
# didn't found any required module, maybe i have to much installed to find
#BuildRequires:	perl-Fi
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl module Module::Load eliminates the need to know whether you are
trying to require either a file or a module. If you consult "perldoc
-f require" you will see that "require" will behave differently when
given a bareword or a string. In the case of a string, "require"
assumes you are wanting to load a file. But in the case of a bareword,
it assumes you mean a module. This gives nasty overhead when you are
trying to dynamically require modules at runtime, since you will need
to change the module notation ("Acme::Comment") to a file notation
fitting the particular platform you are on. This module elimates the
need for this overhead and will just DWYM.

%description -l pl.UTF-8
Moduł Perla Module::Load eliminuje potrzebę wiedzy, czy próbujemy
wczytać plik, czy moduł. Zgodnie z "perldoc -f require" instrukcja
"require" zachowuje się różnie w przypadku podania słowa i łańcucha. W
przypadku łańcucha "require" zakłada, że chcemy wczytać plik.
Natomiast w przypadku słowa, zakłada, ze chodzi o moduł. Daje to
dodatkowy narzut jeśli próbujemy dynamicznie wczytywać moduły w czasie
działania programu, ponieważ musimy zmieniać notację modułową
("Acme::Comment") na notację plikową dopasowując się do platformy. Ten
moduł eliminuje potrzebę tego narzutu i robi to, o co chodzi.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Module/Load.pm
%{_mandir}/man3/*
