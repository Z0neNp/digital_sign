#!/usr/bin/env python3
from unittest import TestLoader, TextTestRunner, TestSuite

from test.hash import TestFoldingHash
from test.rsa import TestRSA

if __name__ == "__main__":
  loader = TestLoader()
  suite = TestSuite([
    loader.loadTestsFromTestCase(TestFoldingHash),
    loader.loadTestsFromTestCase(TestRSA)
  ])
  runner = TextTestRunner(verbosity=2)
  runner.run(suite)