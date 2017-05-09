# qff-methane-test

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
