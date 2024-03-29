%define modname	Test-Differences
%define modver 0.69

Summary:	Test strings and data structures and show differences if not ok 
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	2
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://metacpan.org/pod/Test::Differences
Source0:	http://www.cpan.org/modules/by-module/Test/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test)
BuildRequires:	perl-Text-Diff
BuildRequires:	perl(Capture::Tiny)
BuildRequires:	perl-devel

%description
When the code you're testing returns multiple lines, records or data structures
and they're just plain wrong, an equivalent to the Unix diff utility may be
just what's needed.

%prep
%setup -qn %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes
%{perl_vendorlib}/Test
%{_mandir}/man3/*
