
def match_paths(endpoints, path):
	found = []
	for endpoint in endpoints:
		if endpoint.path_regex.fullmatch(path) is not None:
			found.append(endpoints)
	return found
