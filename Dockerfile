#
# Dockerfile to build latest upstream qemu master.
#
FROM centos:centos7

#
# Update yum and install required packages.
#
RUN yum -y update
RUN yum install -y git glib2 glib2-devel pixman-devel zlib-devel bzip2 python3 libaio-devel libcap-devel libiscsi-devel make gcc rpmdevtools rpmlint centos-release-scl scl-utils
RUN yum install -y devtoolset-8
RUN pip3 install --upgrade pip
RUN pip3 install ninja==1.8.2

#
# Setting devtoolset-8/gcc as the default.
#
ENV PATH /opt/rh/devtoolset-8/root/usr/bin:$PATH

#
# Configure and build qemu.
#
WORKDIR /rpmbuild

CMD /bin/sh
