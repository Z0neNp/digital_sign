#!/usr/bin/env python3
from unittest import TestLoader, TextTestRunner, TestSuite

from test.rsa import TestRSA

if __name__ == "__main__":
  loader = TestLoader()
  suite = TestSuite([
    loader.loadTestsFromTestCase(TestRSA)
  ])
  runner = TextTestRunner(verbosity=2)
  runner.run(suite)