def create_rooted_spanning_tree(G, root):
    S = {}
    open_list = [root]
    
    while len(open_list) > 0:
    	node = open_list[0]
    	del open_list[0]
    	if node not in S:
    		S[node] = {}

    	for neighbour in G[node]:
    		if neighbour not in S:
    			S[node][neighbour] = "green"
    			S[neighbour] = {}
    			S[neighbour][node] = "green"
    			open_list.append(neighbour)
    	else:
    		if node in S[neighbour]:
    			pass
    		else:
    			S[node][neighbour] = "red"
    			S[neighbour][node] = "red"
    return S


def get_children(S, root, parent):
    """returns the children from following the
    green edges"""
    child =  [n for n, e in S[root].items()
            if ((not n == parent) and
                (e == 'green'))]
    if child:
    	child.sort()
    return child

def _post_order(S, root, parent, val, po):
    children = get_children(S, root, parent)    
    for c in children:
        val = _post_order(S, c, root, val, po)
    po[root] = val
    return val + 1

def post_order(S, root):
    po = {}
    _post_order(S, root, None, 1, po)
    return po

def number_of_descendants(S, root):
    # return mapping between nodes of S and the number of descendants
    # of that node
    nd = {}
    __number_of_descendants(S, root, None, nd)
    return nd

def __number_of_descendants(S, root, parent, nd):
	children = get_children(S, root, parent)
	arr = []
	for c in children:
		arr.append(__number_of_descendants(S, c, root, nd))

	nd[root] = sum(arr) + 1
	return nd[root]





def post_order5(S, root):
    # return mapping between nodes of S and the post-order value
    # of that node
    po = {}
    stack = [root]
    ranking = 1;
    cursor  = 0;

    while len(stack) > 0:
    	recent_node = stack[cursor]
    	cursor +=1
    	#check
    	for child in S[recent_node]:
    		if S[recent_node][child] == "green":
    			if child in stack:
    				pass
    			else:
    				stack.append(child)
    				#top_node = stack[len(stack) -1]
    		else:
    			if recent_node not in po and child not in po:
    				po[recent_node] = ranking
    				cursor = cursor -1
    				del stack[cursor]
    				ranking += 1

        while cursor >= len(stack) and stack:
        	top_node = stack.pop()
        	po[top_node] = ranking
        	ranking += 1


    return po
    #pass


def get_neighbors(S, root, parent):
    """returns the children from following the
    green edges and red"""
    child =  [n for n, e in S[root].items()
            if not n == parent ]
    child.append(root)
    if child:
    	child.sort()
    return child


def _lowest_post_order(S,root,parent,po,l):
	children = get_children(S, root, parent)

	for c in children:
		_lowest_post_order(S, c, root,po, l)

	neighbours = get_neighbors(S,root,parent)
	array = []
	for node in neighbours:
		if node not in l:
			array.append(po[node])
		else:
			array.append(l[node])
	l[root] = min(array)
	return l[root]

def lowest_post_order(S, root, po):
    # return a mapping of the nodes in S
    # to the lowest post order value
    # below that node
    # (and you're allowed to follow 1 red edge)
    l = {}
    _lowest_post_order(S,root,None,po,l)
    return l


def test_lowest_post_order():
    S = {'a': {'c': 'green', 'b': 'green'}, 
         'b': {'a': 'green', 'd': 'red'}, 
         'c': {'a': 'green', 'd': 'green'}, 
         'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
         'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
         'f': {'e': 'green', 'g': 'red'},
         'g': {'e': 'green', 'f': 'red'} 
         }
    po = post_order(S, 'a')
    l = lowest_post_order(S, 'a', po)
    print l
    assert l == {'a':1, 'b':1, 'c':1, 'd':1, 'e':2, 'f':2, 'g':2}


