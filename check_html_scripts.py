import re
import subprocess
import sys

def check_html(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract all <script> contents (excluding script tags with src attribute)
    scripts = re.findall(r'<script(?:\s+(?!src=)[^>]*)?>(.*?)</script>', content, re.DOTALL | re.IGNORECASE)
    print(f"Found {len(scripts)} inline script tags in {filepath}")

    has_error = False
    for idx, script in enumerate(scripts, 1):
        clean_script = script.strip()
        if not clean_script:
            continue

        proc = subprocess.run(
            ['node', '--input-type=commonjs', '--check'],
            input=clean_script,
            capture_output=True,
            text=True
        )
        if proc.returncode != 0:
            print(f"❌ Syntax Error in script #{idx} in {filepath}:")
            print(proc.stderr)
            has_error = True
        else:
            print(f"✓ Script #{idx} passed syntax check.")

    if has_error:
        sys.exit(1)
    else:
        print(f"✅ All scripts in {filepath} passed node syntax check!")

if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else 'index.html'
    check_html(target)
