#! /bin/bash
gcc $1.c && ./a.out
pstree | grep a.out
