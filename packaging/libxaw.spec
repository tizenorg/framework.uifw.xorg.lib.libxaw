
Name:       libxaw
Summary:    X.Org X11 libXaw runtime library
Version:    1.0.8
Release:    2.7
Group:      System/Libraries
License:    MIT
URL:        http://www.x.org/
Source0:    http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.gz
Source101:  libxaw-rpmlintrc
Source1001: packaging/libxaw.manifest 
Patch1:     01_Xaw_StripChart_fix.diff
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xpm)

%description
Description: %{summary}


%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Description: %{summary}

%prep
%setup -q -n %{name}-%{version}

# 01_Xaw_StripChart_fix.diff
%patch1 -p1


%build
cp %{SOURCE1001} .
export LDFLAGS+=" -Wl,--hash-style=both -Wl,--as-needed"
%reconfigure --disable-xaw6 --disable-xaw8

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

rm -rf %{buildroot}/%{_datadir}/doc/libXaw



%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig






%files
%manifest libxaw.manifest
%defattr(-,root,root,-)
%doc COPYING README ChangeLog
%{_libdir}/libXaw.so.7
%{_libdir}/libXaw7.so.7
%{_libdir}/libXaw7.so.7.0.0


%files devel
%manifest libxaw.manifest
%defattr(-,root,root,-)
%dir %{_includedir}/X11
%dir %{_includedir}/X11/Xaw
%doc COPYING
%{_includedir}/X11/Xaw/*.h
%{_includedir}/X11/Xaw/Template.c
%{_libdir}/libXaw.so
%{_libdir}/libXaw7.so
%{_libdir}/pkgconfig/xaw7.pc
%{_mandir}/man3/*.3*


