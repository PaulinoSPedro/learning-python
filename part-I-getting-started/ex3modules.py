'''

 1. Open terminal

 2. type "import ex2programs"
 When it's run internally python will compile the source code into byte code and create (if not exists) the directory __pycache__

 3. Move ex2programs.py to different_dir

 4. Try import it again
 It will not work since the cache will look at old directory and not the newer  directory

 5. Type "import different_dir.ex2programs"
 It will work and generate a new byte code on different_dir.

'''