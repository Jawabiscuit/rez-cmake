# Rez `cmake` package for Windows
[Rez](https://github.com/AcademySoftwareFoundation/rez) package for Kitware's cmake utility.

## Requirements 📦

- 🚧 At the time of writing, the rez experience on Windows while using `gitbash` as the default shell is still being tested. A [PR](https://github.com/AcademySoftwareFoundation/rez/pull/1364) exists that aims to improve it.
- [gitbash](https://gitforwindows.org/)

## Building 🔨

- Fork this repo
- Download the [cmake](https://github.com/Kitware/CMake/releases/download/v3.17.0/cmake-3.17.0-win32-x86.zip) zip archive for Windows from the internet and place in `rel/`
- Build

```sh
rez build -i
```

## Release 🚢

- Set `SYSTEM_REZ_EXTERNAL_PACKAGES` in your environment or remove / edit the block below in package.py so that it points to the default or desired release path respectively.

```python
with scope('config') as config:
    config.release_packages_path = '${SYSTEM_REZ_EXTERNAL_PACKAGES}'
```

- If changing package.py is necessary then git commit and push that code before releasing, otherwise it's as simple as:

```sh
rez release -m "Initial release"
```
