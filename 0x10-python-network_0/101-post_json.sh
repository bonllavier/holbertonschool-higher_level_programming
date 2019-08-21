#!/bin/bash
# 8. cURL a JSON file
curl -X POST "$1" -H "Content-Type: application/json" -d @"$2"
