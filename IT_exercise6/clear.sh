#!/bin/bash
#

## Deleting a project

if [ -d "./$1" ]; then
	read -p "Are you sure you want to delete $1 (Y/N)?" answer

	if [ $answer == 'Y' ] || [ $answer == 'y' ]; then
  		rm -rf $1
		echo "Project $1 deleted."
	fi
fi