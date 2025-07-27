#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.dirname(__file__))

from examples.circle_packing.evaluator import run_with_timeout

try:
    result = run_with_timeout('examples/circle_packing/initial_program.py', 30)
    print("SUCCESS:", result)
except Exception as e:
    print("ERROR:", str(e))
    import traceback
    traceback.print_exc()
