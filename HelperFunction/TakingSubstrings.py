def take_substring_from_request(request, begin_string, end_string):
    begin = request.find(begin_string) + len(begin_string)
    end = request.find(end_string)

    substring = request[begin : end]

    return substring