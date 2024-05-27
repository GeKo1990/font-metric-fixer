# Font Metrics Fixer Script

This script takes a font file as an argument, applies common fixes to the font metrics, and saves the fixed font. 

## Changes Applied

1. **Ascender and Descender Values:**
   - **Ascender:** Ensured that the `hhea.ascent` value is at least as large as the `OS/2.sTypoAscender` value.
   - **Descender:** Ensured that the `hhea.descent` value is at most as small as the `OS/2.sTypoDescender` value.

2. **Line Gap:**
   - Set the `hhea.lineGap` value to 0, which is a common practice to avoid extra spacing issues.

3. **Consistency in OS/2 Table:**
   - Made sure that the `OS/2` table metrics are consistent with the `hhea` table:
     - `OS/2.sTypoAscender` was set to the `hhea.ascent` value.
     - `OS/2.sTypoDescender` was set to the `hhea.descent` value.
     - `OS/2.sTypoLineGap` was set to the `hhea.lineGap` value.
     - `OS/2.usWinAscent` was set to the `hhea.ascent` value.
     - `OS/2.usWinDescent` was set to the negative of `hhea.descent` value.

4. **Bounding Box Calculation:**
   - Updated the `head` table to recalculate the font bounding box (`xMin`, `yMin`, `xMax`, `yMax`) using all the glyphs that have these attributes.

5. **Post Table Adjustments:**
   - Set the `post.underlinePosition` to half of the `hhea.descent` value.
   - Set the `post.underlineThickness` to half of the `hhea.lineGap` value.

These adjustments ensure that the font metrics are consistent and reasonable, which can help prevent rendering issues.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## Usage

./run_fixer.sh <path_to_font_file>

### Requirements

Ensure you have `fontTools` installed. If not, you can install it using pip:

```bash
pip install fonttools
