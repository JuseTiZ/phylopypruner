"""
Amino acid or nucleotide sequence data type.
"""

import re

AMINO_ACIDS = "^[ABCDEFGHIKLMNPQRSTUVWYZX*-.]*$"
NUCLEOTIDES = "^[ATKMBVCNSWDGUYRH-.]*$"
IUPAC_CODES = (AMINO_ACIDS, NUCLEOTIDES)

class Sequence(object):
    """
    Represents a biological sequence. If no data type is provided, it will be
    determined based on the file's extension or the sequence content.
    """
    def __init__(self, description="", sequence_data=""):
        self._description = str(description)
        self._sequence_data = str(sequence_data)
        self._is_alignment = True if self.is_alignment else False
        if description:
            self._otu = re.split(r"\||@", description)[0]
            self._identifier = re.split(r"\||@", description)[1]
        else:
            self._otu = ""
            self._identifier = ""

    def __str__(self):
        return self.description

    def __len__(self):
        return len(self.sequence_data)

    def __nonzero__(self):
        return True

    def __bool__(self):
        return True

    @property
    def description(self):
        """A description or name of the sequence."""
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def sequence_data(self):
        """The raw sequence data."""
        return self._sequence_data

    @sequence_data.setter
    def sequence_data(self, value):
        self._sequence_data = value

    @property
    def otu(self):
        """
        The operational taxonomical unit (OTU) to which this sequence belongs to.
        """
        return self._otu

    @otu.setter
    def otu(self, value):
        self._otu = value

    @property
    def identifier(self):
        """
        A unique identifier for this sequence.
        """
        return self._identifier

    @identifier.setter
    def identifier(self, value):
        self._identifier = value

    @property
    def is_alignment(self):
        """
        Returns True if the sequence contain at least one gap character. Only
        dashes, '-' or dots '.' are considered to be gap characters.
        """
        return bool("-" in self.sequence_data)

    @is_alignment.setter
    def is_alignment(self, value):
        self._is_alignment = value

    def _validate_sequence(self):
        if not self.sequence_data:
            return
        for letter in self.sequence_data:
            if letter not in IUPAC_CODES:
                raise AssertionError('Non-IUPAC codes found in sequence \
                        {}.'.format(self.description))

    def count(self, letter):
        """Returns the frequency of the provided letter in this sequence."""
        return self._sequence_data.count(letter)

    def gc_content(self):
        """
        Return this sequence's GC content as a floating point number.
        """
        sequence = self.sequence_data
        seq_lower = sequence.lower()
        nucleotides = 'acgt'
        for base in seq_lower:
            if not base in nucleotides:
                print('Expected a nucleotide base (a, c, g, t), but found {} \
                        in sequence {}.'.format(base, self.description))
        gc_count = seq_lower.count('g') + seq_lower.count('c')
        return round(float(gc_count) / len(sequence), 2)

    def ungapped(self):
        """
        Return this sequence without any gap character ('-').
        """
        return self.sequence_data.replace("-", "")
