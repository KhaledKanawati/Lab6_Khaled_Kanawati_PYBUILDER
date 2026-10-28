# Calculator build

Run `pyb run_unit_tests` from this folder to run the calculator tests. Run `pyb` to test and package the project. The `build.py` file enables PyBuilder's core, unittest, and distribution tasks. The calculator code is under `src/main/python`, and the tests are under `tests/unittest`.

The calculator provides addition, subtraction, multiplication, division, modulus, exponentiation, and square root. Division by zero raises `ValueError`; square root uses Python's `math.sqrt` behavior for negative inputs.
