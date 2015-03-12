from PIL import Image
im = Image.open('cave.jpg')
w, h = im.size
imgs = [Image.new(im.mode, (w / 2, h / 2)) for dummy in xrange(4)]
imgs_load = [i.load() for i in imgs]
org = im.load()
for i in xrange(w):
    for j in xrange(h):
        org_pos = (i, j)
        new_pos = (i // 2, j // 2)
        imgs_load[i % 2 + j % 2 * 2 ][new_pos] = org[org_pos]
[imgs[i].save('%d.png' % i) for i in xrange(4)]
