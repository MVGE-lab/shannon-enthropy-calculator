shannon-enthropy-calculator
===========================

Python script for calculating of Shannon enthropy value using multiple sequence alignment in FASTA format.
Produces Tab-delimited list of Shannon enthropy of sequence alignment positions.
For using this tool you must have Matplotlib installed.

USAGE:

python Shannon.py input_file

input_file must be a properly formed FASTA-formatted sequence alignment file.

Example format:

"\>Sequence1_name(new line)
SEQUENCE1(new line)

\>Sequence2(new line)
SEQUENCE2"

Improper format:

"\>Sequence1_name(new line)
SEQUENCE1>Sequence2(new line)
SEQUENCE2"