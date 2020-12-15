import molecool as mc # our package
import os # file paths
import matplotlib.pyplot as plt

benzene_file_path = os.path.join('D:\\Notre-Dame\\Classes_Research\\conferences_summer_school\\molssi-best-practices\\starting_material\\data\\xyz','benzene.xyz')
benzene_symbols, benzene_coords = mc.open_xyz(benzene_file_path)
benzene_bonds = mc.build_bond_list(benzene_coords)

print(benzene_bonds)

avg_sum = 0

for atoms, bl in benzene_bonds.items():
    avg_sum += bl

avg_bl = avg_sum/len(benzene_bonds)

print('The average bond length is {}'.format(avg_bl))

benzene_fig = mc.draw_molecule(benzene_coords, benzene_symbols, draw_bonds=benzene_bonds)

plt.savefig('benzene.png', dpi=300)

mc.bond_histogram(benzene_bonds, save_location="benzene_histogram.png")
