
def readCsvWskipRows():
    import pandas as pd
    import numpy as np
    filePath = "./tes1.csv"
    headers = ["yMax", "lost", "frame", "label", "xMax", "xMin", "yMin"]
    sampleSize = 4000
    pdData = pd.read_csv(filePath, names=headers, skiprows=sampleSize,
                                                        dtype= {"frame": np.int,
                                                            "xMax": np.float,
                                                            "yMax": np.float,
                                                            "xMin": np.float,
                                                            "yMin": np.float,
                                                            "lost": bool,
                                                            "label": str})
    sampleData = pdData

def readCsvWrandom():
    import pandas as pd
    import numpy as np
    import random
    filePath = "./tes1.csv"
    headers = ["yMax", "lost", "frame", "label", "xMax", "xMin", "yMin"]
    sampleSize = 400
    pdData = pd.read_csv(filePath, names=headers, dtype= {"frame": np.int,
                                                            "xMax": np.float,
                                                            "yMax": np.float,
                                                            "xMin": np.float,
                                                            "yMin": np.float,
                                                            "lost": bool,
                                                            "label": str})
    sampleData = pdData.iloc[random.sample(pdData.index, sampleSize)]

readCsvWrandomStr = '''import pandas as pd
import numpy as np
import random
filePath = "./tes1.csv"
headers = ["yMax", "lost", "frame", "label", "xMax", "xMin", "yMin"]
sampleSize = 400
pdData = pd.read_csv(filePath, names=headers, dtype= {"frame": np.int,
                                                            "xMax": np.float,
                                                            "yMax": np.float,
                                                            "xMin": np.float,
                                                            "yMin": np.float,
                                                            "lost": bool,
                                                            "label": str})
sampleData = pdData.iloc[random.sample(pdData.index, sampleSize)]
'''

readCsvWskipRowsStr = '''import pandas as pd
import numpy as np
import subprocess
filePath = "./tes1.csv"
fileRecords = int(subprocess.check_output("wc -l %s"% filePath, shell=True).split(' ')[0])
headers = ["yMax", "lost", "frame", "label", "xMax", "xMin", "yMin"]
sampleSize = 4000
pdData = pd.read_csv(filePath, names=headers, skiprows=fileRecords-sampleSize,
                                                        dtype= {"frame": np.int,
                                                            "xMax": np.float,
                                                            "yMax": np.float,
                                                            "xMin": np.float,
                                                            "yMin": np.float,
                                                            "lost": bool,
                                                            "label": str})
sampleData = pdData'''

if __name__ == '__main__':
    import hotshot, hotshot.stats
    prof = hotshot.Profile("pandasSkipRows.prof")
    prof.runcall(readCsvWskipRows)
    prof.close()
    stats = hotshot.stats.load("pandasSkipRows.prof")
    stats.strip_dirs()
    stats.sort_stats('time', 'calls')
    stats.print_stats(40)

    prof = hotshot.Profile("pandasRandom.prof")
    prof.runcall(readCsvWrandom)
    prof.close()
    stats = hotshot.stats.load("pandasRandom.prof")
    stats.strip_dirs()
    stats.sort_stats('time', 'calls')
    stats.print_stats(40)

    import timeit
    print timeit.timeit(stmt=readCsvWskipRowsStr, number=300)
    print timeit.timeit(stmt=readCsvWrandomStr, number=300)
