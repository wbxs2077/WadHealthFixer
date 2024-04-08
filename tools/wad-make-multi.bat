@echo off
for /d %%f in (%1\*.wad*) do (
    "%~dp0\wad-make.exe" "%%f"
)
