#!/bin/bash
#

## Creating a project w/ sub-directories

if [ -d "./$1" ]; then
  echo "Project already exists!"
  exit 0
fi

echo "Scaffolding for $1"
echo "Creating project '$1'"

mkdir $1
cd ./$1

for i in etc dist docs script src classes libs 
do
  echo "Creating folder ./$1/$i"
  mkdir $i
done

cd ./src

for i in main test
do
  echo "Creating folder ./$1/src/$i"
  mkdir $i
  cd ./$i
  echo "Creating files"
  touch file1.txt && touch file2.txt
  cd ../
done

cd ../../