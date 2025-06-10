#!/usr/bin/env python3
import sys
import test_config
sys.path.append("..")
import goat
goat.REPO_ROOT = test_config.REPO_ROOT
v1 = goat.add("testfile1", "test1.txt")
v2 = goat.add("testfile1", "test2.txt")
goat.mark_current("dev", "testfile1", v2 )
goat.mark_current("acc", "testfile1", v2 )
goat.mark_current("main", "testfile1", v1)

v_acc =  goat.get_current_version("acc", "testfile1")
v_main = goat.get_current_version("main", "testfile1")
print(v_acc)
print(v_main)

f_acc = goat.get_file_content("testfile1", v_acc)
f_main = goat.get_file_content("testfile1", v_main)
print(f_acc)
print(f_main)       