Summary: Interface between a chess engine and FICS
Name: icsdroneng
Version: 0.29
Release: 1
License: GPL
Group: Amusement/Games
URL: http://alpha.uhasselt.be/Research/Algebra

Source: http://alpha.uhasselt.be/Research/Algebra/Toga/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
 icsdroneng acts as an interface between a chess engine 
 and FICS (the Free Internet Chess Server). It knows how 
 to create games, ask people to continue any adjourned 
 games, ask for games when bored and much more.  The 
 engine itself can be administrated or configured 
 remotely.

%prep
%setup

%build
%configure 
%{__make}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc %{_mandir}/man6/icsdrone.6* 
%doc %{_docdir}/%{name}/README*
%doc %{_docdir}/%{name}/THANKS_old 
%doc %{_docdir}/%{name}/ChangeLog_old 
%{_bindir}/icsdrone

%changelog
* Sat May 22 2009 Michel Van den Bergh <michel.vandenbergh@uhasselt.be> - %{version}-%{release}
- Initial spec file

