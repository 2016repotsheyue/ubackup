--- Lib/distutils/command/build_py.py.orig	2011-06-11 08:46:24.000000000 -0700
+++ Lib/distutils/command/build_py.py	2012-02-04 12:18:03.532991973 -0800
@@ -326,11 +326,12 @@
         return outputs
 
     def build_module(self, module, module_file, package):
-        if isinstance(package, str):
+        if isinstance(package, str) or isinstance(package, unicode):
             package = package.split('.')
         elif not isinstance(package, (list, tuple)):
             raise TypeError(
-                  "'package' must be a string (dot-separated), list, or tuple")
+                  "'package' must be a string (dot-separated), list, or tuple," + \
+                  "got " + repr(package))
 
         # Now put the module source file into the "build" area -- this is
         # easy, we just copy it somewhere under self.build_lib (the build
