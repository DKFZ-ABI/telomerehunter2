# TelomereHunter2 (TH2)

**⚠️ BETA VERSION - We welcome contributions and feedback!**

TelomereHunter2 is a complete reimplementation of the established TelomereHunter software, providing a sustainable framework for telomere analysis from whole genome sequencing data.

## About TelomereHunter

The original TelomereHunter software has been a key bioinformatics tool for digital diagnosis of telomere maintenance mechanisms (TMM) in precision oncology programs including MASTER and INFORM. It has been validated through comprehensive PCAWG studies and is actively used in clinical practice and neuroblastoma research.

**Original TelomereHunter:**
- Website: [TelomereHunter Website](https://www.dkfz.de/angewandte-bioinformatik/telomerehunter)
- Publication: [TelomereHunter Paper](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-019-2851-0)
- Software: pip install telomerehunter

## Key Features of TelomereHunter2

- **🐍 Pure Python3 implementation** - No R or external Samtools dependencies
- **🚀 Up to 80% runtime improvement** - Parallelized processing and algorithm optimizations
- **📦 Containerized distribution** - Docker and Apptainer support for diverse IT infrastructures
- **🔧 Enhanced format support** - CRAM files, hg19/hg38/T2T cytobanding files
- **🌍 Non-human genome support** - Mouse, dog, and other species analysis
- **🧬 Single-cell compatibility** - scATAC-seq data analysis capabilities

## Quick Start

```bash
# not implemented yet
# pip install telomerehunter2
# git clone https://github.com/ferdinand-popp/telomerehunter2.git
# apptainer pull docker://fpopp/telomerehunter2:latest

# Run tumor vs control analysis
telomerehunter2 -p Patient1 -ibt /files/sample01_tumor.cram -ict /files/sample01_control.cram -b cytobanding_hg38.txt
```

## Beta Testing
TelomereHunter2 is currently in beta testing phase. We are actively seeking:

- User feedback and bug reports
- Feature requests
- Contributions to code and documentation
- Validation studies across different datasets

## Contributing
We welcome contributions from the research community! Please:

- Report issues and bugs
- Submit feature requests
- Contribute code improvements
- Share your use cases and results

## Contact & Support
For questions, feedback, or contributions, please open an issue on this repository.
---
TelomereHunter2 addresses the growing challenges of analyzing large genomic datasets while maintaining the reliability needed for precision oncology and research applications.