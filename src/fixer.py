def get_glyph_bbox(glyph, glyf_table):
    try:
        if glyph.isComposite():
            return None  # Composite glyphs can have complex structures
        glyph.expand(glyf_table)  # Ensure the glyph data is expanded
        if hasattr(glyph, 'xMin') and hasattr(glyph, 'yMin') and hasattr(glyph, 'xMax') and hasattr(glyph, 'yMax'):
            bbox = glyph.xMin, glyph.yMin, glyph.xMax, glyph.yMax
        else:
            bbox = None
    except Exception as e:
        bbox = None
    return bbox

def fix_font_metrics(font):
    # Set reasonable ascender, descender, and line gap values
    hhea = font['hhea']
    os2 = font['OS/2']
    
    hhea.ascent = max(hhea.ascent, os2.sTypoAscender)
    hhea.descent = min(hhea.descent, os2.sTypoDescender)
    hhea.lineGap = 0  # Common practice to set this to zero
    
    # Ensure OS/2 metrics are consistent
    os2.sTypoAscender = hhea.ascent
    os2.sTypoDescender = hhea.descent
    os2.sTypoLineGap = hhea.lineGap
    
    os2.usWinAscent = hhea.ascent
    os2.usWinDescent = -hhea.descent
    
    os2.sxHeight = 0  # Typically zero if unknown
    os2.sCapHeight = 0  # Typically zero if unknown
    
    if 'glyf' in font:
        # Update the head table to recalculate font bounding box
        head = font['head']
        glyf = font['glyf']
        
        xMin = min((glyph.xMin for glyph in glyf.glyphs.values() if hasattr(glyph, 'xMin')), default=head.xMin)
        yMin = min((glyph.yMin for glyph in glyf.glyphs.values() if hasattr(glyph, 'yMin')), default=head.yMin)
        xMax = max((glyph.xMax for glyph in glyf.glyphs.values() if hasattr(glyph, 'xMax')), default=head.xMax)
        yMax = max((glyph.yMax for glyph in glyf.glyphs.values() if hasattr(glyph, 'yMax')), default=head.yMax)
        
        head.xMin = xMin
        head.yMin = yMin
        head.xMax = xMax
        head.yMax = yMax
    else:
        print("Warning: 'glyf' table not found. Bounding box adjustments are skipped.")
    
    # Update the 'post' table, especially the underline position and thickness
    post = font['post']
    post.underlinePosition = int(hhea.descent / 2)
    post.underlineThickness = int(hhea.lineGap / 2)
    
    return font
