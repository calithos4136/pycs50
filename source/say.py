import sys
# importing local files
from git.source.sayings import goodbye

if len(sys.argv) == 2:
    # cowsay.trex("Hello," + sys.argv[1])
    goodbye(sys.argv[1])
