#!/usr/bin/env python

from distutils.core import setup, Extension

opts = ["-O", "-nodefaultctor"]
include = ["../include", "/Users/admin/code/cpp/libnl/include"]
library_dirs = ["../lib/.libs"]

netlink_capi = Extension(
    "netlink/_capi",
    sources=["/Users/admin/code/cpp/libnl/python/netlink/capi.i"],
    include_dirs=include,
    swig_opts=opts,
    library_dirs=library_dirs,
    libraries=["nl-3"],
)

route_capi = Extension(
    "netlink/route/_capi",
    sources=["/Users/admin/code/cpp/libnl/python/netlink/route/capi.i"],
    include_dirs=include,
    swig_opts=opts,
    library_dirs=library_dirs,
    libraries=["nl-3", "nl-route-3"],
)

genl_capi = Extension(
    "netlink/genl/_capi",
    sources=["/Users/admin/code/cpp/libnl/python/netlink/genl/capi.i"],
    include_dirs=include,
    swig_opts=opts,
    library_dirs=library_dirs,
    libraries=["nl-3", "nl-genl-3"],
)

setup(
    name="netlink",
    version="1.0",
    description="Python wrapper for netlink protocols",
    author="Thomas Graf",
    author_email="tgraf@suug.ch",
    url="http://www.infradead.org/~tgr/libnl/",
    license="LGPL 2",
    platforms="linux2",
    long_description="Experimental python bindings for libnl",
    ext_modules=[netlink_capi, route_capi, genl_capi],
    package_dir={"": "/Users/admin/code/cpp/libnl/python"},
    packages=[
        "netlink",
        "netlink.genl",
        "netlink.route",
        "netlink.route.links",
        "netlink.route.qdisc",
    ],
)
