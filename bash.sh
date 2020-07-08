#!/bin/bash

echo "Normalizing data..."

# Remove tildas

perl -pi -e s,~,,g data/*.txt