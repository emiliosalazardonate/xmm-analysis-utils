#
# def plotFermiSources():
#     TSplotlim = 1
#     ss = [50, 171, 585, 2000]  # GeV
#     e_2fhl = zeros(len(ss) - 1, dtype=float)
#     eerrl_2fhl = zeros(len(ss) - 1, dtype=float)
#     eerru_2fhl = zeros(len(ss) - 1, dtype=float)
#     for i in range(len(ss) - 1):
#         e_2fhl[i] = stats.gmean((ss[i], ss[i + 1]))  # GeV
#         eerrl_2fhl[i] = e_2fhl[i] - ss[i]
#         eerru_2fhl[i] = ss[i + 1] - e_2fhl[i]
#
#     s = ['Flux50_171GeV', 'Flux171_585GeV', 'Flux585_2000GeV']
#     flux_2fhl = zeros(len(s), dtype=float)
#     fluxerrl_2fhl = zeros(len(s), dtype=float)
#     fluxerru_2fhl = zeros(len(s), dtype=float)
#     fluxul95_2fhl = zeros(len(s), dtype=float)
#     TS_2fhl = zeros(len(s), dtype=float)
#     q2 = []
#     q2ul = []
#     for i in range(len(s)):
#         # print s[i]
#         TS_2fhl[i] = tbdata_2fhl['Sqrt_TS' + s[i][4:]][myind] ** 2
#         esize = (eerru_2fhl[i] + eerrl_2fhl[i])
#         flux_2fhl[i] = tbdata_2fhl[s[i]][myind] / esize  # ph/cm2/s/GeV
#         fluxerrl_2fhl[i] = abs(tbdata_2fhl['Unc_' + s[i]][myind][0]) / esize  # ph/cm2/s/GeV
#         fluxerru_2fhl[i] = tbdata_2fhl['Unc_' + s[i]][myind][1] / esize  # ph/cm2/s/GeV
#         fluxul95_2fhl[i] = flux_2fhl[i] + 2 * fluxerru_2fhl[i]  # ph/cm2/s/GeV
#         if (TS_2fhl[i] >= TSplotlim):
#             q2.append(i)
#         elif (TS_2fhl[i] < TSplotlim):
#             q2ul.append(i)