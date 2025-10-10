# 3. Source code control with Git and GitHub

## Setup

1. Make sure you installed have installed `git` on your computer (not in the project venv).
   See [computer setup](1-06-opt-computer_setup.md).

2. Make sure you created a GitHub account. See [computer setup](1-06-opt-computer_setup.md).

3. You may also want to install a gitignore plugin for your IDE, e.g.

- [gitignore for VS Code](https://marketplace.visualstudio.com/items?itemName=codezombiech.gitignore)
- [.ignore for PyCharm](https://plugins.jetbrains.com/plugin/7495--ignore)

4. Tool to work with GitHub

   You can work with GitHub directly from a Git command prompt. However, unless you feel comfortable using command line
   environments then this method isn't generally recommended for those just starting to learn Git and GitHub.

   PyCharm and VS Code have tools that integrate with GitHub. If you are using a python editor/IDE that doesn't have Git
   support you may need to install a local Git desktop application. There are many Git clients that are freely
   available,
   for convenience you might want to use GitHub Desktop software.

## Introduction

GitHub a tool that’s become widely used in the world of software development and data science.

GitHub is like a social network for code—a platform where you can store your projects, track changes, collaborate
with others, and showcase your work.

There are some key terms need to know:

- **Git**: Git is a version control system. It tracks changes to files over time, so you can revert to earlier versions,
  compare edits, and collaborate without overwriting each other’s work. GitHub uses Git.
- **GitHub**: GitHub is a cloud-based platform that hosts Git repositories. It adds powerful collaboration features like
  issue tracking, pull requests, and project management tools. You can access your work from anywhere and invite others
  to contribute.
- **Repository** (or "**repo**"): A repository is a project folder managed by Git. It contains all your files, history
  of changes, and instructions for collaborators. You can have public repos (visible to everyone) or private ones (just
  for you or your team).

## Overview of GitHub

GitHub holds a 'master' version of your project code, you can then have many copies (or 'clones') on one or more
computers that you and others use to work with the code. GitHub uses workflows to manage these changes and allow them to
be kept in sync.

There is no single way to work with GitHub though a minimal workflow would be:

1. Create repo on GitHub
2. Clone a repo to work locally
3. Commit changes as you work
4. Push one or more 'commit's (updates) to GitHub

If you are working with others, you would also need to 'pull' their changes, and make 'pull requests' to ask them to
take your changes.

This introduced some further terms:

- **Branch**: A branch is a separate line of development within your project. It lets you work on new features,
  experiments, or fixes without affecting the main codebase (usually called the main or master branch). Once your
  changes are ready, you can merge your branch back into the main project.
- **Commit**: A commit is like saving a snapshot of your project. It records the changes you've made to your files and
  includes a message describing what you did (e.g., “Fixed login bug” or “Added new chart to report”). Each commit is
  part of your project’s history, so you can always go back and see what changed, when, and why.
- **Push**: means you're sending your local commits to the remote repository on GitHub. You’ve made changes and
  committed them locally. Now you want to share those changes with others or back them up online.
- **Pull**: means you're downloading changes from GitHub to your local machine. Someone else may have updated the
  project on GitHub. You want to get the latest version before you start working. Pull will fetch and merge those
  changes into your local copy.

## Additional files to create when using source code control

Typically, you add 2 further files to your project in the root folder when working with Git and GitHub:

1. `.gitignore`
2. `README.MD`

## .gitignore

A `.gitignore` file is used to tell Git which files should not be tracked in the repository.

Create this before you use git for the first time in your project.

For example, you don’t want to track configuration files that are specific to the code
editor or IDE (e.g. VS Code), particularly when collaborating with others in a repo, as each person is likely to have a
different local config (Windows v. Mac, file locations etc.). If you don’t exclude these files from GitHub, then you may
unintentionally cause problems for each other by overwriting each other’s IDE configuration when you commit and push
changes to the repo. You also don’t want to track common python files such as the virtual environment for your project.
These take up space and as you have seen the venv can be quickly recreated and packages added using `requirements.txt`
or `pyproject.toml`.

You can create a typical .gitignore in your IDE using a text editor, though using a plugin in your IDE, PyCharm and VS
Code can make it easier to create a .gitgnore file from
templates.

- [VS Code .gitignore extensions](https://code.visualstudio.com/docs/editor/versioncontrol#_scm-provider-extensions)
- [Pycharm create .gitignore](https://www.jetbrains.com/help/pycharm/set-up-a-git-repository.html#ignore-files)

## README.md

`README.md` tells other developers important information about your repo such as what the repo contains, any set-up
instructions etc. You need to edit this for your coursework to explain to the markers anything they need to know to
set up and run your code.

`.md` means it is a Markdown format file. Markdown is widely used for documentation of code. It is not difficult to
learn, you just need a few basic syntax rules. Refer to
the [GitHub markdown guide](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).

1. Create a new file named `README.md` in your 'practice' project and open it.
2. Add a few lines e.g.:

    - A first level heading "Practice".
    - Add a second level heading e.g. "Introduction"
    - Add a line of text e.g. "This repository is for learning to use GitHub"

   ```markdown
   # A level 1 heading

   ## A level 2 heading

   Some text
   ```
3. Save the file.

## Task: Add your project code to a GitHub repo

There are various ways to create a repository (your project code) in GitHub, including

- Create a new empty repo on GitHub
- Create a new repo by pushing code from your IDE to GitHub
- Create a new repo by 'fork'ing another person's repo
- Create a repo by accepting a GitHub Classroom assignment (uses fork)

For this activity you will create a new repo on GitHub from your IDE.

The steps you need to follow will vary depending on IDE so check their documentation.

First you need to link your IDE to your GitHub account:

- VS Code
- [PyCharm](https://www.jetbrains.com/help/pycharm/github.html)

For PyCharm
you [share the code with GitHub](https://www.jetbrains.com/help/pycharm/manage-projects-hosted-on-github.html#share-on-GitHub).
Enter the login when prompted.

The [VS Code GitHub documentation](https://code.visualstudio.com/docs/editor/github) tells you to install the Pull
requests extension which is not strictly necessary for this course. This
is [an alternative guide here that simplifies the guidance](https://graphite.dev/guides/how-to-push-code-from-vscode-to-github).

You can do also this with 'git' commands from the terminal in either IDE:

1. Go to GitHub (and log in)
2. Click New repository
3. Give it a name and choose visibility (public/private)
4. Do not initialize with README (you already have files locally)
5. Return to your computer. Use the IDE Terminal, or a command prompt tool where you are in the project root folder:

    ```bash
    git init
    git add .
    git commit -m "Initial commit"
    git remote add origin https://github.com/USERNAME/REPO-NAME.git # replace USERNAME and REPO-NAME with your GitHub username and repo name 
    git push -u origin main # If your default branch is called master, use master instead of main.
    ```
6. Return to GitHub, you many need to refresh the page, but you should now see your files on GitHub.

You do not need to keep this practice repository. To delete:

- Close your IDE (close not minimise)
- Go to the folder structure on your computer and delete the folder.
- Go to GitHub and
  use [their documentation](https://docs.github.com/en/repositories/creating-and-managing-repositories/deleting-a-repository)
  to delete the repo.

## Next steps

For the rest of COMP0035 you should be able to manage with a minimum of two repositories:

1. Tutorial activities
2. Coursework (one repo for both)

The next two activities walk you through how to set these up. Each uses a different method.

You may also want to optionally [integrate your IDE with GitHub](1-07-opt-integrate-IDE-GitHub.md) to make it easier to
work between your IDE and GitHub.

[Next activity](1-04-activities-repo.md)