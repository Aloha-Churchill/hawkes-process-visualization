from MHP import MHP

P=MHP()
P.generate_seq(60)

print(P.data)
P.plot_events()