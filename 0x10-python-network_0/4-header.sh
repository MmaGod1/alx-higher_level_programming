#!/bin/bash
# it takes in a URL and displays all HTTP methods the server will accept.
curl -sH "X-School-User-Id: 98" "${1}"
