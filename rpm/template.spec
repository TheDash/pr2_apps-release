Name:           ros-hydro-pr2-teleop-general
Version:        0.5.6
Release:        0%{?dist}
Summary:        ROS pr2_teleop_general package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/pr2_teleop_general
Source0:        %{name}-%{version}.tar.gz

Requires:       bullet-devel
Requires:       ros-hydro-actionlib
Requires:       ros-hydro-actionlib-msgs
Requires:       ros-hydro-angles
Requires:       ros-hydro-geometry-msgs
Requires:       ros-hydro-moveit-msgs
Requires:       ros-hydro-polled-camera
Requires:       ros-hydro-pr2-common-action-msgs
Requires:       ros-hydro-pr2-controller-manager
Requires:       ros-hydro-pr2-controllers-msgs
Requires:       ros-hydro-pr2-mechanism-msgs
Requires:       ros-hydro-pr2-msgs
Requires:       ros-hydro-ps3joy
Requires:       ros-hydro-roscpp
Requires:       ros-hydro-sensor-msgs
Requires:       ros-hydro-urdf
BuildRequires:  bullet-devel
BuildRequires:  ros-hydro-actionlib
BuildRequires:  ros-hydro-actionlib-msgs
BuildRequires:  ros-hydro-angles
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-geometry-msgs
BuildRequires:  ros-hydro-moveit-msgs
BuildRequires:  ros-hydro-polled-camera
BuildRequires:  ros-hydro-pr2-common-action-msgs
BuildRequires:  ros-hydro-pr2-controller-manager
BuildRequires:  ros-hydro-pr2-controllers-msgs
BuildRequires:  ros-hydro-pr2-mechanism-msgs
BuildRequires:  ros-hydro-pr2-msgs
BuildRequires:  ros-hydro-ps3joy
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-sensor-msgs
BuildRequires:  ros-hydro-urdf

%description
pr2_teleop_general

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
* Sun Sep 07 2014 Gil Jones <gil@willowgarage.com> - 0.5.6-0
- Autogenerated by Bloom

