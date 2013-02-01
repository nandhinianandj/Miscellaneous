import rpy2
import rpy2.robjects.lib.ggplot2 as ggplot2
import rpy2.robjects as robjects
import timeit

class Profiler_Rstat(object,timeit.Timer):
    def __init__(self,func,args,RepeatCount=1,Stats_file='stats',**kwargs):
        self.func = func
        self.args = args

        for attr,value in kwargs:
            setattr(self,attr,value)

        self.Timer = timeit.Timer(func)
        self.RepeatCounts = RepeatCount

        self.Stats_file = Stats_file
        self.Stats = None

    def get_timeit_stats(self):
        if self.args:
            self.repeat(self.func,self.args)
        else:
            self.repeat(self.func)
        self.Stats = self.Prof.getstats()

    def plot_timeit_stats(self):

#       pp = ggplot2.ggplot(self.Stats.get('callcount')) + ggplot2.aes_string(x='calls', y='time', col='factor(cyl)') + \
#     ggplot2.geom_point() + ggplot2.geom_smooth(ggplot2.aes_string(group = 'cyl'),method = 'lm')
#        pp.plot()
        pass

    def anova_analysis(self):
        r = robjects.r
        ctl = robjects.FloatVector([4.17,5.58,5.18,6.11,4.50,4.61,5.17,4.53,5.33,5.14])
        trt = robjects.FloatVector([4.81,4.17,4.41,3.59,5.87,3.83,6.03,4.89,4.32,4.69])
        group = r.gl(2, 10, 20, labels = ["Ctl","Trt"])
        weight = ctl + trt

        robjects.globalenv["weight"] = weight
        robjects.globalenv["group"] = group
        lm_D9 = r.lm("weight ~ group")

        # omitting the intercept
        lm_D90 = r.lm("weight ~ group - 1")

    def principal_component_analysis(self):
        base = importr('base')
        stats = importr('stats')
        graphics = importr('graphics')

        m = base.matrix(r.norm(100),ncol = 5)
        pca = stats.princomp(m)
        graphics.plot(pca,main ="Eigen Values")
        stats.biplot(pca,main="biplot")

def long_running_arith_calc_func():
    # Just a lot of junk
    import time
    a = 6
    ab = 6 **8
    time.sleep(2)
    cd = 45

def main():
    kwargs = args = None
    RProf = Profiler_Rstat(long_running_arith_calc_func,args,kwargs)
    RProf.get_timeit_stats()
    RProf.plot_timeit_stats()

if __name__ == '__main__':
    main()
