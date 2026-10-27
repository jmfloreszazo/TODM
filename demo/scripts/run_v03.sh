#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
python3 scripts/verify_all.py
python3 scripts/signed_assurance.py
python3 scripts/verify_signed.py
