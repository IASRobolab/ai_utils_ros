cmake_minimum_required(VERSION 3.5)
project(ai_utils_ros)

find_package(catkin REQUIRED rospy std_msgs sensor_msgs cv_bridge)

catkin_python_setup()

catkin_package(DEPENDS rospy sensor_msgs sensor_msgs cv_bridge)

install(DIRECTORY launch/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch
  PATTERN ".svn" EXCLUDE)

install(DIRECTORY config/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/config
  PATTERN ".svn" EXCLUDE)
  
install(DIRECTORY weights/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/weights
  PATTERN ".svn" EXCLUDE)

install(DIRECTORY scripts/
        DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
        USE_SOURCE_PERMISSIONS
        PATTERN ".svn" EXCLUDE)
