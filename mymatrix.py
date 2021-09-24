class MyMatrix:
  def __init__(self):
    pass
  
  def __str__(self):
    pass
  
  def __mul__(self):
    pass
  
  def __add__(self, x, y):
    """
    x, y are MyMatrix object, the return is also MyMatrix object.
    here, I assume __getitem__ is defined
	here, I assume the init of MyMatrix using the nested list,
	which is like this [[], []]
    """
    sums = []
    for i in range(len(x)):
    	row = []
    	for j in range(len(y)):
    		# row.append(x.index(i, j) + y.index(i, j))
    		row.append(x[i][j] + y[i][j])
    	sums.append(row)

    return MyMatrix(sums)
  
 
