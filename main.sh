#!/usr/bin/env bash
PYTHONPATH=src python src/main.py
cd public && python3 -m http.server 8888
