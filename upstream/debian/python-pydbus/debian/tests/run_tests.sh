#!/bin/sh
set -e

TESTS_DIR=pydbus/tests

PYTHON=${1:-python}

dbus-run-session "$PYTHON" $TESTS_DIR/context.py
dbus-run-session "$PYTHON" $TESTS_DIR/identifier.py
dbus-run-session "$PYTHON" $TESTS_DIR/publish.py
dbus-run-session "$PYTHON" $TESTS_DIR/publish_properties.py
dbus-run-session "$PYTHON" $TESTS_DIR/publish_multiface.py
