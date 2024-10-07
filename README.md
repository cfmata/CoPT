# [ECCV 2024] CoPT: Unsupervised Domain Adaptive Segmentation using Domain-Agnostic Text Embeddings
by
[Cristina Mata](https://cfmata.github.io/),
[Kanchana Ranasinghe](https://kahnchana.github.io) and 
[Michael Ryoo](https://michaelryoo.com)

[[Paper]](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/07950.pdf)

## Abstract

Unsupervised domain adaptation (UDA) involves learning class semantics from labeled data within a source domain that 
generalize to an unseen target domain. UDA methods are particularly impactful for semantic segmentation, where 
annotations are more difficult to collect than in image classification. Despite recent advances in large-scale 
vision-language representation learning, UDA methods for segmentation have not taken advantage of the domain-agnostic 
properties of text. To address this, we present a novel Covariance-based Pixel-Text loss, CoPT, that uses 
domain-agnostic text embeddings to learn domain-invariant features in an image segmentation encoder. The text 
embeddings are generated through our LLM Domain Template process, where an LLM is used to generate source and target 
domain descriptions that are fed to a frozen CLIP model and combined. In experiments on four benchmarks we show that a 
model trained using CoPT achieves the new state of the art performance on UDA for segmentation.

# Installation

Create a virtual environment, install pip and the packages needed:
```
conda create -n copt python=3.8.5
conda activate copt
conda install pip
pip install -r requirements.txt -f https://download.pytorch.org/whl/torch_stable.html
pip install mmcv-full==1.3.7
```
CoPT is built on top of [MIC](https://github.com/lhoyer/MIC/tree/master/seg). 
That page has instructions on how to set up the datasets and train a baseline MIC model. Please make sure you update the paths to your datsets in the config files in the configs folder.

# Experiments

To train MIC with CoPT on the benchmarks reported in the paper you can use the following config files in configs/mic/:
* GTA to Cityscapes: gta2cs_copt.py
* Synthia to Cityscapes: synthia2cs_copt.py
* Cityscapes to ACDC: cityscapes2acdc_copt.py
* Cityscapes to DarkZurich: cs2dz_copt.py

# Checkpoints

Coming Soon...

# Acknowledgements

Huge shout out to Lukas Hoyer and fellow authors of MIC, HRDA and DAFormer for distributing such easy to use code!

# Citation

If you find CoPT useful in your research, please consider citing:

```
@InProceedings{mata2024copt,
  title={CoPT: Unsupervised Domain Adaptive Segmentation using Domain-Agnostic Text Embeddings},
  author={Mata, Cristina and Ranasinghe, Kanchana and Ryoo, Michael},
  booktitle={Proceedings of the European Conference on Computer Vision (ECCV)},
  year={2024}
}
```

Questions? Contact cfmata@cs.stonybrook.edu.