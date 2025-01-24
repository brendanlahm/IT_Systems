#!/bin/bash
#

## Creating a project (1st Parameter) w/ n (3rd Parameter) sub-directories
## Copy a file (2nd Parameter) to n sub-directories

if [ -d "./$1" ]; then
  echo "Project already exists!"
  exit 0
fi

echo "Scaffolding for $1"
echo "Create project '$1'"

mkdir $1
cd ./$1

for i in $(seq 1 $3)
do
  echo "Create folder ./$1/sub$i"
  mkdir sub$i
  cp ../$2 ./sub$i
done

cd ../
