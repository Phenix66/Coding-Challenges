#!/usr/bin/env python3
import argparse
import os
import re
import sys

video_exts = ['mkv', 'mp4']

def file_rename(old, new):
    os.rename(old, new)

def tv_shows(files):
    pattern = re.compile('S[0-9]{2}E[0-9]{2}', re.IGNORECASE)
    for file in files:
        if os.path.isfile(file):
            parts = file.split('.')
            nameparts = []
            epi = ''
            ext = parts[-1]
            if ext in video_exts:
                for part in parts:
                    if pattern.match(part):
                        epi = part
                        break
                    nameparts.append(part)
                newname = (' '.join(nameparts)).title()
                newfilename = f'{newname} - {epi}.{ext}'
                file_rename(file, newfilename)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    ops = parser.add_mutually_exclusive_group()
    ops.add_argument('--tv', action='store_true', help='Rename TV shows in bulk')
    parser.add_argument('path', help='Directory containing target files')
    args = parser.parse_args()
    files = os.listdir(args.path)
    if args.tv:
        os.chdir(args.path)
        tv_shows(files)
    else:
        parser.print_help()
        print('\nPlease specify an operation to perform')
