def check_face_card(cards):
    for card in ['J', 'Q', 'K']:
        if card in cards:
            cards = (",").join(cards).replace(card, '10').split(',')
    return cards


def calculate_points(cards):
    if 'A' not in cards:
        for_sum = tuple(map(lambda x: int(x), cards))
        points = sum(for_sum)
        return points
    else:
        num_of_A_cards = cards.count('A')
        for i in range(num_of_A_cards):
            cards.remove('A')
        rest_sum = sum(tuple(map(lambda x: int(x), cards)))
        for i in range(num_of_A_cards):
            if 10 + rest_sum < 21: 
                rest_sum += 10
            elif 1 + rest_sum < 21 & 10 + rest_sum > 21:
                rest_sum += 1
            else:
                rest_sum += 1
        return rest_sum

def compare(points_1, points_2):
    if (points_1 <= 21) & (points_2 <= 21):
        if points_1 <= points_2 :
            return False
        else:
            return True
    elif (points_1 < 21) & (points_2 > 21):
        return True
    elif (points_1 > 21) & (points_2 < 21):
        return False
    else:
        return "Again"