# aoc


# Misc
If .DS_Store was never added to your git repository, simply add it to your .gitignore file.

If you don't have one, create a file called
.gitignore
In your the root directory of your app and simply write

**/.DS_Store
In it. This will never allow the .DS_Store file to sneak in your git.

if it's already there, write in your terminal:
find . -name .DS_Store -print0 | xargs -0 git rm -f --ignore-unmatch
then commit and push the changes to remove the .DS_Store from your remote repo:

git commit -m "Remove .DS_Store from everywhere"

git push

And now add .DS_Store to your .gitignore file, and then again commit and push with the 2 last pieces of code (git commit..., git push...)

