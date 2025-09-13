#!/usr/bin/env python3
"""
Simple CSV reader/writer.
Usage:
  python scripts/csv_reader.py read data.csv
  python scripts/csv_reader.py read --dict data.csv
  python scripts/csv_reader.py write output.csv "name,age,city" "Alice,25,Tokyo"
"""
import csv
import argparse
import sys

def read_csv(path, use_dict=False):
    with open(path, newline='', encoding='utf-8') as f:
        if use_dict:
            reader = csv.DictReader(f)
            for row in reader:
                print(row)
        else:
            reader = csv.reader(f)
            for row in reader:
                print(row)

def write_csv(path, rows):
    # rows: list of comma-separated strings
    parsed = [r.split(',') for r in rows]
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(parsed)
    print(f"Wrote {len(parsed)} rows to {path}")

def main():
    parser = argparse.ArgumentParser(description="CSV read/write helper")
    sub = parser.add_subparsers(dest='cmd', required=True)
    r = sub.add_parser('read')
    r.add_argument('file')
    r.add_argument('--dict', action='store_true', help='use DictReader')
    w = sub.add_parser('write')
    w.add_argument('file')
    w.add_argument('rows', nargs='+', help='rows as comma-separated strings')

    args = parser.parse_args()
    if args.cmd == 'read':
        read_csv(args.file, use_dict=args.dict)
    elif args.cmd == 'write':
        write_csv(args.file, args.rows)

if __name__ == '__main__':
    main()
