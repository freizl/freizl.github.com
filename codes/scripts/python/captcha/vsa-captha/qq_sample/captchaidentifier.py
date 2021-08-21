import ImageFilter
from features import FEATURES

class CaptchaIdentifier():
    def __init__(self):
        pass

    def parse(self, img):
        i = img.filter(ImageFilter.CONTOUR).convert('1')
        i.show()

        blocks_tmp = [i.crop(b) for b in [(4, 3, 15, 20), (15, 3, 24, 20), (24, 3, 35, 20), (35, 3, 46, 20)]]
        f = open('feature_ext.txt', 'wb')
        for item in blocks_tmp:
            f.write(str(list(item.getdata())))
        #    item.show()

        blocks = [list(i.crop(b).getdata()) for b in [(5, 3, 17, 16), (18, 3, 30, 16), (31, 3, 43, 16), (44, 3, 56, 16)]]

#        return '123'
        return '%s%s%s%s' % tuple([self.identify_number(b) for b in blocks])

    def list_distance(self, m, n):
        len_plus = lambda x: len(x) + 1

        c = [[i] for i in range(0, len_plus(m))]
        c[0] = [j for j in range(0, len_plus(n))]

        for i in range(0, len(m)):
            for j in range(0, len(n)):
                c[i+1].append(
                    min(
                        c[i][j+1] + 1,
                        c[i+1][j] + 1,
                        c[i][j] + (0 if m[i] == n[j] else 1)
                    )
                )

        return c[-1][-1]

    def identify_number(self, source):
        distance = [self.list_distance(source, i) for i in FEATURES]
        minimal = min(distance)
        return distance.index(minimal)

