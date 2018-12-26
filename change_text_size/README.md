# Change Text Size

This script changes (reduces) sizes of texts on PCB with the following rules (Unit: mm).

| Text | Default Size | New Size |
|---|---|---|
| Reference (Silk screen) | 1.0 | 0.4 |
| Value (Fabrication) | 1.0 | 0.4 |
| Other texts | varies | invisible |

## Usage
 After import net list from schematics to pcbnew, Click "Tools" -> "Script Console". Type the following command in the console and hit enter.

 `shell.runfile("path to this script")`
