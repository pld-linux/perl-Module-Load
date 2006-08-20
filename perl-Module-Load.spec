#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Module
%define		pnam	Load
Summary:	Module::Load - runtime require of both modules and files
Summary(pl):	Module::Load - wymaganie zarówno modu³ów jak i plików w czasie dzia³ania programu
Name:		perl-Module-Load
Version:	0.10
Release:	0.1
# "same as perl"
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ee40eb2fa3059381e43d1f14d414fe67
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

%description -l pl
Modu³ Perla Module::Load eliminuje potrzebê wiedzy, czy próbujemy
wczytaæ plik, czy modu³. Zgodnie z "perldoc -f require" instrukcja
"require" zachowuje siê ró¿nie w przypadku podania s³owa i ³añcucha. W
przypadku ³añcucha "require" zak³ada, ¿e chcemy wczytaæ plik.
Natomiast w przypadku s³owa, zak³ada, ze chodzi o modu³. Daje to
dodatkowy narzut je¶li próbujemy dynamicznie wczytywaæ modu³y w czasie
dzia³ania programu, poniewa¿ musimy zmieniaæ notacjê modu³ow±
("Acme::Comment") na notacjê plikow± dopasowuj±c siê do platformy. Ten
modu³ eliminuje potrzebê tego narzutu i robi to, o co chodzi.

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
