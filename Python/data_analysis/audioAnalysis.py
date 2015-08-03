import librosa
import numpy as np

import sklearn
import sklearn.cluster
import sklearn.pipeline

import matplotlib.pyplot as plt
import seaborn

seaborn.set(style='ticks')


def main():
    MelSpec = librosa.util.FeatureExtractor(librosa.feature.melspectrogram,
                                            n_fft=2048,
                                            n_mels=128,
                                            fmax=librosa.midi_to_hz(116),
                                            fmin=librosa.midi_to_hz(24))
    LogAmp  = librosa.util.FeatureExtractor(librosa.logamplitude,
                                            ref_power=np.max)
    Transpose=librosa.util.FeatureExtractor(np.transpose)
    Stack   = librosa.util.FeatureExtractor(np.vstack, iterate=False)

    C       = sklearn.cluster.MiniBatchKMeans()
    ClusterPipe= sklearn.pipeline.Pipeline([('Mel Spectrogram', MelSpec),
                                            ('Log amplitude', LogAmp),
                                            ('Transpose', Transpose),
                                            ('Stack',   Stack),
                                            ('Cluster', C)])

    y_train, sr = librosa.load(librosa.util.example_audio_file(), duration=20, offset=0.0)
    ClusterPipe.fit([y_train])

    plt.figure(figsize=(4,4))
    librosa.display.specshow(C.cluster_centers_.T)

    plt.xticks(range(len(C.cluster_centers_.T)))
    plt.xlabel('Cluster #')

    plt.ylabel('Mel frequency')
    plt.colorbar(format='%+02.0f dB')

    plt.tight_layout()

    y_test, sr = librosa.load(librosa.util.example_audio_file(), duration=5, offsert=20.0)
    ClusterPipe.predict([y_test])
