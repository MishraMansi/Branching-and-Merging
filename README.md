# Branching-and-Merging"Added version 1.2 info" 
# Branching-and-Merging"Added version 1.2 info" 
# The below mentioned information are the task performed in Branching and Merging
Microsoft Windows [Version 10.0.19045.5608]
(c) Microsoft Corporation. All rights reserved.

C:\Users\LENOVO>git clone <https://github.com/MishraMansi/Branching-and-Merging>
The syntax of the command is incorrect.

C:\Users\LENOVO>git clone https://github.com/MishraMansi/Branching-and-Merging
Cloning into 'Branching-and-Merging'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
Receiving objects: 100% (3/3), done.

C:\Users\LENOVO>cd Branching-and-Merging

C:\Users\LENOVO\Branching-and-Merging>git commit -m "Initial commit with README"
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean

C:\Users\LENOVO\Branching-and-Merging>git remote add origin <your-repo-url>
The syntax of the command is incorrect.

C:\Users\LENOVO\Branching-and-Merging>git branch -M main

C:\Users\LENOVO\Branching-and-Merging>git push -u origin main
branch 'main' set up to track 'origin/main'.
Everything up-to-date

C:\Users\LENOVO\Branching-and-Merging>git remote add origin https://github.com/MishraMansi/Branching-and-Merging
error: remote origin already exists.

C:\Users\LENOVO\Branching-and-Merging>git branch -M main

C:\Users\LENOVO\Branching-and-Merging>git push -u origin main
branch 'main' set up to track 'origin/main'.
Everything up-to-date

C:\Users\LENOVO\Branching-and-Merging>git pull origin main
From https://github.com/MishraMansi/Branching-and-Merging
 * branch            main       -> FETCH_HEAD
Already up to date.

C:\Users\LENOVO\Branching-and-Merging>
C:\Users\LENOVO\Branching-and-Merging>git checkout -b feature/swagger-parser
Switched to a new branch 'feature/swagger-parser'

C:\Users\LENOVO\Branching-and-Merging>git add swagger_parser.py
warning: in the working copy of 'swagger_parser.py', LF will be replaced by CRLF the next time Git touches it

C:\Users\LENOVO\Branching-and-Merging>git commit -m "Added Swagger JSON parser"
[feature/swagger-parser 135b8c5] Added Swagger JSON parser
 1 file changed, 15 insertions(+)
 create mode 100644 swagger_parser.py

C:\Users\LENOVO\Branching-and-Merging>git push origin feature/swagger-parser
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 4 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 539 bytes | 134.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
remote:
remote: Create a pull request for 'feature/swagger-parser' on GitHub by visiting:
remote:      https://github.com/MishraMansi/Branching-and-Merging/pull/new/feature/swagger-parser
remote:
To https://github.com/MishraMansi/Branching-and-Merging
 * [new branch]      feature/swagger-parser -> feature/swagger-parser

C:\Users\LENOVO\Branching-and-Merging>git pull origin main
From https://github.com/MishraMansi/Branching-and-Merging
 * branch            main       -> FETCH_HEAD
Already up to date.

C:\Users\LENOVO\Branching-and-Merging>git checkout main
Switched to branch 'main'
Your branch is up to date with 'origin/main'.

C:\Users\LENOVO\Branching-and-Merging>git merge feature/swagger-parser
Updating 006b507..135b8c5
Fast-forward
 swagger_parser.py | 15 +++++++++++++++
 1 file changed, 15 insertions(+)
 create mode 100644 swagger_parser.py

C:\Users\LENOVO\Branching-and-Merging>git push -u origin main
Total 0 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/MishraMansi/Branching-and-Merging
   006b507..135b8c5  main -> main
branch 'main' set up to track 'origin/main'.

C:\Users\LENOVO\Branching-and-Merging>git fetch
From https://github.com/MishraMansi/Branching-and-Merging
 * [new branch]      ui-new-feature -> origin/ui-new-feature

