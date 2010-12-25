%define upstream_name    LWPx-ParanoidAgent
%define upstream_version 1.07

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Paranoid subclass of LWP::UserAgent
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/LWPx/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(Net::DNS)
BuildRequires: perl(Time::HiRes)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc ChangeLog META.yml
%{_mandir}/man3/*
%perl_vendorlib/*


