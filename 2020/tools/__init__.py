from functools import wraps
import time

def timer(func):
    @wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.6f} seconds")
        return value
    return wrapper_timer


def hk(graph):
    '''
    Hopcroft-Karp bipartite matching
    '''
    res = {}
    for u, v in graph.items():
        for x in v:
            if x not in res:
                res[x] = u
                break
    while True:
	    possible = {}
	    remaining = []
	    pred = {u: remaining for u in graph}
	    for v in res:
		    del pred[res[v]]
	    layer = list(pred)
	    while layer and not remaining:
		    new_layer = {}
		    for u in layer:
			    for v in graph[u]:
				    if v not in possible:
					    new_layer.setdefault(v,[]).append(u)
		    layer = []
		    for v in new_layer:
			    possible[v] = new_layer[v]
			    if v in res:
				    layer.append(res[v])
				    pred[res[v]] = v
			    else:
				    remaining.append(v)
	    if not remaining:
		    unlayered = {}
		    for u in graph:
			    for v in graph[u]:
				    if v not in possible:
					    unlayered[v] = None
		    return res

	    def recurse(v):
		    if v in possible:
			    cur = possible[v]
			    del possible[v]
			    for u in cur:
				    if u in pred:
					    pu = pred[u]
					    del pred[u]
					    if pu is remaining or recurse(pu):
						    res[v] = u
						    return True
		    return False
	    for v in remaining: recurse(v)