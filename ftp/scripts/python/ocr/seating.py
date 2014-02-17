from PIL import Image
from string import maketrans
from BeautifulSoup import BeautifulSoup
from pytesser import *
import ImageFilter
import ImageEnhance
import re
import sys
#import getopt

xred   = (255, 20,  20)
xpink  = (255, 20,  255)
xgreen = (20,  250, 20)
white  = (255, 255, 255)
w_index  = 0
h_index  = 1
trans_table = maketrans("ZGSDOT", "2C5001")

def tuple_comp(xs, ys, comp_func = lambda x,y: x <= y):
    comp = map(comp_func, xs, ys)
    return reduce(lambda x,y: x and y, comp)

def is_not_white(xs):
    return not (xs == white)

def is_light_white(xs):
    return tuple_comp(xs, (15, 15, 25)) 

def is_seat_num_color(xs):
    return tuple_comp(xs, xred) or tuple_comp(xs, xgreen) or tuple_comp(xs, xpink)

def fix_inaccurary(value):
    try:
        strvalue = str(value).upper()
    except  UnicodeEncodeError:
        return value
    #TODO: elegant re exp??
    strvalue = strvalue.translate(trans_table)
    strvalue = re.sub(r'^2([0|6|O])([A-Z0-9]{2})$',r'2C\2', strvalue)
    return strvalue;

"""
inputfile: the target image
crop_list: list of 4 element tuple which stands for top-left and bottom-right coordanation for croping image.
"""
def get_seats_coordination(inputfile, crop_list = []):
    img = Image.open(inputfile)
    if not crop_list: crop_list = [(0, 0) + img.size]
   
    clist = map(lambda xs : _do_seats_scan(img.crop(xs), xs[w_index], xs[h_index], True, True), crop_list)
    return reduce(lambda xs,x : xs+x, clist)
    
def _do_seats_scan(img, left, top, save_temp=False, more=False):
    clist = _extrace_raw_list(img, save_temp)
    if more: dig_detail(img, clist)

    result = []
    for item in clist:
        try:
            l = left + item[0]
            t = top + item[1]
            seatid = fix_inaccurary(item[-1])
            if re.match(r'[A-Z0-9]{4,}', seatid):
                result.append((l, t, seatid))
            else:
                print '>>> %04d %04d, %s, %s' % (l, t, item[-1], seatid)
        except UnicodeEncodeError:
            print "error:", item
    return result

def _extrace_raw_list(img, save_temp=False):
    img = img.convert("RGB")
    pixdata = img.load()
    reduce_noise(img, pixdata)
    if save_temp: img.save("temp.png")
    return extrace_relative_coord(image_to_string(img))

""" 
crop each seat section and to OCR.
not finished yet since it looks like not improve a lot.
"""
def dig_detail(img, clist, adj=8):
    cclist = [ (x-adj, y-adj, z+adj, k+adj) for x,y,z,k,d in clist ]
    tmplist = map(lambda xs : _extrace_raw_list(img.crop(xs), True), cclist)

"""
extract OCR value and its coordanations
"""    
def extrace_relative_coord(html_text):
    soup = BeautifulSoup(html_text)
    result = []
    for x in soup.findAll(attrs={'class':'xocr_word'}):
        parent = x.findParent('span')
        left_top = [ int(y) for y in parent.attrMap.get('title').split(" ")[1:] ]
        left_top.append(x.text)
        result.append(left_top)
    return result


"""
trying to reduce noise
"""
def reduce_noise(img, pixdata):
    for y in xrange(img.size[h_index]):
        for x in xrange(img.size[w_index]):
            if is_not_white(pixdata[x,y]) and ( is_light_white(pixdata[x,y]) or not is_seat_num_color(pixdata[x, y])) :
                pixdata[x, y] = white
              
def prepare_sql_scripts(clist, section_ids = { 'A':17, 'B':16, 'C':15}):
    def prep_sql(*values):
        return "insert into seat values('%s', %d, 1, 1, '0', %d, %d);" % values

    return map(lambda xs: prep_sql(xs[2], section_ids.get(xs[2][1]), xs[0], xs[1]), clist)

if __name__ == '__main__':
    crops = [(1000, 200, 2400, 1230), (1500, 1230, 2000, 1800), (2000, 2460, 3620, 3260)]
    cropsmore = [(1000, 200, 2400, 1230), (1500, 1230, 2000, 1800), (2830, 2470, 3620, 2810), (2060,2840,3620,3260)]

    coord_list = get_seats_coordination(sys.argv[1], cropsmore)
    
    sqls = prepare_sql_scripts(coord_list)
    #for x in sqls: print x

    





"""                
#img2 = Image.open(inputfile)
#img2 = img2.filter(ImageFilter.CONTOUR).convert("RGB")
#pixdata2 = img2.load()
                
#enh = ImageEnhance.Contrast(img2)
#enh = ImageEnhance.Color(img2)
#enh = ImageEnhance.Sharpness(img2)
#enh = ImageEnhance.Brightness(img2)
#enh.enhance(0.3).show("30% more contrast")
#img2.filter(ImageFilter.MinFilter).show("test")
                
2M -> 2A4
^M -> 2A
"""
