# TelomereHunter2

[![PyPI version](https://badge.fury.io/py/telomerehunter2.svg)](https://badge.fury.io/py/telomerehunter2)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE.txt)
[![Build Status](https://img.shields.io/github/workflow/status/fpopp22/telomerehunter2/CI)](https://github.com/fpopp22/telomerehunter2/actions)

TelomereHunter2 is a Python-based tool for estimating telomere content and analyzing telomeric variant repeats (TVRs) from genome sequencing data. It supports BAM/CRAM files, flexible repeat and banding inputs, and provides outputs for bulk and single-cell (scATAC-seq) data.

## Features

- Fast, container-friendly Python 3 implementation
- Supports BAM/CRAM, custom telomeric repeats, and non-human genomes
- Interactive HTML reports (Plotly)
- Docker and Apptainer/Singularity containers
- scATAC-seq support (barcode splitting and per-cell analysis)
- Robust input handling and exception management

## Installation

**Recommended:**  
```bash
pip install telomerehunter2
```

**From source:**  
```bash
git clone https://odcf-gitlab.dkfz.de/abi/comparative-cancer-genomics/telomere_hunter_2.git
cd telomere_hunter_2
python -m venv venv
source venv/bin/activate
pip install -e . --no-cache-dir
```

**Container usage:**  
See [Container Usage](#container-usage) for Docker/Apptainer instructions.

## Quickstart

```bash
telomerehunter2 -ibt sample.bam -o results/ -p SampleID -b telomerehunter2/cytoband_files/hg19_cytoBand.txt
```
For all options:  
```bash
telomerehunter2 --help
```

## Usage

### Bulk Analysis

- **Single sample:**  
  `telomerehunter2 -ibt tumor.bam -o out/ -p TumorID -b cytoband.txt`
- **Tumor vs Control:**  
  `telomerehunter2 -ibt tumor.bam -ibc control.bam -o out/ -p PairID -b cytoband.txt`
- **Custom repeats/species:**  
  `telomerehunter2 ... --repeats TTTAGGG TTAAGGG --repeatsContext TTAAGGG`

### scATAC-seq Analysis

Requires BAM with CB barcode tag and Sinto for splitting:
```bash
python sc_barcode_splitter_run.py -ibt input.bam -b cytoband.txt -p PatientID -o out/ --keep-bams
```
See `tests/run_sc_atac.py` for examples.

## Input & Output

**Input:**  
- BAM/CRAM files (aligned reads)
- Cytoband file (tab-delimited, e.g. `hg19_cytoBand.txt`)
- Optional: custom telomeric repeats

**Output:**  
- `summary.tsv`, `TVR_top_contexts.tsv`, `singletons.tsv`
- Plots (`plots/` directory, PNG/HTML)
- Logs (run status/errors)
- For scATAC: per-cell results in subfolders

## Dependencies

- Python >=3.8
- pysam, numpy, pandas, plotly
- Sinto (for scATAC-seq)
- Docker/Apptainer (optional)

Install all dependencies:  
```bash
pip install -r requirements.txt
```

## Container Usage

**Docker:**  
```bash
docker pull fpopp22/telomerehunter2
docker run --rm -it -v /data:/data fpopp22/telomerehunter2 telomerehunter2 -ibt /data/sample.bam -o /data/results -p SampleID -b /data/hg19_cytoBand.txt
```

**Apptainer/Singularity:**  
```bash
apptainer pull docker://fpopp22/telomerehunter2:latest
apptainer run telomerehunter2_latest.sif telomerehunter2 ...
```

## Troubleshooting

- **Memory errors:** Use more RAM or containers.
- **Missing dependencies:** Check `requirements.txt`.
- **CRAM support:** Needs reference FASTA (see pysam docs).
- **Plotly HTML issues:** Try disabling with `--no_html_report`.

For help: [GitHub Issues](https://github.com/fpopp22/telomerehunter2/issues)

## Documentation & Resources

- [Wiki](https://github.com/fpopp22/telomerehunter2/wiki)
- [Example Data](tests/)
- [Tutorial Videos](LICENSE.txt)
- [Original TelomereHunter Paper](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-019-2851-0)

## Citation

If you use TelomereHunter2, please cite:
- Sieverling, L., et al. "Genomic footprints of activated telomere maintenance mechanisms in cancer." Nature Communications 11.1 (2020): 733.
- This repository ([Zenodo DOI](https://zenodo.org/record/XXXXXX) when available)

## Contributing

Fork, branch, and submit pull requests. Please add tests and follow code style. For major changes, open an issue first.

## License

GNU General Public License v3.0. See [LICENSE](LICENSE.txt).

## Contact

- Ferdinand Popp (f.popp@dkfz.de)
- Lars Feuerbach (l.feuerbach@dkfz.de)

## Acknowledgements

Developed by Ferdinand Popp, Lina Sieverling, Philip Ginsbach, Lars Feuerbach. Supported by DKFZ Applied Bioinformatics.

---

Copyright 2025 Ferdinand Popp, Lina Sieverling, Philip Ginsbach, Lars Feuerbach
