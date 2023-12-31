import numpy as np
import networkx as nx


class Graf:
    def __init__(self, matice_vah):
        # třída pro zobrazení grafu
        self.pocet_uzlu = np.size(matice_vah,1)
        self.matice_vah = matice_vah
        self.graf = nx.from_numpy_array(np.array(matice_vah))
        self.sousednost = []
        for i in range(0, self.pocet_uzlu):
            self.sousednost.append(list(np.where(matice_vah[i] > 0)[0]))