C:\Users\LENOVO\Branching-and-Merging>git branch -r    # lists all remote branches
usage: git branch [<options>] [-r | -a] [--merged] [--no-merged]
   or: git branch [<options>] [-f] [--recurse-submodules] <branch-name> [<start-point>]
   or: git branch [<options>] [-l] [<pattern>...]
   or: git branch [<options>] [-r] (-d | -D) <branch-name>...
   or: git branch [<options>] (-m | -M) [<old-branch>] <new-branch>
   or: git branch [<options>] (-c | -C) [<old-branch>] <new-branch>
   or: git branch [<options>] [-r | -a] [--points-at]
   or: git branch [<options>] [-r | -a] [--format]

Generic options
    -v, --[no-]verbose    show hash and subject, give twice for upstream branch
    -q, --[no-]quiet      suppress informational messages
    -t, --[no-]track[=(direct|inherit)]
                          set branch tracking configuration
    -u, --[no-]set-upstream-to <upstream>
                          change the upstream info
    --[no-]unset-upstream unset the upstream info
    --[no-]color[=<when>] use colored output
    -r, --remotes         act on remote-tracking branches
    --contains <commit>   print only branches that contain the commit
    --no-contains <commit>
                          print only branches that don't contain the commit
    --[no-]abbrev[=<n>]   use <n> digits to display object names

Specific git-branch actions:
    -a, --all             list both remote-tracking and local branches
    -d, --[no-]delete     delete fully merged branch
    -D                    delete branch (even if not merged)
    -m, --[no-]move       move/rename a branch and its reflog
    -M                    move/rename a branch, even if target exists
    --[no-]omit-empty     do not output a newline after empty formatted refs
    -c, --[no-]copy       copy a branch and its reflog
    -C                    copy a branch, even if target exists
    -l, --[no-]list       list branch names
    --[no-]show-current   show current branch name
    --[no-]create-reflog  create the branch's reflog
    --[no-]edit-description
                          edit the description for the branch
    -f, --[no-]force      force creation, move/rename, deletion
    --merged <commit>     print only branches that are merged
    --no-merged <commit>  print only branches that are not merged
    --[no-]column[=<style>]
                          list branches in columns
    --[no-]sort <key>     field name to sort on
    --[no-]points-at <object>
                          print only branches of the object
    -i, --[no-]ignore-case
                          sorting and filtering are case insensitive
    --[no-]recurse-submodules
                          recurse through submodules
    --[no-]format <format>
                          format to use for the output


C:\Users\LENOVO\Branching-and-Merging>git checkout -b ui-new-feature origin/ui-new-feature
branch 'ui-new-feature' set up to track 'origin/ui-new-feature'.
Switched to a new branch 'ui-new-feature'

C:\Users\LENOVO\Branching-and-Merging>git tag release-1.1

C:\Users\LENOVO\Branching-and-Merging>git push origin release-1.1
Total 0 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/MishraMansi/Branching-and-Merging
 * [new tag]         release-1.1 -> release-1.1

C:\Users\LENOVO\Branching-and-Merging>echo "Added version 1.2 info" >> README.md

C:\Users\LENOVO\Branching-and-Merging>git add README.md

C:\Users\LENOVO\Branching-and-Merging>git commit -m "Updated for release 1.2"
[ui-new-feature a4d5008] Updated for release 1.2
 1 file changed, 1 insertion(+), 1 deletion(-)

C:\Users\LENOVO\Branching-and-Merging>git tag release-1.2

C:\Users\LENOVO\Branching-and-Merging>git push origin release-1.2
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 4 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 341 bytes | 85.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/MishraMansi/Branching-and-Merging
 * [new tag]         release-1.2 -> release-1.2

C:\Users\LENOVO\Branching-and-Merging>git tag
release-1.1
release-1.2

C:\Users\LENOVO\Branching-and-Merging>git push origin --delete release-1.1
To https://github.com/MishraMansi/Branching-and-Merging
 - [deleted]         release-1.1

C:\Users\LENOVO\Branching-and-Merging>git tag -d release-1.1
Deleted tag 'release-1.1' (was 135b8c5)

C:\Users\LENOVO\Branching-and-Merging>
