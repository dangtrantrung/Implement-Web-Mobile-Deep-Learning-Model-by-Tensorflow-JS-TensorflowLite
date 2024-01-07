# Python

import tensorflowjs as tfjs
model='models/best.hdf5'
tfjs_target_dir="tfjsmodel1"

tfjs.converters.save_keras_model(model, tfjs_target_dir)
