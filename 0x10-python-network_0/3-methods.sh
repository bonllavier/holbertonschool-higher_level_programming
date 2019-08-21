#!/bin/bash
# cURL only methods
curl -s -i -X OPTIONS "$1" | grep "Allow" | sed -e "s/Allow: //g"
