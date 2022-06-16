start 

minlim@Mins-MBP bm_learn % git status  
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .DS_Store
        01 html/
        02 python/
        "03 python \354\235\264\354\203\201\355\230\225/"
        04 javascript/

nothing added to commit but untracked files present (use "git add" to track)
minlim@Mins-MBP bm_learn % cd ..
minlim@Mins-MBP com~apple~CloudDocs % ll
zsh: command not found: ll
minlim@Mins-MBP com~apple~CloudDocs % git status
fatal: not a git repository (or any of the parent directories): .git
minlim@Mins-MBP com~apple~CloudDocs % cd bm_learn 
minlim@Mins-MBP bm_learn % ll
zsh: command not found: ll
minlim@Mins-MBP bm_learn % ls
01 html                 02 python               03 python 이상형        04 javascript           05 python2
minlim@Mins-MBP bm_learn % git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .DS_Store
        01 html/
        02 python/
        "03 python \354\235\264\354\203\201\355\230\225/"
        04 javascript/

nothing added to commit but untracked files present (use "git add" to track)
minlim@Mins-MBP bm_learn % git branch
minlim@Mins-MBP bm_learn % 
minlim@Mins-MBP bm_learn % 
minlim@Mins-MBP bm_learn % 
minlim@Mins-MBP bm_learn % git checkout master
error: pathspec 'master' did not match any file(s) known to git
minlim@Mins-MBP bm_learn % git branch master
fatal: Not a valid object name: 'master'.
minlim@Mins-MBP bm_learn % git --version
git version 2.32.0 (Apple Git-132)
minlim@Mins-MBP bm_learn % git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .DS_Store
        01 html/
        02 python/
        "03 python \354\235\264\354\203\201\355\230\225/"
        04 javascript/

nothing added to commit but untracked files present (use "git add" to track)
minlim@Mins-MBP bm_learn % git add --all
error: '04 javascript/Product3. MiniStarcraft/' does not have a commit checked out
fatal: adding files failed
minlim@Mins-MBP bm_learn % cd 03\ python\ 이상형 
minlim@Mins-MBP 03 python 이상형 % cd ..
minlim@Mins-MBP bm_learn % ll
zsh: command not found: ll
minlim@Mins-MBP bm_learn % cd Pro
minlim@Mins-MBP bm_learn % cd 04\ javascript 
minlim@Mins-MBP 04 javascript % git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        ../.DS_Store
        ../01 html/
        ../02 python/
        "../03 python \354\235\264\354\203\201\355\230\225/"
        ./

nothing added to commit but untracked files present (use "git add" to track)
minlim@Mins-MBP 04 javascript % git pull
There is no tracking information for the current branch.
Please specify which branch you want to merge with.
See git-pull(1) for details.

    git pull <remote> <branch>

If you wish to set tracking information for this branch you can do so with:

    git branch --set-upstream-to=<remote>/<branch> master

minlim@Mins-MBP 04 javascript % ls -a
.                       .vscode                 Product3. MiniStarcraft product1. lotto
..                      Product2. Jasoseol      Product4. Anniversary
minlim@Mins-MBP 04 javascript % cd Product3.\ MiniStarcraft 
minlim@Mins-MBP Product3. MiniStarcraft % ls -a
.               .git            bunker.png      index.html      spit.png
..              background.png  drone.png       index_1.html
minlim@Mins-MBP Product3. MiniStarcraft % git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        background.png
        bunker.png
        drone.png
        index.html
        index_1.html
        spit.png

nothing added to commit but untracked files present (use "git add" to track)
minlim@Mins-MBP Product3. MiniStarcraft % git pull
There is no tracking information for the current branch.
Please specify which branch you want to merge with.
See git-pull(1) for details.

    git pull <remote> <branch>

If you wish to set tracking information for this branch you can do so with:

    git branch --set-upstream-to=<remote>/<branch> master

minlim@Mins-MBP Product3. MiniStarcraft % rm -rf .git
minlim@Mins-MBP Product3. MiniStarcraft % cd ../../
minlim@Mins-MBP bm_learn % ll
zsh: command not found: ll
minlim@Mins-MBP bm_learn % git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .DS_Store
        01 html/
        02 python/
        "03 python \354\235\264\354\203\201\355\230\225/"
        04 javascript/

