#!/usr/bin/bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
BASE_DIR=$( cd "$SCRIPT_DIR/.." &> /dev/null && pwd )

pytest $BASE_DIR/test/ -c $BASE_DIR/test/pytest.ini