Java Module
===========

The java module is an emk module for compiling Java code and creating jar files. This module will autodetect .java files
in the current directory, compile them (with javac), and create a jar file out of the compiled classes. It will also autodetect
classes that contain a main() method; for each class with a main() method, the java module will create an executable jar
(named &lt;class name>.jar) that can be run using "java -jar &lt;class name>.jar".

Note that autodetection of main() methods will only work if the main() method is in the toplevel class in the
.java file (ie, it won't work if the main() method is in a static inner class). However you can explicitly
define classes that contain a main() method using the `exe_classes` property.

You can use the `depdirs` or `projdirs` properties to specify other directories (that emk builds in) that the Java
files in the current directory depend on. Using the `jar_in_jar` or `exe_jar_in_jar` properties, you can tell emk to merge
the jar files creates for those other directories into the jar file created for this directory.
Currently, the jar_in_jar/exe_jar_in_jar properties will only cause the emk-managed dependency jar contents
to be included in the jar file - this does not include the `sysjars` (ie, jar files that are built externally to emk).

Properties
----------
All properties are inherited from the parent scope if there is one.

 * **javac_cmd**: The path to the java compiler. The default value is "javac".
 * **jar_cmd**: The path to the jar utility. The default value is "jar".
  
 * **compile_flags**: Additional flags to pass to the java compiler. If you have a 'flag' that is more than one argument,
                      pass it as a tuple. Duplicate flags will be removed.
 * **exts**: A list of file extensions (suffixes) for autodetection of Java source code. The default value is [".java"].
 * **source_files**: A list of explicitly defined Java source files to compile.

 * **autodetect**: If True, the java module will autodetect Java source code to compile based on the file name suffix.
 * **autodetect_from_targets**: If True, then the autodetection of Java source files will include files generated by rules
                                in this directory. The default value is True.
 * **excludes**: A list of files that should not be compiled, even if they are autodetected.
  
 * **exe_classes**: A list of fully-qualified class names that contain valid main() methods. These will be built into executable jar files.
 * **exclude_exe_classes**: A list of fully-qualified class names that should not be considered for executables, even if
                            they contain a valid main() method.
 * **autodetect_exe**: If True, the java module will autodetect classes that contain valid main() methods and build them
                       into executable jar files. The default value is True.
  
 * **resources**: A list of (source path, relative jar path) tuples for resources to be added to the jar file.
                  The source path is the path of the file or directory that will be added to the jar file;
                  the relative jar path is that path relative to the jar file root where the source will be added.
  
 * **make_jar**: If True, all compiled java classes in the current directory will be added into a single jar file.
                 The default jar file path is &lt;build dir>/&lt;directory name>.jar. The default value is True.
 * **jarname**: If not None, this string will be used as the jar name instead of the name of the current directory. The default value is None.
 * **jar_in_jar**: If True, the contents of all jar dependencies (ie, from depdirs and projdirs) will be included in the generated
                   jar file for the current directory (assuming make_jar is True). The default value is False.
 * **exe_jar_in_jar**: If True, the contents of all jar dependencies (ie, from depdirs and projdirs) will be included in the generated
                       jar files for executable classes (to allow a self-contained jar executable). The default value is True.
 * **unique_names**: If True, the output jar files will be named according to the path from the project directory, to avoid
                     naming conflicts when the build directory is not a relative path. The default value is False.
  
 * **depdirs**: A list of directories that the java files in this directory depend on. The java module will instruct emk
                to recurse into these directories, and the java classes in those directories will be compiled before
                the java files in the current directory. When compiling java files, these directories will be added
                to the classpath. Currently, circular directory dependencies are not supported for java.
 * **projdirs**: A list of dependency directories (like depdirs) that are resolved relative to the project directory.
 * **sysjars**: A set of other jar files that the java files in this directory depend on. Will be added to the classpath.
