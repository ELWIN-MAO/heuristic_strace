Format: 3.0 (quilt)
Source: strace
Binary: strace, strace64, strace-udeb
Architecture: linux-any
Version: 4.11-1ubuntu3
Maintainer: Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com>
Homepage: http://sourceforge.net/projects/strace/
Standards-Version: 3.9.6
Build-Depends: libc6-dev (>= 2.2.2) [!alpha !ia64], libc6.1-dev (>= 2.2.2) [alpha ia64], gcc-multilib [i386 powerpc s390 sparc], debhelper (>= 7.0.0), gawk
Package-List:
 strace deb utils optional arch=linux-any
 strace-udeb udeb debian-installer extra arch=linux-any
 strace64 deb utils extra arch=i386,powerpc,s390,sparc
Checksums-Sha1:
 8fd717dc3c51b69fde51ce0bdb066404a678363c 679924 strace_4.11.orig.tar.xz
 071bae8393034d9f2b02b5b289de8a4e26ea5f2c 124820 strace_4.11-1ubuntu3.debian.tar.xz
Checksums-Sha256:
 e86a5f6cd8f941f67f3e4b28f4e60f3d9185c951cf266404533210a2e5cd8152 679924 strace_4.11.orig.tar.xz
 b2562158101515173bb6201270a2320d4b36ffa25cc167f976b24e9406e39e31 124820 strace_4.11-1ubuntu3.debian.tar.xz
Files:
 a15d2555a7febb56d00c6e1a51c655dc 679924 strace_4.11.orig.tar.xz
 666f0b515d0a0734628eb8b0010328c1 124820 strace_4.11-1ubuntu3.debian.tar.xz
Original-Maintainer: Steve McIntyre <93sam@debian.org>
