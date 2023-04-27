def sorting_cheeses(**kwargs):
    sorted_cheeses = dict(sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0])))
    result = ""
    for cheese in sorted_cheeses.keys():
        result += cheese + "\n"
        current_pieces = sorted(sorted_cheeses[cheese], reverse=True)
        for piece in current_pieces:
            result += str(piece) + "\n"
    return result
