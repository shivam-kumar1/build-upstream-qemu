#
# Dockerfile to build latest upstream qemu master.
#
FROM quay.io/centos/centos:stream9

#
# Update yum and install required packages.
#
RUN sed -i 's|enabled=0|enabled=1|g' /etc/yum.repos.d/centos*.repo
RUN yum -y update
RUN yum install -y git glib2 glib2-devel pixman-devel zlib-devel bzip2 \
                   python3.9 libaio-devel libcap-devel libiscsi-devel make gcc \
                   rpmdevtools rpmlint python-pip flex bison
RUN pip3 install --upgrade pip
RUN pip3 install ninja tomli

#
# Configure and build qemu.
#
WORKDIR /rpmbuild

CMD /bin/sh
