#!/bin/sh

if [ -n "$1" ]
then
  NEXT_RELEASE_VERSION=$1
else
  echo "A release version must be supplied"
  exit 1
fi

echo "PyPi Deployment..."
echo "Building distribution"
python setup.py sdist bdist_wheel
echo "Pushing new version to PyPi"
twine upload dist/* -u $PYPI_USERNAME -p $PYPI_PASSWORD 
