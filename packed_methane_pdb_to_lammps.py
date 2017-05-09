import sys

a2 = a1 = None
in_header = True
while (in_header):
    line = sys.stdin.readline()
    if line.startswith("ATOM") or line.startswith("HETATM"):
        in_header = False

eof = False

atoms = []
bonds = []
angles = []

abs_bonds = []
abs_angles = []

order = ["C1", "H1", "H2", "H3", "H4"]
atoms_per_molecule = len(order)
atom_index = 0

relative_bonds = [[1,2],[1,3],[1,4],[1,5]]
relative_angles = [[2,1,3],[2,1,4],[2,1,5],[3,1,4],[3,1,5],[4,1,5]]
num_molecules = 0

while (line):
    v = [line[:6], line[6:11], line[12:16], line[17:20], line[21], line[22:26], line[30:38], line[38:46], line[46:54]]

    a = {'atom_id': v[1], 'local_index': v[2].strip(), 'molecule_id': v[5], 'x': v[6], 'y': v[7], 'z': v[8]}

    # last molucule in file should be the total number
    num_molecules = v[5]

    # IMPORTANT: these checks are important to make sure that the file is ordered as we expect
    # otherwise, when we extrapolate the atoms to types, they will not be correct.
    atom_index += 1
    # make sure our expected atom_index equals the index in file
    assert atom_index == int(v[1])
    # make sure our expected order equals order in file
    assert order[(atom_index - 1) % atoms_per_molecule] == v[2].strip()


    if a['local_index'] == "C1":
        a['atom_type'] = "1"
        a['charge'] = "-0.542"
    else:
        a['atom_type'] = "2"
        a['charge'] = "0.135"

    atoms += [" ".join([a['atom_id'], a['molecule_id'], a['atom_type'], a['charge'], a['x'], a['y'], a['z']])]

    line = sys.stdin.readline()
    if not line.startswith("ATOM") and not line.startswith("HETATM"):
        line = None

assert atom_index % atoms_per_molecule == 0

for m in range(0, int(num_molecules)):
    a0 = m * atoms_per_molecule # starting atom index

    abs_bonds += [[str(x[0] + a0), str(x[1] + a0)] for x in relative_bonds]
    abs_angles += [[str(x[0] + a0), str(x[1] + a0), str(x[2] + a0)] for x in relative_angles]

bonds = [" ".join([str(i), "1", *x]) for i,x in enumerate(abs_bonds)]
angles = [" ".join([str(i), "1", *x]) for i,x in enumerate(abs_angles)]

print("# lammps data file generated from packed_methane_pdb_to_lammps.py")
print("%s atoms" % len(atoms))
print("%s bonds" % len(bonds))
print("%s angles" % len(angles))

print("\n\n Atoms\n\n" + "\n".join(atoms))
print("\n\n Bonds\n\n" + "\n".join(bonds))
print("\n\n Angles\n\n" + "\n".join(angles))
