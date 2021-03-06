import params as p
from src.config import DB

# IMPORTANT! The criteria used to choose the parameters is that there are 3 samples of +/- per subject
# in every subepoch. There are 600 segments / subepoch.
# 1*5*20*100 = 10000 ( N_EXAMPLES_PER_CLASS * N_CLASSES * N_SUBEPOCHS * N_SUBJECTS_TRAIN = N_SEGMENTS_TRAIN )
def get_params():
    params = {
        p.DATABASE: DB.IBSR,
        p.INPUT_DIM: [256,128,256],

        p.N_CLASSES: 4,
        p.N_EPOCHS: 150,
        p.N_SUBEPOCHS: 1,
        p.BATCH_SIZE: 1,
        p.CLASS_WEIGHTS: 'inverse_weights',

        p.SAMPLING_SCHEME: 'whole',
        p.SAMPLING_WEIGHTS: [0.5, 0.5],
        p.N_SEGMENTS_TRAIN: 120,
        p.N_SUBJECTS_TRAIN: None,

        p.N_SEGMENTS_VALIDATION: 10,
        p.N_SUBJECTS_VALIDATION: None,

        p.TRAIN_SIZE: 0.6,
        p.DEV_SIZE: 0.4,

        p.DATA_AUGMENTATION_FLAG: True,
        p.NUM_MODALITIES:1,

        p.OUTPUT_PATH: '/work/acasamitjana/segmentation/IBSR/VNet',
        p.MODEL_NAME: 'v_net',
        p.LR: 0.0005
    }

    return params

