# ASReview CNN classifier
This repository contains a plugin for [ASReview](https://github.com/asreview) ![logo](https://raw.githubusercontent.com/asreview/asreview-artwork/e2e6e5ea58a22077b116b9c3d2a15bc3fea585c7/SVGicons/IconELAS/ELASeyes24px24px.svg "ASReview"). This plugin adds a convolutional neural network (CNN) model, that has been shown to outperform classical algorithms.

## Getting started

Run install.sh or install the new classifier with:

```bash
pip install .
```

or

```bash
python -m pip install git+https://github.com/JTeijema/asreview-plugin-model-cnn-17-layer.git
```

## Usage
The new convolutional neural network is implemented in [`asreviewcontrib/models/cnn.py`](asreviewcontrib/models/cnn.py) , usable with `-m power_cnn`:
```bash
asreview simulate benchmark:van_de_Schoot_2017 -m power_cnn -e doc2vec
```


## License
Apache-2.0 License 
