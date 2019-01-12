import pydicom as d

def extract(fname):
    data = d.read_file(fname)
    for key in data.keys():
        val = data[key].value
        print(val)
        output = open('output.txt', 'a')
        output.write(str(val))
        output.write(str('\n'))

extract('bmode.dcm')
extract('ttfm.dcm')