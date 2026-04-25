#!/usr/bin/env python3
"""
Generate Figure 1 (Architecture) and Figure 2 (Biological Pathway)
Editable SVGs with large fonts. svg.fonttype='none' for Inkscape editability.

FONT SIZING (current — user wants LARGER, see handoff):
  Titles: 24pt, Panel titles: 18pt, Labels: 13-16pt, Annotations: 10-14pt
  USER REQUIREMENT (not yet applied): minimum 20pt for dense box text, 32pt for all other text.
"""
import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams['svg.fonttype'] = 'none'
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from matplotlib.colors import LinearSegmentedColormap
import numpy as np

OUT = '.'

def gen_fig1():
    fig, ax = plt.subplots(1, 1, figsize=(16, 22))
    ax.set_xlim(0, 16); ax.set_ylim(0, 22); ax.axis('off')
    fig.patch.set_facecolor('white')

    C_TEAL = '#1A7A5C'; C_TEAL_BG = '#E8F4F0'; C_TEAL_DK = '#15624A'
    C_ORANGE = '#E89830'; C_ORANGE_BG = '#FFF3E0'
    C_PARAM_BG = '#EDF6F3'; C_MAROON = '#8B2252'; C_MAROON_BG = '#F5E0E8'

    ax.text(8, 21.3, 'Multi-Timepoint Computational Framework Architecture',
            fontsize=24, fontweight='bold', ha='center', va='center')
    ax.text(8, 20.65, 'Six-Stage Frontline Pipeline + Salvage Pathway Module (v3.0)',
            fontsize=16, ha='center', va='center', color='#666666', fontstyle='italic')
    ax.text(4.5, 19.9, 'General Framework', fontsize=18, fontweight='bold',
            ha='center', va='center', color=C_TEAL)
    ax.text(12.5, 19.9, 'Ewing Sarcoma Parameters', fontsize=18, fontweight='bold',
            ha='center', va='center', color=C_TEAL)

    stages = [
        ('Stage 1', 'Baseline Risk\nAssessment',
         'GRS: TP53 (2.0\u00D7), RB1 (1.2\u00D7),\nSTAG2 (1.15\u00D7), CDKN2A (1.1\u00D7)',
         'DP1: Diagnosis', 18.3),
        ('Stage 2', 'Dynamic Response\nAssessment',
         'BRS: w_ctDNA, w_LDH, w_ALP\n(genotype-conditional weights)',
         'DP2: Weeks 4\u20138', 16.0),
        ('Stage 3', 'Treatment-Related\nMortality',
         'Base 2.5%, age/extent\nmodifiers (COG, EE99)', None, 13.8),
        ('Stage 4', 'Treatment Failure\n& Histologic Response',
         'Necrosis \u226590%: good;\n<50%: poor response', None, 11.6),
        ('Stage 5', 'Post-Surgical MRD\nAssessment',
         'ctDNA-based MRD detection\n16.1\u00D7 risk ratio (MRD+/MRD\u2212)',
         'DP3: Post-Surgery', 9.4),
        ('Stage 6', 'Recurrence &\nOutcome Modeling',
         'MRD-stratified recurrence\n5-yr EFS: 5%\u201396%', None, 7.2),
    ]

    for snum, desc, params, dp, y in stages:
        box = FancyBboxPatch((1.0, y - 0.85), 7.0, 1.9,
                              boxstyle="round,pad=0.15", facecolor=C_TEAL_BG,
                              edgecolor=C_TEAL, linewidth=2.0)
        ax.add_patch(box)
        ax.text(1.7, y + 0.50, snum, fontsize=16, fontweight='bold',
                ha='left', va='center', color=C_TEAL_DK)
        ax.text(4.5, y - 0.15, desc, fontsize=14, ha='center', va='center', color='#333333')
        pbox = FancyBboxPatch((9.0, y - 0.85), 6.2, 1.9,
                               boxstyle="round,pad=0.15", facecolor=C_PARAM_BG,
                               edgecolor=C_TEAL, linewidth=1.5)
        ax.add_patch(pbox)
        ax.text(12.1, y + 0.05, params, fontsize=13, ha='center', va='center',
                color='#333333', linespacing=1.4)
        if dp:
            dpbox = FancyBboxPatch((7.1, y + 0.15), 2.4, 0.7,
                                    boxstyle="round,pad=0.1", facecolor=C_ORANGE_BG,
                                    edgecolor=C_ORANGE, linewidth=2.0)
            ax.add_patch(dpbox)
            ax.text(8.3, y + 0.50, dp, fontsize=13, fontweight='bold',
                    ha='center', va='center', color='#B07020')

    for i in range(5):
        y_top = stages[i][4] - 0.85; y_bot = stages[i+1][4] + 1.05
        ax.annotate('', xy=(4.5, y_bot), xytext=(4.5, y_top),
                    arrowprops=dict(arrowstyle='->', color=C_TEAL, lw=2.5, mutation_scale=20))

    sal_y = 4.4
    ax.annotate('', xy=(4.5, sal_y + 1.05), xytext=(2.5, stages[5][4] - 0.85),
                arrowprops=dict(arrowstyle='->', color=C_MAROON, lw=2.0,
                               linestyle='dashed', mutation_scale=18))
    ax.text(1.8, 5.7, 'Treatment\nFailure /\nRecurrence', fontsize=13, fontweight='bold',
            ha='center', va='center', color=C_MAROON, fontstyle='italic')
    sbox = FancyBboxPatch((1.0, sal_y - 0.85), 7.0, 1.9,
                            boxstyle="round,pad=0.15", facecolor=C_MAROON_BG,
                            edgecolor=C_MAROON, linewidth=2.5)
    ax.add_patch(sbox)
    ax.text(4.5, sal_y + 0.50, 'Salvage Pathway Module (v3.0)',
            fontsize=16, fontweight='bold', ha='center', va='center', color=C_MAROON)
    ax.text(4.5, sal_y - 0.15, 'Relapsed/Refractory Extension',
            fontsize=14, ha='center', va='center', color='#555555', fontstyle='italic')
    spbox = FancyBboxPatch((9.0, sal_y - 0.85), 6.2, 1.9,
                             boxstyle="round,pad=0.15", facecolor='#FCE8EF',
                             edgecolor=C_MAROON, linewidth=1.5)
    ax.add_patch(spbox)
    ax.text(12.1, sal_y + 0.25, 'Early (<2yr) vs Late (>2yr) relapse',
            fontsize=13, ha='center', va='center', color='#333333')
    ax.text(12.1, sal_y - 0.30, 'rEECur regimens: HD-IFOS, TC, IT, GD',
            fontsize=13, ha='center', va='center', color='#333333')
    ax.text(8, 2.8,
            'DP = Decision Point; GRS = Genetic Risk Score; BRS = Biomarker Response Score; '
            'MRD = Minimal Residual Disease; EFS = Event-Free Survival; TRM = Treatment-Related Mortality',
            fontsize=11, ha='center', va='center', color='#666666', fontstyle='italic')

    plt.tight_layout(pad=0.5)
    fig.savefig(f'{OUT}/Fig1_Architecture_v4.png', bbox_inches='tight', facecolor='white')
    fig.savefig(f'{OUT}/Fig1_Architecture_v4.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close(); print("Fig1 saved")


def gen_fig2():
    fig, ax = plt.subplots(1, 1, figsize=(14, 18))
    ax.set_xlim(0, 14); ax.set_ylim(0, 18); ax.axis('off')
    fig.patch.set_facecolor('white')

    C_GENE = '#2C3E6B'; C_GENE_L = '#D6DCE8'
    C_BIO = '#1A7A5C'; C_BIO_L = '#D0EDE3'
    C_MRD = '#B85C2F'; C_MRD_L = '#F0DDD0'
    C_OUT = '#8B2252'; C_CITE = '#666666'

    ax.text(7.0, 17.3, 'LAYER 1: GENETIC ALTERATIONS', fontsize=18, fontweight='bold',
            ha='center', va='center', color=C_GENE, fontstyle='italic')
    genes = [('TP53', '2.0\u00D7 failure\nrisk', 2.0), ('STAG2', '1.15\u00D7 failure\nrisk', 5.0),
             ('RB1', '1.2\u00D7 failure\nrisk', 8.5), ('CDKN2A', '1.1\u00D7 failure\nrisk', 11.5)]
    for name, desc, x in genes:
        box = FancyBboxPatch((x - 1.2, 15.5), 2.4, 1.3,
                              boxstyle="round,pad=0.1", facecolor=C_GENE_L,
                              edgecolor=C_GENE, linewidth=2.0)
        ax.add_patch(box)
        ax.text(x, 16.3, name, fontsize=16, fontweight='bold', ha='center', va='center', color=C_GENE)
        ax.text(x, 15.85, desc, fontsize=11, ha='center', va='center', color='#333333', linespacing=1.2)

    ax.annotate('', xy=(2.8, 13.6), xytext=(2.0, 15.3),
                arrowprops=dict(arrowstyle='->', color=C_GENE, lw=2.0, connectionstyle='arc3,rad=-0.1'))
    ax.text(1.0, 14.4, '\u2193 Apoptosis\n(0.70\u00D7 factor)', fontsize=11,
            ha='center', va='center', color=C_CITE, fontstyle='italic')
    ax.annotate('', xy=(6.5, 13.6), xytext=(2.0, 15.3),
                arrowprops=dict(arrowstyle='->', color=C_GENE, lw=1.5, connectionstyle='arc3,rad=-0.15'))
    ax.text(3.6, 15.0, '\u2191 Necrosis', fontsize=11, ha='center', va='center', color=C_CITE, fontstyle='italic')
    ax.annotate('', xy=(2.8, 13.6), xytext=(5.0, 15.3),
                arrowprops=dict(arrowstyle='->', color=C_GENE, lw=2.5, connectionstyle='arc3,rad=0.15'))
    ax.text(4.6, 14.1, '6\u00D7 ctDNA\nshedding', fontsize=11, fontweight='bold',
            ha='center', va='center', color=C_CITE, fontstyle='italic')
    ax.annotate('', xy=(6.5, 13.6), xytext=(5.0, 15.3),
                arrowprops=dict(arrowstyle='->', color=C_GENE, lw=1.2, connectionstyle='arc3,rad=0.05'))
    ax.text(6.3, 14.8, '1.13\u00D7 (2\u00D7 tumor\nvolume)', fontsize=10,
            ha='center', va='center', color=C_CITE, fontstyle='italic')
    ax.annotate('', xy=(2.8, 13.6), xytext=(8.5, 15.3),
                arrowprops=dict(arrowstyle='->', color=C_GENE, lw=1.0, connectionstyle='arc3,rad=0.2', linestyle='dashed'))
    ax.annotate('', xy=(6.5, 13.6), xytext=(11.5, 15.3),
                arrowprops=dict(arrowstyle='->', color=C_GENE, lw=1.0, connectionstyle='arc3,rad=0.2', linestyle='dashed'))
    ax.text(11.5, 14.4, 'Tirode 2014\nBosma 2019\nGillani 2025\nShulman 2018',
            fontsize=10, ha='center', va='center', color=C_CITE,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#F5F5F5', edgecolor='#CCCCCC', alpha=0.8))

    L2_y = 12.4
    ax.text(7.0, 13.6, 'LAYER 2: BIOMARKER DYNAMICS', fontsize=18, fontweight='bold',
            ha='center', va='center', color=C_BIO, fontstyle='italic')
    biomarkers = [('ctDNA', 't\u00BD \u2248 42 min', 'Apoptotic + Necrotic\n+ Exosomal release', 2.8),
                  ('LDH', 't\u00BD \u2248 3 days', 'Necrosis-dominant\n(5:1 over apoptosis)', 6.8),
                  ('ALP', 't\u00BD \u2248 7 days', 'Bone remodeling\n(site-dependent)', 10.8)]
    for name, hl, mech, x in biomarkers:
        box = FancyBboxPatch((x - 1.5, L2_y - 0.65), 3.0, 1.6,
                              boxstyle="round,pad=0.1", facecolor=C_BIO_L, edgecolor=C_BIO, linewidth=2.0)
        ax.add_patch(box)
        ax.text(x, L2_y + 0.45, name, fontsize=16, fontweight='bold', ha='center', va='center', color=C_BIO)
        ax.text(x, L2_y + 0.10, hl, fontsize=12, ha='center', va='center', color=C_BIO, fontstyle='italic')
        ax.text(x, L2_y - 0.35, mech, fontsize=10, ha='center', va='center', color='#333333', linespacing=1.2)

    wt_y = 10.5
    wt_box = FancyBboxPatch((2.0, wt_y - 0.55), 10.0, 1.2,
                              boxstyle="round,pad=0.12", facecolor='#FFF8E7',
                              edgecolor='#C8A84E', linewidth=2.0, linestyle='--')
    ax.add_patch(wt_box)
    ax.text(7.0, wt_y + 0.25, 'GENOTYPE-CONDITIONAL WEIGHTING', fontsize=14,
            fontweight='bold', ha='center', va='center', color='#7A6520')
    ax.text(7.0, wt_y - 0.18,
            'BRS = w\u2081(genotype,site)\u00B7ctDNA + w\u2082(site)\u00B7LDH + w\u2083(genotype)\u00B7ALP',
            fontsize=12, ha='center', va='center', color='#555555', fontstyle='italic')

    ax.annotate('', xy=(4.5, 8.3), xytext=(2.8, 9.7),
                arrowprops=dict(arrowstyle='->', color=C_BIO, lw=2.5))
    ax.text(2.2, 9.0, 'ctDNA+ \u2192 7\u00D7 MRD\ntumor cell load', fontsize=11,
            ha='center', va='center', color=C_CITE, fontstyle='italic', fontweight='bold')
    ax.annotate('', xy=(9.5, 8.3), xytext=(2.8, 9.7),
                arrowprops=dict(arrowstyle='->', color='#CC4444', lw=2.0, connectionstyle='arc3,rad=-0.15'))
    ax.text(6.5, 8.8, 'TGF-\u03B2 \u2192 NKG2D\nsuppression (0.6\u00D7)', fontsize=11,
            ha='center', va='center', color='#CC4444', fontstyle='italic')
    ax.annotate('', xy=(4.5, 8.3), xytext=(6.8, 9.7),
                arrowprops=dict(arrowstyle='->', color=C_BIO, lw=1.5, connectionstyle='arc3,rad=0.1'))
    ax.annotate('', xy=(4.5, 8.3), xytext=(10.8, 9.7),
                arrowprops=dict(arrowstyle='->', color=C_BIO, lw=1.0, connectionstyle='arc3,rad=0.15', linestyle='dashed'))
    ax.text(9.0, 9.2, 'Bone response\n(osseous only)', fontsize=10,
            ha='center', va='center', color=C_CITE, fontstyle='italic')
    ax.text(12.5, 9.0, 'Krumbholz 2016\nShulman 2018\nLee 2004\nBailey 2025',
            fontsize=9, ha='center', va='center', color=C_CITE,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#F5F5F5', edgecolor='#CCCCCC', alpha=0.8))

    L3_y = 7.2
    ax.text(7.0, 8.5, 'LAYER 3: POST-SURGICAL MRD ASSESSMENT', fontsize=18,
            fontweight='bold', ha='center', va='center', color=C_MRD, fontstyle='italic',
            bbox=dict(facecolor='white', edgecolor='none', pad=2, alpha=0.9))
    box3a = FancyBboxPatch((1.5, L3_y - 0.5), 5.0, 1.5,
                             boxstyle="round,pad=0.1", facecolor=C_MRD_L, edgecolor=C_MRD, linewidth=2.0)
    ax.add_patch(box3a)
    ax.text(4.0, L3_y + 0.35, 'Tumor Cell Burden', fontsize=15, fontweight='bold',
            ha='center', va='center', color=C_MRD)
    ax.text(4.0, L3_y - 0.10, 'ctDNA-detectable\nresidual disease', fontsize=11,
            ha='center', va='center', color='#333333')
    box3b = FancyBboxPatch((7.5, L3_y - 0.5), 5.0, 1.5,
                             boxstyle="round,pad=0.1", facecolor=C_MRD_L, edgecolor=C_MRD, linewidth=2.0)
    ax.add_patch(box3b)
    ax.text(10.0, L3_y + 0.35, 'Immune Surveillance', fontsize=15, fontweight='bold',
            ha='center', va='center', color=C_MRD)
    ax.text(10.0, L3_y - 0.10, 'NK cell capacity\n(ctDNA-trajectory dependent)', fontsize=11,
            ha='center', va='center', color='#333333')
    ax.annotate('', xy=(7.6, L3_y + 0.2), xytext=(6.4, L3_y + 0.2),
                arrowprops=dict(arrowstyle='<->', color=C_MRD, lw=2.0))
    ax.text(7.0, L3_y + 0.6, '16.1\u00D7\nrisk ratio', fontsize=12,
            fontweight='bold', ha='center', va='center', color=C_MRD,
            bbox=dict(boxstyle='round,pad=0.15', facecolor='white', edgecolor=C_MRD, alpha=0.9))

    ax.annotate('', xy=(7.0, 4.9), xytext=(4.0, 6.4),
                arrowprops=dict(arrowstyle='->', color=C_MRD, lw=2.5, connectionstyle='arc3,rad=-0.1'))
    ax.annotate('', xy=(7.0, 4.9), xytext=(10.0, 6.4),
                arrowprops=dict(arrowstyle='->', color=C_MRD, lw=2.5, connectionstyle='arc3,rad=0.1'))
    ax.text(2.8, 5.5, 'MRD+: 87.8%\nrecurrence', fontsize=12,
            ha='center', va='center', color=C_CITE, fontstyle='italic')
    ax.text(11.2, 5.5, 'MRD\u2212: 5.5%\nrecurrence', fontsize=12,
            ha='center', va='center', color=C_CITE, fontstyle='italic')

    L4_y = 4.0
    ax.text(7.0, 5.0, 'LAYER 4: RISK-STRATIFIED OUTCOME', fontsize=18, fontweight='bold',
            ha='center', va='center', color=C_OUT, fontstyle='italic')
    gradient = np.linspace(0, 1, 256).reshape(1, -1)
    cmap = LinearSegmentedColormap.from_list('risk', ['#2E8B57', '#FFD700', '#CC2222'])
    ax.imshow(gradient, aspect='auto', cmap=cmap, extent=[2.0, 12.0, L4_y - 0.45, L4_y + 0.45], zorder=2)
    border = FancyBboxPatch((2.0, L4_y - 0.45), 10.0, 0.90,
                              boxstyle="round,pad=0.0", facecolor='none',
                              edgecolor=C_OUT, linewidth=2.0, zorder=3)
    ax.add_patch(border)
    ax.text(1.8, L4_y, '96%\nEFS', fontsize=14, fontweight='bold', ha='right', va='center', color='#2E8B57')
    ax.text(12.2, L4_y, '5%\nEFS', fontsize=14, fontweight='bold', ha='left', va='center', color='#CC2222')
    ax.text(7.0, L4_y, '80-point survival range', fontsize=14,
            fontweight='bold', ha='center', va='center', color='white', zorder=4)

    dp_x = 13.5
    for label, y_pos in [('DP1\nDiagnosis', 16.0), ('DP2\nWeeks 4\u20138', 12.0), ('DP3\nPost-surgical', 7.2)]:
        ax.text(dp_x, y_pos, label, fontsize=12, ha='center', va='center',
                color='#666666', fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.2', facecolor='#F0F0F0', edgecolor='#999999'))
    ax.plot([dp_x, dp_x], [15.0, 8.0], color='#BBBBBB', linewidth=2.0, linestyle=':')

    caption = ("Figure 2. Biological pathway framework for genotype-conditional biomarker weighting. "
               "Four interconnected layers show how genetic alterations (Layer 1) modify biomarker "
               "dynamics (Layer 2) across distinct biological timescales, which in turn determine "
               "post-surgical MRD interpretation (Layer 3) and recurrence risk (Layer 4). "
               "Solid arrows = primary effects; dashed = secondary. Red arrow = immunosuppressive coupling. "
               "DP = Decision Point; BRS = Biomarker Response Score; MRD = Minimal Residual Disease; "
               "EFS = Event-Free Survival.")
    ax.text(7.0, 2.2, caption, fontsize=10, ha='center', va='top', color='#333333',
            wrap=True, fontstyle='italic',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#F8F8F8', edgecolor='#DDDDDD'))

    plt.tight_layout(pad=0.5)
    fig.savefig(f'{OUT}/Fig2_Biological_Pathway.png', bbox_inches='tight', facecolor='white')
    fig.savefig(f'{OUT}/Fig2_Biological_Pathway.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close(); print("Fig2 saved")

if __name__ == '__main__':
    gen_fig1(); gen_fig2()
