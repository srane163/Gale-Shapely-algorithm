# Gale-Shapely aka college admission problem
def admissions_matching(n, doc_ranks, hosp_ranks):
    """Optimally matches doctors to hospitals as per each ranking

    Args:
        n (int): Number of elements(doctors & hospitals)
        doc_ranks: List of list - hospital preferences
        hosp_ranks: List of list - doctor preferences

    Returns:
        The ordered set of matched hospital for each potential candidate doctor.
    """
    unmatched_docs = list(range(n))  # Initially every doctor is unmatched
    accepted_docs = [None] * n  # Placeholders and initially no one is accepted
    accepted_hosps = [None] * n  # Placeholders and initially no one is accepted
    next_doc_choice = [0] * n  # Initialize matching

    while unmatched_docs:
        # Pick an arbitrary unmatched doctor
        doc = unmatched_docs[0]
        # Stores doctor ranking in the variable for convenience
        doc_pref = doc_ranks[doc]
        # checking matching ranks
        hosp = doc_pref[next_doc_choice[doc]]
        # Stores hospitals ranking in the variable for convenience
        hosp_pref = hosp_ranks[hosp]
        # Stores current matched doctor for the hospital
        curr_matched_doc = accepted_hosps[hosp]
        if curr_matched_doc is not None:  # if assignment exists
            if hosp_pref.index(curr_matched_doc) > hosp_pref.index(doc):
                # If current matched doctor is more preferred
                accepted_hosps[hosp] = doc  # Assign pair to each other
                accepted_docs[doc] = hosp
                unmatched_docs.remove(doc)  # Doctor is no longer unmatched
                unmatched_docs.append(curr_matched_doc)
            else:
                next_doc_choice[doc] += 1  # # current doctors next preference will be considered later on
        else:
            accepted_hosps[hosp] = doc
            accepted_docs[doc] = hosp
            unmatched_docs.remove(doc)
    return accepted_docs


assert(admissions_matching(1, [[0]], [[0]]) == [0])
assert(admissions_matching(2, [[0, 1], [1, 0]], [[0, 1], [1, 0]]) == [0, 1])

# Tests:
# print(admissions_matching(3, [[1, 0, 2], [1, 2, 0], [0, 2, 1]], [[1, 0, 2], [1, 2, 0], [1, 0, 2]]))
# print(admissions_matching(4, [[0, 1, 2, 3], [0, 2, 3, 1], [0, 3, 2, 1], [3, 1, 2, 0]], [[3, 1, 2, 0], [1, 2, 3, 0], [0, 3, 2, 1], [0, 1, 2, 3]]))
# print(admissions_matching(4, [[0, 1, 3, 2], [0, 2, 3, 1], [1, 0, 2, 3], [0, 3, 1, 2]], [[3, 1, 2, 0], [3, 1, 0, 2], [0, 3, 1, 2], [1, 0, 3, 2]]))

# Returns:
# [0, 1, 2]
# [2, 0, 3, 1]
# [1, 2, 3, 0]
