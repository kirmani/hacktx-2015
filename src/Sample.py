#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 sean <sean@wireless-10-147-252-146.public.utexas.edu>
#
# Distributed under terms of the MIT license.
"""TODO(sean): DO NOT SUBMIT without one-line documentation for test

TODO(sean): DO NOT SUBMIT without a detailed description of test.
"""
import argparse
import inspect
import os
import re
import sys
import time
import traceback

src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = '../lib/x64' if sys.maxsize > 2**32 else '../lib/x86'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))

import Leap
from Leap import CircleGesture
from Leap import KeyTapGesture
from Leap import ScreenTapGesture
from Leap import SwipeGesture

class SampleListener(Leap.Listener):
  def on_connect(self, controller):
    print("Connected")
    controller.enable_gesture(Leap.Gesture.TYPE_SWIPE)

  def on_frame(self, controller):
    frame = controller.frame()

    print("Frame id: %d, timestamp: %d, hands: %d, fingers: %d, tool: %d, "
            "gestures: %d" % (frame.id, frame.timestamp, len(frame.hands),
                len(frame.fingers), len(frame.tools), len(frame.gestures())))

def main():
  global args
  listener = SampleListener()
  controller = Leap.Controller()

  controller.add_listener(listener)

  print "Press Enter to quit..."
  try:
    sys.stdin.readline()
  except KeyboardInterrupt:
   pass
  finally:
      controller.remove_listener(listener)

if __name__ == '__main__':
  try:
    start_time = time.time()
    parser = argparse.ArgumentParser()
    parser.add_argument('-v','--verbose', action='store_true', default=False, \
        help='verbose output')
    parser.add_argument('-d','--debug', action='store_true', default=False, \
        help='debug output')
    args = parser.parse_args()
    # if len(args) < 1:
    #   parser.error('missing argument')
    if args.verbose: print(time.asctime())
    main()
    if args.verbose: print(time.asctime())
    if args.verbose: print('TOTAL TIME IN MINUTES:')
    if args.verbose: print(time.time() - start_time) / 60.0
    sys.exit(0)
  except KeyboardInterrupt, e: # Ctrl-C
    raise e
  except SystemExit, e: # sys.exit()
    raise e
  except Exception, e:
    print('ERROR, UNEXPECTED EXCEPTION')
    print(str(e))
    traceback.print_exc()
    os._exit(1)
