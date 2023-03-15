import pandas as pd
df = pd.read_table("alfonso.txt")
df
df = pd.read_table("alfonso.txt", columns=["Clado", "sp", "taxid", "gid", "freq"])
df = pd.read_table("alfonso.txt", column=["Clado", "sp", "taxid", "gid", "freq"])
df = pd.read_table("alfonso.txt", column_stack =["Clado", "sp", "taxid", "gid", "freq"])
df = pd.read_table?
df = pd.read_table("alfonso.txt", header=["Clado", "sp", "taxid", "gid", "freq"])
df = pd.read_table("alfonso.txt", header=["Clado", "sp", "taxid", "gid", "freq"])
df = pd.read_table?
df = pd.read_table("alfonso.txt", names=["Clado", "sp", "taxid", "gid", "freq"])
df
medias = df.groupby("Clade").mean()
medias = df.groupby("Clado").mean()
medias
stds = df.groupby("Clado").std()
stds
medias
stds
medias.plot.bar("freqs")
medias.plot.bar("freq")
tight_layout()
medias.plot.bar?
medias
medias.plot.bar("Clado", "freq")
medias.plot.bar(medias.index, "freq")
medias.plot.bar(x=medias.index, y="freq")
%history -f alfonsostale.py
