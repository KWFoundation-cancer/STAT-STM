# STM Foundation Model v3.0

A six-stage discrete-event Monte Carlo simulation framework for multi-timepoint risk stratification in Ewing Sarcoma. This repository contains the production model, the figure-generation scripts, and the data files used to produce the figures in:

> Kress, J.W. *Multi-Timepoint Risk Stratification in Rare Cancers: A Computational Framework.* Submitted to the *Journal of Biomedical Informatics* (2026).
>
> DOI: *will be provided on acceptance.*

---

## ⚠️ Not for clinical use

This is **research code**. It is not a medical device. It has not been cleared by the FDA, the EMA, or any other regulatory body. It must not be used to make clinical decisions for individual patients. The simulation framework is published for scientific reproducibility and methodological review only.

---

## Repository contents

| File | Role |
|---|---|
| `stm_foundation_model_v3_0.py` | Production simulation model. Six-stage discrete-event Monte Carlo framework with genotype-conditional biomarker weighting, post-surgical MRD assessment, and 30-year survivorship modeling. |
| `stm_v3_figure_data.json` | Authoritative data source for all main-text and supplementary figures. Output of validated simulation runs against COG AEWS0031, Euro-EWING 99, and rEECur trial data. |
| `data_brs_and_fig2.json` | Authoritative data source for the Biomarker Risk Score (BRS) discrimination metrics and the genetic-subgroup / biomarker / quartile / MRD panels. **Filename is historical**: `fig2` predates the figure renumbering performed during manuscript revision. The file is referenced by name inside several scripts and has been retained for traceability with the manuscript. |
| `LICENSE` | Apache License 2.0. |
| `CITATION.cff` | Citation File Format metadata for automated citation tools. |

---

## Reproducibility

### Verified file integrity

The production model has md5:

```
b85bba87fc23b4a168fce56b3bbe3023 stm_foundation_model_v3_0.py
```

This is the byte-identical copy used to produce every numerical result in the JBI submission.

### Software environment

- Python 3.11 (developed and tested on RHEL 8.10; no platform-specific code)
- Encoding: UTF-8 throughout

### Dependencies

Model (`stm_foundation_model_v3_0.py`):
- `numpy`
- `pandas`


No version pins are imposed; any reasonably current release of the above libraries is expected to work. If a divergence is observed against the JBI figures, please open an issue with the library versions used.

---

### Running the model
bash
python stm_foundation_model_v3_0.py
No arguments. The simulation runs three cohorts (localized, mixed, metastatic) at 10,000 patients each with fixed seed 42, and writes outputs to a sibling outputs_v3/ directory: per-cohort CSVs and stm_v3_figure_data.json (the data file used to produce all figures in the manuscript).

---

## What is intentionally **not** in this repository

- **Patient-level data of any kind.** The model is calibrated against published aggregate trial data only. No individual-patient records were used to train, validate, or run the simulation. Trial-level summary statistics from COG AEWS0031, Euro-EWING 99, and rEECur are cited in the manuscript and supplementary materials.

---

## License

Apache License 2.0. See `LICENSE` for the full text.

The Apache 2.0 license is used in preference to MIT specifically for the explicit patent-grant clause, which is appropriate for clinical-decision-support adjacent code where downstream patent ambiguity could deter legitimate research adoption.

---

## Citation

If this work informs your research, please cite the JBI publication. A `CITATION.cff` file is provided to enable automatic citation extraction by GitHub and reference managers. Once the DOI is assigned, both the citation file and this README will be updated with the resolved DOI.

A Zenodo-archived snapshot of this repository is recommended for citation in lieu of the bare GitHub URL, to provide a stable identifier independent of the repository's lifecycle.

---

## Author

James W. Kress, Ph.D.
The KressWorks Foundation
Northville, Michigan 48168, USA
ORCID: [0000-0002-2511-6822](https://orcid.org/0000-0002-2511-6822)
Contact: jimkress_58@kressworks.org

---

## Acknowledgments

The author acknowledges the support of Dave and Geri Brown, and Henriette Eles. This work is dedicated to the memory of Patience Canice Kress Hensley (1951-2009) a victim of recurrent Ewing Sarcoma..
