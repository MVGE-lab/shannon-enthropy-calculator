shannon-enthropy-calculator
===========================

Python script for calculating of Shannon enthropy value using multiple sequence alignment in fasta format.
Produces Tab-delimited list of Shannon enthropy of sequence alignment positions.
If you have Matplotlib installed you can uncomment corresponding lines in the script.

USAGE:

python Shannon.py input_file

input_file must be a properly formed FASTA-formatted sequence alignment file.

Example format:

"\>Sequence1_name
SEQUENCE1
\>Sequence2
SEQUENCE2"

Improper format:

"\>Sequence1_name
SEQUENCE1>Sequence2
SEQUENCE2"