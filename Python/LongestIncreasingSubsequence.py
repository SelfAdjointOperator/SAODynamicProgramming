"""
We are given a sequence [a_0, a_1, a_2, ..., a_(n-1)] of numbers. We wish to find (the size of) a maximal length strictly increasing subsequence. This is a problem that can be best seen as a Directed Acyclic Graph.
We will use the acronyms SIS for "strictly increasing subsequence", and MSIS for "maximal SIS".
Let d be the array of length n whose i'th entry is the length of a MSIS that ends with a_i.
d[0] is of course equal to 1, the MSIS being a_0.
Given d[0], d[1], ..., d[i-1], we can calculate d[i]: a MSIS ending at a_i is either a_i alone, or a_i joined with a MSIS ending at a_j for some j < i with a_j < a_i.
Hence d[i] = 1 + max_j(d[j] : j < i and a_j < a_i), where by convention max takes value 0 on an empty list.
Once all of d[i] have been calculated we can take l = max_i(d[i] : 0 <= i < n) as the length of a MSIS in [a_0, a_1, a_2, ..., a_(n-1)]
We also define the array p (p for 'previous') of length n, whose i'th entry is defined at each step as the value j that gives us our value of d[i], or None if no such j exists.
p allows us to construct the indices of our MSIS: letting k be the value of i that maximises l, the indices of our MSIS are given by [..., p[p[p[k]]], p[p[k]], p[k], k].
Our MSIS is therefore given as [a_p_0, a_p_1, ..., a_p_(l-1)].

TODO: Consider finding ALL MSISs of a given sequence.

"""

from Auxiliary.Decorators import AllNonFalsyArgs

@AllNonFalsyArgs([],0) # special case immediate return here if an empty sequence is provided; easier than overengineering main body of function
def MSIS_IndicesAndLength(sequence):
    """Returns a 2-tuple: a list of the indices of the MSIS we find, and its length.
    We return the length to save re-computation outside of this function as we necessarily calculate the length inside it.
    Using the returned indices of the MSIS to find the actual values of the method can be done outside if needed."""
    d = []
    p = []
    for i in range(len(sequence)):
        d_new_minusOne, p_new = max([[d[j], j] for j in range(i) if x[j] < x[i]] or [[0, None]])
        d.append(d_new_minusOne + 1)
        p.append(p_new)
    MSIS_length, sequenceEndIndex = max((value, index) for (index, value) in enumerate(d))
    MSIS_indices = [sequenceEndIndex]
    while (indexOfPrevious := p[MSIS_indices[-1]]) is not None:
        MSIS_indices.append(indexOfPrevious)
    MSIS_indices.reverse()
    return MSIS_indices, MSIS_length

def SampleSequence(sequence, subsequenceIndices):
    return [sequence[i] for i in subsequenceIndices]

def MSIS_Sequence(sequence):
    return SampleSequence(sequence, MSIS_IndicesAndLength(sequence)[0])

if __name__ == "__main__":
    from random import randint
    # print(x := [])
    # print(x := [50, 40, 30, 20, 10])
    print(x := [randint(1,20) for _ in range(10)])
    print(MSIS_IndicesAndLength(x))
    print(MSIS_Sequence(x))
