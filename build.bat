@echo off
echo Construyendo ejecutable...
python -m PyInstaller --onefile --clean src\\calculadora.py
echo EXE generado en carpeta dist
pause
