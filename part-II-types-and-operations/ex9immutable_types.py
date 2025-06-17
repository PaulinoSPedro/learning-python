S = "spam"

S = S[0] + "l" + S[2:]

# Only works on mutable and str is immutable
S[:] = "slam" # Str object does not support item assignment