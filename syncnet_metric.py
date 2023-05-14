import argparse, glob, os
import numpy as np
import cv2

import time, subprocess, pdb
from SyncNetInstance import *

# ==================== PARSE ARGUMENT ====================

parser = argparse.ArgumentParser(description="SyncNetMetric")
parser.add_argument('--syncnet-itype', type=str, default='vid', choices=['imgdir', 'vid'], \
    help="format of input pair (img->static image, dir->directory of frames, vid->video file)")
parser.add_argument('--syncnet-ext', type=str, default='.mp4', \
    help="extention format of input files (e.g., .jpg, .png, .mp4, .avi)")

parser.add_argument('--initial_model', type=str, default="data/syncnet_v2.model", help='')
parser.add_argument('--batch_size', type=int, default='20', help='')
parser.add_argument('--vshift', type=int, default='15',
    help='tuning parameter(window length)')
parser.add_argument('--input-path', type=str, default="data/example.avi",
    help='target video')
parser.add_argument('--tmp_dir', type=str, default="./data/ffmpeg_outputs",
    help='directory to save')
parser.add_argument('--reference', type=str, default="demo",
    help='video name')

args = parser.parse_args()


# ==================== MAIN FUNCTION ====================

if __name__=='__main__':
    # Load SyncNet metric
    MSN = SyncNetInstance()

    # Load model
    MSN.loadParameters(args.initial_model)

    if args.syncnet_itype == 'imgdir':
        offset, conf, _ = MSN.evaluate(args, input_path='./data/example')
    elif args.syncnet_itype == 'vid':
        offset, conf, _ = MSN.evaluate(args, input_path=args.input_path)
    
    print("##====== SyncNet metric score ======##")
    print("  Offset: %d" %offset)
    print("  Confidence: %.3f" %conf)
    print("##==================================##\n")