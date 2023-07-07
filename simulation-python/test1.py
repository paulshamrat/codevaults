import random
from Bio.PDB import PDBIO, Structure, Chain, Residue, Atom

# Select a random amino acid
random_aa = random.choice(["ALA", "ARG", "ASN", "ASP", "CYS", "GLN", "GLU", "GLY", "HIS", "ILE",
                           "LEU", "LYS", "MET", "PHE", "PRO", "SER", "THR", "TRP", "TYR", "VAL"])

# Create a structure with a single amino acid residue
structure = Structure.Structure("random_amino_acid")
chain = Chain.Chain("A")
structure.add(chain)
residue = Residue.Residue((' ', 1, ' '), random_aa, " ")
chain.add(residue)

# Set coordinates for the residue
atom_n = Atom.Atom("N", (0.0, 0.0, 0.0), 0.0, 1.0, " ", "N", 0, "N")
atom_ca = Atom.Atom("CA", (1.5, 0.0, 0.0), 0.0, 1.0, " ", "CA", 0, "CA")
atom_c = Atom.Atom("C", (3.0, 0.0, 0.0), 0.0, 1.0, " ", "C", 0, "C")
residue.add(atom_n)
residue.add(atom_ca)
residue.add(atom_c)

# Define the PDB file name
pdb_file_name = "random_amino_acid.pdb"

# Save the structure as a PDB file
pdb_io = PDBIO()
pdb_io.set_structure(structure)
pdb_io.save(pdb_file_name)
