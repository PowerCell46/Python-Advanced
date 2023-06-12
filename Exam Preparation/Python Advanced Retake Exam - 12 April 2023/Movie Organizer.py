def movie_organizer(*args):
    dict = {}
    for el in args:
        current_movie = el[0]
        current_ganre = el[1]
        if current_ganre not in dict.keys():
            dict[current_ganre] = [current_movie]
        else:
            dict[current_ganre].append(current_movie)

    sort = sorted(dict.items(), key=lambda x: (-len(x[1]), x[0]))
    return_list = []
    for ganre in sort:
        current_movies = sorted(ganre[1])
        return_list.append(f'{ganre[0]} - {len(current_movies)}')
        for el in current_movies:
            return_list.append(f'* {el}')

    return "\n".join(return_list)
