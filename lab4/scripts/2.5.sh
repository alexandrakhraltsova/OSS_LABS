#!/bin/bash
find ~ -type f -name "*.txt" > /tmp/temp.txt
cat /tmp/temp.txt
cat /tmp/temp.txt | xargs du -acb 2>/dev/null | tail -1 | cut -f1
cat /tmp/temp.txt | xargs wc -l 2>/dev/null | tail -1 | awk '{print $1}'
rm /tmp/temp.txt
