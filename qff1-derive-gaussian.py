
# import numpy as np

from quickff.program import Program
from quickff.system import System
from quickff.model import Model


system = System.from_files(['ben.fchk', 'ben.h5'], ei_path='')
system.guess_ffatypes('low')
system.determine_ics_from_topology()

model = Model.from_system(system, ei_pot_kind='HarmPoint', vdw_pot_kind='HarmLJ', ic_ids=['bonds', 'bends'])

#initialize and run program
program = Program(system, model)
program.run()