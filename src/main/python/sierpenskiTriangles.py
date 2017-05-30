import numpy as np

def createTexture(r = 32, c = 63):
	tex = np.chararray((r,c))
	tex[:] = '_'
	return tex

def getCenters(num_per_frac, base_cords):
	centers = [[[each[0]+num_per_frac, each[1]-(num_per_frac-1)-1],[each[0]+num_per_frac, each[1]+(num_per_frac-1)+1]] for each in base_cords]
	return reduceCenters(reduce(lambda a,b: a+b, centers))

def reduceCenters(centers):
	dic = {}
	for center in centers:
		k = str(center[0])+'_'+str(center[1])
		if k not in dic:
			dic[k] = 1
		else:
			dic[k] += 1
	ele_to_filter = {k : v for k,v in dic.iteritems() if v%2 == 0}
	for k in ele_to_filter.iterkeys():
		centers = filter(lambda a: a != [int(k.split('_')[0]),int(k.split('_')[1])], centers)
	return centers

def subStrings(centers, frac_num, tex):
	for v in centers.itervalues():
		for cord in v:
			if tex[cord[0]][cord[1]] == '_':
				tex[cord[0]][cord[1]] = '1	'
			else:
				tex[cord[0]][cord[1]] = '_'
			tex = subChildren(tex, 32/(2**frac_num), cord)
	makeItString(tex)

def subChildren(tex, layers_to_sub, coordinate):
	for i in range(1,layers_to_sub):
		tex[coordinate[0]+i][coordinate[1]-i:coordinate[1]+i+1] = '1'
	return tex

def makeItString(tex):
	for each in tex: 
		print "".join(each)

def main(frac_num):
	tex = createTexture()
	(frac_num, cols) = (frac_num, 63)
	primary_center = [[0,31]]
	centers = {0:primary_center}
	num_per_frac = 32/2**frac_num
	layers_numbers = 2**frac_num
	for layer in range(1, layers_numbers):
		centers[layer] = getCenters(num_per_frac, centers[layer-1])
	subStrings(centers, frac_num, tex)

if __name__ == '__main__':
	main(3)