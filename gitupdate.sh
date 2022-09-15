#!/bin/bash
echo Please enter a commit message.
read message

git add -A
git commit -m "$message"
git push https://cinikobr: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@github.com/cinikobr/python-projects.git

function pause(){
 read -s -n 1 -p "Press any key to continue . . ."
 echo ""
}

pause
