Name:           ros-hydro-pr2-position-scripts
Version:        0.5.9
Release:        0%{?dist}
Summary:        ROS pr2_position_scripts package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/pr2_position_scripts
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-actionlib
Requires:       ros-hydro-pr2-controllers-msgs
Requires:       ros-hydro-rospy
Requires:       ros-hydro-tf
BuildRequires:  ros-hydro-actionlib
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-pr2-controllers-msgs
BuildRequires:  ros-hydro-rospy
BuildRequires:  ros-hydro-tf

%description
This package contains a number of scripts to set various components of the PR2.
They are used in the apps to improve usablity.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Wed Oct 01 2014 Tony Pratkanis <tony@willowgarage.com> - 0.5.9-0
- Autogenerated by Bloom

* Mon Sep 08 2014 Tony Pratkanis <tony@willowgarage.com> - 0.5.6-1
- Autogenerated by Bloom

* Sun Sep 07 2014 Tony Pratkanis <tony@willowgarage.com> - 0.5.6-0
- Autogenerated by Bloom

