## buildInstaller ##

Last modified: 4 June 2008


### Summary ###

buildInstaller is a command-line, Python script to generate user-friendly FLW installers for your [FontLab Studio](http://fontlab.com) Python scripts, macros and modules. Thanks to the FLW installer users do not have to copy the files to the FontLab or Python file structure manually or use command-line installers for more complicated projects.
The buildInstaller script only needs a simple configuration file to know which files from your development file structure will be included in the generated installer and where these files should go when installed.

If you want to find out easily what this can do, try the example installer.


### License ###

buildInstaller was originally developed for [Tiro Typeworks](http://www.tiro.ca), but it has been significantly extended and is distributed for free now.
Redistribution and use of the script is limited by the BSD licence:
[BSD licence](http://creativecommons.org/licenses/BSD/)

*If you use it commercially, be nice and buy me a drink at ATypI or anywhere else we might meet. Any suggestions for improvements are welcome.*


### What is a FLW installer? ###

FLW files are Python scripts with ``.flw`` extension. They are assigned to FontLab Studio by default, hence when user opens the FLW file (e.g. by double-clicking) it is opened in FontLab and executed as a common macro. FLW installer stands for a FLW file which contains macros within itself and can copy them out, when executed by FontLab, in order to install them on the user’s computer (the originator of this approach is [Tim Ahrens](http://justanotherfoundry.com/)).


### What can the generated FLW installers do? ###

The installers generated by the buildInstaller script have several important features:

* they work equally well on Windows and Mac (in general).
* the installer can contain text files as well as binary files, any file type.
* the files can be bundled in one or more bundles. When installing, users can select which bundles to install from a dialog.
* the files included are categorized into three groups: "macros", "modules" and "site-packages".
* under "macros" are files which will be installed to the FontLab's ``Macros`` folder (current user's folder is used)
* under "modules" are files to be installed to ``System/Modules/`` subfolder of the FontLab's Macros folder. This is where shared modules used by your macros should go, if they are used only in FontLab.
* under "site-packages" are files to be installed in Python's site-packages directory. This is where modules accessed by your python scripts should go, if they are used outside FontLab as well.
* paths to the folders containing modules need to be added to the Python environment. This is done by adding the module folders under ``modules-paths`` and ``site-packages-paths`` (see the configuration file for more information)
* the installer contains a licence. Users have to agree with the licence in order to proceed.
* the installer uses FontLab’s Python, so there is no risk of installing macros and modules to a different version of Python on the user’s computer.


### How to install buildInstaller ###

1. Copy buildInstaller.py anywhere you want to use it (possibly to folder which is in your PATH).
2. The script requires [PyYAML](http://pyyaml.org/). PyYAML is a YAML parser and emitter and it is very very easy to install. It is used to parse the configuration file.
3. You are done.


### How to use the buildInstaller ###

When you are in the same directory:

``$ python buildInstaller.py configuration.yaml generatedInstaller.flw``  

or

``$ ./buildInstaller.py configuration.yaml generatedInstaller.flw``

When the script is in your PATH environment:

``$ buildInstaller.py configuration.yaml generatedInstaller.flw``  

The script takes two arguments: first is the path to the configuration file, second is the name (and path) of the to-be-generated FLW installer.


### Example ###

The example.zip contains all files necessary to build an examplatory installer (including two bundles with macros and modules, and configuration file) and the built FLW installer.


### Regarding the size ###

Produced FLW installers can be quite large because the encoding method actually doubles the size of the bundled content, however, zip can effectively make them small again.
