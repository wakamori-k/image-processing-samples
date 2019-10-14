import numpy as np
import cv2
import sys
import argparse
import os

def get_args():
    parser = argparse.ArgumentParser(add_help=True)

    parser.add_argument('-f', '--file', help="video file path", required=True)
    parser.add_argument('-i', '--interval', type=int, help="sampling interval", default=10)
    parser.add_argument('-o', '--output', help="output directory", default="./")
    parser.add_argument('-q', '--quality', type=int, help="jpeg quality", default=100)

    args = parser.parse_args()

    return args

def main():
    args = get_args()
    cap = cv2.VideoCapture(args.file)

    frame_cnt = -1
    vfile_name = os.path.basename(args.file) # video file name
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), args.quality]

    while(cap.isOpened()):
        ret, frame = cap.read()
        frame_cnt += 1

        if not ret:
            sys.stderr.write("Error: failing capture in frame {}\n".format(frame_cnt))

        if frame_cnt % args.interval != 0:
            continue
        
        fname = "{}_{}.jpg".format(os.path.splitext(vfile_name)[0], frame_cnt)
        save_path = os.path.join(args.output, fname)
        print("save {}".format(fname))
        cv2.imwrite(save_path, frame, [cv2.IMWRITE_JPEG_QUALITY, args.quality])

    cap.release()
    cv2.destroyAllWindows()

if __name__=="__main__":
    main()

