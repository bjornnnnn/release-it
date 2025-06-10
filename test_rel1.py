#!/usr/bin/env python3

import releaseit
ver_last = releaseit.publish("test1", "test1.txt")
releaseit.mark_current("dev", "test1", ver_last )
releaseit.mark_current("prod", "test1", ver_last)