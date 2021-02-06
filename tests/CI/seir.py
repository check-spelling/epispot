import epispot as epi


def R_0(t):
    return 5 * 2.718 ** ((- 1 / 500) * (t - 30) ** 2)


def N(t):
    return 1e5 + 10 * t


def p_rec(t):
    return 1.0


def rec_rate(t):
    return 1 / 7


def delta(t):
    return 1 / 2


Model = epi.pre.SEIR(R_0, N, p_rec, rec_rate, delta)
epi.plots.plot_comp_nums(Model, range(0, 120))
print('Test complete: Build passing.')
