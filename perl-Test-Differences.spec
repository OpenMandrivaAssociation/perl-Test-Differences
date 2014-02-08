%define upstream_name	 Test-Differences
%define upstream_version 0.61

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Test strings and data structures and show differences if not ok 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-Text-Diff
BuildRequires:	perl-devel
BuildArch:	noarch

%description
When the code you're testing returns multiple lines, records or data structures
and they're just plain wrong, an equivalent to the Unix diff utility may be
just what's needed.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes
%{perl_vendorlib}/Test
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.610.0-3mdv2012.0
+ Revision: 765677
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.610.0-2
+ Revision: 764189
- rebuilt for perl-5.14.x

* Sat Jun 25 2011 Shlomi Fish <shlomif@mandriva.org> 0.610.0-1
+ Revision: 687178
- New version - 0.61

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.500.0-3
+ Revision: 667324
- mass rebuild

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.500.0-2mdv2011.0
+ Revision: 555308
- rebuild

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.500.0-1mdv2010.1
+ Revision: 460993
- update to 0.500

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.480.100-1mdv2010.0
+ Revision: 405549
- rebuild using %%perl_convert_version

* Sun Aug 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.48.01-1mdv2009.0
+ Revision: 270510
- new version

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.47-5mdv2009.0
+ Revision: 224134
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 0.47-4mdv2008.1
+ Revision: 180592
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat May 05 2007 Olivier Thauvin <nanardon@mandriva.org> 0.47-3mdv2008.0
+ Revision: 23307
- rebuild


* Sun Mar 12 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.47-2mdk
- %%mkrel

* Fri Mar 04 2005 Guillaume Rousse <guillomovitch@mandrake.org> 0.47-1mdk 
- first mdk release

