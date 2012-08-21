Summary: X Athena Widget Set
Name: libXaw
Version: 1.0.11
Release: 1
License: MIT
URL: http://www.x.org
Group: System Environment/Libraries

Source0: %{name}-%{version}.tar.gz

BuildRequires: pkgconfig(xproto) pkgconfig(x11) pkgconfig(xt)
BuildRequires: pkgconfig(xmu) pkgconfig(xpm) pkgconfig(xext)
BuildRequires:  pkgconfig(xorg-macros)
# Required by the configury.
BuildRequires: ed
BuildRequires: xorg-x11-xutils-dev

%description
Xaw is a widget set based on the X Toolkit Intrinsics (Xt) Library.

%package devel
Summary: Development files for %{name}
Group: Development/Libraries
Provides: libxaw-devel 
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig
Requires: pkgconfig(xproto) pkgconfig(xmu) pkgconfig(xt) pkgconfig(xpm)

%description devel
X.Org X11 libXaw development package

%prep
%setup -q

%build
export CFLAGS="${CFLAGS} $RPM_OPT_FLAGS -Os"
%reconfigure \
           LDFLAGS="${LDFLAGS} -Wl,--hash-style=both -Wl,--as-needed" \
	       --disable-xaw8 --disable-static \
	       --disable-xaw6
make %{?jobs:-j%jobs}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%remove_docs

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING README ChangeLog
%{_libdir}/libXaw.so.7
%{_libdir}/libXaw7.so.7
%{_libdir}/libXaw7.so.7.0.0

%files devel
%defattr(-,root,root,-)
%dir %{_includedir}/X11/Xaw
%doc COPYING
%{_includedir}/X11/Xaw/*.h
# FIXME:  Is this C file really supposed to be here?
%{_includedir}/X11/Xaw/Template.c
%{_libdir}/libXaw.so
%{_libdir}/libXaw7.so
%{_libdir}/pkgconfig/xaw7.pc
#%{_mandir}/man3/*.3*
#%dir %{_docdir}/%{name}-%{version}-%{release}
#%{_docdir}/%{name}-%{version}-%{release}/*.xml
#{_docdir}/%{name}-%{version}-%{release}/%{name}.html
#{_docdir}/%{name}-%{version}-%{release}/%{name}.txt