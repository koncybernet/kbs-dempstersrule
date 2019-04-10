def get_belief_from_list(emotion, belief):
    for emo, bel in belief:
        if emo == emotion:
            return bel