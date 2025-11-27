[Setup]
AppName=Calculadora CLI
AppVersion=1.0
DefaultDirName={pf}\\CalculadoraCLI
DefaultGroupName=Calculadora CLI
OutputBaseFilename=InstaladorCalculadora
UninstallDisplayIcon={app}\\calculadora.exe
Compression=lzma
SolidCompression=yes


[Files]
Source: "..\\dist\\calculadora.exe"; DestDir: "{app}"; Flags: ignoreversion


[Icons]
Name: "{group}\\Calculadora"; Filename: "{app}\\calculadora.exe"


[Tasks]
Name: addtopath; Description: "Agregar al PATH"; Flags: checkedonce


[Registry]
Root: HKCU; Subkey: "Environment"; ValueType: expandsz; ValueName: "Path"; ValueData: "{olddata};{app}"; Tasks: addtopath