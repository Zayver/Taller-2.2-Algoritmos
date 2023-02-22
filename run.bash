#!/bin/bash

python main.py

gnuplot -persist <<EOF
    plot "out.txt" using 1:1 with linespoints title "Iterativo", \
    "out.txt" using 1:2 with linespoints title "Dividir y Vencer"
EOF

gnuplot -persist <<EOF
    plot "out1.txt" using 1:1 with linespoints title "Iterativo", \
    "out1.txt" using 1:2 with linespoints title "Dividir y Vencer"
EOF
