def foo(name,/,**kwds):
    return 'name' in kwds

print(foo(1,**{'name':2}))