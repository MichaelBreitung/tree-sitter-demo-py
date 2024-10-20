#!/usr/bin/bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
BASE_DIR=$( cd "$SCRIPT_DIR/.." &> /dev/null && pwd )
cd $BASE_DIR

pip3 install -r requirements.txt