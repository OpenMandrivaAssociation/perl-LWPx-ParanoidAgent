%define upstream_name    LWPx-ParanoidAgent
%define upstream_version 1.09

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 1.09
Release:	1

Summary:	Paranoid subclass of LWP::UserAgent
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/LWPx/LWPx-ParanoidAgent-1.09.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(Net::DNS)
BuildRequires:	perl(Time::HiRes)
BuildArch:	noarch

%description
The 'LWPx::ParanoidAgent' is a class subclassing 'LWP::UserAgent', but
paranoid against attackers. It's to be used when you're fetching a remote
resource on behalf of a possibly malicious user.

This class can do whatever 'LWP::UserAgent' can (callbacks, uploads from
files, etc), except proxy support is explicitly removed, because in that
case you should do your paranoia at your proxy.

Also, the schemes are limited to http and https, which are mapped to
'LWPx::Protocol::http_paranoid' and 'LWPx::Protocol::https_paranoid',
respectively, which are forked versions of the same ones without the
"_paranoid". Subclassing them didn't look possible, as they were
essentially just one huge function.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# Fail on ABF
#make test

%install
%makeinstall_std

%files
%doc ChangeLog META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Dec 25 2010 Shlomi Fish <shlomif@mandriva.org> 1.70.0-1mdv2011.0
+ Revision: 624861
- import perl-LWPx-ParanoidAgent


