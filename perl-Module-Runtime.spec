%define upstream_name    Module-Runtime
%define upstream_version 0.013

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    2

Summary:    Runtime module handling
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Module/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(Exporter)
BuildRequires: perl(Math::Complex)
BuildRequires: perl(Math::Trig)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Test::More)
BuildRequires: perl(parent)
BuildRequires: perl(strict)
BuildRequires: perl(warnings)
BuildRequires: perl(Module::Build::Compat)
BuildRequires: perl(Params::Classify)
BuildArch: noarch

%description
The functions exported by this module deal with runtime handling of Perl
modules, which are normally handled at compile time.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Thu Feb 02 2012 Bernhard Rosenkraenzer <bero@bero.eu> 0.11.0-1
+ Revision: 770666
- Build for perl 5.14.x, Update to 0.011

* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 0.7.0-3
+ Revision: 653600
- rebuild for updated spec-helper

* Sat Aug 28 2010 Shlomi Fish <shlomif@mandriva.org> 0.7.0-2mdv2011.0
+ Revision: 573834
- Bump the release number and add Params::Classify to the requires
- import perl-Module-Runtime

