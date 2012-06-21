#! /usr/bin/env bash

# a completely automated yet disgusting process to push html to a gh-pages branch on github

# clobber the old local gh-pages branch, if any
git checkout master
git branch -D gh-pages || true

# make a new empty gh-pages branch holding an empty index.html
git symbolic-ref HEAD refs/heads/gh-pages
rm .git/index
git clean -fdx
touch index.html
git add -f index.html
git commit -m 'initial'

# now, build the actual index.html but call it something else
git checkout master
make index.html
cp index.html index.html.0
cp -r static static_0

# add the actual index.html to our fresh local gh-pages branch
git checkout gh-pages
mv index.html.0 index.html
mv static_0 static
git add -f index.html
git add -f static
git commit -m 'publishing index.html ...'

# delete the remote gh-pages branch
git push origin :gh-pages

# push our new one
git push origin HEAD:gh-pages

# switch back to master and destroy the local gh-pages branch
git checkout master
git branch -D gh-pages || true
