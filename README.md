# EGFR Kinase Domain: 3D Structure Prediction and Validation

![ColabFold](https://img.shields.io/badge/prediction-ColabFold%20%2F%20AlphaFold2-orange) ![PyMOL](https://img.shields.io/badge/visualisation-PyMOL-blue)

## Objective

Predict, visualise and independently validate the 3D structure of the kinase domain of the human Epidermal Growth Factor Receptor (EGFR) from its amino-acid sequence. EGFR is one of the most studied targets in cancer biology (lung, breast, colorectal), and this model is the starting point for a planned docking project.

## Target

| | |
|---|---|
| UniProt | [P00533 (EGFR_HUMAN)](https://www.uniprot.org/uniprotkb/P00533) |
| Modelled region | Kinase domain, residues 712–979 (268 aa) |
| Full-length protein | 1210 aa |

## Methods

1. Full EGFR sequence downloaded from UniProt (FASTA)
2. Kinase domain (712–979) extracted with Biopython
3. Structure predicted with **ColabFold** (AlphaFold2 on Google Colab; 5 models, MMseqs2 MSA, 3 recycles)
4. Highest-confidence model selected (rank_1: pLDDT 91.1, pTM 0.91)
5. Visualised in **PyMOL**, coloured by pLDDT and N→C (`scripts/visualize_pymol.py`)
6. Sequence-based domain validation with **InterProScan** (EBI web service)

## Results

| Coloured by pLDDT | Coloured N → C |
|---|---|
| ![pLDDT](figures/EGFR_kinase_pymol_pLDDT.png) | ![Rainbow](figures/EGFR_kinase_pymol_rainbow.png) |

### AlphaFold confidence

| Model | pLDDT | pTM |
|---|---|---|
| rank_1 | 91.1 | 0.910 |
| rank_2 | 90.9 | 0.912 |
| rank_3 | 89.5 | 0.896 |
| rank_4 | 90.9 | 0.906 |
| rank_5 | 89.8 | 0.905 |

pLDDT > 90 is the "very high confidence" range. The catalytic core is almost entirely in this range; confidence drops only at the flexible termini/loops.

### Structural check

The model shows the canonical protein kinase fold: a β-sheet-rich N-lobe and an α-helix-rich C-lobe, consistent with known kinase structures.

### Independent validation (InterProScan)

| Database | Hit |
|---|---|
| Pfam PF07714 | Protein tyrosine kinase, positions 2–257 |
| SMART SM00219 | Tyrosine kinase catalytic domain, positions 2–256 |
| PRINTS PR00109 | Tyrosine kinase, 5 motif matches |
| PROSITE PS00107 / PS00109 | Conserved kinase motifs |
| PANTHER PTHR24416 | Tyrosine kinase family |

This confirms at database level that the predicted structure is a tyrosine kinase domain.

## Repository Structure

```
egfr-kinaz-yapi-tahmini/
├── data/      # full EGFR and kinase-domain FASTA files
├── scripts/   # PyMOL visualisation script
└── figures/   # PyMOL images and best model (EGFR_kinase_best_model.pdb)
```

## Limitations

- This is a predicted structure, not an experimental (X-ray / cryo-EM) one. Experimental EGFR kinase structures exist in the PDB; comparing against them (e.g. RMSD) is a natural next step.
- Only the kinase domain is modelled; the extracellular and transmembrane regions of the 1210-aa protein are not included.
- Ligand/inhibitor interactions are not analysed here (planned for the docking project).
- Learning/portfolio project; not for drug design or clinical decisions.

## Next Step

Docking of known EGFR inhibitors against this model with AutoDock Vina.

## Author

**Atakan Aslan** · Molecular Biology and Genetics, Sivas Cumhuriyet University
