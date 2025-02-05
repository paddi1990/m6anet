r"""
This module is a collection of builder functions used during training and inference for building Python object from configuration files
"""
import pkg_resources
from itertools import product
import numpy as np


DEFAULT_MODEL_CONFIG = pkg_resources.resource_filename('m6anet.model', 'configs/model_configs/m6anet.toml')
DEFAULT_MODEL_WEIGHTS = pkg_resources.resource_filename('m6anet.model', 'model_states/human_hct116.pt')
DEFAULT_NORM_PATH = pkg_resources.resource_filename('m6anet.model', 'norm_factors/norm_factors_hct116.joblib')
DEFAULT_MIN_READS = 20
DEFAULT_READ_THRESHOLD = 0.033379376


NUM_NEIGHBORING_FEATURES = 1
CENTER_MOTIFS = [['A', 'G', 'T'], ['G', 'A'], ['A'], ['C'], ['A', 'C', 'T']]
FLANKING_MOTIFS = [['G', 'A', 'C', 'T'] for i in range(NUM_NEIGHBORING_FEATURES)]
ALL_KMERS = list(["".join(x) for x in product(*(FLANKING_MOTIFS + CENTER_MOTIFS + FLANKING_MOTIFS))])
ALL_KMERS = np.unique(np.array(list(map(lambda x: [x[i:i+5] for i in range(len(x) -4)],
                                    ALL_KMERS))).flatten())
KMER_TO_INT = {ALL_KMERS[i]: i for i in range(len(ALL_KMERS))}
INT_TO_KMER =  {i: ALL_KMERS[i] for i in range(len(ALL_KMERS))}
M6A_KMERS = ["".join(x) for x in product(*CENTER_MOTIFS)]
