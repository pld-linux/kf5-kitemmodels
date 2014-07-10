# TODO:
# - dir /usr/include/KF5 not packaged
%define         _state          stable
%define		orgname		kitemmodels

Summary:	Set of item models extending the Qt model-view framework
Name:		kf5-%{orgname}
Version:	5.0.0
Release:	0.1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/frameworks/%{version}/%{orgname}-%{version}.tar.xz
# Source0-md5:	c1bb781f39b2c6d232a0fb490f2aa9dc
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5Gui-devel >= 5.3.1
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5Widgets-devel >= 5.2.0
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= 1.0.0
BuildRequires:	qt5-linguist
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
Summary:	Header files for %{orgname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{orgname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{orgname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{orgname}.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	-DBIN_INSTALL_DIR=%{_bindir} \
	-DKCFG_INSTALL_DIR=%{_datadir}/config.kcfg \
	-DPLUGIN_INSTALL_DIR=%{qt5dir}/plugins \
	-DQT_PLUGIN_INSTALL_DIR=%{qt5dir}/plugins \
	-DQML_INSTALL_DIR=%{qt5dir}/qml \
	-DIMPORTS_INSTALL_DIR=%{qt5dirs}/imports \
	-DSYSCONF_INSTALL_DIR=%{_sysconfdir} \
	-DLIBEXEC_INSTALL_DIR=%{_libexecdir} \
	-DKF5_LIBEXEC_INSTALL_DIR=%{_libexecdir} \
	-DKF5_INCLUDE_INSTALL_DIR=%{_includedir} \
	-DECM_MKSPECS_INSTALL_DIR=%{qt5dir}/mkspecs/modules \
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
%attr(755,root,root) %{_libdir}/libKF5ItemModels.so.5.0.0

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/KItemModels
%{_includedir}/KF5/kitemmodels_version.h
%{_libdir}/cmake/KF5ItemModels
%attr(755,root,root) %{_libdir}/libKF5ItemModels.so
%{qt5dir}/mkspecs/modules/qt_KItemModels.pri
