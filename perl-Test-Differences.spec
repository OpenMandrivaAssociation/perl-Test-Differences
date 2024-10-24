%define modname	Test-Differences

Summary:	Test strings and data structures and show differences if not ok 
Name:		perl-%{modname}
Version:	0.71
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/pod/Test::Differences
Source0:	http://www.cpan.org/modules/by-module/Test/%{modname}-%{version}.tar.gz
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
%autosetup -p1 -n %{modname}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%make_install

%files
%doc Changes
%{perl_vendorlib}/Test
%{_mandir}/man3/*
