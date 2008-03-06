%define module	Test-Differences
%define name	perl-%{module}
%define version 0.47
%define release %mkrel 4

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Test strings and data structures and show differences if not ok 
License:	GPL or Artistic
Group:		Development/Perl
Source:		http://search.cpan.org/CPAN/authors/id/R/RB/RBS/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
BuildRequires:	perl-Text-Diff
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
When the code you're testing returns multiple lines, records or data structures
and they're just plain wrong, an equivalent to the Unix diff utility may be
just what's needed.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%clean 
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/Test
%{_mandir}/*/*

