%define		kdeframever	5.19
%define		qtver		5.3.2
%define		kfname		kitemmodels

Summary:	Set of item models extending the Qt model-view framework
Name:		kf5-%{kfname}
Version:	5.19.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	acf477f070df240248cb7eab316ff370
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Test-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= 1.0.0
BuildRequires:	qt5-linguist >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
KItemModels provides the following models:

- KBreadcrumbSelectionModel - Selects the parents of selected items to
  create breadcrumbs
- KCheckableProxyModel - Adds a checkable capability to a source model
- KDescendantsProxyModel - Proxy Model for restructuring a Tree into a
  list
- KLinkItemSelectionModel - Share a selection in multiple views which
  do not have the same source model
- KModelIndexProxyMapper - Mapping of indexes and selections through
  proxy models
- KRecursiveFilterProxyModel - Recursive filtering of models
- KSelectionProxyModel - A Proxy Model which presents a subset of its
  source model to observers

%package devel
Summary:	Header files for %{kfname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kfname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%prep
%setup -q -n %{kfname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %ghost %{_libdir}/libKF5ItemModels.so.5
%attr(755,root,root) %{_libdir}/libKF5ItemModels.so.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/KItemModels
%{_includedir}/KF5/kitemmodels_version.h
%{_libdir}/cmake/KF5ItemModels
%attr(755,root,root) %{_libdir}/libKF5ItemModels.so
%{qt5dir}/mkspecs/modules/qt_KItemModels.pri
