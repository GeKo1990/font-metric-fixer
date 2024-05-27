import sys
from fixer import fix_font_metrics
from fontTools.ttLib import TTFont

if len(sys.argv) != 2:
    print("Usage: python fix_font_metrics.py <path_to_font_file>")
    sys.exit(1)

font_path = sys.argv[1]
font = TTFont(font_path)

# Apply fixes to the font metrics
fixed_font = fix_font_metrics(font)

# Save the fixed font to a new file
fixed_font_path = font_path.rsplit('.', 1)[0] + '_fixed.ttf'
fixed_font.save(fixed_font_path)

print(f"Fixed font saved as {fixed_font_path}")

