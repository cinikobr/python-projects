#!/bin/bash
echo Please enter a commit message.
read message

git add -A
git commit -m "$message"
git push

function pause(){
 read -s -n 1 -p "Press any key to continue . . ."
 echo ""
}

pause
