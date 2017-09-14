rm -rf dist || true
rm -rf build || true
python setup.py bdist_wheel
twine upload dist/*
