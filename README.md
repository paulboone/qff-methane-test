# QuickFF Force Field Fit on Methane - Test

## QuickFF

This is _close_ to what we want, but assumes a scale of [1,1,1,1] instead of [0.0, 0.0, 0.5, 1.0]. We are using the programatic interface still due to this lack of configuration options.

```
qff-input-ei.py --ffatypes="low" -o ei_pars.yaff ./qff_inputs/ch4.fchk ./qff_inputs/ch4.h5 '/'
qff.py -m "DeriveDiagFF" --ei=ei_pars.yaff --ffatypes=low ./qff_inputs/ch4.fchk

```

Actual run instructions:

```
cd results && python ../qff2-derive-gaussian.py
```

Results should look like:

```
BondHarm/C.H (kjmol/A^2  A)                                             
    fc =  3072 ± .000    rv = 1.093 ± .132

BendAHarm/H.C.H (kjmol/rad^2  deg)                                      
    fc = 276.7 ± .000    rv = 109.4 ± .001
```

Notes:
- For CH4, VDW and EI interactions make no difference when using the scales [0.0, 0.0, 0.5, 1.0]
  because there are no 1-4, 1-5 pairs.
- Using the DeriveNonDiagFF (i.e. with cross terms) does change the produced parameters.


## Packmol / LAMMPS

IMPORTANT: The LAMMPS input file lamps-NPT.input needs to be manually updated with the FF parameters
from QuickFF!

```
mkdir results

~/workspace/packmol/packmol < ./packmol-methane.txt
python3 ./packed_methane_pdb_to_lammps.py < ./results/methane2087.pdb > ./results/methane2087.data

# ADD THE CORRECT HEADER INFO to the data file

cd results && ~/workspace/lammps/src/lmp_serial < ../lammps-NPT.input

```
