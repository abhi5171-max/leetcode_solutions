This is Codeforces 158A - Next Round.

Idea

A participant advances if:

Their score is greater than or equal to the score of the participant in the k-th position.
Their score is positive (> 0).

Since the scores are already sorted in non-increasing order, we can:

Find the k-th score: scores[k-1] (because Python uses 0-based indexing).

Count how many scores satisfy:

score >= scores[k-1] and score > 0