import gensim
#from pyemd import emd
model = gensim.models.KeyedVectors.load_word2vec_format('/home/sinchan/Videos/slot_filling/slotfilling/GoogleNews-vectors-negative300.bin', binary=True,limit=50000)
documents= []
with open('doc','r') as f:
    for line in f:
        documents.append(line)
for i in range(len(documents)):
    for j in range(len(documents)):
        distance = model.wmdistance(documents[i], documents[j])
        print str('%.2f' % distance)+"    ",
    print "\n"


