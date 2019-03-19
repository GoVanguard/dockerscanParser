#!/bin/bash
rm -Rf dist/
rm -Rf build/
rm -Rf dockerscanParser.egg-info/
python3 setup.py sdist bdist_wheel
