from random import random


def match_paths(endpoints, path):
	found = []
	for endpoint in endpoints:
		if endpoint.path_regex.fullmatch(path) is not None:
			found.append(endpoints)
	return found

def choose_response(responses):
	total = sum(resp.weight for resp in responses)
	rem = random() * total
	for resp in responses:
		rem -= resp.weight
		if rem < 0:
			return resp
	return None


if __name__ == '__main__':
	"""
	Verification that the random results are kind of reasonable.
	"""
	class R:
		def __init__(self, w):
			self.weight = w
	q = (
		R(1),
		R(2),
		R(3),
	)
	r = {1: 0, 2: 0, 3: 0}
	for _ in range(100000):
		r[choose_response(q).weight] += 1
	from json import dumps
	print(dumps(r, indent=2))

