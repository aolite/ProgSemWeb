
class SimpleGraph:
    def __init__(self):
        self._spo = {}
        self._pos = {}
        self._osp = {}

    def add(self, (sub, pred, obj)):
        self._addToIndex(self._spo, sub, pred, obj)
        self._addToIndex(self._pos, pred, obj, sub)
        self._addToIndex(self._osp, obj, sub, pred)

    def _addToIndex(self, index, a, b, c):
        if a not in index:
            index[a] = {b: set([c])}
        else:
            if b not in index[a]:
                index[a][b] = set([c])
            else:
                index[a][b].add(c)

    def remove(self, (sub, pred, obj)):

        triples = list(self.triples((sub, pred, obj)))

        for (delSub, delPred, delObj) in triples:
            self._removeFromIndex(self._spo, delSub, delPred, delObj)
            self._removeFromIndex(self._pos, delPred, delObj, delSub)
            self._removeFromIndex(self._osp, delObj, delSub, delPred)

    def _removeFromIndex(self, index, a, b, c):
        try:
            bs = index[a]
            cset = bs[b]
            cset.remove(c)
            if len(cset) == 0: del bs[b]
            if len(bs) == 0: del index[a]
        # KeyErrors occur if a term was missing, which means that it wasn't a # valid delete:
        except KeyError:
            pass


