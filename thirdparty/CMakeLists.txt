add_subdirectory(gtest)

# build zeromq
add_custom_target(zeromq ALL DEPENDS)
if (EXISTS ${CMAKE_CURRENT_SOURCE_DIR}/zeromq/src/.libs/libzmq.so)
    add_custom_command(TARGET zeromq
	PRE_BUILD
	COMMAND
	echo "ZeroMQ Is Builded"
	COMMENT "Build ZeroMQ")
else()
    add_custom_command(TARGET zeromq
	PRE_BUILD
	COMMAND
	cd ${CMAKE_CURRENT_SOURCE_DIR}/zeromq/ && ./autogen.sh && ./configure --prefix=${CMAKE_INSTALL_PREFIX} && make -j 4
	COMMENT "Build ZeroMQ")
endif()

add_library(libzeromq SHARED IMPORTED GLOBAL)
set_target_properties(libzeromq PROPERTIES IMPORTED_LOCATION
    ${CMAKE_CURRENT_SOURCE_DIR}/zeromq/src/.libs/libzmq.so)

# build openmpi
add_custom_target(ompi ALL DEPENDS)
if (EXISTS ${CMAKE_CURRENT_SOURCE_DIR}/ompi/ompi/.libs/libmpi.so)
    add_custom_command(TARGET ompi
	PRE_BUILD
	COMMAND
	echo "OMPI Is Builded"
	COMMENT "Build MPI")
else()
    add_custom_command(TARGET ompi
	PRE_BUILD
	COMMAND
	cd ${CMAKE_CURRENT_SOURCE_DIR}/ompi/ && ./autogen.pl && ./configure --prefix=${CMAKE_INSTALL_PREFIX} --enable-mpi-fortran=no && make -j 4
	COMMENT "Build OMPI")
endif()

add_library(libompi SHARED IMPORTED GLOBAL)
set_target_properties(libompi PROPERTIES IMPORTED_LOCATION
    ${CMAKE_CURRENT_SOURCE_DIR}/ompi/ompi/.libs/libmpi.so)

install(CODE "execute_process(COMMAND sh ${CMAKE_CURRENT_SOURCE_DIR}/install.sh)")
