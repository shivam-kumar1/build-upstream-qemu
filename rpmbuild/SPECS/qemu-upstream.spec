Name:           qemu-upstream
Version:        1.0
Release:        1%{?dist}
Summary:        Upstream qemu

License:        GPL
Source0:        qemu-upstream-1.0.tar.gz

Requires:       bash

%description
Upstream qemu


%prep
%setup -q


%install
QEMU_SOURCE_DIR=/rpmbuild/SOURCES/qemu
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/share/qemu
mkdir -p $RPM_BUILD_ROOT/usr/local/bin
mkdir -p $RPM_BUILD_ROOT/usr/local/libexec
mkdir -p $RPM_BUILD_ROOT/usr/local/include
mkdir -p $RPM_BUILD_ROOT/usr/local/share/icons/hicolor/16x16/apps
mkdir -p $RPM_BUILD_ROOT/usr/local/share/icons/hicolor/24x24/apps
mkdir -p $RPM_BUILD_ROOT/usr/local/share/icons/hicolor/32x32/apps
mkdir -p $RPM_BUILD_ROOT/usr/local/share/icons/hicolor/48x48/apps
mkdir -p $RPM_BUILD_ROOT/usr/local/share/icons/hicolor/64x64/apps
mkdir -p $RPM_BUILD_ROOT/usr/local/share/icons/hicolor/128x128/apps
mkdir -p $RPM_BUILD_ROOT/usr/local/share/icons/hicolor/256x256/apps
mkdir -p $RPM_BUILD_ROOT/usr/local/share/icons/hicolor/512x512/apps
mkdir -p $RPM_BUILD_ROOT/usr/local/share/icons/hicolor/scalable/apps
mkdir -p $RPM_BUILD_ROOT/usr/local/share/applications
mkdir -p $RPM_BUILD_ROOT/usr/local/share/qemu/firmware
mkdir -p $RPM_BUILD_ROOT/usr/local/share/qemu/keymaps
mkdir -p $RPM_BUILD_ROOT/var/local/run
cp trace/trace-events-all $RPM_BUILD_ROOT/usr/local/share/qemu
cp qemu-system-x86_64 $RPM_BUILD_ROOT/usr/local/bin
cp qga/qemu-ga $RPM_BUILD_ROOT/usr/local/bin
cp qemu-img $RPM_BUILD_ROOT/usr/local/bin
cp qemu-io $RPM_BUILD_ROOT/usr/local/bin
cp qemu-nbd $RPM_BUILD_ROOT/usr/local/bin
cp storage-daemon/qemu-storage-daemon $RPM_BUILD_ROOT/usr/local/bin
cp qemu-edid $RPM_BUILD_ROOT/usr/local/bin
cp qemu-bridge-helper $RPM_BUILD_ROOT/usr/local/libexec
cp qemu-pr-helper $RPM_BUILD_ROOT/usr/local/bin
cp pc-bios/edk2-aarch64-code.fd $RPM_BUILD_ROOT/usr/local/share/qemu
cp pc-bios/edk2-arm-code.fd $RPM_BUILD_ROOT/usr/local/share/qemu
cp pc-bios/edk2-arm-vars.fd $RPM_BUILD_ROOT/usr/local/share/qemu
cp pc-bios/edk2-i386-code.fd $RPM_BUILD_ROOT/usr/local/share/qemu
cp pc-bios/edk2-i386-secure-code.fd $RPM_BUILD_ROOT/usr/local/share/qemu
cp pc-bios/edk2-i386-vars.fd $RPM_BUILD_ROOT/usr/local/share/qemu
cp pc-bios/edk2-x86_64-code.fd $RPM_BUILD_ROOT/usr/local/share/qemu
cp pc-bios/edk2-x86_64-secure-code.fd $RPM_BUILD_ROOT/usr/local/share/qemu
cp $QEMU_SOURCE_DIR/include/qemu/qemu-plugin.h $RPM_BUILD_ROOT/usr/local/include
cp $QEMU_SOURCE_DIR/ui/icons/qemu_16x16.png $RPM_BUILD_ROOT/usr/local/share/icons/hicolor/16x16/apps
cp $QEMU_SOURCE_DIR/ui/icons/qemu_24x24.png $RPM_BUILD_ROOT/usr/local/share/icons/hicolor/24x24/apps
cp $QEMU_SOURCE_DIR/ui/icons/qemu_32x32.png $RPM_BUILD_ROOT/usr/local/share/icons/hicolor/32x32/apps
cp $QEMU_SOURCE_DIR/ui/icons/qemu_48x48.png $RPM_BUILD_ROOT/usr/local/share/icons/hicolor/48x48/apps
cp $QEMU_SOURCE_DIR/ui/icons/qemu_64x64.png $RPM_BUILD_ROOT/usr/local/share/icons/hicolor/64x64/apps
cp $QEMU_SOURCE_DIR/ui/icons/qemu_128x128.png $RPM_BUILD_ROOT/usr/local/share/icons/hicolor/128x128/apps
cp $QEMU_SOURCE_DIR/ui/icons/qemu_256x256.png $RPM_BUILD_ROOT/usr/local/share/icons/hicolor/256x256/apps
cp $QEMU_SOURCE_DIR/ui/icons/qemu_512x512.png $RPM_BUILD_ROOT/usr/local/share/icons/hicolor/512x512/apps
cp $QEMU_SOURCE_DIR/ui/icons/qemu_32x32.bmp $RPM_BUILD_ROOT/usr/local/share/icons/hicolor/32x32/apps
cp $QEMU_SOURCE_DIR/ui/icons/qemu.svg $RPM_BUILD_ROOT/usr/local/share/icons/hicolor/scalable/apps
cp $QEMU_SOURCE_DIR/ui/qemu.desktop $RPM_BUILD_ROOT/usr/local/share/applications
cp $QEMU_SOURCE_DIR/pc-bios/bios.bin $RPM_BUILD_ROOT/usr/local/share/qemu
cp $QEMU_SOURCE_DIR/pc-bios/bios-256k.bin $RPM_BUILD_ROOT/usr/local/share/qemu
cp $QEMU_SOURCE_DIR/pc-bios/bios-microvm.bin $RPM_BUILD_ROOT/usr/local/share/qemu
cp $QEMU_SOURCE_DIR/pc-bios/qboot.rom $RPM_BUILD_ROOT/usr/local/share/qemu
cp $QEMU_SOURCE_DIR/pc-bios/sgabios.bin $RPM_BUILD_ROOT/usr/local/share/qemu
cp $QEMU_SOURCE_DIR/pc-bios/vgabios.bin $RPM_BUILD_ROOT/usr/local/share/qemu
cp $QEMU_SOURCE_DIR/pc-bios/vgabios-cirrus.bin $RPM_BUILD_ROOT/usr/local/share/qemu
cp $QEMU_SOURCE_DIR/pc-bios/vgabios-stdvga.bin $RPM_BUILD_ROOT/usr/local/share/qemu
cp $QEMU_SOURCE_DIR/pc-bios/vgabios-vmware.bin $RPM_BUILD_ROOT/usr/local/share/qemu
cp $QEMU_SOURCE_DIR/pc-bios/vgabios-qxl.bin $RPM_BUILD_ROOT/usr/local/share/qemu
cp $QEMU_SOURCE_DIR/pc-bios/vgabios-virtio.bin $RPM_BUILD_ROOT/usr/local/share/qemu
cp $QEMU_SOURCE_DIR/pc-bios/vgabios-ramfb.bin $RPM_BUILD_ROOT/usr/local/share/qemu
cp $QEMU_SOURCE_DIR/pc-bios/vgabios-bochs-display.bin $RPM_BUILD_ROOT/usr/local/share/qemu
cp $QEMU_SOURCE_DIR/pc-bios/vgabios-ati.bin $RPM_BUILD_ROOT/usr/local/share/qemu
cp $QEMU_SOURCE_DIR/pc-bios/openbios-sparc32 $RPM_BUILD_ROOT/usr/local/share/qemu
cp $QEMU_SOURCE_DIR/pc-bios/openbios-sparc64 $RPM_BUILD_ROOT/usr/local/share/qemu
cp $QEMU_SOURCE_DIR/pc-bios/openbios-ppc $RPM_BUILD_ROOT/usr/local/share/qemu
cp $QEMU_SOURCE_DIR/pc-bios/QEMU,tcx.bin $RPM_BUILD_ROOT/usr/local/share/qemu
cp $QEMU_SOURCE_DIR/pc-bios/QEMU,cgthree.bin $RPM_BUILD_ROOT/usr/local/share/qemu
cp $QEMU_SOURCE_DIR/pc-bios/pxe-e1000.rom $RPM_BUILD_ROOT/usr/local/share/qemu
cp $QEMU_SOURCE_DIR/pc-bios/pxe-eepro100.rom $RPM_BUILD_ROOT/usr/local/share/qemu
cp $QEMU_SOURCE_DIR/pc-bios/pxe-ne2k_pci.rom $RPM_BUILD_ROOT/usr/local/share/qemu
cp $QEMU_SOURCE_DIR/pc-bios/pxe-pcnet.rom $RPM_BUILD_ROOT/usr/local/share/qemu
cp $QEMU_SOURCE_DIR/pc-bios/pxe-rtl8139.rom $RPM_BUILD_ROOT/usr/local/share/qemu
cp $QEMU_SOURCE_DIR/pc-bios/pxe-virtio.rom $RPM_BUILD_ROOT/usr/local/share/qemu
cp $QEMU_SOURCE_DIR/pc-bios/efi-e1000.rom $RPM_BUILD_ROOT/usr/local/share/qemu
cp $QEMU_SOURCE_DIR/pc-bios/efi-eepro100.rom $RPM_BUILD_ROOT/usr/local/share/qemu
cp $QEMU_SOURCE_DIR/pc-bios/efi-ne2k_pci.rom $RPM_BUILD_ROOT/usr/local/share/qemu
cp $QEMU_SOURCE_DIR/pc-bios/efi-pcnet.rom $RPM_BUILD_ROOT/usr/local/share/qemu
cp $QEMU_SOURCE_DIR/pc-bios/efi-rtl8139.rom $RPM_BUILD_ROOT/usr/local/share/qemu
cp $QEMU_SOURCE_DIR/pc-bios/efi-virtio.rom $RPM_BUILD_ROOT/usr/local/share/qemu
cp $QEMU_SOURCE_DIR/pc-bios/efi-e1000e.rom $RPM_BUILD_ROOT/usr/local/share/qemu
cp $QEMU_SOURCE_DIR/pc-bios/efi-vmxnet3.rom $RPM_BUILD_ROOT/usr/local/share/qemu
cp $QEMU_SOURCE_DIR/pc-bios/qemu-nsis.bmp $RPM_BUILD_ROOT/usr/local/share/qemu
cp $QEMU_SOURCE_DIR/pc-bios/bamboo.dtb $RPM_BUILD_ROOT/usr/local/share/qemu
cp $QEMU_SOURCE_DIR/pc-bios/canyonlands.dtb $RPM_BUILD_ROOT/usr/local/share/qemu
cp $QEMU_SOURCE_DIR/pc-bios/petalogix-s3adsp1800.dtb $RPM_BUILD_ROOT/usr/local/share/qemu
cp $QEMU_SOURCE_DIR/pc-bios/petalogix-ml605.dtb $RPM_BUILD_ROOT/usr/local/share/qemu
cp $QEMU_SOURCE_DIR/pc-bios/multiboot.bin $RPM_BUILD_ROOT/usr/local/share/qemu
cp $QEMU_SOURCE_DIR/pc-bios/multiboot_dma.bin $RPM_BUILD_ROOT/usr/local/share/qemu
cp $QEMU_SOURCE_DIR/pc-bios/linuxboot.bin $RPM_BUILD_ROOT/usr/local/share/qemu
cp $QEMU_SOURCE_DIR/pc-bios/linuxboot_dma.bin $RPM_BUILD_ROOT/usr/local/share/qemu
cp $QEMU_SOURCE_DIR/pc-bios/kvmvapic.bin $RPM_BUILD_ROOT/usr/local/share/qemu
cp $QEMU_SOURCE_DIR/pc-bios/pvh.bin $RPM_BUILD_ROOT/usr/local/share/qemu
cp $QEMU_SOURCE_DIR/pc-bios/s390-ccw.img $RPM_BUILD_ROOT/usr/local/share/qemu
cp $QEMU_SOURCE_DIR/pc-bios/s390-netboot.img $RPM_BUILD_ROOT/usr/local/share/qemu
cp $QEMU_SOURCE_DIR/pc-bios/slof.bin $RPM_BUILD_ROOT/usr/local/share/qemu
cp $QEMU_SOURCE_DIR/pc-bios/skiboot.lid $RPM_BUILD_ROOT/usr/local/share/qemu
cp $QEMU_SOURCE_DIR/pc-bios/palcode-clipper $RPM_BUILD_ROOT/usr/local/share/qemu
cp $QEMU_SOURCE_DIR/pc-bios/u-boot.e500 $RPM_BUILD_ROOT/usr/local/share/qemu
cp $QEMU_SOURCE_DIR/pc-bios/u-boot-sam460-20100605.bin $RPM_BUILD_ROOT/usr/local/share/qemu
cp $QEMU_SOURCE_DIR/pc-bios/qemu_vga.ndrv $RPM_BUILD_ROOT/usr/local/share/qemu
cp $QEMU_SOURCE_DIR/pc-bios/edk2-licenses.txt $RPM_BUILD_ROOT/usr/local/share/qemu
cp $QEMU_SOURCE_DIR/pc-bios/hppa-firmware.img $RPM_BUILD_ROOT/usr/local/share/qemu
cp $QEMU_SOURCE_DIR/pc-bios/opensbi-riscv32-generic-fw_dynamic.bin $RPM_BUILD_ROOT/usr/local/share/qemu
cp $QEMU_SOURCE_DIR/pc-bios/opensbi-riscv64-generic-fw_dynamic.bin $RPM_BUILD_ROOT/usr/local/share/qemu
cp $QEMU_SOURCE_DIR/pc-bios/npcm7xx_bootrom.bin $RPM_BUILD_ROOT/usr/local/share/qemu
cp $QEMU_SOURCE_DIR/pc-bios/vof.bin $RPM_BUILD_ROOT/usr/local/share/qemu
cp $QEMU_SOURCE_DIR/pc-bios/vof-nvram.bin $RPM_BUILD_ROOT/usr/local/share/qemu
cp pc-bios/descriptors/50-edk2-i386-secure.json $RPM_BUILD_ROOT/usr/local/share/qemu/firmware
cp pc-bios/descriptors/50-edk2-x86_64-secure.json $RPM_BUILD_ROOT/usr/local/share/qemu/firmware
cp pc-bios/descriptors/60-edk2-aarch64.json $RPM_BUILD_ROOT/usr/local/share/qemu/firmware
cp pc-bios/descriptors/60-edk2-arm.json $RPM_BUILD_ROOT/usr/local/share/qemu/firmware
cp pc-bios/descriptors/60-edk2-i386.json $RPM_BUILD_ROOT/usr/local/share/qemu/firmware
cp pc-bios/descriptors/60-edk2-x86_64.json $RPM_BUILD_ROOT/usr/local/share/qemu/firmware
cp $QEMU_SOURCE_DIR/pc-bios/keymaps/ar $RPM_BUILD_ROOT/usr/local/share/qemu/keymaps
cp $QEMU_SOURCE_DIR/pc-bios/keymaps/bepo $RPM_BUILD_ROOT/usr/local/share/qemu/keymaps
cp $QEMU_SOURCE_DIR/pc-bios/keymaps/cz $RPM_BUILD_ROOT/usr/local/share/qemu/keymaps
cp $QEMU_SOURCE_DIR/pc-bios/keymaps/da $RPM_BUILD_ROOT/usr/local/share/qemu/keymaps
cp $QEMU_SOURCE_DIR/pc-bios/keymaps/de $RPM_BUILD_ROOT/usr/local/share/qemu/keymaps
cp $QEMU_SOURCE_DIR/pc-bios/keymaps/de-ch $RPM_BUILD_ROOT/usr/local/share/qemu/keymaps
cp $QEMU_SOURCE_DIR/pc-bios/keymaps/en-gb $RPM_BUILD_ROOT/usr/local/share/qemu/keymaps
cp $QEMU_SOURCE_DIR/pc-bios/keymaps/en-us $RPM_BUILD_ROOT/usr/local/share/qemu/keymaps
cp $QEMU_SOURCE_DIR/pc-bios/keymaps/es $RPM_BUILD_ROOT/usr/local/share/qemu/keymaps
cp $QEMU_SOURCE_DIR/pc-bios/keymaps/et $RPM_BUILD_ROOT/usr/local/share/qemu/keymaps
cp $QEMU_SOURCE_DIR/pc-bios/keymaps/fi $RPM_BUILD_ROOT/usr/local/share/qemu/keymaps
cp $QEMU_SOURCE_DIR/pc-bios/keymaps/fo $RPM_BUILD_ROOT/usr/local/share/qemu/keymaps
cp $QEMU_SOURCE_DIR/pc-bios/keymaps/fr $RPM_BUILD_ROOT/usr/local/share/qemu/keymaps
cp $QEMU_SOURCE_DIR/pc-bios/keymaps/fr-be $RPM_BUILD_ROOT/usr/local/share/qemu/keymaps
cp $QEMU_SOURCE_DIR/pc-bios/keymaps/fr-ca $RPM_BUILD_ROOT/usr/local/share/qemu/keymaps
cp $QEMU_SOURCE_DIR/pc-bios/keymaps/fr-ch $RPM_BUILD_ROOT/usr/local/share/qemu/keymaps
cp $QEMU_SOURCE_DIR/pc-bios/keymaps/hr $RPM_BUILD_ROOT/usr/local/share/qemu/keymaps
cp $QEMU_SOURCE_DIR/pc-bios/keymaps/hu $RPM_BUILD_ROOT/usr/local/share/qemu/keymaps
cp $QEMU_SOURCE_DIR/pc-bios/keymaps/is $RPM_BUILD_ROOT/usr/local/share/qemu/keymaps
cp $QEMU_SOURCE_DIR/pc-bios/keymaps/it $RPM_BUILD_ROOT/usr/local/share/qemu/keymaps
cp $QEMU_SOURCE_DIR/pc-bios/keymaps/ja $RPM_BUILD_ROOT/usr/local/share/qemu/keymaps
cp $QEMU_SOURCE_DIR/pc-bios/keymaps/lt $RPM_BUILD_ROOT/usr/local/share/qemu/keymaps
cp $QEMU_SOURCE_DIR/pc-bios/keymaps/lv $RPM_BUILD_ROOT/usr/local/share/qemu/keymaps
cp $QEMU_SOURCE_DIR/pc-bios/keymaps/mk $RPM_BUILD_ROOT/usr/local/share/qemu/keymaps
cp $QEMU_SOURCE_DIR/pc-bios/keymaps/nl $RPM_BUILD_ROOT/usr/local/share/qemu/keymaps
cp $QEMU_SOURCE_DIR/pc-bios/keymaps/no $RPM_BUILD_ROOT/usr/local/share/qemu/keymaps
cp $QEMU_SOURCE_DIR/pc-bios/keymaps/pl $RPM_BUILD_ROOT/usr/local/share/qemu/keymaps
cp $QEMU_SOURCE_DIR/pc-bios/keymaps/pt $RPM_BUILD_ROOT/usr/local/share/qemu/keymaps
cp $QEMU_SOURCE_DIR/pc-bios/keymaps/pt-br $RPM_BUILD_ROOT/usr/local/share/qemu/keymaps
cp $QEMU_SOURCE_DIR/pc-bios/keymaps/ru $RPM_BUILD_ROOT/usr/local/share/qemu/keymaps
cp $QEMU_SOURCE_DIR/pc-bios/keymaps/th $RPM_BUILD_ROOT/usr/local/share/qemu/keymaps
cp $QEMU_SOURCE_DIR/pc-bios/keymaps/tr $RPM_BUILD_ROOT/usr/local/share/qemu/keymaps
cp $QEMU_SOURCE_DIR/pc-bios/keymaps/sl $RPM_BUILD_ROOT/usr/local/share/qemu/keymaps
cp $QEMU_SOURCE_DIR/pc-bios/keymaps/sv $RPM_BUILD_ROOT/usr/local/share/qemu/keymaps

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/usr/local/share/qemu/*
/usr/local/bin/*
/usr/local/libexec/*
/usr/local/include/*
/usr/local/share/applications/*
/var/local/run
/usr/local/share/icons/*

%changelog
