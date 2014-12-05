#!/bin/sh

# Getting version to build
PACKAGE_VERSION=$(dpkg-parsechangelog | sed -ne 's/^Version: \(\([0-9]\+\):\)\?\(.*\)-.*/\3/p')
# Run with outputs, and force download event if package is present
USCAN_OPTIONS="--verbose --force-download"
# Package name
PACKAGE_NAME=$(basename $(pwd))

# Dowload package version inside .. directory
uscan ${USCAN_OPTIONS} --download-version ${PACKAGE_VERSION}

# Extract tarball in the package dir (sources = quilt 3.0)
tar xzf ../${PACKAGE_NAME}_${PACKAGE_VERSION}.orig.tar.gz --strip-components=1 -C .
