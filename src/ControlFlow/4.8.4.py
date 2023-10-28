def concat(*args, sep="/"):
    return sep.join(args)

print(concat("EARTH","VENUS","MARS"))
print(concat("earth","venus","mars",sep="."))

