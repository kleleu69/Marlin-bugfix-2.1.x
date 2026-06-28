#!/usr/bin/env python3
import os
import sys
from pathlib import Path


def ensure_scons_cache(build_dir: str | None = None) -> Path:
    if build_dir:
        target_dir = Path(build_dir).resolve()
    else:
        target_dir = Path.cwd().resolve()

    target_dir.mkdir(parents=True, exist_ok=True)
    cache_file = target_dir / ".sconsign.dblite"
    cache_file.touch(exist_ok=True)
    return cache_file


if __name__ == "__main__":
    build_dir = sys.argv[1] if len(sys.argv) > 1 else None
    cache_file = ensure_scons_cache(build_dir)
    print(f"Ensured SCons cache file: {cache_file}")
