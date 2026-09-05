@echo off

echo Installing requirements...
python -m pip install -r requirements.txt

echo.
echo Building EXE...

pyinstaller --clean --onefile --noconsole ^
    --collect-all selenium ^
    --add-data "ad.js;." ^
    --add-data "skip.js;." ^
    --add-data "btnPosition.js;." ^
    main.py

echo.
echo Build finished.
echo EXE: dist\main.exe

pause
