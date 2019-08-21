#!/bin/bash
# 0. cURL body size
curl -s -w \%{size_download} -o /dev/null $1; echo
