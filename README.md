FClone
====

### Requirements
* Python 2.7
* Perl

### Build Instructions
1. Download the source code
2. Install [py2exe](http://www.py2exe.org/)
3. Run `python setup.py py2exe` in the source directory
4. Copy `preprocess.pl` into `dist`

### Usage Instructions
**Using a compiled version:**

`fclone file1 file2 threshold`

* `file1` and `file2` are names of Java files **without the `.java` extension**
* `threshold` is an integer

**Using source version:**

`python fclone.py file1 file2 threshold`

* Arguments are the same as above
