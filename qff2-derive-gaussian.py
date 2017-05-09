
import h5py

from molmod.io.fchk import FCHKFile

from quickff.program import DeriveDiagFF, DeriveNonDiagFF
from quickff.reference import SecondOrderTaylor, get_ei_ff
from quickff.tools import guess_ffatypes
from yaff import System

fchk = FCHKFile('../qff_inputs/ch4.fchk')
numbers = fchk.fields.get('Atomic numbers')
energy = fchk.fields.get('Total Energy')
coords = fchk.fields.get('Current cartesian coordinates').reshape([len(numbers), 3])
grad = fchk.fields.get('Cartesian Gradient').reshape([len(numbers), 3])
hess = fchk.get_hessian().reshape([len(numbers), 3, len(numbers), 3])


system = System(numbers, coords)
system.detect_bonds()         # doesn't change anything?
system.set_standard_masses()  # doesn't change anything?

#Construct a QuickFF SecondOrderTaylor object containing the AI reference
ai = SecondOrderTaylor('ai', coords=coords, energy=energy, grad=grad, hess=hess)

guess_ffatypes(system, 'low')

#construct electrostatic force field from HE charges in gaussian_wpart.h5
f = h5py.File('../qff_inputs/ch4.h5')
charges = f['charges'][:]
scales = [0.0, 0.0, 0.5, 1.0]
ff_ei = get_ei_ff('EI', system, charges, scales, radii=None, average=True, pbc=[0,0,0])

#initialize and run program
program = DeriveDiagFF(system, ai, ffrefs=[ff_ei], fn_yaff='pars_cov.txt', plot_traj=True, xyz_traj=True)
program.run()
