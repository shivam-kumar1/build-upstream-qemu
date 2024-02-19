SELF_DIR := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
CONTAINER_NAME := "QEMU_BUILD"

MAKE_SCRIPT := "cd /rpmbuild/SOURCES/qemu && ./configure --target-list=x86_64-softmmu --enable-debug && make -j $(nproc) && cd /rpmbuild/SOURCES && mv qemu/build qemu-upstream-1.0 && tar --create --file qemu-upstream-1.0.tar.gz qemu-upstream-1.0 && rm -rf qemu-upstream-1.0 && rpmbuild --define \"_topdir /rpmbuild\" -v -ba /rpmbuild/SPECS/qemu-upstream.spec"

all:
	docker rm -f $(CONTAINER_NAME)
	docker run -itv $(SELF_DIR)rpmbuild:/rpmbuild --name=$(CONTAINER_NAME) qemu-upstream /bin/sh -c $(MAKE_SCRIPT)
configure:
	docker build -t qemu-upstream .
	git clone https://github.com/qemu/qemu $(SELF_DIR)rpmbuild/SOURCES/qemu
console:
	docker rm -f $(CONTAINER_NAME)
	docker run -itv $(SELF_DIR)rpmbuild:/rpmbuild --name=$(CONTAINER_NAME) qemu-upstream /bin/sh
clean:
	docker rm -f $(CONTAINER_NAME)
	docker run -itv $(SELF_DIR)rpmbuild:/rpmbuild --name=$(CONTAINER_NAME) qemu-upstream /bin/sh -c "rm -rf /rpmbuild/BUILD /rpmbuild/RPMS/* /rpmbuild/SRPMS/* /rpmbuild/SOURCES/*.tar.gz"
realclean:
	docker rm -f $(CONTAINER_NAME)
	docker run -itv $(SELF_DIR)rpmbuild:/rpmbuild --name=$(CONTAINER_NAME) qemu-upstream /bin/sh -c "rm -rf /rpmbuild/BUILD /rpmbuild/RPMS/* /rpmbuild/SRPMS/* /rpmbuild/SOURCES/*"
