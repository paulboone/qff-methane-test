# qff-methane-test

This is _close_ to what we want, but assumes a scale of [1,1,1,1] instead of [0.0, 0.0, 0.5, 1.0]. We are using the programatic interface still due to this lack of configuration options.

```
qff-input-ei.py --ffatypes="low" -o ei_pars.yaff ./ben.fchk ./ben.h5 '/'
qff.py -m "DeriveDiagFF" --ei=ei_pars.yaff --ffatypes=low ben.fchk

```

Actual run instructions:

```
python qff2-derive-gaussian.py
```
