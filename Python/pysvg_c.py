import pysvg as ps

import numpy as np

test_d = np.arange(10,40,5)
actual_data = np.linspace(-1,1,15)

filename = "test.svg"
#svg_obj = ps.SVG()

start_svg = "<svg xmlns='http://www.w3.org/2000/svg' width='100%' height='100%' version='1.1'>\n"

#<polyline points="0,40 40,40 40,80 80,80 80,120 120,120 120,160" style="fill:white;stroke:red;stroke-width:4"/>

end_svg = "\n</svg>"


normal = np.linalg.norm(actual_data)

test_data = actual_data/normal

x_max = 180
y_max = 160

x_pts = [each*x_max/15 for each in range(15)]
y_pts = [each*y_max/15 for each in test_data]



#print y_pts
points = zip(x_pts,y_pts)

#print points

#calibrate(points)
l = [] 
for each in points:
    l.append(str(each[0])+','+str(each[1]))

print l
start_elem = "<polyline points= \" "
end_elem = " style='fill:white;stroke:red;stroke-width:4'/>\n"
elem = start_elem + ' '.join(l) + '\"' + end_elem 

#svg_obj.addElement(start_svg)
#svg_obj.addElement(elem)
#svg_obj.addElement(end_svg)
#svg_obj.saveSVG(filename)

with open(filename,'w') as fd:
    fd.write(start_svg)
    fd.write(elem)
    fd.write(end_svg)


