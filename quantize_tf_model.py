# -*- coding: utf-8 -*-
# -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.#

#* File Name : quantize_tf_model.py
#
#* Purpose :
#
#* Creation Date : 08-12-2018
#
#* Last Modified : Sat 08 Dec 2018 10:44:15 AM IST
#
#* Created By :

#_._._._._._._._._._._._._._._._._._._._._.#

import tensorflow as tf
converter = tf.lite.TocoConverter.from_saved_model(saved_model_dir)
converter.post_training_quantize = True
tflite_quantized_model = converter.convert()
open("quantized_model.tflite", "wb").write(tflite_quantized_model)

