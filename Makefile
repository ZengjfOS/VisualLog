app = VisualLog

all:
	rm -rf dist
	pip3 uninstall -y $(app)
	python3 setup.py sdist bdist_wheel
	pip3 install dist/$(app)-*-py3-none-any.whl

publish:
	twine upload dist/*

clean:
	pip3 uninstall -y $(app)