nothing added to commit but untracked files present (use "git add" to track)
minlim@Mins-MBP bm_learn % git add --all
warning: adding embedded git repository: 04 javascript/Product4. Anniversary
hint: You've added another git repository inside your current repository.
hint: Clones of the outer repository will not contain the contents of
hint: the embedded repository and will not know how to obtain it.
hint: If you meant to add a submodule, use:
hint: 
hint:   git submodule add <url> 04 javascript/Product4. Anniversary
hint: 
hint: If you added this path by mistake, you can remove it from the
hint: index with:
hint: 
hint:   git rm --cached 04 javascript/Product4. Anniversary
hint: 
hint: See "git help submodule" for more information.
minlim@Mins-MBP bm_learn % ll
zsh: command not found: ll
minlim@Mins-MBP bm_learn % cd 04\ javascript 
minlim@Mins-MBP 04 javascript % ll
zsh: command not found: ll
minlim@Mins-MBP 04 javascript % cd ..
minlim@Mins-MBP bm_learn % ls -a
.                       .DS_Store               01 html                 03 python 이상형        05 python2
..                      .git                    02 python               04 javascript
minlim@Mins-MBP bm_learn % cd 04\ javascript 
minlim@Mins-MBP 04 javascript % cd Product4.\ Anniversary 
minlim@Mins-MBP Product4. Anniversary % ls -a
.               ..              .git            duhee.jpeg      heart.png       index.html      jisook.jpeg
minlim@Mins-MBP Product4. Anniversary % git status
On branch master
nothing to commit, working tree clean
minlim@Mins-MBP Product4. Anniversary % git remote get-url origin
https://github.com/Codin-Go/100product_basic
minlim@Mins-MBP Product4. Anniversary % cd ../..
minlim@Mins-MBP bm_learn % ll
zsh: command not found: ll
minlim@Mins-MBP bm_learn % git init
Reinitialized existing Git repository in /Users/minlim/Library/Mobile Documents/com~apple~CloudDocs/bm_learn/.git/
minlim@Mins-MBP bm_learn % ls -a 
.                       .DS_Store               01 html                 03 python 이상형        05 python2
..                      .git                    02 python               04 javascript
minlim@Mins-MBP bm_learn % rm -rf .git 
minlim@Mins-MBP bm_learn % ls -a
.                       .DS_Store               02 python               04 javascript
..                      01 html                 03 python 이상형        05 python2
minlim@Mins-MBP bm_learn % git init
hint: Using 'master' as the name for the initial branch. This default branch name
hint: is subject to change. To configure the initial branch name to use in all
hint: of your new repositories, which will suppress this warning, call:
hint: 
hint:   git config --global init.defaultBranch <name>
hint: 
hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
hint: 'development'. The just-created branch can be renamed via this command:
hint: 
hint:   git branch -m <name>
Initialized empty Git repository in /Users/minlim/Library/Mobile Documents/com~apple~CloudDocs/bm_learn/.git/
minlim@Mins-MBP bm_learn % ls -a
.                       .DS_Store               01 html                 03 python 이상형        05 python2
..                      .git                    02 python               04 javascript
minlim@Mins-MBP bm_learn % git add --all
warning: adding embedded git repository: 04 javascript/Product4. Anniversary
hint: You've added another git repository inside your current repository.
hint: Clones of the outer repository will not contain the contents of
hint: the embedded repository and will not know how to obtain it.
hint: If you meant to add a submodule, use:
hint: 
hint:   git submodule add <url> 04 javascript/Product4. Anniversary
hint: 
hint: If you added this path by mistake, you can remove it from the
hint: index with:
hint: 
hint:   git rm --cached 04 javascript/Product4. Anniversary
hint: 
hint: See "git help submodule" for more information.
minlim@Mins-MBP bm_learn % git 
minlim@Mins-MBP bm_learn % 
minlim@Mins-MBP bm_learn % 
minlim@Mins-MBP bm_learn % 
minlim@Mins-MBP bm_learn % 
minlim@Mins-MBP bm_learn % rm -rf .git 
minlim@Mins-MBP bm_learn % rm -rf 04\ javascript/
minlim@Mins-MBP bm_learn % cd 04\ javascript/Product4.\ Anniversary 
minlim@Mins-MBP Product4. Anniversary % rm -rf .git 
minlim@Mins-MBP Product4. Anniversary % l
zsh: command not found: l
minlim@Mins-MBP Product4. Anniversary % ls -a
.               ..              duhee.jpeg      heart.png       index.html      jisook.jpeg
minlim@Mins-MBP Product4. Anniversary % cd ..
minlim@Mins-MBP 04 javascript % ll
zsh: command not found: ll
minlim@Mins-MBP 04 javascript % cd ..
minlim@Mins-MBP bm_learn % git init
hint: Using 'master' as the name for the initial branch. This default branch name
hint: is subject to change. To configure the initial branch name to use in all
hint: of your new repositories, which will suppress this warning, call:
hint: 
hint:   git config --global init.defaultBranch <name>
hint: 
hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
hint: 'development'. The just-created branch can be renamed via this command:
hint: 
hint:   git branch -m <name>
Initialized empty Git repository in /Users/minlim/Library/Mobile Documents/com~apple~CloudDocs/bm_learn/.git/
minlim@Mins-MBP bm_learn % git add --all
minlim@Mins-MBP bm_learn % git commit -m "initial commit"
[master (root-commit) 4f98fec] initial commit
 34 files changed, 1412 insertions(+)
 create mode 100644 .DS_Store
 create mode 100644 01 html/box_css.css
 create mode 100644 01 html/box_index.html
 create mode 100644 01 html/codelion.css
 create mode 100644 01 html/codelion_1.css
 create mode 100755 01 html/images/facebook.png
 create mode 100755 01 html/images/insta.png
 create mode 100755 01 html/images/linked-in.png
 create mode 100755 01 html/images/twitter.png
 create mode 100644 01 html/index.html
 create mode 100644 01 html/index_1.html
 create mode 100644 01 html/reference.html
 create mode 100644 01 html/test.html
 create mode 100644 01 html/test2.css
 create mode 100644 01 html/test2.html
 create mode 100644 02 python/codelion.py
 create mode 100644 02 python/likelion.py
 create mode 100644 "03 python \354\235\264\354\203\201\355\230\225/likelion.py"
 create mode 100644 "03 python \354\235\264\354\203\201\355\230\225/lion.py"
 create mode 100644 04 javascript/.vscode/settings.json
 create mode 100644 04 javascript/Product2. Jasoseol/index.html
 create mode 100755 04 javascript/Product3. MiniStarcraft/background.png
 create mode 100755 04 javascript/Product3. MiniStarcraft/bunker.png
 create mode 100755 04 javascript/Product3. MiniStarcraft/drone.png
 create mode 100644 04 javascript/Product3. MiniStarcraft/index.html
 create mode 100755 04 javascript/Product3. MiniStarcraft/index_1.html
 create mode 100755 04 javascript/Product3. MiniStarcraft/spit.png
 create mode 100755 04 javascript/Product4. Anniversary/duhee.jpeg
 create mode 100755 04 javascript/Product4. Anniversary/heart.png
 create mode 100755 04 javascript/Product4. Anniversary/index.html
 create mode 100755 04 javascript/Product4. Anniversary/jisook.jpeg
 create mode 100644 04 javascript/product1. lotto/index.html
 create mode 100644 04 javascript/product1. lotto/myScript.js
 create mode 100644 04 javascript/product1. lotto/style.css
minlim@Mins-MBP bm_learn % git remote add origin https://github.com/Codin-Go/codelion-backup.git
minlim@Mins-MBP bm_learn % git push --set-upstream origin master
Enumerating objects: 45, done.
Counting objects: 100% (45/45), done.
Delta compression using up to 10 threads
Compressing objects: 100% (42/42), done.
Writing objects: 100% (45/45), 268.73 KiB | 29.86 MiB/s, done.
Total 45 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), done.
To https://github.com/Codin-Go/codelion-backup.git
 * [new branch]      master -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.
minlim@Mins-MBP bm_learn % 

zsh terminal
