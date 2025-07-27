#!/bin/bash

# Define the list of m values

m_values=(0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0)

# Loop over each m value
for m in "${m_values[@]}"; do
    python telephone.py message.txt -m "$m"
    echo "   "
done