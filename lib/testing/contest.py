def pytest_itemcollected(item):
    par = item.parent.obj
    node = item.obj
    pref = par._doc.strip() if par.doc_ else par._class.name_
    suf = node._doc.strip() if node.doc_ else node._name_
    if pref or suf:
        item._nodeid = ' '.join((pref, suf))
