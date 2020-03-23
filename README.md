# This project is meant to share code for the CORD-19 kaggle compition across project members. 

The following file structure should be used:

root

|

-- lib

-- notebooks

	|

	-- *fldr per candidate*

		|

		-- *N - notebooks*

	-- deliverable.ipynb

-- src

-- .gitignore

-- requirements.txt


**lib**

lib contains all library code, useful for sharing utility functions, custom algorithms or cleaning functions so that we do not duplicate too much code. These can be imported in any notebook (make sure you add a the lib route to your path structure).


If you are afraid of breaking anything in a common library, create a new branch first and make a merge request, ensuring you do not make breaking changes. 

**notebooks**


Version control is fucked up in notebooks, so if you have shareable code, commit them in the library folders. 


We should work in the deliverable notebook together I suppose, integrating various parts of our project into one notebook. All individual work should be done in private notebooks, identified by you own folder.

**src**


Contains the full contents of the competition zip file. To ensure everyone works with the same data, try not to change anything in source. If we create a new, cleaned dataset that might be usefull, you can do one of two things:

-- Zip the end result and send it around, with instructions on where to put it in SRC to make it work for everyone.

-- Share the cleaning code and let everyone generate the new dataset themselves, and store it in the exact same location. 

**.gitignore**

Basic gitignore, make sure we don't try to upload the entire src folder to git. 

**requirements.txt**

Used to maintain which libraries have been used. Please create a virtualenv to keep libraries consistent. 

*how to create a virtualenv in windows*
1. have pip
2. pip install virtualenv
3. In the command line, go to a folder where you want your environments
4. use 'python -m virtualenv [NAME OF YOUR ENV]'
5. A folder is created called [NAME OF YOUR ENV]
6. In the command line, go to the folder [NAME OF YOUR ENV]/Scripts
7. type 'activate', then enter
8. You are now working in a virtualenv!

*how to install requirements in the virtualenv on windows*
1. Go to the project folder where requirements.txt is located
2. In commandline, type 'pip install -r requirements.txt'
3. All requirements are installed!

*I want to add new requirements*
1. Create your own branch in the git repository
2. Type 'pip freeze > requirements.txt' in the folder containing requirements.txt
3. This creates a text file with all dependencies in your virtualenv
4. At some point, merge the branch with the master to ensure all dependencies are present. Fix any merge issues. 