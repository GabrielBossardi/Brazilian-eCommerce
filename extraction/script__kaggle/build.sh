#!/bin/bash

set -e

IMAGE=`sed -n 's/^LABEL image.name=\(.*\)$/\1/p' Dockerfile`
VERSION=`sed -n 's/^LABEL image.version=\(.*\)$/\1/p' Dockerfile`

docker build . -t $IMAGE:$VERSION
