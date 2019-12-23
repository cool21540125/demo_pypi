# Test PyPI

- https://packaging.python.org/tutorials/packaging-projects/#setup-py
- 2019/12/23

```bash
git push

pip install --user --upgrade setuptools wheel

python setup.py sdist bdist_wheel

twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```