def _highest_post_order(S,root,parent,po,h):
	children = get_children(S, root, parent)

	for c in children:
		_highest_post_order(S, c, root,po, h)

	neighbours = get_neighbors(S,root,parent)
	array = []
	for node in neighbours:
		if node not in h:
			array.append(po[node])
		else:
			array.append(h[node])

	h[root] = max(array)
	return h[root]

def highest_post_order(S, root, po):
    
    # return a mapping of the nodes in S
    # to the highest post order value
    # below that node
    # (and you're allowed to follow 1 red edge)
    h = {}
    _highest_post_order(S,root,None,po,h)
    return h

def test_highest_post_order():
    S = {'a': {'c': 'green', 'b': 'green'}, 
         'b': {'a': 'green', 'd': 'red'}, 
         'c': {'a': 'green', 'd': 'green'}, 
         'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
         'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
         'f': {'e': 'green', 'g': 'red'},
         'g': {'e': 'green', 'f': 'red'} 
         }
    po = post_order(S, 'a')
    h = highest_post_order(S, 'a', po)
    print h
    assert h == {'a':7, 'b':5, 'c':6, 'd':5, 'e':4, 'f':3, 'g':3}
    
# This is just one possible solution
# There are other ways to create a 
# spanning tree, and the grader will
# accept any valid result.
# feel free to edit the test to
# match the solution your program produces

def test_post_order():
    S = {'a': {'c': 'green', 'b': 'green'}, 
         'b': {'a': 'green', 'd': 'red'}, 
         'c': {'a': 'green', 'd': 'green'}, 
         'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
         'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
         'f': {'e': 'green', 'g': 'red'},
         'g': {'e': 'green', 'f': 'red'} 
         }
    po = post_order(S, 'a')
    print po
    assert po == {'a':7, 'b':1, 'c':6, 'd':5, 'e':4, 'f':2, 'g':3}

def test_number_of_descendants():
    S =  {'a': {'c': 'green', 'b': 'green'}, 
          'b': {'a': 'green', 'd': 'red'}, 
          'c': {'a': 'green', 'd': 'green'}, 
          'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
          'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
          'f': {'e': 'green', 'g': 'red'},
          'g': {'e': 'green', 'f': 'red'} 
          }
    nd = number_of_descendants(S, 'a')
    assert nd == {'a':7, 'b':1, 'c':5, 'd':4, 'e':3, 'f':1, 'g':1}

def bridge_edges(G, root):
    # use the four functions above
    # and then determine which edges in G are bridge edges
    # return them as a list of tuples ie: [(n1, n2), (n4, n5)]

    S = create_rooted_spanning_tree(G, root)
    po = post_order(S, root)
    nd = number_of_descendants(S, root)
    l = lowest_post_order(S, root, po)
    h = highest_post_order(S, root, po)
    edges = []
    find_b_edges(S, root, None, po,nd,l,h,edges)
    return edges


def check_b_edge(node,po,nd,l,h):
	if h[node] <= po[node] and abs(nd[node] - po[node]) < l[node]:
		return True
	else:
		return False


def find_b_edges(S, root, parent, po,nd,l,h,edges):
	children = get_children(S, root, parent)
	for c in children:
		find_b_edges(S, c, root, po ,nd,l,h,edges)
	if check_b_edge(root,po,nd,l,h):
		if parent:
			edges.append((parent,root))
	return 


def test_bridge_edges():
    G = {'a': {'c': 1, 'b': 1}, 
         'b': {'a': 1, 'd': 1}, 
         'c': {'a': 1, 'd': 1}, 
         'd': {'c': 1, 'b': 1, 'e': 1}, 
         'e': {'d': 1, 'g': 1, 'f': 1}, 
         'f': {'e': 1, 'g': 1},
         'g': {'e': 1, 'f': 1} 
         }
    bridges = bridge_edges(G, 'a')
    assert bridges == [('d', 'e')]


test_post_order()
test_number_of_descendants()
test_lowest_post_order()
test_highest_post_order()
test_bridge_edges()
