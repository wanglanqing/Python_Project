@echo off

SET MY_TOOLS_BIN=%MY_TOOLS_HOME%\bin
SET MY_TOOLS_LIB=%MY_TOOLS_HOME%\lib

rem SET PYTHONPATH=%MY_TOOLS_LIB%\python

python %MY_TOOLS_BIN%\addhosts.py %*
