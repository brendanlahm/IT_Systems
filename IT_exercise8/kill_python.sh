#!/bin/bash
#

## Kill all actively running Python processes

sudo kill -9 $(ps -A | grep python | awk '{print $1}')