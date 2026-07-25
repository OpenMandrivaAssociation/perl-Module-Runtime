%define modname Module-Runtime
%define modver 0.018

Summary:	Runtime module handling
Name:		perl-%{modname}
Version:	%{modver}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://github.com/haarg/Module-Runtime
Source0:	https://cpan.metacpan.org/authors/id/H/HA/HAARG/Module-Runtime-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl(Carp)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(Math::Complex)
BuildRequires:	perl(Math::Trig)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(parent)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
BuildRequires:	perl(Module::Build::Compat)
BuildRequires:	perl(Params::Classify)
BuildRequires:	perl(JSON::PP)

%description
The functions exported by this module deal with runtime handling of Perl
modules, which are normally handled at compile time.

%prep
%autosetup -p1 -n %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
%make test

%install
%make_install

%files
%doc Changes README
%{perl_vendorlib}/*
%doc %{_mandir}/man3/*
