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

