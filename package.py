# -*- coding: utf-8 -*-

name = "cmake"

version = "3.17.0"

authors = ["kitware"]

description = """\
    CMake is an open-source, cross-platform family of tools designed to build,
    test and package software.
"""

help = "https://cmake.org/"

tools = [
    "cmake-gui", "cmake", "cmcldeps", "cpack", "ctest"
]

variants = [
    ["os-Windows-10"]
]

private_build_requires = []

with scope('config') as config:
    config.release_packages_path = '${SYSTEM_REZ_EXTERNAL_PACKAGES}'


build_command = """\
    set -e

    source_archive=`/usr/bin/find "$REZ_BUILD_SOURCE_PATH/rel" -type f -name '*.zip'`
    unzip -u "$source_archive" -d "$REZ_BUILD_PATH"

    if [ $REZ_BUILD_INSTALL == 1 ]
    then
        echo -e "\e[1m\e[32mInstalling...\e[0m"
        source_dirname=`echo $source_archive | sed 's|\.zip||' | sed 's|.*/||'`
        for item in "$REZ_BUILD_PATH"/"$source_dirname"/*
        do
            if [ -d "$item" ]
            then
                printf '.'
                cp -r "$item" "$REZ_BUILD_INSTALL_PATH"
            fi
        done
    else
        echo -e "\e[1m\e[33mNothing more to do. Run ""rez-build -i"" to install\e[0m"
    fi
"""


def commands():
    import os

    env.PATH.append(os.path.join(this.root, "bin"))
    env.CMAKE_MODULE_PATH.prepend(
        os.path.join(
            this.root,
            "share", "{}-{}.{}".format(
                this.name, this.version.major, this.version.minor
            ),
            "Modules"
        ).replace("\\", "/")
    )