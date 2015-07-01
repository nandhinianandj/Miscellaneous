from pandas import *
import numpy as np
from scipy import stats

def main():
    fileName = ""
    experimentDF = read_csv(fileName, na_values=[" "])
    print experimentDF.dropna()
    print experimentDF["Virulence"].dropna()
    print experimentDF.fillna(0.0)["Virulence"]
    print experimentDF["Virulence"].dropna().mean()
    print experimentDF.fillna(0.0)["Virulence"].mean()
    print ("Mean Shannon Diversity w/ 0.8 Parasite Virulence =",
            experimentDF[experimentDF["Virulence"] == 0.8]["ShannonDiversity"].mean())
    # Find variance
    print ("Variance in Shannon Diversity w/ 0.8 Parasite Virulence =",
                experimentDF[experimentDF["Virulence"] == 0.8]["ShannonDiversity"].var())

    # Standard Error of the mean
    print ("SEM of Shannon Diversity w/ 0.8 Parasite Virulence =",
                stats.sem(experimentDF[experimentDF["Virulence"] == 0.8]["ShannonDiversity"]))

    treatment1 = experimentDF[experimentDF["Virulence"] == 0.5]["ShannonDiversity"]
    treatment2 = experimentDF[experimentDF["Virulence"] == 0.8]["ShannonDiversity"]

    # Mann-Whitney-Wilcoxon Rank test
    z_stat, p_val = stats.ranksums(treatment1, treatment2)

    print "MWW RankSum P for treatments 1 and 2 =", p_val

    # One way ANOVA
    f_val, p_val = stats.f_oneway(treatment1, treatment2, treatment3)

    print "One-way ANOVA P =", p_val

    # # compute 95% confidence intervals around the mean
    CIs = bootstrap.ci(data=treatment1, statfunction=scipy.mean)

    # 80% confidence interval
    CIs = bootstrap.ci(treatment1, scipy.mean, alpha=0.2)
    print "Bootstrapped 80% confidence interval\nLow:", CIs[0], "\nHigh:", CIs[1]

    # bootstrap 20,000 samples instead of only 10,000
    CIs = bootstrap.ci(treatment1, scipy.mean, n_samples=20000)
    print ("Bootstrapped 95% confidence interval w/ 20,000 samples\nLow:",
                CIs[0], "\nHigh:", CIs[1])


if __name__ == "__main__":
    main()
