.PHONY: clean install test lint package

install:
	pip install -r requirements.txt

test:
	python -m unittest discover -s tests

lint:
	flake8 app.py

clean:
	python -c "import pathlib, shutil; [p.unlink() for p in pathlib.Path('.').rglob('*.pyc')]; shutil.rmtree('dist', ignore_errors=True)"

package:
	python setup.py sdist bdist_wheel
