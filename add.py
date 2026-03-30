#!/usr/bin/env python3

"""Add a part from LCSC to the local KiCad parts library."""

import argparse
from pathlib import Path
import subprocess


def main() -> None:
	parser = argparse.ArgumentParser(
		description="Fetch a part with easyeda2kicad and write into ./myparts."
	)
	parser.add_argument("lcsc_pn", help="LCSC part number, e.g. C114599")
	args = parser.parse_args()

	command = [
		"easyeda2kicad",
		"--full",
		f"--lcsc_id={args.lcsc_pn}",
		"--output",
		"./myparts",
		"--overwrite",
	]

	subprocess.run(command, check=True)

	# Keep KiCad symbol namespace consistent after import.
	symbol_file = Path("myparts.kicad_sym")
	if symbol_file.exists():
		content = symbol_file.read_text(encoding="utf-8")
		updated = content.replace("myparts:", "MyParts:")
		if updated != content:
			symbol_file.write_text(updated, encoding="utf-8")


if __name__ == "__main__":
	main()
