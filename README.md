FClone
====

FClone is a simple code similarity detector for Java source code.

### Requirements
* Python 2.7 (source version)
* Perl

### Build Instructions
1. Download the source code
2. Install [py2exe](http://www.py2exe.org/)
3. Run `python setup.py py2exe` in the source directory
4. Copy `preprocess.pl` and `README.md` into `dist`

### Usage Instructions

FClone is available in two versions: source and compiled. The source version is the raw source code, and can be run like any regular Python script.

`python fclone.py file1 file2 threshold`

* `file1` and `file2` are names of Java files **without the `.java` extension**
* `threshold` is an integer

The compiled version of FClone is compiled using py2exe and can be found [here](https://github.com/andrewjli/fclone/releases). These versions are able to run on computers that do not have Python installed, but *Perl is still required for FClone to work!*

`fclone file1 file2 threshold`

* Arguments are the same as above

**NOTE: Compiled versions of FClone have only been tested on Windows.**
