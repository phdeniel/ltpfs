Summary: Linux Test Project (LTP) Software Development Kit (SDK)
Name: ltp
Version: 2.0
Release: 0.0%{?dist}
Group: Development/Libraries
License: GPLv2
URL: http://www.linuxtestproject.org
Packager: Philippe Deniel <philippe.deniel@cea.fr>
Provides: LTP
Source: http://sourceforge.net/projects/ltp/files/ltp-20130503/ltp.tar.gz

%define debug_package %{nil}

%description
This is a package of the Linux Test Project (LTP).


%prep
%setup -q -n %{name}-%{version}

%build
%configure
make -i 

%install
rm -rf %{buildroot} 
mkdir -p %{buildroot}
make -i install DESTDIR=%{buildroot}
mkdir %{buildroot}/opt
mv %{buildroot}/usr %{buildroot}/opt/ltp



%files 
/opt/ltp/*

%clean
[ $RPM_BUILD_ROOT != "/" ] && rm -fr $RPM_BUILD_ROOT


