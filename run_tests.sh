#!/bin/bash

# activate the virtual environment (bin on Linux, Scripts on Windows)
if [ -d "venv/bin" ]; then
    source venv/bin/activate
    python_bin="venv/bin/python"
else
    source venv/Scripts/activate
    python_bin="venv/Scripts/python"
fi

# run the test suite
"$python_bin" -m pytest test_app.py

# return the result of pytest (0 if passed, 1 if a test failed)
exit $?
