AlmaLinux9 Bash shell
=======================

## Table of contents:

- Basic stuff
- Find, Grep, Sed and Rename
- Regular Expressions (Regexs)
- GitHub environment


# Basic stuff:

`cd ..` allows you to move up one level in the directory hierarchy.

`ls` command is used to list the files and directories in the current working directory.

`cdls() { cd "$@" && ls; }` defines a function named "cdls" that combines the functionalities of both the "cd" and "ls" commands.

`touch` create an empty file, but it can also be used to modify the access and modification timestamps of existing files.

`vim` allows to edit a file. To save the changes and exit Vim, press the Esc key to exit insert mode, then type :wq and press Enter.

`mkdir` creates a new directory with the specified name in the current working directory. 

`mkdir folder1 folder2 folder3` is used to create multiple directories at once. 

`rmdir` removes **empty** directories or folders.

`rm` removes a **file**.

`rm -rf` forcefully and recursively delete directories and their contents (**warning!**)

`cp file1 file2` is used to copy the contents of one file (file1) to another file (file2).

`cp -r` is used to recursively copy directories and their contents.

`cp /home/asd/folder/{file{1,2},xyz,abc} /home/asd/dest` uses brace expansion in the shell to copy multiple files from a source directory to a destination directory.

`mv file1 file2` rename/move a file.

`pwd` will output the name of the present working directory.

`ln -s source_file symbolic_link` is used to create a symbolic link, also known as a soft link, between a source file and a symbolic link.

`type` determines the type and location of a command or program.

`xzless` - Read compressed text from `.xz` file.

`shift+g` - Go to the bottom.

`q` - Quit.

`?` - Search **UPWARDS (case-sensitive!)**.

`/` - Search **DOWNWARDS**.

`n` - Next occurrence.

`N` - Previous occurrence.

# Find, Grep, Sed and Rename:

### find

`find . -name "*.cpp"` will find all files ending in `.cpp` in the current directory `.` and its subdirectories.

To match the actual `.` or `*` symbols, you can escape them as `\.` and `\*`. Case sensitive! For a partial match, use `"OUT*"` like for `OUTPUT`.

`find . -maxdepth 1 -type d` searches for all subfolders (up to a maximum depth of 1).

`find . -maxdepth 1 -type d \( ! -name . \) -exec bash -c "cd '{}' && pwd && script.sh" \;` searches for folders and executes a script inside them.

`find "$(pwd)" -type f` prints all the absolute paths of the files in a folder (+ `> file.txt`).

### grep

`grep -rni --include="*.txt" * -e 'hello'` searches recursively in THAT directory for all `.txt` files for the word "hello" case insensitive. For the whole word, use `-w`.

`grep -3 searchtext filename` will additionally output 3 lines before and after any lines containing `searchtext`. Any number of lines can be used here.

`grep -B 3 -A 2 foo README.txt` will print all lines containing "foo" plus 3 lines before and 2 lines after (case insensitive).

`grep -v searchtext filename` will output all lines EXCEPT those containing `searchtext`.

`grep -r searchtext` will recursively search all files and folders starting from the current directory.

`tac stdout | grep E0 -m 1` searches from the bottom and stops at the first occurrence.

`history | grep command` finds all recent commands related to that.

### sed and rename

**IMPORTANT NOTE ON SED.**

To make it work the same way on both Linux and Mac (OS 10.9+), you need to remove the space `sed -i'' -e ...`

`sed -i '' -e 's/T/F/g' FILE` replaces `T` with `F` line by line.

`sed -i '' -e '142,145s/T/F/g' FILE` replaces `T` with `F` line by line from line 142 to 145 inclusive.

`sed -i 's/\r$//' filename` if you have a file created in Windows, this is used to remove the carriage return that can cause errors in Linux. Pay attention to the `-i` which means "in-line mode".

`tac file.txt | sed '1,50s/T/F/g' | tac` replaces every `T` with `F` in the last 50 lines of `file.txt`.

`sed '/PATTERN/q' FILE` prints the entire file until it finds `PATTERN`.
