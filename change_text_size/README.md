# Change Text Size

This script changes (reduces) sizes of texts on PCB with the following rules (Unit: mm).

| Text | Default Size | New Size |
|---|---|---|
| Reference (Silk screen) | 1.0 | 0.4 |
| Value (Fabrication) | 1.0 | 0.4 |
| Other texts | varies | invisible |

## Installation
Copy `change_text_size.py` to one of the following folers based on your system.

Linux
* /usr/share/kicad/scripting/plugins/
* ~/.kicad/scripting/plugins
* ~/.kicad_plugins/

Windows
* \%KICAD_INSTALL_PATH%/share/kicad/scripting/plugins
* \%APPDATA%/Roaming/kicad/scripting/plugins

macOS
* /Applications/kicad/Kicad/Contents/SharedSupport/scripting/plugins
* ~/Library/Application Support/kicad/scripting/plugins

## Usage
 After import net list from schematics to pcbnew, Click "Tools" -> "External Plugins" -> "SmallTextSize".
