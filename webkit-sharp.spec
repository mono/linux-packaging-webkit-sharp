#
# spec file for package webkit-sharp
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#
%define _version 0.3

Name:           webkit-sharp
Url:            http://www.go-mono.org/
BuildRequires:  automake
BuildRequires:  gtk-sharp2
BuildRequires:  gtk-sharp2-gapi
BuildRequires:  mono-devel
BuildRequires:  monodoc-core
%if 0%{?fedora} || 0%{?rhel} || 0%{?centos}
BuildRequires: webkitgtk-devel
%else
%if 0%{?suse_version} >= 1140
BuildRequires:  libwebkitgtk-devel
%else
BuildRequires:  libwebkit-devel
%endif
%endif
License:        MIT
Group:          Development/Languages/Mono
Summary:        WebKit bindings for Mono
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Version:	0.3
Release:	0.xamarin.1
BuildArch:      noarch
Source:         %{name}_%{version}.orig.tar.gz
Patch0:         %{name}-pkgconfigdir.patch
Patch1:         %{name}-0.3.diff
%if 0%{?suse_version} >= 1140
Requires:       libwebkitgtk-1_0-0
%else
%if 0%{?suse_version} >= 1120
Requires:       libwebkit-1_0-2
%else
Requires:       libwebkit-1_0-1
%endif
%endif

%description
WebKit is a web content engine, derived from KHTML and KJS from KDE,
and used primarily in Apple's Safari browser. It is made to be embedded
in other applications, such as mail readers, or web browsers.

This package provides Mono bindings for WebKit libraries.



Authors:
--------
    Everaldo Canuto <ecanuto@novell.com>

%prep
%setup -q
%patch0
%if 0%{?suse_version} >= 1140
%patch1 -p1
%endif

%build
autoreconf
./configure --prefix=%{_prefix} --libdir=%{_prefix}/lib
make

%install
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc AUTHORS COPYING README
%{_prefix}/lib/mono/gac/webkit-sharp
%{_prefix}/lib/mono/webkit-sharp
%{_prefix}/lib/monodoc/sources/webkit-sharp-docs*
%{_datadir}/pkgconfig/webkit-sharp-1.0.pc

%changelog

