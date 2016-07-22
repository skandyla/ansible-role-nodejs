#!/usr/bin/env python
# testinfra

def test_nodejs_is_installed(Package):
  nodejs = Package("nodejs")
  assert nodejs.is_installed
#  assert nodejs.version.startswith("4")

