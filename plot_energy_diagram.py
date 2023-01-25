import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 14})
# Define the energy difference values for each reaction
differences1 = [0,-0.73,-0.6,0.01,-0.26,-1.58,-0.01]
differences2 = [0,-1.02,-0.16,-0.48,-0.40,-1.25,0.15]
differences3 = [0,-0.96,-0.62,0.03,-0.37,-1.34,0.08]
label_xaxis = ['Surface + NH$_2$NH$_2$', 'NH$_2$NH$_2$','NH$_2$NH', 'NHNH','NHN','N$_2$', 'Surface+N$_2$(g)' ]
# Create a list of energy difference values
differences_list = [differences1, differences2, differences3]
label_list = ['Rh (111)', 'RhRu (Tog_Sub)','RhRu (Scat_Sub)']
# Create a list of colors
colors = ['r','g','b']

# Create a figure and axes
fig, ax = plt.subplots(figsize=(10, 1))

# Create the energy values for each reaction by summing the differences
for idx, differences in enumerate(differences_list):
    energy_values = [sum(differences[:i+1]) for i in range(len(differences))]
    for i, y in enumerate(energy_values):
        if i<len(energy_values) - 1:
            ax.hlines(y, i-0.25, i+0.25, color=colors[idx], linewidth=3)
        else:
            ax.hlines(y, i-0.25, i+0.25, color=colors[idx], linewidth=3, label=label_list[idx])
        if i < len(differences) - 1:
            ax.plot([i+0.25, i+1-0.25], [y, energy_values[i+1]], '--', color='black', linewidth=1)
# Add labels and a title
ax.set_xlim(-0.5, len(differences1) - 0.5)
min_energy = min([min(differences) for differences in differences_list]) - 1.5
ax.set_ylim(min_energy-0.5, max([max(differences) for differences in differences_list]) +0.5)
ax.spines['left'].set_linewidth(2)
ax.spines['right'].set_linewidth(2)
ax.spines['top'].set_linewidth(2)
ax.spines['bottom'].set_linewidth(2)
#ax.set_xlabel('Reactions')
ax.set_ylabel('Energy (eV)')
#ax.set_title('Energy Diagram for 6 Elementary Reactions')
ax.set_xticks(range(len(differences1)))
ax.set_xticklabels(label_xaxis)
# Show the plot
plt.legend(loc='right')
plt.show()
