@echo off
echo Construyendo ejecutable...
python -m PyInstaller --onefile --console --clean calculadora.py
echo EXE generado en carpeta dist
pause
