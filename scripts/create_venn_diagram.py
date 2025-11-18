import matplotlib.pyplot as plt
from matplotlib_venn import venn2

fig, axes = plt.subplots(2, 2, figsize=(14, 12))
fig.suptitle('Set operations visualized with Venn diagrams', fontsize=18, fontweight='bold')

# Union
ax1 = axes[0, 0]
v1 = venn2(subsets=(3, 3, 1), set_labels=('Land animals', 'Water animals'), ax=ax1)
v1.get_patch_by_id('10').set_color('#ff6b6b')
v1.get_patch_by_id('01').set_color('#ff6b6b')
v1.get_patch_by_id('11').set_color('#ff6b6b')
v1.get_label_by_id('10').set_text('dog\ncat\nelephant')
v1.get_label_by_id('10').set_fontsize(14)
v1.get_label_by_id('11').set_text('frog')
v1.get_label_by_id('11').set_fontsize(14)
v1.get_label_by_id('01').set_text('fish\nwhale\nseal')
v1.get_label_by_id('01').set_fontsize(14)
v1.get_label_by_id('A').set_fontsize(14)
v1.get_label_by_id('B').set_fontsize(14)
ax1.set_title('Union\n(all animals)', fontsize=14, fontweight='bold')

# Intersection
ax2 = axes[0, 1]
v2 = venn2(subsets=(3, 3, 1), set_labels=('Land animals', 'Water animals'), ax=ax2)
v2.get_patch_by_id('10').set_color('#e0e0e0')
v2.get_patch_by_id('01').set_color('#e0e0e0')
v2.get_patch_by_id('11').set_color('#4ecdc4')
v2.get_label_by_id('10').set_text('')
v2.get_label_by_id('11').set_text('frog')
v2.get_label_by_id('11').set_fontsize(14)
v2.get_label_by_id('01').set_text('')
v2.get_label_by_id('A').set_fontsize(14)
v2.get_label_by_id('B').set_fontsize(14)
ax2.set_title('Intersection\n(amphibians)', fontsize=14, fontweight='bold')

# Difference
ax3 = axes[1, 0]
v3 = venn2(subsets=(3, 3, 1), set_labels=('Land animals', 'Water animals'), ax=ax3)
v3.get_patch_by_id('10').set_color('#95e1d3')
v3.get_patch_by_id('01').set_color('#e0e0e0')
v3.get_patch_by_id('11').set_color('#e0e0e0')
v3.get_label_by_id('10').set_text('dog\ncat\nelephant')
v3.get_label_by_id('10').set_fontsize(14)
v3.get_label_by_id('11').set_text('')
v3.get_label_by_id('01').set_text('')
v3.get_label_by_id('A').set_fontsize(14)
v3.get_label_by_id('B').set_fontsize(14)
ax3.set_title('Difference\n(only land animals)', fontsize=14, fontweight='bold')

# Symmetric difference
ax4 = axes[1, 1]
v4 = venn2(subsets=(3, 3, 1), set_labels=('Land animals', 'Water animals'), ax=ax4)
v4.get_patch_by_id('10').set_color('#f9ca24')
v4.get_patch_by_id('01').set_color('#f9ca24')
v4.get_patch_by_id('11').set_color('#e0e0e0')
v4.get_label_by_id('10').set_text('dog\ncat\nelephant')
v4.get_label_by_id('10').set_fontsize(14)
v4.get_label_by_id('11').set_text('')
v4.get_label_by_id('01').set_text('fish\nwhale\nseal')
v4.get_label_by_id('01').set_fontsize(14)
v4.get_label_by_id('A').set_fontsize(14)
v4.get_label_by_id('B').set_fontsize(14)
ax4.set_title('Symmetric difference\n(one environment only)', fontsize=14, fontweight='bold')

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig('think_and_compute/img/venn_diagram_operations.png', dpi=300, bbox_inches='tight')