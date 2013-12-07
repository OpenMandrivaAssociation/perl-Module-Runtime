%define modname	Module-Runtime
%define modver	0.013

Summary:	Runtime module handling
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	4
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Module/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
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

%description
The functions exported by this module deal with runtime handling of Perl
modules, which are normally handled at compile time.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

