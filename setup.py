from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='telomerehunter2',
    version='1.0.0',
    description='An advanced test version for TelomereHunter',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='telomere content read NGS WGS tumor control',
    author='LS, CH, LF, FP',
    author_email='f.popp@dkfz.com',
    license='GPL',
    packages=find_packages(),
    install_requires=[
        'numpy==1.26.4',
        'pysam',
        'pandas<2',
        'PyPDF2',
        'plotly',
        'kaleido',
        'sinto'
    ],
    include_package_data=True,
    zip_safe=False,
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'telomerehunter2 = telomerehunter2.telomerehunter2_main:main',
            'sc-barcode-split-run-telomerehunter2 = telomerehunter2.sc_barcode_splitter_run:main',
        ],
    },
)
