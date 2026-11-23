#!/usr/bin/env python3
"""
Alisia Font Automated QA & Google Fonts Compliance Validator
"""

import os
import sys
from fontTools import ttLib

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
FONTS_DIR = os.path.join(ROOT_DIR, "fonts")
TTF_DIR = os.path.join(FONTS_DIR, "ttf")
SOURCES_DIR = os.path.join(ROOT_DIR, "sources")

STYLES = ["Alisia-Regular.ttf", "Alisia-Medium.ttf", "Alisia-Bold.ttf"]
TARGET_REPO = "https://github.com/FoxHound-X/alisia-font"
OLD_REPO = "https://github.com/FoxHound-X/font-alisia"

def check_file(path, desc):
    exists = os.path.exists(path)
    status = "PASS" if exists else "FAIL"
    print(f"[{status}] {desc}: {path}")
    return exists

def run_audit():
    print("=" * 70)
    print(" Alisia Font Family - Technical QA & Google Fonts Compliance Audit")
    print("=" * 70)
    
    passes = 0
    failures = 0

    # 1. Structural Checks
    print("\n--- 1. Struktur & Dokumen Repositori ---")
    required_files = [
        (os.path.join(ROOT_DIR, "OFL.txt"), "OFL 1.1 License text"),
        (os.path.join(ROOT_DIR, "METADATA.pb"), "Google Fonts METADATA.pb"),
        (os.path.join(ROOT_DIR, "DESCRIPTION.en_us.html"), "DESCRIPTION.en_us.html"),
        (os.path.join(ROOT_DIR, "AUTHORS.txt"), "AUTHORS.txt"),
        (os.path.join(ROOT_DIR, "CONTRIBUTORS.txt"), "CONTRIBUTORS.txt"),
        (os.path.join(ROOT_DIR, "FONTLOG.txt"), "FONTLOG.txt"),
        (os.path.join(ROOT_DIR, "README.md"), "README.md"),
        (os.path.join(SOURCES_DIR, "Alisia.designspace"), "Sources: Alisia.designspace"),
        (os.path.join(SOURCES_DIR, "build.py"), "Sources: build.py"),
        (os.path.join(SOURCES_DIR, "README.md"), "Sources: README.md"),
    ]
    for p, desc in required_files:
        if check_file(p, desc):
            passes += 1
        else:
            failures += 1

    # 2. Check sources
    print("\n--- 2. File Sumber Master (Sources) ---")
    for s in ["Alisia-Regular.ttx", "Alisia-Medium.ttx", "Alisia-Bold.ttx"]:
        p = os.path.join(SOURCES_DIR, s)
        if check_file(p, f"Master Source XML ({s})"):
            passes += 1
        else:
            failures += 1

    # 3. Check Font Binaries and Technical Metrics
    print("\n--- 3. Pemeriksaan Teknis Binary Font & Metrik Vertikal ---")
    for font_name in STYLES:
        font_path = os.path.join(TTF_DIR, font_name)
        if not os.path.exists(font_path):
            print(f"[FAIL] Font binary not found: {font_path}")
            failures += 1
            continue

        font = ttLib.TTFont(font_path)
        os2 = font["OS/2"]
        hhea = font["hhea"]
        head = font["head"]
        names = font["name"]

        print(f"\n* Analisis {font_name}:")

        # Metric checks
        # TypoLineGap must be 0
        if os2.sTypoLineGap == 0:
            print("  [PASS] OS/2.sTypoLineGap == 0")
            passes += 1
        else:
            print(f"  [FAIL] OS/2.sTypoLineGap is {os2.sTypoLineGap} (expected 0)")
            failures += 1

        # hhea.lineGap must be 0
        if hhea.lineGap == 0:
            print("  [PASS] hhea.lineGap == 0")
            passes += 1
        else:
            print(f"  [FAIL] hhea.lineGap is {hhea.lineGap} (expected 0)")
            failures += 1

        # Match typo and hhea ascender/descender
        if os2.sTypoAscender == hhea.ascent:
            print(f"  [PASS] OS/2.sTypoAscender == hhea.ascent ({hhea.ascent})")
            passes += 1
        else:
            print(f"  [FAIL] OS/2.sTypoAscender ({os2.sTypoAscender}) != hhea.ascent ({hhea.ascent})")
            failures += 1

        if os2.sTypoDescender == hhea.descent:
            print(f"  [PASS] OS/2.sTypoDescender == hhea.descent ({hhea.descent})")
            passes += 1
        else:
            print(f"  [FAIL] OS/2.sTypoDescender ({os2.sTypoDescender}) != hhea.descent ({hhea.descent})")
            failures += 1

        # Check winAscent >= yMax and winDescent >= abs(yMin)
        if os2.usWinAscent >= head.yMax:
            print(f"  [PASS] usWinAscent ({os2.usWinAscent}) >= yMax ({head.yMax}) [No top clipping]")
            passes += 1
        else:
            print(f"  [FAIL] usWinAscent ({os2.usWinAscent}) < yMax ({head.yMax}) [Clipping hazard]")
            failures += 1

        if os2.usWinDescent >= abs(head.yMin):
            print(f"  [PASS] usWinDescent ({os2.usWinDescent}) >= |yMin| ({abs(head.yMin)}) [No bottom clipping]")
            passes += 1
        else:
            print(f"  [FAIL] usWinDescent ({os2.usWinDescent}) < |yMin| ({abs(head.yMin)}) [Clipping hazard]")
            failures += 1

        # fsSelection bit 7 (USE_TYPO_METRICS)
        use_typo = bool(os2.fsSelection & 0x80)
        if use_typo:
            print("  [PASS] OS/2.fsSelection bit 7 (USE_TYPO_METRICS) is ENABLED")
            passes += 1
        else:
            print("  [FAIL] OS/2.fsSelection bit 7 (USE_TYPO_METRICS) is NOT set")
            failures += 1

        # Check name table URL consistency
        has_old_url = False
        has_target_repo = False
        for rec in names.names:
            u_text = rec.toUnicode()
            if OLD_REPO in u_text:
                has_old_url = True
            if TARGET_REPO in u_text:
                has_target_repo = True

        if not has_old_url:
            print(f"  [PASS] No legacy URL ({OLD_REPO}) present in name table")
            passes += 1
        else:
            print(f"  [FAIL] Legacy URL ({OLD_REPO}) still detected in name table")
            failures += 1

        if has_target_repo:
            print(f"  [PASS] Official repository URL ({TARGET_REPO}) confirmed in name table")
            passes += 1
        else:
            print(f"  [FAIL] Official repository URL ({TARGET_REPO}) missing in name table")
            failures += 1

    # 4. Content consistency across text documents
    print("\n--- 4. Konsistensi URL pada Dokumen Teks ---")
    doc_files = ["METADATA.pb", "OFL.txt", "DESCRIPTION.en_us.html", "FONTLOG.txt", "specimen.html"]
    for doc in doc_files:
        doc_path = os.path.join(ROOT_DIR, doc)
        with open(doc_path, "r", encoding="utf-8") as f:
            content = f.read()
        if OLD_REPO in content:
            print(f"  [FAIL] {doc} contains old repository URL!")
            failures += 1
        else:
            print(f"  [PASS] {doc} URL synchronized with official repository.")
            passes += 1

    print("\n" + "=" * 70)
    print(f" HASIL AUDIT: {passes} PASSED, {failures} FAILED")
    print("=" * 70)
    return failures == 0

if __name__ == "__main__":
    success = run_audit()
    sys.exit(0 if success else 1)
