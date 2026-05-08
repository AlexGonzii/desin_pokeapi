[Setup]
AppName=PokeAPI App
AppVersion=1.0
DefaultDirName={autopf}\PokeAPIApp
DefaultGroupName=PokeAPI App
OutputDir=dist_installer
OutputBaseFilename=PokeAPIInstaller
Compression=lzma
SolidCompression=yes

[Files]
Source: "dist\main.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\PokeAPI App"; Filename: "{app}\main.exe"
Name: "{commondesktop}\PokeAPI App"; Filename: "{app}\main.exe"

[Run]
Filename: "{app}\main.exe"; Flags: nowait postinstall skipifsilent