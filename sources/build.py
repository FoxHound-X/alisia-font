#!/usr/bin/env python3
"""
Alisia Font Family Build Pipeline
Reproducible compilation and Google Fonts specification alignment.
"""

import os
import sys
from fontTools import ttLib
from fontTools.ttLib.woff2 import compress

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SOURCES_DIR = os.path.join(ROOT_DIR, "sources")
FONTS_DIR = os.path.join(ROOT_DIR, "fonts")
TTF_DIR = os.path.join(FONTS_DIR, "ttf")
OTF_DIR = os.path.join(FONTS_DIR, "otf")
WOFF2_DIR = os.path.join(FONTS_DIR, "woff2")

STYLES = [
    {
        "filename": "Alisia-Regular",
        "weight": 400,
        "is_bold": False,
        "is_italic": False,
    },
    {
        "filename": "Alisia-Medium",
        "weight": 500,
        "is_bold": False,
        "is_italic": False,
    },
    {
        "filename": "Alisia-Bold",
        "weight": 700,
        "is_bold": True,
        "is_italic": False,
    },
]

# Google Fonts Vertical Metrics Standard
TYPO_ASCENDER = 980
TYPO_DESCENDER = -220
TYPO_LINE_GAP = 0
HHEA_ASCENT = 980
HHEA_DESCENT = -220
HHEA_LINE_GAP = 0
WIN_ASCENT = 1050    # Bounding box yMax is 1044 -> 1050 ensures zero clipping
WIN_DESCENT = 260    # Bounding box yMin is -237 -> 260 ensures zero clipping
REPO_URL = "https://github.com/FoxHound-X/alisia-font"
OLD_REPO_URL = "https://github.com/FoxHound-X/font-alisia"

def calibrate_and_build(style_info):
    name = style_info["filename"]
    ttx_path = os.path.join(SOURCES_DIR, f"{name}.ttx")
    ttf_input = os.path.join(TTF_DIR, f"{name}.ttf")

    # Load from TTX if available, otherwise compile from existing TTF
    if os.path.exists(ttx_path):
        print(f"[{name}] Loading from XML source: {ttx_path}")
        font = ttLib.TTFont()
        font.importXML(ttx_path)
    else:
        print(f"[{name}] Loading base binary: {ttf_input}")
        font = ttLib.TTFont(ttf_input)

    # 1. Calibrate OS/2 Table (Google Fonts Specification)
    os2 = font["OS/2"]
    os2.sTypoAscender = TYPO_ASCENDER
    os2.sTypoDescender = TYPO_DESCENDER
    os2.sTypoLineGap = TYPO_LINE_GAP
    os2.usWinAscent = WIN_ASCENT
    os2.usWinDescent = WIN_DESCENT
    
    # fsSelection: bit 7 (USE_TYPO_METRICS = 128 / 0x80)
    fs_val = 0
    if style_info["is_bold"]:
        fs_val |= 0x20  # Bit 5: Bold
    elif not style_info["is_italic"]:
        fs_val |= 0x40  # Bit 6: Regular
    if style_info["is_italic"]:
        fs_val |= 0x01  # Bit 0: Italic
    fs_val |= 0x80      # Bit 7: USE_TYPO_METRICS
    os2.fsSelection = fs_val

    # 2. Calibrate hhea Table (Match Typo Metrics)
    hhea = font["hhea"]
    hhea.ascent = HHEA_ASCENT
    hhea.descent = HHEA_DESCENT
    hhea.lineGap = HHEA_LINE_GAP

    # 3. Synchronize Name Table to target repository
    name_table = font["name"]
    for record in name_table.names:
        text = record.toUnicode()
        if OLD_REPO_URL in text:
            new_text = text.replace(OLD_REPO_URL, REPO_URL)
            record.string = new_text.encode(record.getEncoding())
        elif record.nameID == 0 and REPO_URL not in text:
            record.string = f"Copyright 2026 The Alisia Project Authors ({REPO_URL})".encode(record.getEncoding())

    # 4. Save lossless XML source in sources/ if not yet created or update it
    print(f"[{name}] Exporting synchronized TTX source...")
    font.saveXML(ttx_path)

    # 5. Output TTF
    os.makedirs(TTF_DIR, exist_ok=True)
    out_ttf = os.path.join(TTF_DIR, f"{name}.ttf")
    print(f"[{name}] Saving TTF -> {out_ttf}")
    font.save(out_ttf)

    # 6. Output WOFF2
    os.makedirs(WOFF2_DIR, exist_ok=True)
    out_woff2 = os.path.join(WOFF2_DIR, f"{name}.woff2")
    print(f"[{name}] Compressing WOFF2 -> {out_woff2}")
    compress(out_ttf, out_woff2)

    # 7. Output OTF
    os.makedirs(OTF_DIR, exist_ok=True)
    out_otf = os.path.join(OTF_DIR, f"{name}.otf")
    print(f"[{name}] Saving OTF -> {out_otf}")
    font.save(out_otf)

    print(f"[{name}] Build completed successfully.\n")

def main():
    print("=" * 60)
    print(" Alisia Font Family Build Pipeline")
    print(" Target Repository:", REPO_URL)
    print(" Google Fonts Compliance: Active")
    print("=" * 60 + "\n")

    for style in STYLES:
        calibrate_and_build(style)

    print("All fonts built, calibrated, and exported successfully.")

if __name__ == "__main__":
    main()
