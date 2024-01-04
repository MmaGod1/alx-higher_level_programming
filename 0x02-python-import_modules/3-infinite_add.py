#!/usr/bin/python3
import sys

if __name__ == "__main__":
    sumArg = 0

    for i in range(1, len(sys.argv)):
        sumArg += int(sys.argv[i])
    print("{}".format(sumArg))
