---
title: Notes: ProGit
author: Haisheng, Wu
tags: reading, git
---

# Chapter 9.3
   - refs
   - refs/heads
   - refs/tags

~~~~~~{.sh}
[remote "origin"]
    url = ...
    fetch = +refs/heads/* : refs/remotes/origin/*
      ===> fetch all the references under "refs/heads" on the server
           and writes them to refs/remotes/origin locally
~~~~~~

_Questions_

   1. What does 'git branch B_NAME' actually do?
   2. What happened to HEAD when switching branch?

# Chapter 6

~~~~~~{.sh}
git add -i
~~~~~~

~~~~~~{.sh}
###
### revision selection
### ^ ::= parent of something, only two format ^ and ^2
git log HEAD^2
git log d107aoeu^2
git log HEAD~3
~~~~~~

~~~~~~{.sh}
git log master..branchA
git log origin/master..HEAD
git log branchA branchB ^branchC
git log master...branchA
~~~~~~

# Internal

Questions

![Git internal in one image](http://freizl.github.com/images/git_internal.png)

# Reference
  + [ProGit](http://progit.org/book/)
