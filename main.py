#!/usr/bin/env python3
"""News Image entry: writes the Nov 13, 2026 world news summary to /output/entry.png.

Deterministic: copies the same bytes every run.
"""
import os
import shutil

def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, 'entry.png')
    out_dir = '/output'
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, 'entry.png')
    shutil.copyfile(src, dst)
    print(f'Wrote {dst} ({os.path.getsize(dst)} bytes)')

if __name__ == '__main__':
    main()
