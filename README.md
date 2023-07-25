# mech6480-2023
Resources for students enrolled in MECH6480 at UQ.

It is recommended that you clone this repository next to your own repository where you can store your personal work for this course. To clone a repository, you can do this through GitHub Desktop - there are many instructions available for this online e.g., https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository

If you would like guidance on setting up your own repository to store your work during the semester, one option is described as follows:

1. Create a GitHub account (hopefully if you are viewing this you already have one).
2. Create a new private repository, a suggestion would be to call this using your student number, e.g. s41234567_mech6480.
3. To use GitHub on your local device you can use GitDesktop (there are other options e.g., GitforWindows is installed on the UQ lab PCs).
4. Using GitDesktop you can clone your remote repository (the one stored in the cloud) to any local computer you happen to be working on.
5. Once you have done this, you have a folder on your machine that has a link to the repository on the cloud. Now you can create a file called README.md in your local folder that states the purpose of your repository.
6. Now you want to add this README.md to the remote repository. 

   Option 1: Interacting through GitHub Desktop:
   
   a. Add the file to the git history (you will need to add changes to this file later)
   
   b. Commit the file (or file changes) with a comment that describes the change.
   
   c. Push the committed files to the remote repository.

   Option 2: Interacting through a commandline Git tool:
   
   ```bash
   git add README.md
   git commit -m "Adding README.md to descript my repository"
   git push 
   ```
   
You now have a working directory that will allow you to practice version control and computational project development skills. 

## Python editors

A large portion of the code that we demo in contact sessions will be done using VS code. You are welcome to install this and test it out, but you are also welcome to use something like Spyder, PyCharm, Idle, etc. if you prefer.

