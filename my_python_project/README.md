# PyBuilder and Makefile build

Run `make all` in this folder to clean the previous output, install the listed dependency, run unit tests, and package the project. `make clean`, `make install_deps`, `make test`, and `make build` run those steps individually. The Makefile saves the commands so they can be repeated consistently.

PyBuilder reads `build.py`, loads the build plugins, installs the declared build dependencies, runs tests from `src/unittest/python`, and writes the package under `target`. The source module is in `src/main/python`.
