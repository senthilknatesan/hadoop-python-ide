# always start with hello world?
print "hello world"

myd = lambda x: x%2 == 0

mym = lambda x : x*2

print myd(8)
print mym (14.2)

ml = [1,5,2,4,8,123,0, -1, 2.3]

nml = filter (myd, ml )
print nml

nm1 = filter( mym, ml)
print nml

nmm = map (myd, ml)
print nmm

nmm = map (mym, ml)
print nmm





