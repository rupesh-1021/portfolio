"""Prepare the static site and stamp its deployment date in India time."""

from datetime import datetime, timedelta, timezone
from pathlib import Path
import re
import shutil


def build():
    root = Path(__file__).resolve().parents[1]
    output = root / "_site"
    output.mkdir(exist_ok=True)
    # Include the current website files and assets, even in an uncommitted preview.
    # Keep server-side code and configuration outside the published site.
    files = [root / name for name in ("index.html", "favicon.png", "portfolio pic.jpg")]
    files.extend(path for path in (root / "assets").rglob("*") if path.is_file())
    for source in files:
        path = source.relative_to(root)
        destination = output / path
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(root / path, destination)

    now = datetime.now(timezone(timedelta(hours=5, minutes=30)))
    page = output / "index.html"
    html = page.read_text(encoding="utf-8")
    html, count = re.subn(
        r'<time id="last-updated"[^>]*>.*?</time>',
        f'<time id="last-updated" datetime="{now:%Y-%m-%d}">{now.day} {now:%B %Y}</time>',
        html,
    )
    if count != 1:
        raise RuntimeError("Expected exactly one last-updated footer element")
    page.write_text(html, encoding="utf-8")
    print(f"Built site with deployment date: {now.day} {now:%B %Y} (IST)")


if __name__ == "__main__":
    build()
