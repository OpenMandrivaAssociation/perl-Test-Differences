%define module	Test-Differences
%define name	perl-%{module}
%define version 0.48.01
%define up_version  0.4801
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Test strings and data structures and show differences if not ok 
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Test/%{module}-%{up_version}.tar.gz
BuildRequires:	perl-Text-Diff
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
When the code you're testing returns multiple lines, records or data structures
and they're just plain wrong, an equivalent to the Unix diff utility may be
just what's needed.

%prep
%setup -q -n %{module}-%{up_version}

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

